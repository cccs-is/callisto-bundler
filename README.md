# jupyter-bundler-openhumans

Work in Progress. The goal is to use the access tokens that are already in
the Personal Data Notebooks to push a notebook to open humans.

## Development
To install on your own Jupyter Notebook setup to test:

```
git clone https://github.com/gedankenstuecke/jupyter-bundler-openhumans.git
cd jupyter-bundler-openhumans
pip install -e .
jupyter bundlerextension enable --py oh_bundler
```

Now you can run `jupyter notebook` as usual and you're good to go.
