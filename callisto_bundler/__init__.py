from .helper import share

def _jupyter_nbextension_paths():
    """Required to load JS button"""
    return [dict(
        section="notebook",
        src="static",
        dest="callisto_bundler",
        require="callisto_bundler/index")]


def _jupyter_bundlerextension_paths():
    """Declare bundler extensions provided by this package."""
    return [{
        # unique bundler name
        "name": "callisto_bundler",
        # module containing bundle function
        "module_name": "callisto_bundler",
        # human-readable menu item label
        "label": "Upload to Callisto Gallery",
        # group under 'deploy' menu
        "group": "deploy",
    }]


def bundle(handler, model):
    share(handler, model)
