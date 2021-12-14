

import json
import pandas as pd
from flatten_json import flatten

def json_tocsv(filename):

    file = filename

    partition = file.partition('.')

    csv_filename = partition[0]
    f = open(file)
    data= json.load(f)

    flat = flatten(data)



    flat_values = flat.values()
    flat_keys = flat.keys()
   

    t_hold = []

    for item in flat:
        t_hold.append(type(flat[item]))




    df = pd.DataFrame(
        {"Attribute": flat_keys,
        'Sample Value': flat_values,
        'Data Type': t_hold }
    )

   

    df.to_csv(f'{csv_filename}.csv')

    print(df)
    main()

def main():
    print('\n')
    print('\n')

    value = input('Press 1 to convert a file from json to csv, Press 2 to quit: ')
    print('\n')
    if value == '1':
        f = input('please enter the file name,please include the extension i;e [.json] :')
        print('\n')
        json_tocsv(f)
    elif value == '2':
        exit()
    else:
        main()

main()
