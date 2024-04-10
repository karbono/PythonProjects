##Writing to CSV file and testing

w = open("csv.txt", "w")
w.write("Lorenzo,Aceituno,Moreno,España \n")
w.write("Andrea,Aceituno,Moreno,España \n")
w.write("Lourdes,Peñarrubia,Martínez,España \n")
w.close()

import os

with open("csv.txt") as we:
    for line in we:
        print(line)

os.remove("csv.txt")

##Reading CSV files

import csv

def print_csv():
    f = open("csv.txt")
    csv_f = csv.reader(f)
    for row in csv_f:
        name, surname, surname2, country = row
        print("Nombre: {}, Apellidos: {} {}, País: {}".format(name, surname, surname2, country))
    f.close()

print_csv()

##Generating CSV files

import csv

#We add the content

import csv
hosts = [["workstation.local", "192.168.1.100"], ["webserver.cloud", "192.168.2.100"]]
with open('hosts.csv', 'w', newline='') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#Create the function to format the data

import csv
def print_csv2():
    d = open("hosts.csv")
    csv_d = csv.reader(d)
    for rows in csv_d:
        name, ip = rows
        print("Nombre: {}, IP: {}".format(name, ip))
    d.close()

#Call the function
print_csv2()

#Remove the file to rewrite it
import os
d.close()
os.remove("hosts.csv")

with open("hosts.csv") as host_csv:
    for line in host_csv:
        print(line)

#Reading and writing CSV files with dictionaries

import csv
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open("by_department.csv") as department_csv:
    for line in department_csv:
        print(line)

#--------------------
#QUIZ Exercises
        
# Question 1
# We're working with a list of flowers and some information about each one. The create_file function writes 
# this information to a CSV file. The contents_of_file function reads this file into records and 
# returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function 
# to turn the data in the CSV file into a dictionary using DictReader.
        
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    dictionary = csv.DictReader(file)
    # Process each item of the dictionary
    for row in dictionary:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#Question 2
#Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process 
#the data without turning it into a dictionary. How do you skip over the header record with the field names?

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in rows:
      name, color, ty = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(name, color, ty)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))