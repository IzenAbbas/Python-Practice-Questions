import datetime

class CheckExpiry:
    def __init__(self, m, e):
        if m>e:
            raise ValueError('Manufacturing must be greater than Expiry')
        self.manuf=m
        self.expiry=e

    def time_left(self):
        print('Time(in days) left for Expiry:',self.expiry - self.manuf)
        return self.expiry - self.manuf

print('Enter Manufacturing Date')
day=int(input('Input the day: '))
month=int(input('Input the month: '))
year=int(input('Input the year: '))
manuf=datetime.date(year, month, day)

print('Enter Expiry Date')
day=int(input('Input the day: '))
month=int(input('Input the month: '))
year=int(input('Input the year: '))
expiry=datetime.date(year, month, day)


CheckExpiry(manuf,expiry).time_left()
