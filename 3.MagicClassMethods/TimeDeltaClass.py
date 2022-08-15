class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2
        if self.clock2.get_time() > self.clock1.get_time():
            self.delta = 0
        else:
            self.delta = self.clock1.get_time() - self.clock2.get_time()

    def __len__(self):
        return self.delta

    def __str__(self):
        self.dsec = self.delta % 60
        self.dmin = (self.delta // 60) % 60
        self.dhrs = (self.delta // 3600) % 24
        return f'{str(self.dhrs).rjust(2, "0")}: {str(self.dmin).rjust(2, "0")}: {str(self.dsec).rjust(2, "0")}'

cl2 = Clock(2, 15, 46)
dt = DeltaClock(Clock(1, 21, 4), cl2)
# print(cl1.get_time())
print(dt)