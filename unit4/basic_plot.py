from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year_csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/

    hr_year = pandas.read_csv(hr_year_csv)
    print (ggplot(hr_year, aes('yearID', 'HR')) + 
           geom_point(color = 'coral') + geom_line(color = 'coral') + 
           ggtitle('Home Runs by Year') + xlab('Year') + ylab('Home Runs'))
    
    #gg = #YOUR CODE GOES HERE
    #return gg
    return 0

local_dir = "/Users/johnmorgan/datasci/unit4"
input_file = "%s/hr_year.csv" % local_dir
print(lineplot(input_file))