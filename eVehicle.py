from google.appengine.ext import ndb
import datetime

class EVehicle(ndb.Model):
    name = ndb.StringProperty(required = True)
    manufacturer = ndb.StringProperty(required = True)
    year = ndb.IntegerProperty(default = datetime.datetime.now().year)
    batterySize = ndb.FloatProperty(default = 0)
    wltpRange = ndb.FloatProperty(default = 0)
    cost = ndb.FloatProperty(default = 0)
    power = ndb.FloatProperty(default = 0)

    # method to check for duplicate entry
    def isUnique(self):
        query = EVehicle.query(EVehicle.name == self.name , EVehicle.manufacturer == self.manufacturer
                , EVehicle.year == self.year).fetch()
        if len(query) == 0:
            return True
        else:
            return False
