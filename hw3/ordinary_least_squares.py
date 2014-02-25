# Note that I did not fully complete this optional assignment. The EC2 instance
# timed out once I got statsmodels going and I was not too interested in stripping
# out the critical code, as do I have the linear algebra background to do so without
# cheating and copying other solutions in the forums (from which I already needed some 
# tips to get statsmodels running. Meh. Oddly enough the grader accepted my old 
# gradient descent code as an improvement!)

import numpy as np
import pandas
import scipy
import statsmodels

"""
In this optional exercise, you should complete the function called 
predictions(turnstile_weather). This function takes in our pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  

You should attempt to implement another type of linear regression, 
that you may have read about, such as ordinary least squares regression: 
http://en.wikipedia.org/wiki/Ordinary_least_squares

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~15%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting 
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""

def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    
    This should be the same code as the compute_cost function in the lesson #3 exercises. But
    feel free to implement your own.
    """
    
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This is the same gradient descent code as in the lesson #3 exercises. But feel free
    to implement your own.
    """
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        cost_history.append(compute_cost(features, values, theta))
        theta += alpha / m * np.dot(values - (np.sum(theta * features, axis = 1)) , features)
        #print i
    return theta, pandas.Series(cost_history)

def predictions(weather_turnstile):
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    features = weather_turnstile[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = weather_turnstile[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m)
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)

    theta_OLS = np.zeros(len(features.columns))

    # this caused a timeout on the official server, so I moved on.
    theta_OLS = statsmodels.OLS(values_array, features_array) 
    results = model.fit
    print results.summary() 

    # prediction = np.dot(features_array, theta_OLS)
    return prediction