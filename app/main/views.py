from flask import render_template, redirect, url_for, redirect
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from ..models import User, Comments, Mininfo
from ..main import main
from ..import db, photos
from .forms import InForm, lamentform, UpdateProfile


# @main.route
