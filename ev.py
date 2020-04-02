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
        # get the user
        user = users.get_current_user()

        # get the key to get the object
        key = ndb.Key('EVehicle', int(self.request.get('key')))


        # get the object from the key
        ev = key.get()

        # storing the key to pass it html
        urlKey = self.request.get('key')




        template_values = {
            'name' : ev.name,
            'manufacturer' : ev.manufacturer,
            'year' : ev.year,
            'batterySize' : ev.batterySize,
            'wltpRange' : ev.wltpRange,
            'cost' : ev.cost,
            'power' : ev.power,
            'user': user,
            'key': urlKey,
            'reviews': ev.reviews,
            'rating': ev.avgRating()
        }


        template = JINJA_ENVIRONMENT.get_template('ev.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        # get the object which the user wants
        key = ndb.Key('EVehicle', int(self.request.get('urlKey')))
        ev = key.get()

        # if the user want to update
        if self.request.get('button') == 'Update':
            ev.name = self.request.get('name')
            ev.manufacturer = self.request.get('manufacturer')
            ev.year = int(self.request.get('year'))
            ev.batterySize = float(self.request.get('batterySize'))
            ev.wltpRange = float(self.request.get('wltpRange'))
            ev.cost = float(self.request.get('cost'))
            ev.power = float(self.request.get('power'))
            # to avoid empty reviews and ratings posted automatically
            if self.request.get('rating'):
                ev.rating.append(int(self.request.get('rating')))
            if self.request.get('review'):
                ev.reviews.insert(0,self.request.get('review'))


            ev.put()
            self.redirect('/search')

        # if the user wants to delete
        elif self.request.get('button') == 'Delete':
            ev.key.delete()
            self.redirect('/search')
