def main(interests):
    # Print the interests
    print("Interests:")
    for interest in interests:
        print(interest)

    # Save the interests to a new file
    with open('processed_interests.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(interests)
