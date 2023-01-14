import csv

def main(interests):
    # code to use the interests in the main function
    pass

with open('interests.csv', 'r') as file:
    csv_reader = csv.reader(file)
    interests = []
    for row in csv_reader:
        interests.append(row[0])
    only_interests = interests_with_header[1:]
    main(interests)
