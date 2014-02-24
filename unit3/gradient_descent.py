import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write some code here that updates the values of theta a number of times equal to
    # num_iterations.  Everytime you have computed the cost for a given set of thetas,
    # you should append it to cost_history.  The function should return both the final
    # values of theta and the cost history.


    # My initial brute force nested loop method, too slow for the assignment
    # However, it does produce the right result!
    # Note that I had to "cheat" and look up m in the discussions because the 
    # instructor never mentioned it.
    # Without introducing m, alpha is WAY too high and I was getting 
    # nonsensical results.

    m = len(values)
    cost_history = []
    values = numpy.array(values)
    while num_iterations:
        cost_history.append(compute_cost(features, values, theta))
        for theta_index, theta_val in enumerate(theta):
            diff_sum = 0
            for val_index, value in enumerate(values):
                diff_sum += alpha / m * (values[val_index] - theta[theta_index]*features[val_index][theta_index])*features[val_index][theta_index]
            theta[theta_index] += diff_sum

        num_iterations -= 1


    # Actual submitted solution
    m = len(values)
    cost_history = []
    values = numpy.array(values)
    while num_iterations:
        cost_history.append(compute_cost(features, values, theta))
        theta += alpha / m * numpy.dot(values - (numpy.sum(theta * features, axis = 1)) , features)
        num_iterations -= 1

    return theta, pandas.Series(cost_history)