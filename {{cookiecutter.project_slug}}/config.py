# Imports
import os
from dotenv import load_dotenv

# Basedir project .env configuration
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """ Class with params of configurations """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '{{cookiecutter.project_slug}}.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
