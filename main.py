#!/usr/bin/python3

import csv

from season import Season;
from race import Race;
from driver import Driver;


drivers = {}
seasons = {}

def main(start, end):
    for year_int in range(start, end+1):
        year = str(year_int)
        seasons[year] = Season(year)
        path = "drivers_data/"+year+".csv"
        print(path)
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            raw_races = reader.fieldnames[3:-1]
            races = []
            for race in raw_races:
                if len(race) != 0 and race != " ":
                    seasons[year].add_race(race)
                    races.append(race)
            for row in reader:
                driver = row["Driver"].lstrip(" ").rstrip(" ")
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
        if (worst[name] > 0):
            print((str(count).ljust(2)) +".: "+
             name.ljust(20) +
             " Score: "+ score+
             " Races: "+str(len(drivers[name].reverse_finishes)))
            count += 1
    print(str(count) +" Drivers Finished 1 Race. "+ str(len(worst)) + " Drivers Overall")

if __name__ == "__main__":
    import sys
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except IndexError:
        print("Please give a start and end year\n pull_data.py 2014 2019")
        exit(1)
    main(start, end)
