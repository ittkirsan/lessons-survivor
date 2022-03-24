
def odometer(oksana):

    if len(oksana) % 2 == 0:
        mas = len(oksana)
    else:
        mas = len(oksana) - 1

    time_trip = 0
    distance_traveled = 0
    for i in range(1, mas, 2):
        distance_traveled = distance_traveled + \
            oksana[i-1] * (oksana[i]-time_trip)
        time_trip = oksana[i]
    time_trip = -1
    return distance_traveled
