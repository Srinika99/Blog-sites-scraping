import csv
import os


def load_urls():
    dirname = os.path.dirname(__file__)
    urls_with_header = []

    with open(f"{dirname}/./../../data/websites.csv", 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            urls_with_header.append(row[0])
    only_urls = urls_with_header[1:]

    return only_urls
