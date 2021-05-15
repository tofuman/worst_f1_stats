#!/usr/bin/python3

import csv

from season import Season;
from race import Race;
from driver import Driver;

# data_set = ["2018"]
data_set = ["2018", "2019", "2020", "2021_spain"]

drivers = {}
seasons = {}


for year in data_set:
    seasons[year] = Season(year)
    with open("data/"+year+".csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        raw_races = reader.fieldnames[1:]
        races = []
        for race in raw_races:
            if len(race) != 0 and race != " ":
                seasons[year].add_race(race)
                races.append(race)
        for row in reader:
            driver = row["Driver"]
            if driver not in drivers:
                drivers[driver] = Driver(driver, year)
            seasons[year].add_driver(driver)
            for race in races:
                # print(year + ", " + driver + ", " + race + " = " + row[race])
                seasons[year].add_result(race, driver, row[race])
        for driver in seasons[year].drivers:
            seasons[year].calc_drivers_avg_finish(drivers[driver])

worst = {}
for name, driver in drivers.items():
    worst[name] = driver.calc_number_weighted_reverse_finish()

sorted_worst = {}
sorted_keys = sorted(worst, key=worst.get, reverse=True)

count = 1
for name in sorted_keys:
    score = "{:.3f}".format(worst[name])
    print((str(count).ljust(2)) +".: "+
     name.ljust(20) +
     " Score: "+ score+
     " Races: "+str(len(drivers[name].reverse_finishes)))
    count += 1
