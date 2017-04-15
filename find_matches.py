import sys
import csv
import re

input_file = sys.argv[1]
matching_type = sys.argv[2].lower()


def find_matches(input_file, matching_type):
    """ Takes a .csv input file and a matching type and returns a copy of the original csv with the unique identifier of the person each row represents prepended to the row.

    Matching types:
    > email
    > phone
    > email_phone
    """

    with open(input_file, 'rU') as csv_file_in:
        reader = csv.reader(csv_file_in)

        rownum = 0
        header = None
        email_col = None
        email_col_2 = None
        phone_col = None
        phone_col_2 = None  # For secondary phone column if it exists

        # Keep track of entry duplicates/key assignments
        ids = {}
        key = ''
        id = 1

        # Declare the header for the file
        for row in reader:
            if rownum == 0:
                header = row
                rownum += 1
                break

        # Get the column number for email
        for col in range(len(header)):
            if 'email2' in header[col].lower():
                email_col_2 = col
            if 'email1' in header[col].lower() or 'email' == header[col].lower():
                email_col = col

        # Get the column number for phone(s)
        for col in range(len(header)):
            if 'phone2' in header[col].lower():
                phone_col_2 = col
            if 'phone1' in header[col].lower() or 'phone' == header[col].lower():
                phone_col = col

        # Iterate through each row (excluding header) to find matches
        with open('output_file.csv', 'w') as csv_file_out:
            writer = csv.writer(csv_file_out)

            # Add 'id' column to header
            header = ['id'] + header

            # Write header row to new file
            writer.writerow(header)

            # Write subsequent rows to new file with id value from ids dictionary
            for row in reader:

                # Clean phone numbers to 10 digit integers before finding matches
                # Assigns the phone number as the dictionary key
                if matching_type == 'phone' or matching_type == 'email_phone':
                    key1 = re.sub('\D+','',row[phone_col])
                    if len(key1) > 10:
                        key1 = key1[1:]

                    key2 = re.sub('\D+','',row[phone_col_2])
                    if len(key2) > 10:
                        key2 = key2[1:]

                # Assigns the email as the dictionary key
                if matching_type == 'email' or matching_type == 'email_phone':
                    key1 = row[email_col].lower()
                    key2 = row[email_col_2].lower()

                # Pairs the email/phone with an id in the dictionary if one exists
                if key1:
                    ids[key1] = ids.get(key1, id)
                if key2:
                    ids[key2] = ids.get(key2, id)

                # Determines the id values in each row
                if key1 and key2:
                    if ids[key1] != ids[key2]:
                        row_ids = '{},{}'.format(ids[key1], ids[key2])
                    else:
                        row_ids = ids[key1]
                elif not key1:
                    row_ids = ids[key2]
                elif not key2:
                    row_ids = ids[key1]

                row = [row_ids] + row
                writer.writerow(row)
                id += 1







find_matches(input_file, matching_type)


