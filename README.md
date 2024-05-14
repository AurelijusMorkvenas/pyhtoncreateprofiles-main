CI/CD Pipeline for Fake Customer Profiles

This repository demonstrates a CI/CD pipeline that generates, processes, tests, and deploys a list of fake customer profiles. 
The workflow is fully automated using GitHub Actions.

CI/CD Pipeline:

-runs generate.py -> creates profiles1.csv (fake list of customers)

-runs csvtojson.py -> changes profiles1.csv to data.json

-runs tests:
    -Verifies that the CSV file contains 12 columns.
    -Verifies that the CSV file contains 900+ rows.
    -Verifies that the JSON file contains all the required properties.
    -Verifies that the JSON file contains 900+ rows.

-deploys index.html + script.js + data.json to Github Pages
