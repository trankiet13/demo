from src import app, views, checker_loader

# from src.decorators import admin_required

#
# @app.route("/")
# def home():
#     return render_template('index.html')
#
# @login.user_loader
# def load_user(user_id):
#     return dao.get_user_by_id(user_id)
#
# @app.route('/login-admin', methods=['post'])
# def admin_login():
#     username = request.form['username']
#     password = request.form['password']
#
#     user = dao.auth_user(username = username, password = password, role = AccountRoleEnum.ADMIN)
#     if user:
#         login_user(user=user)
#
#     return redirect('/admin')
#
# @app.route("/login", methods=['get', 'post'])
# def login_process():
#     err_msg = None
#     if request.method.__eq__('POST'):
#         username = request.form.get('username')
#         password = request.form.get('password')
#         u = dao.auth_user(username=username, password=password)
#         if u:
#             login_user(u)
#             return redirect('/')
#         else:
#             err_msg = "Tài khoản hoặc mật khẩu không đúng"
#
#     return render_template('authentication.html',err_msg = err_msg)
#
# @app.route('/register', methods=['get', 'post'])
# def register_process():
#     err_msg = None
#     if request.method.__eq__('POST'):
#         password = request.form.get('password')
#         confirm = request.form.get('confirm')
#         print(request.form)
#         if password.__eq__(confirm):
#             data = request.form.copy()
#             del data['confirm']
#
#             avatar = request.files.get('avatar')
#
#             dao.add_user(avatar=avatar, **data)
#
#             return redirect('/login')
#         else:
#             err_msg = 'Mật khẩu KHÔNG khớp!'
#
#     return render_template('register.html', err_msg=err_msg)
#
# @app.route("/logout", methods=['get', 'post'])
# def logout_process():
#     logout_user()
#     return redirect("/login")


app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/about', 'about', views.about)
app.add_url_rule('/medicine', 'medicine', views.medicine)
app.add_url_rule('/notification', 'notification', views.notification)
app.add_url_rule('/authentication', 'authentication', views.authentication)
app.add_url_rule('/healthcare-staff', 'healthcare_staff', views.healthcare_staff)
app.add_url_rule('/pay', 'pay', views.pay)

app.add_url_rule('/authentication/signout', 'signout', views.signout)
app.add_url_rule('/authentication/signup', 'signup', views.signup, methods=['GET', 'POST'])
app.add_url_rule('/authentication/signin', 'signin', views.signin, methods=['GET', 'POST'])
app.add_url_rule('/authentication/forgot-password', 'forgot_password', views.forgot_password, methods=['GET', 'POST'])
app.add_url_rule('/authentication/reset-with-token/<token>', 'reset_with_token', views.reset_with_token,
                 methods=['POST'])

app.add_url_rule('/user/appointment', 'appointment', views.appointment, methods=['GET', 'POST'])
app.add_url_rule('/user/account-settings/<slug>', 'account_settings', views.account_settings, methods=['GET', 'POST'])
app.add_url_rule('/user/profile-settings/<slug>', 'profile_settings', views.profile_settings, methods=['GET', 'POST'])

app.add_url_rule('/employee/account-settings/<slug>', 'account_settings', views.account_settings,
                 methods=['GET', 'POST'])
app.add_url_rule('/employee/profile-settings/<slug>', 'profile_settings', views.profile_settings,
                 methods=['GET', 'POST'])

app.add_url_rule('/employee', 'employee', views.employee)
app.add_url_rule('/employee/login', 'employee_login', views.employee_login, methods=['GET', 'POST'])
app.add_url_rule('/employee/nurse', 'employee_nurse', views.employee_nurse, methods=['GET', 'POST'])
app.add_url_rule('/employee/doctor', 'employee_doctor', views.employee_doctor, methods=['GET', 'POST'])
app.add_url_rule('/employee/cashier', 'employee_cashier', views.employee_cashier, methods=['GET', 'POST'])

app.add_url_rule('/admin', 'admin', views.admin_login, methods=['GET', 'POST'])
app.add_url_rule('/admin/medicine/new', 'admin_medicine_new', views.create_medicine, methods=['POST'])

app.add_url_rule('/mail/confirm/<token>', 'confirm_email', views.confirm_email)
app.add_url_rule('/mail/resend', 'resend_confirmation', views.resend_confirmation)
app.add_url_rule('/mail/password-reset/<token>', 'password_reset', views.password_reset)

app.add_url_rule('/api/employee/doctor/load-packages', 'load_packages', checker_loader.load_packages_list,
                 methods=['POST'])
app.add_url_rule('/api/employee/doctor/load-medicine', 'load_medicine', checker_loader.load_medicines_list,
                 methods=['POST'])
app.add_url_rule('/api/authentication/check-signin-infor', 'check_signin_infor', checker_loader.check_signin_infor,
                 methods=['POST'])
app.add_url_rule('/api/authentication/check-signup-infor', 'check_signup_infor', checker_loader.check_signup_infor,
                 methods=['POST'])
app.add_url_rule('/api/authentication/check-profile-infor', 'check_profile_infor', checker_loader.check_profile_infor,
                 methods=['POST'])
app.add_url_rule('/api/authentication/check-account-exists', 'check_account_exists',
                 checker_loader.check_account_exists, methods=['POST'])
app.add_url_rule('/api/appointment/check-appointment-availability', 'check_appointment_availability',
                 checker_loader.check_appointment_availability, methods=['POST'])
app.add_url_rule(
    '/api/authentication/load-chart-stats-medicine-by-month',
    'load_chart_stats_medicine_by_month',
    checker_loader.load_chart_stats_medicine_by_month,
    methods=['POST']
)
app.add_url_rule(
    '/api/employee/doctor/load-medicine-by-medical-bill-id',
    'load_medicines_list_by_medical_bill_id',
    checker_loader.load_medicines_list_by_medical_bill_id,
    methods=['POST']
)
app.add_url_rule(
    '/api/authentication/load-examination-schedule-list-by-date',
    'load_examination_schedule_list_by_date',
    checker_loader.load_examination_schedule_list_by_date,
    methods=['POST']
)

if __name__ == '__main__':
    app.run(debug=True)
