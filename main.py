import functions
import numpy as np

filename = 'table42.txt'

admittances_array = functions.read_textfile(filename, skiprows=1)
#print(admittances_array)                                            #look at textfile to see what is what. Does not really matter dont bother
plot_real = functions.plots_epsilon(admittances_array, realpart=True)

# next is generated for possible cover image
# We're going to do this differently however, because parsing the dataset results in problems.
# We're making a new function, however making the other curves transparent
# This code is horrible.

plot_cover = functions.plots_epsilon_cover(admittances_array, realpart=True)
