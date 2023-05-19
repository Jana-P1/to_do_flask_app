from flask import render_template, request, Blueprint
from myapplication.models.models import ToDo

landing = Blueprint('landing', __name__)


@landing.route('/')
def index():
  return render_template('index.html')