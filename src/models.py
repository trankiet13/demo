import hashlib
from datetime import datetime

from flask_login import UserMixin
from slugify import slugify
from sqlalchemy import Column, String, Boolean, Enum, DateTime, ForeignKey, BigInteger, Double, Integer
from sqlalchemy import event
from sqlalchemy.orm import relationship

from src import db, app

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class User(BaseModel):
    __tablename__ = 'users'
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    employees = relationship('Employee', backref='user', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = Column(BigInteger, ForeignKey('users.id'), primary_key=True)
    salary = Column(Double, default=0)


if __name__ == '__main__':

    # Sử dụng ứng dụng context để tạo các bảng
    with app.app_context():
        db.create_all()
