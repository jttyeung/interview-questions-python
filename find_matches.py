import sys
import csv
import re


class FindMatches(object):
    """ Takes a .csv input file and a matching type and returns a copy of the original csv with the unique identifier of the person each row represents prepended to the row.

    Matching types:
    > email
    > phone
    > email_phone
    """

    def __init__(self, input_file, matching_type):
        """ Opens the csv file and declares the phone and email columns. """

        # Check if matching_type input is valid
        self.matching_type = matching_type.lower()
        if self.matching_type not in ['email', 'phone', 'email_phone']:
            print "Please use a valid matching type: 'email', 'phone', or 'email_phone'."

        # Initialize variables for later assignment
        self.input_file = input_file
        self.rownum = 0
        self.header = None
        self.email_col = None
        self.email_col_2 = None
        self.phone_col = None
        self.phone_col_2 = None

        # Keep track of entry duplicates/key assignments via ids dictionary
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

        # # Runs matching type tests based on match type given
        # for row in reader:
        #     if self.matching_type == 'email':
        #         email_key = self.email_match(row)
        #         self.write_csv(row, email_key, self.header)
        #     elif self.matching_type == 'phone':
        #         phone_key = self.phone_match(row)
        #         self.write_csv(row, phone_key, self.header)
        #     elif self.matching_type == 'email_phone':
        #         self.email_match(row)
        #         self.phone_match(row)

        #     # Increments id in ids dictionary for unique row ids
        #     self.id += 1

        # Write to csv after all ids are assigned
        self.write_csv(reader, self.header)


    # def email_match(self, row):
    #     """ Creates email tuples and insert unique tuples into the ids dictionary. """

    #     # Creates a sorted list of emails
    #     # ids_key = sorted([row[self.email_col].lower(), row[self.email_col_2].lower()])
    #     ids_key = row[self.email_col].lower()
    #     self.add_key_to_dict(ids_key)
    #     if self.email_col_2:
    #         ids_key = row[self.email_col_2].lower()
    #         self.add_key_to_dict(ids_key)
    #     # Puts list of emails into a tuple for the dictionary
    #     # ids_key = tuple(ids_key)
    #     return ids_key


    def email_match(self, row, column):
        """ Creates email tuples and insert unique tuples into the ids dictionary. """

        ids_key = row[column].lower()
        self.add_key_to_dict(ids_key)

        return ids_key


    def phone_match(self, row, column):
        """ Creates phone tuples and insert unique tuples into the ids dictionary. """

        # Removes formatting of phone numbers for direct comparison
        format_phone_col = re.sub('\D+','',row[column])

        if len(format_phone_col) > 10:
            format_phone_col[1:]

        ids_key = format_phone_col
        self.add_key_to_dict(ids_key)

        return ids_key

    # def phone_match(self, row):
    #     """ Creates phone tuples and insert unique tuples into the ids dictionary. """

    #     # Removes formatting of phone numbers for direct comparison
    #     format_phone_col = re.sub('\D+','',row[self.phone_col])
    #     format_phone_col_2 = re.sub('\D+','',row[self.phone_col_2])

    #     if len(format_phone_col) > 10:
    #         format_phone_col[1:]
    #     if len(format_phone_col_2) > 10:
    #         format_phone_col_2[1:]

    #     # Creates a sorted list of emails
    #     # ids_key = sorted([format_phone_col, format_phone_col_2])
    #     ids_key = format_phone_col
    #     self.add_key_to_dict(ids_key)
    #     if self.format_phone_col_2:
    #         ids_key = format_phone_col_2
    #         self.add_key_to_dict(ids_key)


    def add_key_to_dict(self, ids_key):
        """ Places keys into a dictionary. If the key exists the key-value pair does not change. Otherwise, place it in the dictionary and assign it a new id. """

        self.ids[ids_key] = self.ids.get(ids_key, self.id)


    def write_csv(self, reader, header, row_is_header=True):
        """ Using a csv writer, creates a copy of the file with unique ids prepended to each row. """

        csv_file_out = open('output_file.csv', 'w')
        writer = csv.writer(csv_file_out)

        while row_is_header:
            # Add 'id' column to header
            header = ['id'] + self.header

            # Write header row to new file
            writer.writerow(header)

            row_is_header = False

        # Runs matching type tests based on match type given
        for row in reader:
            row_id = None

            if self.matching_type == 'email':

                if row[self.email_col_2]:
                    ids_key = self.email_match(row, self.email_col_2)

                    if self.ids.get(ids_key):
                        row_id = self.ids.get(ids_key)

                if row[self.email_col] and row_id is None:
                    ids_key = self.email_match(row, self.email_col)
                    row_id = self.ids.get(ids_key, self.id)


            elif self.matching_type == 'phone':

                if row[self.phone_col_2]:
                    ids_key = self.phone_match(row, self.phone_col_2)

                    if self.ids.get(ids_key):
                        row_id = self.ids.get(ids_key)

                if row[self.phone_col] and row_id is None:
                    ids_key = self.phone_match(row, self.phone_col)
                    row_id = self.ids.get(ids_key, self.id)



            elif self.matching_type == 'email_phone':
                self.email_match(row)
                self.phone_match(row)

            # Writes the new row: id of the row + copied csv row
            # row_id = self.ids[ids_key]
            new_row = [row_id] + row
            writer.writerow(new_row)

            # Increments id in ids dictionary for unique row ids
            self.id += 1

        # Gets the row id value from the dictionary:
        # for row in reader:
            # if self.matching_type == 'email':
            #     row_id = ids[email]
            # elif self.matching_type == 'phone':
            #     self.phone_match(row)
            # elif self.matching_type == 'email_phone':
            #     self.email_match(row)
            #     self.phone_match(row




FindMatches(input_file=sys.argv[1], matching_type=sys.argv[2])


