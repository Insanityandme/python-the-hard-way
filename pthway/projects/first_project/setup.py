try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'A test project to learn how things work.',
        'author': 'Filip Bengtegård Book',
        'url': 'http://www.firstproject.com',
        'download_url': 'http://www.packagedownloads.com',
        'author_email': 'bengtegardbook@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['first_project'],
        'scripts': [],
        'name': 'first_project'
}

setup(**config)
