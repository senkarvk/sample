# sample

## Test Automation using python, Selenium, and Pytest
Ran sucessfully on windows with chrome browser

### Install :
Python Modules:
```bash
pip install -r requirements.txt
```
Download chrome webdriver and place it in the path
### To run :
use below command from parent folder:
```bash
pytest -s -v .\test\test_filter_data.py 
```

for running and  generating allure reports:
eg: 
```bash
pytest -s -v --alluredir="Reports\report1" .\test\test_filter_data.py 
```
script takes test data from 
\test_data\TableData.xlsx

## Test Flow:

- Reading Test data from xlsx sheet into a data structure list of lists   [filterdata,sortdata]  eg:  .
     ```bash
      [['s','impact score'],[]]
     ```
- itering over this test data.

- Getting the initial table rows in the application page.
     ```bash
      [['Man in the Middle', '95k', '8.12', 'high'], ['Password attack', '32.85M', '5', 'low'], ['Phishing', '25.12M', '7.18', 'low'], ['Session hijack', '9024
          ', '5.79', 'high'], ['SQL Injection', '1.25M', '10.21', 'medium'], ['XSS', '29850', '2.19', 'low']]
     ```
- Filter and sort using python logic to get the expected output.
    ```bash
      [['xss', 29850.0, 2.19, 0], ['password attack', 32850000.0, 5.0, 0], ['session hijack', 9024.0, 5.79, 2], ['phishing', 25120000.0, 7.18, 0], ['sql injection', 1250000.
        0, 10.21, 1]]
     ```
- Apply filter and sort on the application page, and get the table details for Actual output.
    ```bash
      [['xss', 29850.0, 2.19, 0], ['password attack', 32850000.0, 5.0, 0], ['session hijack', 9024.0, 5.79, 2], ['phishing', 25120000.0, 7.18,
       0], ['sql injection', 1250000.0, 10.21, 1]]
     ```
- comparing actual and expected asserting PASS or FAIL.


