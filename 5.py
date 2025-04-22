class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Normalize seconds to minutes
        self.minutes += self.seconds // 60
        self.seconds %= 60

        self.hours += self.minutes // 60
        self.minutes %= 60

    def display(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def add(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def subtract(self, other):
      
        t1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        t2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff_seconds = abs(t1 - t2)

        hours = diff_seconds // 3600
        diff_seconds %= 3600
        minutes = diff_seconds // 60
        seconds = diff_seconds % 60

        return Time(hours, minutes, seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

if __name__ == "__main__":
    time1 = Time(2, 45, 50)
    time2 = Time(1, 20, 30)

    print("Time 1:", time1.display())
    print("Time 2:", time2.display())

    time_sum = time1.add(time2)
    print("Time Sum:", time_sum.display())

    time_diff = time1.subtract(time2)
    print("Time Difference:", time_diff.display())

    total_secs = time1.to_seconds()
    print("Time 1 in Seconds:", total_secs)

    new_time = Time.from_seconds(5000)
    print("5000 Seconds = ", new_time.display())
