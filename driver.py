

class Driver(object):

    def __init__(self, driver, year):
        self.years = []
        self.reverse_finishes = []
        self.avg_finish = 0
        self.name = driver
        self.years.append(year)

    def __str__(self):
        return self.name

    def get_number_seasons(self):
        return len(self.years)

    def add_revese_finish(self, result):
        self.reverse_finishes.append(result)

    def calc_reverse_finish(self):
        avg = 0
        for finish in self.reverse_finishes:
            avg += finish
        if len(self.reverse_finishes) >0:
            self.avg_finish = avg / len(self.reverse_finishes)
        # print(self.name + " Finsihed " + str(len(self.reverse_finishes)) + " with " + str(self.avg_finish))
        return self.avg_finish
