import csv
import os


def load_interests():
    dirname = os.path.dirname(__file__)
    print(dirname)
    interests_with_header = []

    with open(f"{dirname}/./../../data/interests.csv", 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            interests_with_header.append(row[0])
    only_interests = interests_with_header[1:]

    return only_interests
