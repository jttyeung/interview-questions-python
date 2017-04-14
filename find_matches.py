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
    > email&&phone
    """

    with open(input_file, 'rU') as csv_file_in:
        reader = csv.reader(csv_file_in)

        rownum = 0
        header = None
        email_col = None
        phone_col = None
        phone_col_2 = None  # For secondary phone column if it exists

        # Keep track of entry duplicates/key assignments
        ids = {}
        id = 1

        # Declare the header for the file
        for row in reader:
            if rownum == 0:
                header = row
                rownum += 1
                break

        # Get the column number for email
        if matching_type == 'email':
            for col in range(len(header)):
                if 'email' in header[col].lower():
                    email_col = col

        # Get the column number for phone(s)
        if matching_type == 'phone':
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
                phone_num = re.sub('\D+','',row[phone_col])
                if len(phone_num) > 10:
                    phone_num = phone_num[1:]
                ids[phone_num] = ids.get(phone_num, id)
                row = [ids[phone_num]]  + row
                writer.writerow(row)
                id += 1

                # email = row[email_col].lower()
                # ids[email] = ids.get(email, id)
                # row = [ids[email]] + row
                # writer.writerow(row)
                # id += 1





find_matches(input_file, matching_type)


