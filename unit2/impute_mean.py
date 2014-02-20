from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    print baseball.describe()
    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))
    print baseball.describe()
    
    #YOUR CODE GOES HERE

    return baseball

def read_file(path_to_csv):
    print path_to_csv
    baseball_data = pandas.read_csv(path_to_csv)
    print baseball_data['nameFull']
    return

local_dir = "/Users/johnmorgan/datasci/unit2"
input_file = "%s/Master.csv" % local_dir
output_file = "%s/output.csv" % local_dir
baseball = imputation(input_file)

  