import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import re

# NLTK stopwords download
nltk.download('stopwords')

def analyze_chat_log(csv_file_path):
    # Read the CSV file with the chats into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Strip any leading/trailing spaces from the column headers
    df.columns = df.columns.str.strip()

    # Stripping spaces from the Date column
    df['Date'] = df['Date'].str.strip()

    # Converting 'Date' and 'Time' columns to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    df['Time'] = pd.to_datetime(df['Time'].str.strip(), format='%H:%M:%S', errors='coerce').dt.time

    # Dropping rows with NaT in 'Date' or NaT in 'Time'
    df.dropna(subset=['Date', 'Time'], inplace=True)
    
    # 1. Comparison of messages sent between two participants
    participant1 = 'Prie♥️'  
    participant2 = 'Google Jr' 
    
    participant1_messages = df[df['Sender'] == participant1]
    participant2_messages = df[df['Sender'] == participant2]
    
    participant1_message_count = len(participant1_messages)
    participant2_message_count = len(participant2_messages)
    
    print(f"\nComparison of messages sent between {participant1} and {participant2}:")
    print(f"{participant1}: {participant1_message_count} messages")
    print(f"{participant2}: {participant2_message_count} messages")
    
    # 2. Day with the most activity
    most_active_day = df['Date'].value_counts().idxmax()
    print("\nDay with the most activity:", most_active_day.date())
    
    # 3. Most active time during the day
    df['Hour'] = df['Time'].apply(lambda x: x.hour)
    most_active_time = df['Hour'].value_counts().idxmax()
    print("\nMost active time during the day:", most_active_time, ":00")

    # 4. Commonly used words
    stop_words = set(stopwords.words('english'))
    def preprocess_message(message):
        # Removing punctuation and converting all words to lowercase
        message = re.sub(r'[^\w\s]', '', message).lower()
        return message

    # Combining all messages into a single string
    all_messages = ' '.join(df['Message'].apply(preprocess_message))
    
    # Tokenizing the string into words. Magic happens here!
    words = all_messages.split()
    
    # Removing stopwords
    words = [word for word in words if word not in stop_words]
    
    # Counting the frequency of each word using built-in Counter for efficiency
    word_freq = Counter(words)
    
    # Get the 20 most common words. You can filter out some words if needed e.g. yes, no, ok, etc.
    most_common_words = word_freq.most_common(20)
    print("\nMost Commonly Used Words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")
    
    # Getting the top participants
    top_participants = df['Sender'].value_counts().nlargest(2)
    
    # Plotting the participants
    top_participants = df['Sender'].value_counts().nlargest(2)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_participants.values, y=top_participants.index, palette='viridis')
    plt.title('Top Participants')
    plt.xlabel('Number of Messages')
    plt.ylabel('Participant')
    plt.show()
    
    # Message count by hour
    hourly_counts = df['Hour'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o')
    plt.title('Messages Sent by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Messages')
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.show()
    
    # Generate a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_messages)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Commonly Used Words')
    plt.show()

# How to use the function
csv_file_path = 'whatsapp_chat_with_prie.csv'  # Place the path to your CSV file here
analyze_chat_log(csv_file_path)
