# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
        medals = {}
        for row in csv_reader:
            if medals.get(row['Athlete']):
                medals[row['Athlete']] += 1
            else:
                medals[row['Athlete']] = 1
    return max(medals, key=medals.get)


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    with open('data/dictionary.csv', mode='r', encoding="utf-8") as country_list:
        codes = csv.DictReader(country_list, skipinitialspace=True)
        countries = {}
        for row in codes:
            countries[row['Code']] = row['Country']
        countries['URS'] = 'Soviet Union'

    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
        medals = {}
        for row in csv_reader:
            if int(row['Year']) >= int(min_year) and int(row['Year']) <= int(max_year):
                if row['Medal'] == 'Gold':
                    if medals.get(row['Country']):
                        medals[row['Country']] += 1
                    else:
                        medals[row['Country']] = 1
    return countries[max(medals, key=medals.get)]


def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
        medals = {}
        for row in csv_reader:
            if row['Event'] == '5000M' and row['Gender'] == 'Women':
                if medals.get(row['Athlete']):
                    medals[row['Athlete']] += 1
                else:
                    medals[row['Athlete']] = 1
    podium = []
    for _ in range(3):
        athlete = max(medals, key=medals.get)
        podium.append(athlete)
        del medals[athlete]
    return podium

print(top_three_women_in_five_thousand_meters())
