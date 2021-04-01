# Flask libs
from flask import Blueprint

# Blueprint
bp = Blueprint('api', __name__)

# Import routes of api ....
from app.api import hello
