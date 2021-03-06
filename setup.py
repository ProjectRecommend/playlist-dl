import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    install_requires = ['youtube-dl'],
    name = "playlist-dl",
    version = "0.2",
    author = "Avi Aryan",
    author_email = "avi.aryan123@gmail.com",
    description = "Configurable Youtube Playlist downloader",
    license = "Apache",
    keywords = "youtube playlist download youtube-dl ytd",
    url = "http://github.com/aviaryan/playlist-dl",
    include_package_data = True,
    packages = ['playlist_dl'],
    package_data = {
        '': ['*.py']
    },
    exclude_package_data = {
        '': ['*.pyc']
    },
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only"
    ],
    entry_points = {
        'console_scripts': [
            'playlist-dl = playlist_dl.playlist_dl:run',
        ]
    },
    zip_safe = False
)