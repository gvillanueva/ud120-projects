#!/usr/bin/python

def sortResidualError(entry):
    return entry[0] - entry[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    # create new list of residual errors
    errors = predictions - net_worths

    # combine relevant values into a list of tuples
    cleaned_data = zip(ages, net_worths, errors)
    
    # sort combined values by errors ascending
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    
    # return slice with largest 10% residual error removed
    return cleaned_data[:-int(len(cleaned_data) * 0.1)]

