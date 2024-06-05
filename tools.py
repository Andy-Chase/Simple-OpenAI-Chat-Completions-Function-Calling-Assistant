# Import necessary libraries
from youtube_transcript_api import YouTubeTranscriptApi  # Library for retrieving YouTube video transcripts
from youtube_transcript_api.formatters import TextFormatter  # Library for formatting YouTube video transcripts
import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML
from duckduckgo_search import DDGS  # Library for performing DuckDuckGo searches

#region Functions
def fetch_website_data(url):
    """
    Fetches the text content from a  website.

    Given a URL of a website, this function scrapes
    the content of the page and returns the text found within the <body>.

    Args:
        url (str): The URL of the website.

    Returns:
        Optional[str]: The text content of the website's body, or None if any error occurs."""
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check for successful access to the webpage
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract the content of the <body> tag
            body_content = soup.find("body")
            # Return all the text in the body tag, stripping leading/trailing whitespaces
            return " ".join(body_content.stripped_strings) if body_content else None
        else:
            # Return None if the status code isn't 200 (success)
            return None
    except requests.RequestException:
        # Return None if any request-related exception is caught
        return None


def get_transcript(video_url):
    # Extract video ID from the URL
    video_id = video_url.split('v=')[1].split('&')[0]

    try:
        # Get the transcript using the video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript into plain text
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)

        return formatted_transcript
    except Exception as e:
        return str(e)


def save_to_file(file_content: str, file_path: str):
    """
    Saves the given text to a specified file path with the appropriate file extension.

    :param text_content: The text to save.
    :param file_path: The path where the file should be saved including the file extension.
    """
    try:
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(file_content)  # Write the content to the file
        return f"File saved successfully at {file_path}"  # Return success message
    except Exception as e:
        return f"Error saving markdown file: {str(e)}"  # Return error message if an exception occurs

def web_search(query: str, region: str = "wt-wt", timelimit: str = "7w", max_results: int = 5):
    """
    Searches the web using DuckDuckGo and returns the top search results.

    Args:
    keywords: keywords for query.
    # https://duckduckgo.com/duckduckgo-help-pages/settings/params
    region: Australia, United States, United Kingdom, Worldwide, etc. Defaults to "wt-wt" if not specified.
    timelimit: d, w, m, y. Defaults to None. To specify use number and d,m,y to resprest the period i.e 7 days = 7d, 1 week = 1w, 1 month = 1m, 1 year = 1y
        If user asks for the latest information, we can set the timelimit to 1w. Defaults to None if not specified.
    backend: api, html, lite. Defaults to api.
    max_results: max number of results. If None, returns results only from the first response. Defaults to 5.

    Returns:List of dictionaries with news search results."""

    if region == 'Australia':  # Check if region is Australia
        region = "au-en"  # Set region to Australia
    elif region == 'United States':  # Check if region is United States
        region = "us-en"  # Set region to the United States
    elif region == 'Wordlwide':  # Check if region is Worldwide
        region = "wt-wt"  # Set region to Worldwide
    elif region == 'United Kingdom':  # Check if region is United Kingdom
        region = "uk-en"  # Set region to the United Kingdom
    else:
        region = "wt-wt"  # Set region to Worldwide if no specific region is provided

    results = DDGS().text(  # Perform a text search using DuckDuckGo
        keywords=query,  # Set the search query
        region=region,  # Set the search region
        safesearch="off",  # Disable safe search
        max_results=max_results,  # Set the maximum number of results
        timelimit=timelimit,  # Set the time limit for search results
    )

    results_output = "\n\n".join(  # Join the search results with double line breaks
    [f"Title: {result['title']}\nURL: {result['href']}\nSummary: {result['body'].replace('<strong>', '').replace('</strong>', '')}"
    for result in results])  # Format the search results into a string

    return results_output  # Return the formatted search results

def news_search(query: str, region: str = "wt-wt", timelimit: str = "7w", max_results: int = 5):
    """
    Searches the web for news results using DuckDuckGo news api and returns the top search results.

    Args:
    keywords: keywords for query.
    # https://duckduckgo.com/duckduckgo-help-pages/settings/params
    region: Australia, United States, United Kingdom, Worldwide, etc. Defaults to "wt-wt" if not specified.
    timelimit: d, w, m, y. Defaults to None. To specify use number and d,m,y to resprest the period i.e 7 days = 7d, 1 week = 1w, 1 month = 1m, 1 year = 1y
        If user asks for the latest information, we can set the timelimit to 1w. Defaults to None if not specified.
    backend: api, html, lite. Defaults to api.
    max_results: max number of results. If None, returns results only from the first response. Defaults to 5.
    
    Returns: List of dictionaries with news search results.
    """

    if region == 'Australia':  # Check if region is Australia
        region = "au-en"  # Set region to Australia
    elif region == 'United States':  # Check if region is United States
        region = "us-en"  # Set region to the United States
    elif region == 'Worldwide':  # Check if region is Worldwide
        region = "wt-wt"  # Set region to Worldwide
    elif region == 'United Kingdom':  # Check if region is United Kingdom
        region = "uk-en"  # Set region to the United Kingdom
    else:
        region = "wt-wt"  # Set region to Worldwide if no specific region is provided

    results = DDGS().news(  # Perform a news search using DuckDuckGo
        keywords=query,  # Set the search query
        region=region,  # Set the search region
        safesearch="off",  # Disable safe search
        max_results=max_results,  # Set the maximum number of results
        timelimit=timelimit,  # Set the time limit for search results
    )

    results_output = "\n\n".join(  # Join the search results with double line breaks
        [f"Title: {result.get('title', 'No title')}\nURL: {result.get('href', 'No URL')}\nSummary: {result.get('body', 'No summary').replace('<strong>', '').replace('</strong>', '')}"
            for result in results]  # Format the search results into a string
    )
    return results_output  # Return the formatted search results
#endregion
