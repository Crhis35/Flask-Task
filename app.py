
from Controllers.User import UserController
from flask import Flask


def create_app(config: dict = {}):
    # create app and load config
    app = Flask(__name__)

    # settings
    app.secret_key = "mysecretkey"

    # Init controllers and DB
    UserController.getInstance()

    # bind views
    from Views.Home import home, add_contact, get_contact, delete_contact, update_contact
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/add_contact', 'add_contact', view_func=add_contact,
                     methods=['POST'])
    app.add_url_rule('/edit/<id>', 'get_contact', view_func=get_contact,
                     methods=['POST', 'GET'])
    app.add_url_rule('/delete/<string:id>', 'delete_contact', view_func=delete_contact,
                     methods=['POST', 'GET'])
    app.add_url_rule('/update/<id>', 'update_contact', view_func=update_contact,
                     methods=['POST', 'GET'])

    return app
