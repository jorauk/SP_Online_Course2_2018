"""
pickle etc
"""

import pickle
import shelve
import csv
import json

import pprint
import seed_data


def run_simple_example():
    """Various persistence and serialization scenarios."""

    furniture_items = seed_data.get_furniture_data()

    def run_pickle():
        """
        Write and read with pickle
        """
        print("\n\n====")
        print('Step 1: Demonstrate persistence with pickle')
        print('Write a pickle file with the furniture data')

        pickle.dump(furniture_items, open('../data/data.pkl', 'wb'))

        print('Step 2: Now read it back from the pickle file')
        read_data = pickle.load(open('../data/data.pkl', 'rb'))
        print('Step 3: Show that the write and read were successful')
        assert read_data == furniture_items
        print("and print the data")
        pprint.pprint(read_data)

    def run_shelve():
        """
        write and read with shelve

        """
        print("\n\n====")
        print("Step 4: Demonstrate working with shelve")
        shelf_file = shelve.open('../data/shelve.dat')
        print("Step 5: store data at key")
        shelf_file['key'] = furniture_items

        print("Step 6: Now retrieve a COPY of data at key")
        read_items = shelf_file['key']

        print("Check it worked")
        assert read_items == furniture_items

        print("And now print the copy")
        pprint.pprint(read_items)

        print("Step 7: delete data stored at key to cleanup and close")
        del shelf_file['key']
        shelf_file.close()

    def run_csv():
        """
        write and read a csv
        """
        print("\n\n====")
        peopledata = [
            ('John', 'second guitar', 117.45),
            ('Paul', 'bass', 22.01),
            ('George', 'lead guitar', 45.99),
            ('Ringo', 'drume', 77.0),
            ('Roger', 'vocals', 12.5),
            ('Keith', 'drums', 6.25),
            ('Pete', 'guitar', 0.1),
            ('John', 'bass', 89.71)
        ]
        print("Step 8: Write csv file")
        with open('../data/rockstars.csv', 'w') as people:
            peoplewriter = csv.writer(people)
            peoplewriter.writerow(peopledata)

        print("Step 9: Read csv file back")
        with open('../data/rockstars.csv', 'r') as people:
            people_reader = csv.reader(people, delimiter=',', quotechar='"')
            for row in people_reader:
                pprint.pprint(row)

    def run_json():
        print("\n\n====")
        print("Step 10: Look at working with json data")
        furniture = [{'product': 'Red couch','description': 'Leather low back'},
        {'product': 'Blue couch','description': 'Cloth high back'},
        {'product': 'Coffee table','description': 'Plastic'},
        {'product': 'Red couch','description': 'Leather high back'}]

        print("Step 11: Return json string from an object")
        furniture_string = json.dumps(furniture)

        print("Step 12: Print the json")
        pprint.pprint(furniture_string)

        print("Step 13: Returns an object from a json string representation")
        furniture_object = json.loads(furniture_string)
        print("Step 14: print the string")
        pprint.pprint(furniture_object)

    run_pickle()
    run_shelve()
    run_csv()
    run_json()

if __name__ == '__main__':
    run_simple_example()
