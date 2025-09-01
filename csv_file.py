# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 08:52:11 2025

@author: P.Andise
"""

import csv

# read csv file

my_file = open("products.csv")
my_cvs = csv.DictReader(my_file)
# my_file.close()
process_data=[]

for i in 

my_write_file = open("products2.csv" ,mode="w", newline='')
csv_write = csv.writer(my_write_file, delimiter='|' )

csv_write.writerow("product Name", "Price" , "Quantity" , "Total Price")

total=[]

for i in range(1,5) :
    my_cvs.
    total=i[1]*i[2]
  
    for j in range(1,5):
        total=int(mylist[1])*int(mylist[2])
  
print(total)    

