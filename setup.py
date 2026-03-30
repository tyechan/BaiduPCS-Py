#!/usr/bin/env python

# This is a shim to hopefully allow Github to detect the package, build is done with poetry

import setuptools
from build import build

if __name__ == "__main__":
    setup_kwargs = {
        "name": "baidupcs-py",
        "packages": setuptools.find_packages(include=["baidupcs_py", "baidupcs_py.*"]),
    }
    build(setup_kwargs)
    setuptools.setup(**setup_kwargs)
