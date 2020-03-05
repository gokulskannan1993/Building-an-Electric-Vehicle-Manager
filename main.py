import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os

from eVehicle import EVehicle
from addEV import AddEV
from search import Search
from ev import EV


JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''

        # pull the current user from the Request
        user = users.get_current_user()
        # determine if we have a user logged in or not.
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'


        # generate a map that contains everything that we need to pass to the template
        template_values = {
            'url' : url,
            'url_string' : url_string,
            'user' : user,
        }

        # pull the template file and jinja to render
        # it with the given template template_values
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))



app = webapp2.WSGIApplication(
            [('/', MainPage),
             ('/add', AddEV ),
             ('/search', Search),
             ('/ev', EV)
            ],

            debug = True
        )
