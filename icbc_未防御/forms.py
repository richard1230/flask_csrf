
from flask_wtf import FlaskForm
from wtforms import StringField,ValidationError,IntegerField,FloatField,Form
from wtforms.validators import Email,InputRequired,Length,EqualTo,NumberRange
from models import User

# from models import User
# from exts import db

class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3,20)])
    password = StringField(validators=[Length(6,20)])
    password_repeat = StringField(validators=[EqualTo("password")])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(6,20)])

    # def validate(self):
    #     result = super(LoginForm,self).validate()
    #     if not result:
    #         return False
    #
    #     email = self.email.data
    #     password = self.password.data
    #     user = User.query.filter(User.email==email,User.password==password).first()
    #     if not user:
    #         self.email.errors.append('邮箱或者密码错误!')
    #         return False
    #     return True








class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1,1000000)])



