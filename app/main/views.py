from flask import render_template, redirect, url_for, redirect
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from ..models import User, Comments, Mininfo
from ..main import main
from ..import db, photos
from .forms import InForm, lamentform, UpdateProfile


@main.route('/')
def index ():

    message = 'Gone in 60'
    title = 'Ready? Go!'
    return render_template('index.html', message=message, title= title)

@main.route('/info', methods = ['GET', 'POST'])
@login_required
def new_info():
    form = InForm
    if form.validate_on_submit():
        category = form.category.data
        info = form.info.data
        title = form.title.data

        new_info = InForm(title = title. category=category, info=info, user_id = current_user.id)
         title = 'New Pitch'

         new_pitch.save_pitch()
         return redirect(url_for(main.index))
    return render_template('preach.html', pitch_entry= form)

@main.route('/categories/<cate>')
def category(cate):
    