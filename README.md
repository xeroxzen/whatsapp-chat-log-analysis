# WhatsApp Chat Analyzer

This project consists of three primary scripts: one for parsing WhatsApp chat logs into a CSV format and the other two for analyzing individual WhatsApp chat logs and group chat logs. The aim is to help you gain insights into your WhatsApp conversations through various visualizations and statistics. Hopefully!

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Parsing WhatsApp Chats](#parsing-whatsapp-chats)
   - [Analyzing Individual Chats](#analyzing-individual-chats)
   - [Analyzing Group Chats](#analyzing-group-chats)
5. [Output](#output)
6. [License](#license)

## Overview

This project contains three important scripts

1. **Chat Parser Script** Parses a WhatsApp chat exported as a `.txt` file into a CSV file with the following columns: Date, Time, Sender, and Message.
2. **Two Chat Analyzer Scripts** Analyzes the generated CSV file to provide insights such as the number of messages sent by each participant, the most active day, the most active time of day, commonly used words, and more. You can certainly extend these scripts to include more analysis based on your requirements.

## Prerequisites

To run these scripts, you need the following:

- Python 3.6 or higher
- pandas
- nltk
- matplotlib
- seaborn
- wordcloud
- Data exported from WhatsApp as a `.txt` file

You can install the required packages using the following command. I highly recommend using a virtual environment to manage your dependencies.

```sh
pip3 install pandas nltk matplotlib seaborn wordcloud
```

Additionally, you need to download the NLTK stopwords

```sh
python3 -m nltk.downloader stopwords
```

## Installation

1. **Clone the Repository:**

   ```sh
   git clone git@github.com:xeroxzen/whatsapp-chat-log-analysis.git
   cd whatsapp-chat-log-analysis
   ```

2. **Install Dependencies:**
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage

### Parsing WhatsApp Chats

1. **Export Chat from WhatsApp**

   - Open WhatsApp and select the chat you want to analyze.
   - Go to the chat settings and select "Export Chat."
   - Choose to export "Without Media" and save the exported `.txt` file.

2. **Run the Chat Parser Script**
   - Place your exported `.txt` file in the project directory.
   - Run the script to parse the chat log into a CSV file.
     ```sh
     python3 parse_to_csv.py path_to_your_chat.txt
     ```
   - This will generate a CSV file in the project directory.

### Analyzing Individual Chats

1. **Run the Chat Analyzer Script**
   - Ensure the CSV file generated from the previous step is in the project directory.
   - Run the script to analyze the chat log.
     ```sh
     python3 analyze_chat.py
     ```
   - This script will read the CSV file, perform analysis, and generate visualizations.

### Analyzing Group Chats

2. **Run the Chat Analyzer Script**
   - Same as above, ensure the CSV file generated from the previous step is in the project directory.
   - Run the script to analyze the chat log.
     ```sh
     python3 analyze_group_chats.py
     ```
   - This script will read the CSV file, perform analysis, and generate visualizations.

## Output

The Chat Analyzer Script provides the following insights

1. **Comparison of Messages Sent:** Number of messages sent by each participant.
2. **Most Active Day:** The day with the highest number of messages.
3. **Most Active Time:** The hour of the day with the highest number of messages.
4. **Commonly Used Words:** A list of the most frequently used words in the chat.
5. **Top Participants:** A bar plot showing the top participants by message count.
6. **Messages Sent by Hour:** A line plot showing the number of messages sent by hour of the day.
7. **Word Cloud:** A word cloud visualization of the most frequently used words.

## Bonus

As bonus you can find Notebooks you can use to analyze the data in a more interactive way. You can find them in the `notebooks` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
