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

if __name__ == '__main__':
    # --- Replace with your Video ID ---
    VIDEO_ID = "YOUR_VIDEO_ID"
    # -----------------------------------------

    # Check if running in Google Colab
    try:
        from google.colab import userdata
        API_KEY = userdata.get('YOUTUBE_API_KEY')
    except ImportError:
        API_KEY = "YOUR_API_KEY" # Fallback for local execution

    if API_KEY == "YOUR_API_KEY" or VIDEO_ID == "YOUR_VIDEO_ID":
        print("Please replace 'YOUR_VIDEO_ID' with your actual Video ID.")
        print("If running locally, also replace 'YOUR_API_KEY' with your YouTube Data API Key.")
    else:
        # 1. Get comments from the video
        video_comments = get_video_comments(API_KEY, VIDEO_ID)

        if video_comments:
            # 2. Analyze the sentiment of the comments
            sentiment_df = analyze_sentiment(video_comments)

            # 3. Get the overall sentiment
            overall_sentiment_score = get_overall_sentiment(sentiment_df)

            # Print the results
            print("--- Sentiment Analysis Results ---")
            print(sentiment_df)
            print("\n--- Overall Sentiment ---")
            print(f"The overall sentiment score for the video is: {overall_sentiment_score:.4f}")
        else:
            print("No comments found or an error occurred.")
