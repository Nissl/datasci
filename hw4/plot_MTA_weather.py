from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    turnstile_weather = pandas.read_csv(turnstile_weather)
    turnstile_unit = turnstile_weather[turnstile_weather.UNIT == 'R001']
    #weather_slice = turnstile_weather[:5]
    #print weather_slice
    #print turnstile_weather.columns.values.tolist()
    print (ggplot(turnstile_unit, aes('Hour', 'ENTRIESn_hourly')) + 
          geom_point(color = 'blue') +  
          ggtitle('Number of Entries by Hour at Station R001') + 
          xlab('Hour') + ylab('Number of Station Entries'))
    # print (ggplot(turnstile_weather, aes('rain', 'ENTRIESn_hourly')) + 
    #       geom_point() + ggtitle('Number of Entries by Rain Condition') + 
    #       xlab('Rain') + ylab('Number of Station Entries'))

    # This last one doesn't work, and I'm disinclined to dig through ggplot
    # print (ggplot(turnstile_weather, aes('UNIT', 'ENTRIESn_hourly')) + 
    #       geom_histogram() + ggtitle('Number of Entries by Station') + 
    #       xlab('Station') + ylab('Number of Station Entries'))

    plot = 0 # your code here
    return plot

local_dir = "/Users/johnmorgan/datasci/hw4"
input_file = "%s/turnstile_data_master_with_weather.csv" % local_dir
print(plot_weather_data(input_file))