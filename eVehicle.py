from google.appengine.ext import ndb


class EVehicle(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    year = ndb.IntegerProperty()
    batterySize = ndb.FloatProperty()
    wltpRange = ndb.FloatProperty()
    cost = ndb.FloatProperty()
    power = ndb.FloatProperty()

    # method to check for duplicate entry
    def isUnique(self):
        query = EVehicle.query(EVehicle.name == self.name , EVehicle.manufacturer == self.manufacturer
                , EVehicle.year == self.year).fetch()
        if len(query) == 0:
            return True
        else:
            return False
