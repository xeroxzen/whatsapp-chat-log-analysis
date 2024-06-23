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

import pandas as pd
import re
import sys

def parse_chat_log(txt_file_path, csv_file_path):
    pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{4}), (\d{2}:\d{2}:\d{2})\] (.+?): (.+)")
    data = []

    # Reading the contents of the .txt file
    with open(txt_file_path, "r", encoding="utf-8") as txt_file:
        lines = txt_file.readlines()

    current_message = ""
    current_date = ""
    current_time = ""
    current_sender = ""

    for line in lines:
        match = pattern.match(line)
        if match:
            if current_message:
                # Appending the previous message to the data list
                data.append([current_date, current_time, current_sender, current_message])
            current_date, current_time, current_sender, current_message = match.groups()
        else:
            # Appending the line to the current message
            current_message += "\n" + line.strip()

    if current_message:
        # Appending the last message to the data list
        data.append([current_date, current_time, current_sender, current_message])

    # Creating a DataFrame
    df = pd.DataFrame(data, columns=["Date", "Time", "Sender", "Message"])

    # Writing to the CSV file
    df.to_csv(csv_file_path, index=False, encoding="utf-8")

# How to run the script
txt_file_path = sys.argv[1]
csv_file_path = "./datasets/python_byo_chat_log.csv"

parse_chat_log(txt_file_path, csv_file_path)
