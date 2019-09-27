from flight_class import *

class Passenger(Flight):

    def __init__(self, flight_num, destination, origin, time, name, passport):
        super().__init__(flight_num, destination, origin, time)
        self.name = name
        self.passport = passport

    # def create_passenger(self):
    #     return 'Flight: {}, Destination: {}, Origin: {}, Time: {}, Name: {}, Passport: {}'.format(self.flight_num, self.destination, self.origin, self.time, self.name, self.passport)

