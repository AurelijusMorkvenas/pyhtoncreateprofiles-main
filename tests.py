import unittest
import csv
import json

class TestFileContents(unittest.TestCase):

    def testcsvcolumns(self):
        # Open the CSV file and verify that it contains 12 columns
        with open('profiles1.csv', 'r') as file:
            reader = csv.reader(file)
            columns = next(reader)
            self.assertEqual(len(columns), 12)

    def testcsvrows(self):
        # Open the CSV file and verify that it contains 900+ rows
        with open('profiles1.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertTrue(len(rows) >= 900)

    def test_json_properties(self):
        # Open the JSON file and verify that it contains all required properties
        with open('data.json', 'r') as file:
            data = json.load(file)
            print("Data in JSON file:", data)
            expected_properties = [
                "Givenname",
                "Surname",
                "Streetaddress",
                "City",
                "Zipcode",
                "Country",
                "CountryCode",
                "NationalId",
                "TelephoneCountryCode",
                "Telephone",
                "Birthday",
                "ConsentToContact"
            ]
            print("Expected properties:", expected_properties)
            for obj in data:
                print("Object properties:", obj.keys())
            self.assertTrue(all(prop in obj for obj in data for prop in expected_properties))

    def test_json_rows(self):
        # Open the JSON file and verify that it contains 900+ rows
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertTrue(len(data) >= 900)


if __name__== '__main__':
    unittest.main()       