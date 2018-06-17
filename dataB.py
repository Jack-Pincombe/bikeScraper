import csv, sqlite3

'''
File that will be used to add data from the csv
to the database, that will later be used to 
organise the data from the cheapest etc
'''

connection = sqlite3.connect('database.db')

