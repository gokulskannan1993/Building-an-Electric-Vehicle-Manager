import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os

from eVehicle import EVehicle

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)




class EV(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        key = ndb.Key('MyList', 'default')
        myEV = key.get()

        template = JINJA_ENVIRONMENT.get_template('ev.html')
        self.response.write(template.render())
