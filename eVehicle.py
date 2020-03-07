from google.appengine.ext import ndb


class EVehicle(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    year = ndb.IntegerProperty()
    batterySize = ndb.FloatProperty()
    wltpRange = ndb.FloatProperty()
    cost = ndb.FloatProperty()
    power = ndb.FloatProperty()
    reviews = ndb.StringProperty(repeated=True)
    rating = ndb.IntegerProperty(repeated=True)

    # method to check for duplicate entry
    def isUnique(self):
        query = EVehicle.query(EVehicle.name == self.name , EVehicle.manufacturer == self.manufacturer
                , EVehicle.year == self.year).fetch()
        if len(query) == 0:
            return True
        else:
            return False



    # method to calculate average rating
    def avgRating(self):
        totalRating = 0
        if self.rating:
            for score in self.rating:
                totalRating = totalRating + score
            return totalRating/len(self.rating)
        else:
            return 0


    # method to get the max value of an attribute
    def getMax(self, attribute):
        query = EVehicle.query().Order('-attribute').Limit(1)
        max = query[0].attribute
        return max
