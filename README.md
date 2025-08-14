# YouTube Comment Sentiment Analysis Pipeline

This project demonstrates a complete pipeline for fetching YouTube video comments, performing sentiment analysis using Hugging Face Transformers, and evaluating the model's performance.

## Motivation & Learning Objectives

This project was developed as a practical exercise to solidify several key concepts:

*   **Practicing with Google Cloud & API Integration:** Gaining hands-on experience with the YouTube Data API, including obtaining and securely managing API keys. This showcases the ability to integrate external services into a Python application.
*   **Building a Data Pipeline:** Understanding and implementing a full data flow from data acquisition (fetching comments) through processing (sentiment analysis) to evaluation (confusion matrix generation).
*   **Hugging Face Course Concepts:** Applying concepts learned from the Hugging Face course, particularly the use of the `transformers` library for Natural Language Processing (NLP) tasks like sentiment analysis.
*   **Secure Credential Handling:** Implementing best practices for managing sensitive API keys using environment variables for local development and Colab secrets for cloud execution.

## Features

*   **YouTube Comment Fetching:** Retrieves top-level comments for specified YouTube videos using the YouTube Data API.
*   **Sentiment Analysis:** Utilizes a pre-trained sentiment analysis model from the Hugging Face `transformers` library to determine the sentiment of each comment.
*   **Automated Testing:** Reads a `video_list.json` file containing video IDs and their expected sentiment labels (0 for negative, 1 for positive) to automate the testing process.
*   **Model Evaluation:** Generates a confusion matrix (`confusion_matrix.png`) to visually represent the performance of the sentiment analysis model against the predefined labels.

## Requirements

*   Python 3.x
*   `google-api-python-client`
*   `transformers`
*   `pandas`
*   `matplotlib`
*   `seaborn`
*   `scikit-learn`
*   A YouTube Data API Key.

## Setup and Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/MatteoAldovardi92/youtube-sentiment-analysis.git
    cd youtube-sentiment-analysis
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install google-api-python-client transformers pandas matplotlib seaborn scikit-learn
    ```

4.  **Obtain a YouTube Data API Key:**
    *   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project or select an existing one.
    *   Enable the `YouTube Data API v3` in the API Library.
    *   Create new credentials (API Key) and **restrict it** to the `YouTube Data API v3` for security.

5.  **Set Your API Key:**
    *   **Local Development:** Set the `YOUTUBE_API_KEY` environment variable in your terminal session:
        ```bash
        export YOUTUBE_API_KEY="your_actual_youtube_api_key_here"
        ```
        For persistence, add this line to your `~/.zshrc` (or `~/.bashrc`) file.
    *   **Google Colab:** When opening the notebook in Colab, use the "Secrets" tab (key icon on the left sidebar) to add a new secret named `YOUTUBE_API_KEY` with your actual key as its value.

6.  **Prepare `video_list.json`:**
    This file contains the video IDs and their expected sentiment for testing. An example `video_list.json` is included in the repository. You can modify it to include more videos.
    ```json
    [
      {
        "videoId": "Gyng335nKh4",
        "title": "Miss Italy and the 13-Year-Old Mascot: Rules, Consent, and Rights | BarbieXanax Factory",
        "sentiment": 0
      },
      {
        "videoId": "vWJvu2Fqcb4",
        "title": "Golden Retriever Puppy Settles into his Forever Home | Wonderful World of Puppies | BBC Earth",
        "sentiment": 1
      }
    ]
    ```

7.  **Run the Script:**
    ```bash
    python youtube_sentiment_analysis.py
    ```
    The script will fetch comments, perform sentiment analysis, print results for each video, and generate `confusion_matrix.png` in the project directory.

## Is this project worth of a portfolio?

Absolutely! While it might be a small project, it effectively demonstrates a range of valuable skills and concepts highly relevant in data science, machine learning, and software engineering:

*   **API Integration:** Practical experience consuming and managing external APIs (YouTube Data API).
*   **Natural Language Processing (NLP):** Application of pre-trained models from Hugging Face for a real-world NLP task (sentiment analysis).
*   **Data Pipeline Development:** Shows the ability to build a complete workflow from data acquisition to processing, analysis, and visualization.
*   **Model Evaluation:** Understanding and implementing evaluation metrics like the confusion matrix to assess model performance.
*   **Secure Credential Management:** Demonstrates awareness and implementation of best practices for handling sensitive information (API keys).
*   **Version Control:** Proper use of Git and GitHub for project management and collaboration.
*   **Problem-Solving:** The journey of setting up and troubleshooting (as documented in the `github_manual.md`) itself is a testament to problem-solving skills.

**Captivating Visuals:** The generated `confusion_matrix.png` provides a direct visual output of the project's analytical capability. You could also include a screenshot of the script running in a Colab notebook or a snippet of the console output in your README to make it more engaging.

This project serves as an excellent foundational piece to showcase your understanding of these interconnected concepts.
