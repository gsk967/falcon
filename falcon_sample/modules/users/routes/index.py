from falcon_sample.modules.users.controllers.index import user_controller as user_controller

class Router:
    def __init__(self, app):
        app.add_route('/users',user_controller())