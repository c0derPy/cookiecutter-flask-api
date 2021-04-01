# Flask imports
from flask import jsonify

# Your imports
from app.api import bp


@bp.route('/hello', methods=['GET'])
def hello():
    return jsonify('Hello World!')
