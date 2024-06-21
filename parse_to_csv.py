"""A script that parses a .txt file to csv

- The script parses the file and writes the data to a csv file
- The script breaks down the data into 4 columns [date, time, sender, message]
- Date is the date the message was sent
- Time is the time the message was sent
- Sender is the person who sent the message
- Message is the message that was sent
- Date is in the format dd/mm/yyyy
- Time is in the format hh:mm:ss
"""

import csv
import re
import sys

def parse_chat_log(txt_file_path, csv_file_path):
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] (.+?): (.+)")
    
    # Reading the contents of the .txt file
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    # Writing to the CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # The column names for the CSV file
        csv_writer.writerow(['Date', 'Time', 'Sender', 'Message'])

        # Process the .txt file line by line
        for line in lines:
            match = pattern.match(line)
            if match:
                date, time, sender, message = match.groups()
                # Write the parsed data to the CSV file
                csv_writer.writerow([date, time, sender, message])

# How to run the script
txt_file_path = sys.argv[1]
csv_file_path = 'whatsapp_chat_with_prie.csv'

parse_chat_log(txt_file_path, csv_file_path)



    