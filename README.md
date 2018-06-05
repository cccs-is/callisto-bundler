# jupyter-bundler-openhumans

The goal is to use the `access_tokens` that are already in
the *Personal Data Notebooks* to push a notebook to an Open Humans account.

Post-sharing users are forwarded to a site to share their notebooks.

## Install / Development
To install on your own Jupyter Notebook setup to test:

```
git clone https://github.com/gedankenstuecke/jupyter-bundler-openhumans.git
cd jupyter-bundler-openhumans
pip install -e .
jupyter bundlerextension enable --py oh_bundler
```

To also rename the `deploy` button in the `jupyter` frontend to something more
useful you can also activate the following `nbextension` that's included in this
repository:

```
jupyter nbextension install --py oh_bundler --sys-prefix
jupyter nbextension enable --py oh_bundler --sys-prefix
```

Now you can run `jupyter notebook` as usual and you're good to go.

## Deployment
Post-sharing the user will be redirect to another URL, per default this is
`http://127.0.0.1:5000/shared` to facilitate easy local development.

To set up another redirect_url you can set the environment variable
`JH_BUNDLE_REDIRECT`.

## Demo
A basic file upload to an Open Humans project is already implemented.
For this to work in development you need to have the `OH_ACCESS_TOKEN`
environment variable set to a valid access token for yourself.

On the Personal Data Notebook setup this would be done automagically through the
`token_refresher`.
