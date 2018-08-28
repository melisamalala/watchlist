from flask import Blueprint
# from app.main import main as main_blueprint
main = Blueprint('main',__name__)
from . import views, errors