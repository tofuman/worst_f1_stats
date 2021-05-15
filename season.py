from race import Race

class Season(object):

    def __init__(self, year):
        self.races = {}
        self.drivers = []
        self.year = year

    def __str__(self):
        result = "Year " + self.year + ": "
        for race in self.races.values():
            result += race.__str__() + ","
        return result

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_race(self, name):
        self.races[name] = Race(name, self.year)
        print("Added new Race for " + self.year + " : " + name)

    def add_result(self, race, driver, result):
        self.races[race].add_driver(driver, result)

    def calc_drivers_avg_finish(self, driver):
        for race in self.races.values():
            race.calc_reverse_finish()
        if driver.name in self.drivers:
            for name, race in self.races.items():
                finish = race.get_reverse_finish(driver.name)
                if finish > -1:
                    driver.add_revese_finish(finish)
        return driver
