import os
import nbformat
import requests
import logging

ENDPOINT_UPLOAD = '/nbupload/'
ENDPOINT_POST_SHARE = '/shared/'

# This is the cookie name used by OAuth2 proxy
# By default it is '_oauth2_proxy' and can be changed using '-cookie-name' config on the OAuth2 proxy.
OAUTH_COOKIE_NAME = '_oauth2_proxy'

logger = logging.getLogger(__name__)


def share(handler, model):
    base_url = os.getenv('JUPYTER_CALLISTO_URL', 'http://127.0.0.1:5000/').rstrip('/')
    access_token = os.getenv('NOTEBOOK_ACCESS_TOKEN')
    if not access_token:
        access_token = handler.request.headers.get('X-Access-Token')

    oauth_cookies = None
    if handler.request.cookies is not None and OAUTH_COOKIE_NAME in handler.request.cookies:
        oauth_cookies = {OAUTH_COOKIE_NAME: handler.request.cookies[OAUTH_COOKIE_NAME].value}

    try:
        notebook_filename = model['name']
        notebook_content = nbformat.writes(model['content']).encode('utf-8')
        data = {'notebook_name': notebook_filename, 'notebook_contents': notebook_content}

        post_url = base_url + ENDPOINT_UPLOAD

        headers = {'Authorization': 'Bearer ' + access_token}
        response = requests.post(url=post_url, headers=headers, cookies=oauth_cookies, data=data, timeout=5.0, verify=False)

        if response.status_code != 200:
            # TODO handle token refresh
            handler.finish('Upload failed. Gallery returned code: {0}'.format(response.status_code))
            return

        redirect_url = base_url + ENDPOINT_POST_SHARE
        handler.redirect(redirect_url)
    except Exception as e:
        logger.info('Exception while publishing notebook: {0}'.format(repr(e)))
        handler.finish('Your upload failed. Please contact system administrator.\n{0}'.format(repr(e)))
