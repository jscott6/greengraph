

from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    description = "A package to compute proportion og green land between two locations",
    version = "0.1.0",
    author = "James Scott",
    author_email = "jas15@ic.ac.uk",
    packages = find_packages(exclude = ['*test']),
    scripts = ['bin/greengraph'],
    install_requires = ['argparse'],
    license = 'MIT'
)
