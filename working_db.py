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
