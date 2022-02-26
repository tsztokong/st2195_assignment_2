# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:33:26 2022

@author: ASUS
"""

#import beautifulsoup, urllib and pandas
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

#Open Url
url = urlopen("https://en.wikipedia.org/wiki/Comma-separated_values")
#Parse url
soup = BeautifulSoup(url, 'html.parser')


#find the table
table = soup.find("table", class_="wikitable")

#make the column titles into list
title = []
for i in table.tbody.find_all('th'):
    title.append(i.text)

#make data into list with suitable data types
data = []
data_row = []
for i in table.tbody.find_all('td'):
    try:
        data_row.append(int(i.text))
    except:
        try:
            data_row.append(float(i.text))
        except:
            data_row.append(i.text)
    #make the list become nested with length of each children the same as column names
    if len(data_row) == len(title):
        data.append(data_row)
        data_row = []

#put as dataframe and output as csv
csv_output = pd.DataFrame(data, columns = title)
csv_output.to_csv("csv_example_1.csv", index=False)


#Alternative route: use pd.read_html and select table as dataFrame
alternatives = pd.read_html("https://en.wikipedia.org/wiki/Comma-separated_values")[5]
alternatives.to_csv("csv_example_2.csv", index=False)

