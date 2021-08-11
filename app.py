
from flask import Flask


def create_app(config: dict = {}):
    # create app and load config
    app = Flask(__name__)

    # settings
    app.secret_key = "mysecretkey"

    # bind views
    from Views.Home import home, add_contact, get_contact
    app.add_url_rule('/', view_func=home)
    app.add_url_rule("/add_contact", 'add_contact', view_func=add_contact,
                     methods=['POST'])
    app.add_url_rule("/edit/<id>", 'get_contact', view_func=get_contact,
                     methods=['POST', 'GET'])

    return app
