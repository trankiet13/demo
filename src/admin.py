from src import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app = app, name="Quản trị bệnh viện", template_mode='boostrap4')
