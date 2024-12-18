from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user

from src.models import AccountRoleEnum


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Kiểm tra nếu người dùng hiện tại không phải là admin
        if current_user.role != AccountRoleEnum.ADMIN:
            flash('Bạn không có quyền truy cập vào trang này.', 'danger')
            return redirect(url_for('home'))  # Điều hướng về trang chủ (hoặc trang khác)
        return f(*args, **kwargs)
    return decorated_function