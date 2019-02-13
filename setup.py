try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='responser',  
    version='1.0.0',
    keywords='responser json api decorator',
    scripts=['setup_script'],
    author="Bharath Kumar Ravichandran",
    author_email="bharathkumarravichandran@gmail.com",
    description="Responser is a python package to convert normal strings, objects and other data to REST API response convention and in JSON format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    use_2to3=True,
    url="https://github.com/BharathKumarRavichandran/responser/",
    package_dir = {
        '': 'responser'
    },
    packages=[""],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.6'
    ],
    license="MIT"
)