#!/usr/bin/env python3
"""
This script consists of two functions: populate_dictionary(filename) and find_email(argv). The function populate_dictionary(filename) reads the user_emails.csv file and populates a dictionary with name/value pairs. The other function, find_emails(argv), searches the dictionary created in the previous function for the user name passed to the function as a parameter. It then returns the associated email address. This script accepts employee's first name and last name as command-line arguments and outputs their email address.
The script accepts arguments through the command line. These arguments are stored in a list named sys.argv. The first element of this list, i.e. argv[0], is always the name of the file being executed. So the parameters, i.e., first name and last name, are then stored in argv[1] and argv[2] respectively.
Let's test the script now.
Since you know the contents of the user_emails.csv file, choose any name to be passed as a parameter, or you can use the following name:
"""
import csv
import sys
def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict
def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/mnt/d/Projects/Python/testing/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"
def main():
  print(find_email(sys.argv))
if __name__ == "__main__":
  main()