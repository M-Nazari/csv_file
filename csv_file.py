# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 08:52:11 2025

@author: Mahjoobe Nazari

this is a program that read a csv file and calculate a total price of product 
and then write it in a new csv file

"""

import csv


# read csv file

my_file = open("C:\\Users\\P.Andise\\tmp\\products.csv", encoding='utf-8')
my_csv = csv.DictReader(my_file)


process_data=[]
data ={} 

for row in my_csv :
    product = row["Product Name"]
    price = float(row["Price"])
    quantity = int(row["Quantity"])
    total = price * quantity         # calculate a total price
    
    process_data.append({"Products":product , "Price": price , "Quantity" : quantity , "Total" : total})

#print(process_data) 

# convert new data from list to dictionary

prod=[]
pric=[]
quan=[]
tot=[]

# print(process_data[0].keys())
for row in process_data:
    
    prod.append(row["Products"])
    pric.append(row["Price"])
    quan.append(row["Quantity"])
    tot.append(row["Total"])

#print(prod,pric,quan,tot)

data.update({ "Products": prod , "Price": pric , "Quantity" : quan , "Total" : tot})

print(data)    
 
# open new csv file to write

my_write_file = open("C:\\Users\\P.Andise\\tmp\\products2.csv" ,mode="w", newline='')

Title = ["Products", "Price", "Quantity", "Total"]

csv_write = csv.DictWriter(my_write_file, delimiter='|', fieldnames=Title)

csv_write.writeheader()
csv_write.writerow(data)

my_file.close()
my_write_file.close()

print("writing new csv file is don successfully")    

