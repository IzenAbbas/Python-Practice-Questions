class Car:
    total_instances=0

    def __init__(self):
        Car.total_instances+=1

    @classmethod
    def print_instances(cls):
        print(cls.total_instances)

maruti=Car()
honda=Car()
toyota=Car()
Car.print_instances()