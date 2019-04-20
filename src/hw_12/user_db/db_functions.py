import json


def read_db():
    try:
        with open('users.json') as file:
            data_base = json.loads(file.read())
    except:
        data_base = []

    return data_base


def refresh_db(data_base):
    with open('users.json', 'w') as new_data_base:
        json.dump(data_base, new_data_base, indent=2)


def write_db(new_user):
    data_base = read_db()
    new_user['id'] = len(data_base) + 1
    data_base.append(new_user)
    refresh_db(data_base)
