try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author':'Arjun Sabnis',
	'url':'URL to get it at',
	'download_url':'Where to download',
	'author_email':'arjunsabnis@gmail.com',
	'version':'0.1',
	'install_requires': ['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name':'projectname'
}

setup(**config)