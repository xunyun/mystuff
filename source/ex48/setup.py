try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup
	
config = [
	'description': 'My Project',
	'Author': 'xunyun',
	'url': 'URL to get is at.',
	'download_url': 'Where to download it',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'script':[],
	'name': 'projectname'
]

setup(**config)