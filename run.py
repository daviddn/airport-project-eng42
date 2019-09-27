from plane_class import *
from passenger_class import *
from flight_class import *

flight_1 = Flight('XY123XY', 'London', 'New York', '1030')
print(flight_1.list_flights())

# passenger_1 = Passenger('XY123XY', 'London', 'New York', '1030', 'David', 'AA1234567')
# print(passenger_1.create_passenger())

passenger_1 = Passenger('XY123XY', 'London', 'New York', '1030', 'David', 'AA1234567')
passenger_2 = Passenger('XY123XY', 'London', 'New York', '1030', 'Moustafa', 'AA9876543')
passenger_3 = Passenger('XY123XY', 'London', 'New York', '1030', 'Miles', 'AA1212121')
flight_1.add_passenger(passenger_1.flight_num, passenger_1.destination, passenger_1.origin, passenger_1.time, passenger_1.name, passenger_1.passport)
flight_1.add_passenger(passenger_2.flight_num, passenger_2.destination, passenger_2.origin, passenger_2.time, passenger_2.name, passenger_2.passport)
flight_1.add_passenger(passenger_3.flight_num, passenger_3.destination, passenger_3.origin, passenger_3.time, passenger_3.name, passenger_3.passport)
print(flight_1.passenger_list)

# flight_1.passenger_list('XY123XY', 'London', 'New York', '1030', 'David', 'AA1234567')
# print(flight_1.passenger_list)