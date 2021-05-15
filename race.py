
class Race(object):


    def __init__(self, name, year):
        self.cars_started = 0
        self.cars_finished = 0
        self.results = {}
        self.reverse_finish = {}
        self.dnf = []
        self.dsq = []
        self.dns = []
        self.wd = []
        self.dnq = []
        self.exc = []
        self.drivers = []
        self.fastest_lap = ""
        self.name = name
        self.year = year

    def __str__(self):
        return self.name + "(" + self.year + ")"

    def add_driver(self, driver, result):
        if driver not in self.drivers:
            self.drivers.append(driver)
        else:
            print("Warning Driver racing a race twice!" + str(self))
            return
        position = result.rstrip('*')

        if position.isnumeric():
            self.results[position] = driver
            if(int(position) > self.cars_finished):
                self.cars_finished = int(position)
        elif "DNF" in position:
            self.dnf.append(driver)
        elif "DSQ" in position:
            self.dsq.append(driver)
        elif "DNS" in position:
            self.dns.append(driver)
        elif "DNQ" in position:
            self.dnq.append(driver)
        elif "WD" in position:
            self.wd.append(driver)
        elif "EXC" in position:
            self.exc.append(driver)
        elif len(result) > 1:
                print("Could not map result: "+driver + " ("+ self.name  + ","+ self.year + "): " + result  )
        if "*" in result:
            self.fastest_lap = driver
        self.cars_started = len(self.dnf) + len(self.dsq) + len(self.results)

    def calc_reverse_finish(self):
        for position, driver in self.results.items():
            self.reverse_finish[driver] = float(position) / self.cars_finished

    def get_reverse_finish(self, driver):
        try:
            return self.reverse_finish[driver]
        except:
            return -1;
