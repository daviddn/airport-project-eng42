from flight_class import *

class Plane(Flight):

    def __init__(self, flight_num, destination, origin, time, capacity, year, plane_num):
        super().__init__(flight_num, destination, origin, time)
        self.capacity = capacity
        self.year = year
        self.plane_num = plane_num