from src import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from src.models import Employee

app.config['SECRET_KEY'] = '1HV98N4L#&UNg?:E;82{Ef@Bftfpl9eC#DtTP~oJ"Pufpi|V)2&}_aqM/g?Pbp2'
admin = Admin(app = app, name="Quản trị bệnh viện", template_mode='bootstrap4')
admin.add_view(ModelView(Employee, db.session))