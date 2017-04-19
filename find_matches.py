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
        self.email_col_2 = None
        self.email_col = None
        self.phone_col_2 = None
        self.phone_col = None

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

        # Write to csv after all ids are assigned
        self.write_csv(reader, self.header)


    def email_match(self, row):
        """ Creates email tuples and insert unique tuples into the ids dictionary. """

        row_id = None
        email2 = None
        email1 = None
        min_id = None

        # Check if email columns exist
        if self.email_col_2:
            email2 = row[self.email_col_2]
        if self.email_col:
            email1 = row[self.email_col]

        # Check if either email is in ids dictionary, get the value
        if email2 in self.ids or email1 in self.ids:
            email2_exists = self.ids.get(email2)
            email_exists = self.ids.get(email1)

            id_values = [email2_exists, email_exists]
            min_id = min(id for id in id_values if id is not None)

        # Assigns the id value to min_id if it exists, otherwise assigns it the next id value available
        if min_id:
            id = min_id
        else:
            id = self.id

        # Checks if a second email column exists
        if self.email_col_2:
            # Checks if value exists in second email column/row, and assigns it as the key
            if row[self.email_col_2]:
                email2 = row[self.email_col_2]
                self.add_key_to_dict(email2, id)

                # If key exists in dictionary, assign it the row_id
                if self.ids.get(email2):
                    row_id = self.ids.get(email2)

        if row[self.email_col]:
            email1 = row[self.email_col]
            self.add_key_to_dict(email1, id)
            row_id = self.ids.get(email1, self.id)


        if row_id is None:
            row_id = self.id

        return row_id


    def phone_match(self, row):
        """ Creates phone tuples and insert unique tuples into the ids dictionary. """

        row_id = None
        phone2 = None
        phone1 = None
        min_id = None

        def format_phone(column):
            """ Removes formatting of phone numbers for direct comparison. """

            format_phone_col = re.sub('\D+','',row[column])

            if len(format_phone_col) > 10:
                format_phone_col[1:]

            return format_phone_col


        # Check if phone columns exist
        if self.phone_col_2:
            phone2 = format_phone(self.phone_col_2)
        if self.phone_col:
            phone1 = format_phone(self.phone_col)

        # Check if either email is in ids dictionary, get the value
        if phone2 in self.ids or phone1 in self.ids:
            phone2_exists = self.ids.get(phone2)
            phone_exists = self.ids.get(phone1)

            id_values = [phone2_exists, phone_exists]
            min_id = min(id for id in id_values if id is not None)

        # Assigns the id value to min_id if it exists, otherwise assigns it the next id value available
        if min_id:
            id = min_id
        else:
            id = self.id

        #  Checks if a second phone column exists
        if self.phone_col_2:
            # Checks if value exists in second phone column/row, and assigns it as the key
            if row[self.phone_col_2]:
                ids_key = format_phone(self.phone_col_2)
                self.add_key_to_dict(ids_key, id)

                # If key exists in dictionary, assign it the row_id
                if self.ids.get(ids_key):
                    row_id = self.ids.get(ids_key)

        if row[self.phone_col]:
            ids_key = format_phone(self.phone_col)
            self.add_key_to_dict(ids_key, id)
            row_id = self.ids.get(ids_key, self.id)

        if row_id is None:
            row_id = self.id

        return row_id


    def add_key_to_dict(self, ids_key, id):
        """ Places keys into a dictionary. If the key exists the key-value pair does not change. Otherwise, place it in the dictionary and assign it a new id. """

        self.ids[ids_key] = self.ids.get(ids_key, id)


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
            email_row_id = None
            phone_row_id = None

            # If the matching type is 'email'
            if self.matching_type == 'email':
                # See if a second email column exists
                row_id = self.email_match(row)



            # If the matching type is 'phone'
            elif self.matching_type == 'phone':
                # See if a second phone column exists
                row_id = self.phone_match(row)


            # If the matching type is email OR phone
            elif self.matching_type == 'email_phone':
                row_id_email = self.email_match(row)
                row_id_phone = self.phone_match(row)

                if row_id_email < row_id_phone:
                    row_id = row_id_email
                else:
                    row_id = row_id_phone


            print self.ids
            new_row = [row_id] + row
            writer.writerow(new_row)

            # Increments id in ids dictionary for unique row ids
            self.id += 1



FindMatches(input_file=sys.argv[1], matching_type=sys.argv[2])


