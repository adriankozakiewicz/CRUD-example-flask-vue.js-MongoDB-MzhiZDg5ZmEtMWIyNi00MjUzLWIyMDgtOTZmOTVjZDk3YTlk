import flask

from flask.views import View


# not using jinja on purpose - collidates with vueJS

class Views:
    class Index(View):
        def dispatch_request(self):
            return open('templates/frontend/index.html').read()

    class Dashboard(View):
        def dispatch_request(self):
            return open('templates/frontend/dashboard.html').read()

    class Login(View):
        def dispatch_request(self):
            return open('templates/frontend/login.html').read()

    class Register(View):
        def dispatch_request(self):
            return open('templates/frontend/register.html').read()