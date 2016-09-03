# -*- coding: utf-8 -*-
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
        session['gender'] = form.gender.data
        session['department1'] = form.department1.data
        session['department2'] = form.department2.data
        session['skill'] = form.skill.data
        session['reason'] = form.reason.data
        session['phone_number'] = form.phone_number.data
        session['class_number'] = form.class_number.data
        session['native_place'] = form.native_place.data
        session['former_job'] = form.former_job.data
        session['former_experience'] = form.former_experience.data
        session['expection'] = form.expection.data
        session['obey_swap'] = form.obey_swap.data
        session['turn_major'] = form.turn_major.data

        sum = ''
        for x in form.add_teams.data:
            sum = sum + ' ' + x   
            
        session['add_teams'] = sum

        if Student.query.filter_by(id=form.id_code.data).first() is not None:
            flash(u'你已经完成报名')
            return redirect(url_for('main.index'))

        student = Student(id=session['id_code'], name=session['name'], email=session['email'],
                          department1=session['department1'], department2=session['department2'],
                          skill=session['skill'], reason=session['reason'],phone_number = session['phone_number'],
                          class_number=session['class_number'], native_place = session['native_place'],
                          former_job = session['former_job'], former_experience = session['former_experience'],
                           expection =  session['expection'], obey_swap =session['obey_swap'], turn_major = session['turn_major'],gender = session['gender'], add_teams = session['add_teams'])

        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.finish'))
    return render_template('index.html', form=form, name=None)

@main.route('/finsih', methods=['GET', 'POST'])
def finish():
    return render_template('finish.html')

