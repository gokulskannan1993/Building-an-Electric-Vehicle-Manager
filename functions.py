
# gets the max value for average rating
def getMaxAvgRating(cars):
    maxRating = cars[0].avgRating()
    for car in cars:
        if car.avgRating() > maxRating:
            maxRating = car.avgRating()
    return maxRating

# gets the min value for average rating
def getMinAvgRating(cars):
    minRating = cars[0].avgRating()
    for car in cars:
        if car.avgRating() < minRating:
            minRating = car.avgRating()
    return minRating


# gets the max value of batterySize
def getMaxBattery(cars):
    maxBatterySize = cars[0].batterySize
    for car in cars:
        if car.batterySize > maxBatterySize:
            maxBatterySize = car.batterySize
    return maxBatterySize

# gets the min value of batterySize
def getMinBattery(cars):
    minBatterySize = cars[0].batterySize
    for car in cars:
        if car.batterySize < minBatterySize:
            minBatterySize = car.batterySize
    return minBatterySize



# gets the max value of wltpRange
def getMaxWltpRange(cars):
    maxWltp = cars[0].wltpRange
    for car in cars:
        if car.wltpRange > maxWltp:
            maxWltp = car.wltpRange
    return maxWltp


# gets the min value of wltpRange
def getMinWltpRange(cars):
    minWltp = cars[0].wltpRange
    for car in cars:
        if car.wltpRange < minWltp:
            minWltp = car.wltpRange
    return minWltp

# gets the max value of cost
def getMaxCost(cars):
    maxCost = cars[0].cost
    for car in cars:
        if car.cost > maxCost:
            maxCost = car.cost
    return maxCost


# gets the min value of cost
def getMinCost(cars):
    minCost = cars[0].cost
    for car in cars:
        if car.cost < minCost:
            minCost = car.cost
    return minCost


# gets the max value of Power
def getMaxPower(cars):
    maxPower = cars[0].power
    for car in cars:
        if car.power > maxPower:
            maxPower = car.power
    return maxPower


# gets the min value of Power
def getMinPower(cars):
    minPower = cars[0].power
    for car in cars:
        if car.power < minPower:
            minPower = car.power
    return minPower
