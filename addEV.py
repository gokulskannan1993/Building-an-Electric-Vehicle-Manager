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

class AddEV(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        # pull the current user from the Request
        user = users.get_current_user()

        if user:
            # render the page
            template = JINJA_ENVIRONMENT.get_template('addEV.html')
            self.response.write(template.render())
        else:
            self.response.write("Login to access this feature")





    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        # if the user wants to add vehicle
        if self.request.get('button') == 'Add':
            # creating an object of the EVehicle class
            eVehicle = EVehicle(
                name = self.request.get('name'),
                manufacturer = self.request.get('manufacturer'),
                year = int(self.request.get('year')),
                batterySize = float(self.request.get('batterySize')),
                wltpRange = float(self.request.get('wltpRange')),
                cost = float(self.request.get('cost')),
                power = float(self.request.get('power'))
            )

            # checking for duplicate entries
            if(eVehicle.isUnique()):
                eVehicle.put()
                self.redirect('/')

            else:
                # incase of duplicate entries
                self.response.write('The Car is already in the DataBase')

        # if the user changed his mind
        elif self.request.get('button') == 'Cancel':
            self.redirect('/')
