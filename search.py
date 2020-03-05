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


class Search(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'


        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        name = self.request.get('name')
        manufacturer = self.request.get('manufacturer')
        minYear = self.request.get('minYear')
        maxYear = self.request.get('maxYear')
        minBatterySize = self.request.get('minBatterySize')
        maxBatterySize = self.request.get('maxBatterySize')
        minWltpRange = self.request.get('minWltpRange')
        maxWltpRange = self.request.get('maxWltpRange')
        minCost = self.request.get('minCost')
        maxCost = self.request.get('maxCost')
        minPower = self.request.get('minPower')
        maxPower = self.request.get('maxPower')


        query = EVehicle.query()

        if name:
            query = query.filter(EVehicle.name == name)
        if manufacturer:
            query = query.filter(EVehicle.manufacturer == manufacturer)
        if minYear:
            query = query.filter(EVehicle.year > int(minYear))
        if maxYear:
            query = query.filter(EVehicle.year < int(maxYear))
        if minBatterySize:
            query = query.filter(EVehicle.batterySize > float(minBatterySize))
        if maxBatterySize:
            query = query.filter(EVehicle.batterySize < float(maxBatterySize))
        if minWltpRange:
            query = query.filter(EVehicle.wltpRange > float(minWltpRange))
        if maxWltpRange:
            query = query.filter(EVehicle.wltpRange < float(maxWltpRange))
        if minCost:
            query = query.filter(EVehicle.cost > float(minCost))
        if maxCost:
            query = query.filter(EVehicle.cost < float(maxCost))
        if minPower:
            query = query.filter(EVehicle.power > float(minPower))
        if maxPower:
            query = query.filter(EVehicle.power < float(maxPower))


        # generate a map that contains everything that we need to pass to the template
        template_values = {
            'query': query
        }

        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))
