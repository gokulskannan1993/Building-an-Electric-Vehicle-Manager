from google.appengine.ext import ndb


class EVehicle(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    year = ndb.IntegerProperty()
    batterySize = ndb.FloatProperty()
    wltpRange = ndb.FloatProperty()
    cost = ndb.FloatProperty()
    power = ndb.FloatProperty()
