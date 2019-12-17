import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = [
    'requests>=2.9.1'
]

setuptools.setup(
    name="callisto-bundler",
    version="0.0.1",
    description="Send notebook to Callisto gallery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cccs-is/callisto-bundler",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/callisto_bundler", [
            "callisto_bundler/static/index.js",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/callisto_bundler.json"
        ])
    ]

)
