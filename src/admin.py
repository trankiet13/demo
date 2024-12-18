from flask import Flask, render_template
from flask_login import logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import redirect

from src import db, app
from src.models import Account, Regulation, Medicine, MedicineType, MedicineUnit, Bill
from src.models import AccountRoleEnum

# Khởi tạo Flask-Admin
admin =Admin(app=app, name='eCommerce Admin', template_mode='bootstrap4')

# Custom View để kiểm soát quyền truy cập
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.__eq__(AccountRoleEnum.ADMIN)

class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class StatsView(AuthenticatedView):
    @expose('/')
    def index(self):
        return self.render('admin/reports.html')


# Thêm các bảng vào giao diện admin
admin.add_view(AdminView(Account, db.session, name="Quản lý tài khoản"))
admin.add_view(AdminView(Regulation, db.session, name="Quản lý quy định"))
admin.add_view(AdminView(Medicine, db.session, name="Quản lý thuốc"))
admin.add_view(AdminView(MedicineType, db.session, name="Loại thuốc"))
admin.add_view(AdminView(MedicineUnit, db.session, name="Đơn vị thuốc"))
admin.add_view(AdminView(Bill, db.session, name="Báo cáo doanh thu"))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))