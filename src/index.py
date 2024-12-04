from  src import app, login, dao
from flask import render_template, request, redirect
from src import admin
from flask_login import login_user, logout_user


@app.route("/")
def home():
    return render_template('index.html')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/login-admin', methods=['post'])
def admin_login():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username = username, password = password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route("/login", methods=['get', 'post'])
def login_process():
    err_msg = None
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect('/')
        else:
            err_msg = "Tài khoản hoặc mật khẩu không đúng"

    return render_template('login.html',err_msg = err_msg)

@app.route('/register', methods=['get', 'post'])
def register_process():
    err_msg = None
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        print(request.form)
        if password.__eq__(confirm):
            data = request.form.copy()
            del data['confirm']

            avatar = request.files.get('avatar')

            dao.add_user(avatar=avatar, **data)

            return redirect('/login')
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)

@app.route("/logout", methods=['get', 'post'])
def logout_process():
    logout_user()
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)