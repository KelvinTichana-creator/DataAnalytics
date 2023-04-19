'''
*Author: Kelvin Carrington Tichana
*Course: ALX Data Analys Nanodegree
*Title: Udacity Project 1 - Data Inspection
*Due Date: 20th December 2022
'''

#importing necesarry libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


df = pd.read_csv('tmdb-movies.csv') #reading the csv file containing data of interest
print(df.head())   #print first 5 rows

df.info() #get all possible information

print(df.describe()) #get statistics


print(sum(df.duplicated()))
