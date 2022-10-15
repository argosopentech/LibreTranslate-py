from setuptools import find_packages, setup

setup(name='libretranslatepy',
      version='2.1.3',
      description='Python bindings for LibreTranslate API',
      keywords="translation libretranslate",
      url='https://github.com/argosopentech/LibreTranslate-py',
      python_requires=">=2.6",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        ],
      project_urls={
        "Bug Reports": "https://github.com/argosopentech/LibreTranslate-py/issues",
        "Source": "https://github.com/argosopentech/LibreTranslate-py/",
        },
      packages=find_packages()
)
