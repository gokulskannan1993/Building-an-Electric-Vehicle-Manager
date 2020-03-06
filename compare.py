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

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'


        query = EVehicle.query()

        template_values = {
            'eVehicles': query
        }

        template = JINJA_ENVIRONMENT.get_template('compare.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        query = EVehicle.query()



        if self.request.get('button') == 'Compare':
            car = []
            carIDs = self.request.get('ev', allow_multiple=True)

            for carid in carIDs:
                key = ndb.Key('EVehicle', int(carid))
                ev = key.get()
                car.append(ev)

            if len(car) >=2:

                template_values = {
                    'cars': car,
                    'eVehicles': query
                }

                template = JINJA_ENVIRONMENT.get_template('compare.html')
                self.response.write(template.render(template_values))

            else:
                self.response.write('You have to select atleast 2 cars to Compare')
