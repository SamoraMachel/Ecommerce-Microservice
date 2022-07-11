from sys import api_version
from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__)

from . import products