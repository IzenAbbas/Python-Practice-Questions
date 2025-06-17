class Vehicles:
    def __init__(self,c_v):
        self._capacity=c_v

    def fare(self):
        return self._capacity * 100

class Bus(Vehicles):

    def fare(self):
        return super().fare() +0.1*super().fare()

print('Total fare of vehicle with capacity(50):',Vehicles(50).fare())
print('Total fare of bus with capacity(50):',Bus(50).fare())