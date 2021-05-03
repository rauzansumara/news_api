import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	#SQLALCHEMY_TRACK_MODIFICATIONS = False
	#'sqlite:///' + os.path.join(basedir, 'news.db')