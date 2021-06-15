from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
        name='libretranslatepy',
        version='2.1.0',
        description='Python bindings for LibreTranslate API',
        url='https://www.argosopentech.com',
        packages=find_packages()
)
