import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import re

# Ensure you have downloaded the NLTK stopwords
nltk.download('stopwords')

def analyze_chat_log(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Strip any leading/trailing spaces from the column headers
    df.columns = df.columns.str.strip()

    # Clean the 'Date' column by stripping spaces
    df['Date'] = df['Date'].str.strip()

    # Convert 'Date' and 'Time' columns to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    df['Time'] = pd.to_datetime(df['Time'].str.strip(), format='%H:%M:%S', errors='coerce').dt.time

    # Drop rows with NaT in 'Date' or NaT in 'Time'
    df.dropna(subset=['Date', 'Time'], inplace=True)
    
    # 1. Top 10 participants
    top_participants = df['Sender'].value_counts().head(15)
    print("Top 10 Participants:")
    print(top_participants)
    
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
        # Remove punctuation and convert to lowercase
        message = re.sub(r'[^\w\s]', '', message).lower()
        return message

    # Combine all messages into a single string
    all_messages = ' '.join(df['Message'].apply(preprocess_message))
    
    # Tokenize the string into words
    words = all_messages.split()
    
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    # Get the 20 most common words
    most_common_words = word_freq.most_common(20)
    print("\nMost Commonly Used Words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")
    
    # Plot the top 10 participants
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_participants.values, y=top_participants.index, palette='viridis')
    plt.title('Top 10 Participants')
    plt.xlabel('Number of Messages')
    plt.ylabel('Participant')
    plt.show()
    
    # Plot the message count by hour
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

# Example usage
csv_file_path = 'python_byo_chat_log.csv'  # Replace with the path to your CSV file
analyze_chat_log(csv_file_path)
