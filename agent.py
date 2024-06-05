# Import the necessary modules
from dotenv import load_dotenv  # Used to load environment variables from a .env file
import os  # Used to access environment variables
from openai import OpenAI  # Used to interact with the OpenAI API
from termcolor import colored  # Used to add color to console output
from tools import get_transcript, fetch_website_data, save_to_file, web_search, news_search  # Import custom tool functions from tools.py file
from tools_schema import tools  # Import the tool schema from tools_schema.py file


# Load environment variables from a .env file. These are where you will keep your API keys.
load_dotenv(override=True, dotenv_path=".env")

# Get the OpenAI API key from the environment variables from the .env file using the os and dotenv modules
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAI client using the API key. This client will be used to interact with the OpenAI API.
client = OpenAI(api_key=OPENAI_API_KEY)

# Specify the GPT model to use. This can be changed to any other model available in your OpenAI organization. For example, "gpt-4" or "gpt-3.5-turbo".
GPT_MODEL = "gpt-4o"

def chat_completion_request(messages, tools=None, tool_choice="auto", model=GPT_MODEL):
    try:
        # Send a request to the OpenAI API to generate a chat completion response
        # You can find more details about the parameters and response in the OpenAI API documentation: https://platform.openai.com/docs/api-reference/chat/create
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response

    except Exception as e:
        # Handle any exceptions that occur during the API request
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
    
# Define a system message that introduces the assistant and provides some instructions
system_message = """
You are an assistant called Steve, you reply in a friendly conversational tone. 
You use tools to trigger functions which provide you with relevant information.
Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.
"""

# Create an empty list to store the messages exchanged between the user and the assistant. Note that this will recent everytime you run the main.py file.
messages = []

# Append the system message to the messages list with the role "system"
messages.append({"role": "system", "content": system_message})

def assistant(user_input, messages):
    messages.append({"role": "user", "content": user_input})  # Append user input to the messages list with the role "user"
    chat_response = chat_completion_request(messages, tools=tools)  # Call the chat_completion_request function to get a chat completion response
    assistant_message = chat_response.choices[0].message  # Get the message from the first choice in the chat completion response
    messages.append(assistant_message)  # Append the assistant message to the messages list

    tool_calls = assistant_message.tool_calls  # Get the tool calls from the assistant message
    if tool_calls:  # Check if there are any tool calls
        tool_call_id = tool_calls[0].id  # Get the ID of the first tool call
        tool_function_name = tool_calls[0].function.name  # Get the name of the function called by the tool

        print(colored(f"Function call requested: {tool_function_name}", "cyan"))  # Print the name of the function called

        # Check the name of the function called and execute the corresponding code block
        if tool_function_name == 'fetch_website_data':
            url = eval(tool_calls[0].function.arguments)['url']  # Get the url argument from the tool call
            results = fetch_website_data(url)  # Call the fetch_website_data function with the url argument
        elif tool_function_name == 'web_search':
            query = eval(tool_calls[0].function.arguments)['query']  # Get the query argument from the tool call
            region = eval(tool_calls[0].function.arguments)['region']  # Get the region argument from the tool call
            timelimit = eval(tool_calls[0].function.arguments)['timelimit']  # Get the timelimit argument from the tool call
            max_results = eval(tool_calls[0].function.arguments)['max_results']  # Get the max_results argument from the tool call
            results = web_search(query, region, timelimit, max_results)  # Call the web_search function with the query, region, timelimit, and max_results arguments
        elif tool_function_name == 'news_search':
            query = eval(tool_calls[0].function.arguments)['query']  # Get the query argument from the tool call
            region = eval(tool_calls[0].function.arguments)['region']  # Get the region argument from the tool call
            timelimit = eval(tool_calls[0].function.arguments)['timelimit']  # Get the timelimit argument from the tool call
            max_results = eval(tool_calls[0].function.arguments)['max_results']  # Get the max_results argument from the tool call
            results = news_search(query, region, timelimit, max_results)  # Call the news_search function with the query, region, timelimit, and max_results arguments
        elif tool_function_name == 'get_transcript':
            video_url = eval(tool_calls[0].function.arguments)['video_url']  # Get the video_url argument from the tool call
            results = get_transcript(video_url)  # Call the get_transcript function with the video_url argument
        elif tool_function_name == 'save_to_file':
            text_content = eval(tool_calls[0].function.arguments)['text_content']  # Get the text_content argument from the tool call
            file_path = eval(tool_calls[0].function.arguments)['file_path']  # Get the file_path argument from the tool call
            results = save_to_file(text_content, file_path)  # Call the save_to_file function with the text_content and file_path arguments
        else:
            results = f"Error: function {tool_function_name} does not exist"  # Set the results to an error message if the function name is not recognized

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": tool_function_name,
            "content": results
        })  # Append a tool message to the messages list with the tool call ID, function name, and results

        model_response_with_function_call = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  # Call the OpenAI API to generate a chat completion response with the updated messages list
        response_to_function = model_response_with_function_call.choices[0].message  # Get the message from the first choice in the chat completion response
        messages.append(response_to_function)  # Append the response to the function call to the messages list
        return response_to_function.content  # Return the content of the response to the function call
    else:
        return assistant_message.content  # Return the content of the assistant message


