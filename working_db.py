from main import db, Item, Users


def add_users(password, email, hash_password):
    try:
        res = Users(email=email, password=password, hash_password=hash_password)
        db.session.add(res)
        db.session.commit()
        return False
    except Exception as err:
        return f'Ошибка добавления пользователя {err}'


def add_product(title, price):
    try:
        item = Item(title=title, price=price)
        db.session.add(item)
        db.session.commit()
        return False
    except Exception as err:
        return f'Ошибка добавления товара {err}'


def get_user(user_id):
    try:
        res = Users.query.get(user_id)
        if not res:
            print('Пользователь не найден')
            return False
        return res
    except Exception as err:
        print(f'Ошибка в получении данных {err}')

    return False


def get_email(email):
    try:
        res = Users.query.filter_by(email=email).first()
        print(res.email)
        if not res:
            print('Пользователь не найден')
            return False
        else:
            return res
    except Exception as err:
        print(f'Ошибка в получении данных {err}')
        return False

