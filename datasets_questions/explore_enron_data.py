#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])
#print sorted(enron_data.keys())

# Iterate keys in enron_data, and sum True values for 'poi' sub-key
print "# of POIs ==", sum(enron_data[x]['poi'] for x in enron_data)

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Of the top three executives, who took home the most total payments?
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]# This guy
print enron_data["FASTOW ANDREW S"]["total_payments"]

# How many folks have a quantified salary? Known email address?
print sum(enron_data[x]["salary"] != 'NaN' for x in enron_data)
print sum(enron_data[x]["email_address"] != 'NaN' for x in enron_data)

# How many folks have NaN for their total payments? What percent of the whole?
totalPaymentsNaN = sum(enron_data[x]["total_payments"] == 'NaN' for x in enron_data)
percentOfTotal = 1.0 * totalPaymentsNaN / len(enron_data)
print "# of total_payments == NaN --", totalPaymentsNaN
print "% of total_payments == NaN --", percentOfTotal

# How many persons of interest have NaN for their total payments?
totalPaymentsNaNPoI= sum(enron_data[x]["total_payments"] == 'NaN'
                        and enron_data[x]['poi'] for x in enron_data)
print totalPaymentsNaNPoI
                            