class Flight():

    def __init__(self, flight_num, destination, origin, time):
        self.destination = destination
        self.origin = origin
        self.time = time
        self.flight_num = flight_num
        self.passenger_list = []

    def list_flights(self):
        return 'Flight: {}, Destination: {}, Origin: {}, Time: {}'.format(self.flight_num, self.destination, self.origin, self.time)

    def add_passenger(self, flight_num, destination, origin, time, name, passport):
        self.passenger_list.append(flight_num + ' ' + destination + ' ' + origin + ' ' + time + ' ' + name + ' ' + passport)
