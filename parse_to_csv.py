"""Write a script that will parse the .txt file I have open to csv

- The script should be able to parse the file and write the data to a csv file
- Break down the data into 4 columns [date, time, sender, message]
- Date is the date the message was sent
- Time is the time the message was sent
- Sender is the person who sent the message
- Message is the message that was sent
- Date is in the format dd/mm/yyyy
- Time is in the format hh:mm:ss

Here are some sample messages:

[17/12/2023, 13:50:14] ~ cypher: You mean the functionality for administration and managers ?
[17/12/2023, 13:50:17] ~ cypher: Does switching back to win 11 solve these issues
[17/12/2023, 13:50:32] Henry Ndou: Yes!
[17/12/2023, 13:57:31] ~ cypher: Okay l created another application but with access to the same database. The app has all privileges for administrators
[17/12/2023, 13:59:04] Henry Ndou: Using Java?
"""

import csv
import re
import sys

def parse_chat_log(txt_file_path, csv_file_path):
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] (.+?): (.+)")
    
    # Open the .txt file and read the content
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header row to the CSV file
        csv_writer.writerow(['Date', 'Time', 'Sender', 'Message'])

        # Process each line in the .txt file
        for line in lines:
            match = pattern.match(line)
            if match:
                date, time, sender, message = match.groups()
                # Write the parsed data to the CSV file
                csv_writer.writerow([date, time, sender, message])

# Example usage
txt_file_path = sys.argv[1]
csv_file_path = 'whatsapp_chat_with_prie.csv'

parse_chat_log(txt_file_path, csv_file_path)



    