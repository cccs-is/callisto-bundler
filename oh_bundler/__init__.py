import os
import nbformat
import markdown


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
    notebook_filename = model['name']
    notebook_content = nbformat.writes(model['content']).encode('utf-8')
    print(len(notebook_content))
    notebook_name = os.path.splitext(notebook_filename)[0]
    print(notebook_name)
    markdown_text = markdown.markdown(open('README.md').read())
    print(os.getenv('PWD'))
    handler.finish(str(markdown_text))
