import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    install_requirements = fh.read().splitlines()

with open("toycodeexample/version.py", "r") as fh:
    pkg_version = re.search(r"\d+\.\d+\.\d+", fh.read())[0]

setuptools.setup(
    name="toycodeexample",
    version=pkg_version,
    author="Hiroshi Okada",
    author_email="okadashiroshi@miobox.jp",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HiroshiOkada/toycodeexample",
    packages=setuptools.find_packages(),
    install_requirements=install_requirements,
    entry_points={
        "console_scripts": [
            "countdown=toycodeexample.countdown:countdown",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
