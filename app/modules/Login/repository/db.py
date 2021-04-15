fake_db = {
    '1': {
        'name': 'John',
        'surname': 'Doe',
        'email': 'john@doe.com',
        'password': '1'
    },

    'sandra@johnson.com': {
        'name': 'Sandra',
        'surname': 'Johnson',
        'email': 'sandra@johnson.com',
        'password': 'sandra1243'
    }
}


def query_user(data_login):
    user = fake_db.get(data_login.username)
    if not user:
        return None
    if data_login.password != user.get('password'):
        return None
    return data_login
