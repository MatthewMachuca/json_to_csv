
Overview

Customers of our API Hub suite have routinely asked for data fields/api attributes in CSV format.
This script will take a JSON response, of nested dictionaries and arrays, and create a CSV formatted version of the API response.


Usage

The program accepts the file name of a Complex nested JSON, flattens the values, and writes it to a CSV file.

The file must be located in the same directory of the main.py file.

The output will be named {filename}.csv



Script Details

The script first uses the 'flatten' library to flatten nested dictionaries/arrays in the JSON response.

It then takes this flattened dictionary, identifies the type of each attriute, and adds it to a pandas data frame.

This data fram is then output to the output CSV file
