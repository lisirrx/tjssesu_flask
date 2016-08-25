from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Required


class InputForm(Form):
    departments = [('请选择', '请选择'), ('宣传部', '宣传部'), ('文艺部', '文艺部'),
                   ('体育部', '体育部'), ('外联部', '外联部'), ('学术部', '学术部'), ('组织部', '组织部')]
    name = StringField('姓名', validators=[Required()])
    id_code = StringField('学号', validators=[Required()])
    email = StringField('邮箱', validators=[Required()])
    department1 = SelectField('第一志愿', choices=departments)
    department2 = SelectField('第二志愿', choices=departments)
    skill = TextAreaField('个人能力', validators=[Required()])
    reason = TextAreaField('为什么想加入这个部门', validators=[Required()])
    submit = SubmitField('提交报名表')