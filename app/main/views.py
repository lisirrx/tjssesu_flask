from flask import render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Student
from . import main
from .forms import InputForm



@main.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['id_code'] = form.id_code.data
        session['email'] = form.email.data
        session['department1'] = form.department1.data
        session['department2'] = form.department2.data
        session['skill'] = form.skill.data
        session['reason'] = form.reason.data

        if Student.query.filter_by(id=form.id_code.data).first() is not None:
            flash(u'你已经完成报名')
            return redirect(url_for('main.index'))

        student = Student(id=session['id_code'], name=session['name'], email=session['email'],
                          department1=session['department1'], department2=session['department2'],
                          skill=session['skill'],
                          reason=session['reason'])

        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.finish'))
    return render_template('index.html', form=form, name=None, title = u'同济大学软件学院团学联')

@main.route('/finsih', methods=['GET', 'POST'])
def finish():
    return render_template('finish.html')

