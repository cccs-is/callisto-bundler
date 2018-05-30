import os
import nbformat
import markdown
from ohapi import api
from .helper import upload_notebook


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
        markdown_text = markdown.markdown(open(
                            'templates/finalized_upload.md').read())
        markdown_text = markdown_text.replace(
                '{{title}}', notebook_filename)
        handler.finish(str(markdown_text))
    except:
        print('whopsy, something went wrong')
        markdown_text = markdown.markdown(open(
                            'templates/upload_broken.md').read())
        handler.finish(str(markdown_text))
