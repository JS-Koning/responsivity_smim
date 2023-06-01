import functions
import numpy as np

filename = 'table42.txt'

admittances_array = functions.read_textfile(filename, skiprows=1)
#print(admittances_array)                                            #look at textfile to see what is what.
plot_real = functions.plots_epsilon(admittances_array, realpart=False)
