from exts import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True)#autoincrement=True
    email = db.Column(db.String(50),nullable=False)#,unique=True
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    deposit = db.Column(db.Float,default=0) # 薪水