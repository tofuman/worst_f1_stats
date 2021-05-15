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
                print(year + ", " + driver + ", " + race + " = " + row[race])
                seasons[year].add_result(race, driver, row[race])
        for driver in seasons[year].drivers:
            seasons[year].calc_drivers_avg_finish(drivers[driver])

for name, driver in drivers.items():
    driver.calc_reverse_finish()


# def add_driver_line_to_races(row, year, driver, race_cal):
#     for race, result in row.items():
#         result = result.rstrip('*')
#         if result.isnumeric():
#             races[year][race][result] = driver
#     #races[year][race] = sorted(races[year][race])
#
# def add_driver_line_to_drivers(row, year, driver, race_cal):
#     for race, result in row.items():
#         result = result.rstrip('*')
#         if result.isnumeric():
#             drivers[driver][year][race] = result
#     #races[year][race] = sorted(races[year][race])
#
#
# for year in data_set:
#     with open(year+".csv", newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         race_cal = []
#         race_results = {}
#         races[year] = {}
#         last_finisher = {}
#         race_cal = reader.fieldnames[1:]
#         for race in race_cal:
#             races[year][race] = {}
#         for row in reader:
#             driver = row["Driver"]
#             if driver not in drivers:
#                 drivers[driver] = {}
#             drivers[driver][year] = {}
#         for row in reader:
#             driver = row["Driver"]
#             results = row
#             del results["Driver"]
#             add_driver_line_to_races(results, year, driver, race_cal)
#             add_driver_line_to_drivers(results, year, driver, race_cal)
