import os
import nbformat
from ohapi import api
from .helper import upload_notebook


def _jupyter_nbextension_paths():
    """Required to load JS button"""
    return [dict(
        section="notebook",
        src="static",
        dest="oh_bundler",
        require="oh_bundler/index")]


def _jupyter_bundlerextension_paths():
    """Declare bundler extensions provided by this package."""
    return [{
        # unique bundler name
        "name": "openhumans_bundler",
        # module containing bundle function
        "module_name": "oh_bundler",
        # human-redable menu item label
        "label": "Upload to Open Humans",
        # group under 'deploy' or 'download' menu
        "group": "deploy",
    }]


def bundle(handler, model):
    """Create a compressed tarball containing the notebook document.

    Parameters
    ----------
    handler : tornado.web.RequestHandler
        Handler that serviced the bundle request
    model : dict
        Notebook model from the configured ContentManager
    """
    redirect_url = os.getenv("JH_BUNDLE_REDIRECT",
                             "http://127.0.0.1:5000/shared")
    try:
        access_token = os.getenv('OH_ACCESS_TOKEN')
        ohmember = api.exchange_oauth2_member(access_token)
        project_member_id = ohmember['project_member_id']
        notebook_filename = model['name']
        api.delete_file(access_token,
                        project_member_id,
                        file_basename=notebook_filename)
        print('deleted old_file')
        notebook_content = nbformat.writes(model['content']).encode('utf-8')

        upload_notebook(notebook_content, notebook_filename,
                        access_token, project_member_id)
        handler.redirect(redirect_url)
    except:
        print('whopsy, something went wrong')
        handler.finish(("Your upload failed. "
                        "Please restart your notebook server "
                        "and try again."))
