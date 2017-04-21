class Guitar:
    def __init__(self, name="", year="0", cost="0"):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        if self.is_vintage():
            return "{} ({}) : ${:.2f}(vintage)".format(self.name, self.year, self.cost)
        else:
            return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2017 - int(self.year)
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
