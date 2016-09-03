# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, SelectMultipleField
from wtforms.validators import Required


class InputForm(Form):
    gender_select = [('男','男'),('女','女')]
    classes_select = [('1','1'),('2','2'),('3','3'),('4','4')]
    departments = [('请选择', '请选择'), ('宣传部', '宣传部'), ('文艺部', '文艺部'),
                   ('体育部', '体育部'), ('外联部', '外联部'), ('学术部', '学术部'), ('组织部', '组织部'),('秘书处', '秘书处')]
    teams = [('志愿者中队', '志愿者中队'),('啦啦队', '啦啦队'),('足球队', '足球队'),('篮球队', '篮球队')]
    name = StringField('姓名', validators=[Required()])
    gender = SelectField('性别', choices=gender_select)
    id_code = StringField('学号', validators=[Required()])

    phone_number = StringField('手机号码', validators=[Required()])
    class_number = SelectField('班级', choices=classes_select)
    native_place = StringField('籍贯', validators=[Required()])
    email = StringField('邮箱', validators=[Required()])
    
    department1 = SelectField('第一志愿', choices=departments)
    department2 = SelectField('第二志愿', choices=departments)

    obey_swap = BooleanField('是否服从调剂', false_values='false')
    turn_major = BooleanField('是否有转专业意向', false_values='false')

    former_job = StringField('曾任职务', validators=[Required()])
    skill = TextAreaField('爱好特长', validators=[Required()])


    
    add_teams = SelectMultipleField('是否想加入以下团学联分队（多选）',choices = teams)

    reason = TextAreaField('请给我们一个选择你的理由', validators=[Required()])
    former_experience = TextAreaField('谈谈你在在学生工作和其他方面的经历', validators=[Required()])
    expection = TextAreaField('说说你对学生会或迎新晚会有何期待', validators=[Required()])


    
    submit = SubmitField('提交报名表')