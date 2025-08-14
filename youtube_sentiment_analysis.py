from googleapiclient.discovery import build
from transformers import pipeline
import pandas as pd

def get_video_comments(api_key, video_id):
    """
    Fetches all top-level comments for a YouTube video using the YouTube Data API.
    """
    try:
        # Build the API client
        youtube = build('youtube', 'v3', developerKey=api_key)

        comments = []
        next_page_token = None

        while True:
            # Call the commentThreads.list method
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            ).execute()

            # Extract comment text and store it
            for item in response['items']:
                comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment_text)

            # Check for the next page of results
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break  # No more pages, exit the loop

        return comments

    except Exception as e:
        print(f"An error occurred while fetching comments: {e}")
        return []

def analyze_sentiment(comments_list):
    """
    Performs sentiment analysis on a list of comments using a Hugging Face pipeline.
    Returns a DataFrame with the comments and their sentiment.
    """
    # Create the sentiment analysis pipeline
    sentiment_classifier = pipeline("sentiment-analysis")

    # The pipeline can handle a list of strings directly
    sentiment_results = sentiment_classifier(comments_list)

    # Create a DataFrame to store the results
    results_df = pd.DataFrame(comments_list, columns=['comment'])
    results_df['sentiment_label'] = [result['label'] for result in sentiment_results]
    results_df['sentiment_score'] = [result['score'] for result in sentiment_results]

    return results_df

def get_overall_sentiment(df):
    """
    Calculates the overall sentiment from the dataframe.
    """
    # Simple average of scores for overall sentiment
    overall_sentiment = df['sentiment_score'].mean()
    return overall_sentiment

import json
import matplotlib.pyplot as plt # Added import
import seaborn as sns # Added import
from sklearn.metrics import confusion_matrix # Added import

if __name__ == '__main__':
    # Check if running in Google Colab
    try:
        from google.colab import userdata
        API_KEY = userdata.get('YOUTUBE_API_KEY')
    except ImportError:
        import os
        API_KEY = os.environ.get('YOUTUBE_API_KEY', "YOUR_API_KEY") # Fallback for local execution

    if API_KEY == "YOUR_API_KEY":
        print("Please set your YOUTUBE_API_KEY environment variable or Colab secret.")
    else:
        try:
            with open('video_list.json', 'r') as f:
                video_data = json.load(f)
        except FileNotFoundError:
            print("Error: video_list.json not found. Please create it with your test video data.")
            video_data = []

        if not video_data:
            print("No video data found in video_list.json. Please add videos to test.")

        true_labels = [] # Initialize list for true labels
        predicted_labels = [] # Initialize list for predicted labels

        for video_info in video_data:
            video_id = video_info.get('videoId')
            expected_sentiment = video_info.get('sentiment')
            video_title = video_info.get('title', 'Unknown Title')

            if not video_id:
                print(f"Skipping video with missing ID: {video_title}")
                continue

            print(f"\n--- Analyzing Video: {video_title} (ID: {video_id}) ---")
            print(f"Expected Sentiment: {'Positive' if expected_sentiment == 1 else 'Negative' if expected_sentiment == 0 else 'N/A'}")

            video_comments = get_video_comments(API_KEY, video_id)

            if video_comments:
                sentiment_df = analyze_sentiment(video_comments)
                overall_sentiment_score = get_overall_sentiment(sentiment_df)

                print("\n--- Sentiment Analysis Results ---")
                print(sentiment_df)
                print(f"\nOverall Sentiment Score: {overall_sentiment_score:.4f}")

                # Simple comparison for demonstration
                model_predicted_sentiment = 1 if overall_sentiment_score >= 0.5 else 0 # Assuming 0.5 as threshold
                print(f"Model Predicted Sentiment: {'Positive' if model_predicted_sentiment == 1 else 'Negative'}")

                if expected_sentiment is not None:
                    if model_predicted_sentiment == expected_sentiment:
                        print("Result: MATCHES EXPECTED SENTIMENT!")
                    else:
                        print("Result: DOES NOT MATCH EXPECTED SENTIMENT!")
                    true_labels.append(expected_sentiment) # Append true label
                    predicted_labels.append(model_predicted_sentiment) # Append predicted label
                else:
                    print("No expected sentiment provided for comparison.")
            else:
                print("No comments found or an error occurred for this video.")

        # Plotting the Confusion Matrix
        if len(true_labels) > 0 and len(predicted_labels) > 0:
            print("\n--- Generating Confusion Matrix ---")
            cm = confusion_matrix(true_labels, predicted_labels, labels=[0, 1]) # Labels for Negative (0) and Positive (1)
            
            plt.figure(figsize=(6, 5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                        xticklabels=['Predicted Negative', 'Predicted Positive'],
                        yticklabels=['Actual Negative', 'Actual Positive'])
            plt.xlabel('Predicted Label')
            plt.ylabel('True Label')
            plt.title('Confusion Matrix')
            plt.savefig('confusion_matrix.png')
            print("Confusion matrix saved as 'confusion_matrix.png'")
        else:
            print("\nNot enough data to generate a confusion matrix.")
