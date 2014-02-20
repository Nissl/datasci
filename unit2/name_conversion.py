import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    baseball_data = pandas.read_csv(path_to_csv)
    #print baseball_data ['nameFirst']
    baseball_data['nameFull'] = baseball_data['nameFirst'] + " " + baseball_data['nameLast']
    baseball_data.to_csv(path_to_new_csv)
    return

def read_file(path_to_csv):
    print path_to_csv
    baseball_data = pandas.read_csv(path_to_csv)
    print baseball_data['nameFull']
    return

local_dir = "/Users/johnmorgan/datasci/unit2"
input_file = "%s/names_short.csv" % local_dir
output_file = "%s/output.csv" % local_dir
add_full_name(input_file, output_file)

read_file(output_file)    