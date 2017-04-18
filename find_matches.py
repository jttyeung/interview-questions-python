import sys
import csv
import re


class FindMatches(object):
    """ Takes a .csv input file and a matching type.

    Matching types:
    > email
    > phone
    > email_phone
    """

    def __init__(self, input_file, matching_type):
        """ Opens the csv file and declares the phone and email columns. """

        self.input_file = input_file
        self.matching_type = matching_type.lower()
        self.rownum = 0
        self.header = None
        self.email_col = None
        self.email_col_2 = None
        self.phone_col = None
        self.phone_col_2 = None

        # Keep track of entry duplicates/key assignments
        self.ids = {}
        self.id = 1

        # Open the file with a csv reader
        csv_file_in = open(self.input_file, 'rU')
        reader = csv.reader(csv_file_in)

        # Declare the header for the file
        for row in reader:
            if self.rownum == 0:
                self.header = row
                self.rownum += 1
                break

        # Get the column number(s) for email
        for col in range(len(self.header)):
            if 'email2' in self.header[col].lower():
                self.email_col_2 = col
            if 'email1' in self.header[col].lower() or 'email' == self.header[col].lower():
                self.email_col = col

        # Get the column number(s) for phone
        for col in range(len(self.header)):
            if 'phone2' in self.header[col].lower():
                self.phone_col_2 = col
            if 'phone1' in self.header[col].lower() or 'phone' == self.header[col].lower():
                self.phone_col = col

        # Runs matching type tests based on match type given and writes it to a csv
        for row in reader:
            if self.matching_type == 'email':
                self.email_match(row)
                self.write_csv(row, self.header)
            elif self.matching_type == 'phone':
                self.phone_match(row)
                self.write_csv(row, self.header)
            elif self.matching_type == 'email_phone':
                self.email_match(row)
                self.phone_match(row)
                self.write_csv(row, self.header)
            else:
                print "Please use a valid matching type: 'email', 'phone', or 'email_phone'."
            self.id += 1
        print ids

###  could probably combine both email and phone match into one thing.
###  use a parameter to take matching type into function and use it?

    def email_match(self, row):
        """ Creates email tuples and insert unique tuples into the ids dictionary. """

        # Creates a sorted list of emails
        ids_key = sorted([row[self.email_col].lower(), row[self.email_col_2].lower()])
        # Puts list of emails into a tuple for the dictionary
        ids_key = tuple(ids_key)
        # Places keys into dictionary
        # If key exists the key-value pair does not change,
        # otherwise place it in the dictionary and assign it a new id.
        self.ids[ids_key] = self.ids.get(ids_key, self.id)


    def phone_match(self, row):
        """ Creates phone tuples and insert unique tuples into the ids dictionary. """

        formatted_phone_col = re.sub('\D+','',row[phone_col])
        formatted_phone_col_2 = re.sub('\D+','',row[phone_col_2])

        formatted_phone_col = formatted_phone_col[1:] if len(formatted_phone_col) > 10
        # Creates a sorted list of emails
        ids_key = sorted([row[self.phone_col].lower(), row[self.phone_col_2]])
        # Puts list of emails into a tuple for the dictionary
        ids_key = tuple(ids_key)
        # Places keys into dictionary
        # If key exists the key-value pair does not change,
        # otherwise place it in the dictionary and assign it a new id.
        self.ids[ids_key] = self.ids.get(ids_key, self.id)


    def write_csv(self, row, header, row_is_header=True):
        # Create a new file with a csv writer
        csv_file_out = open('output_file.csv', 'w')
        writer = csv.writer(csv_file_out)

        while row_is_header:
            # Add 'id' column to header
            header = ['id'] + self.header

            # Write header row to new file
            writer.writerow(header)

            row_is_header = False


###  fix this
        # Gets the row id value from the dictionary:
        row_id = self.ids[]

        # Writes the new row: id of the row + copied csv row
        new_row = [row_id] + row
        writer.writerow(new_row)


FindMatches(input_file=sys.argv[1], matching_type=sys.argv[2])


