from cloudipsp import Api, Checkout
from flask import render_template, request, redirect, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from main import app, Item, login_manager, Users
from working_db import add_users, add_product, get_email
from user_login import UserLogin


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prices')
def prices():
    items = Item.query.order_by(Item.price).all()
    return render_template('prices.html', data=items)


@app.route('/buy/<int:id>')
def item_buy(id):
    item = Item.query.get(id)

    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        'currency': 'RUB',
        'amount': str(item.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/create', methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        item = add_product(title=title, price=price)
        if not item:
            flash('Товар добавлен', category='alert-success')
            return redirect('/prices')
        else:
            flash('Товар не добавлен', category='alert-danger')
    else:
        return render_template('create.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        if len(request.form['email']) > 4 and len(request.form['password']) > 4:
            hash_password = generate_password_hash(request.form['password'])
            res = add_users(email=request.form['email'], password=request.form['password'], hash_password=hash_password)
            if not res:
                flash('Регистрация успешно пройдена', category='alert-success')
                return redirect('/login')
            else:
                flash(res, category='alert-danger')
                redirect('/')
        else:
            flash('Неверно заполнены поля', category='alert-danger')
            redirect('/about')
    return render_template('registration.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = get_email(request.form['email'])
        if user:
            if check_password_hash(user.hash_password, request.form['password']):
                # log_ser = UserLogin().create(user)
                # login_user(log_ser)
                flash('Вы успешно вошли', category='alert-success')
                return redirect('/')
            else:
                flash('Неверная пара логин/пароль', category='alert-danger')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
