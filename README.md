# Simple-OpenAI-Chat-Completions-Function-Calling-Assistant
Simple OpenAI Chat Completions Function Calling Assistant (With the actual functions not just the schema)

This repository provides a simple demonstration of an OpenAI Chat Completions assistant that uses function calling to gather data and inform its responses. The purpose is to showcase how AI can interact with various tools and APIs to fetch information and perform tasks such as creating local files.

This project needs only an OpenAI API Key and uses the DuckDuckGo API to search the web. In future, I will be adding more examples with more expansive features like Long-term memory, web search APIs (Tavily, SerpAPI and others) and web automation. I just wanted to keep this one as simple as possible as an introduction to function calling. 

## Project Structure

- `main.py`: Entry point of the application. Handles the interaction with the OpenAI API and manages the conversation flow.
- `agent.py`: Defines the assistant agent, including its functions and behaviour.
- `tools.py`: Contains implementations of the tools that the assistant can call.
- `tools_schema.py`: Defines the schema for the tools and their arguments.
- `requirements.txt`: Lists the dependencies required to run the project.

## Requirements

- Python 3.8 or higher
- Packages listed in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Andy-Chase/Simple-OpenAI-Chat-Completions-Function-Calling-Assistant

cd Simple-OpenAI-Chat-Completions-Function-Calling-Assistant
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Set up your OpenAI API key:

Create a `.env` file in the project root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

2. Run the application:

```bash
python main.py
```

## Functionality

The assistant can perform a variety of tasks by calling different tools. Here are some of the tools and their functionalities:

- **Web Search**: Perform a web search and return the top results.
- **News Search**: Search for news articles based on a query and region.
- **Get Transcript**: Fetch the transcript of a YouTube video.
- **Save to File**: Save a given text content to a specified file.
- **Fetch Data from site**: Extract the page data from a specified URL using BS4

## Tool Definitions

Tools are defined in `tools_schema.py` and implemented in `tools.py`. Each tool has a specific function and argument schema.

Example tool schema:

```python
{
    "name": "web_search",
    "description": "Perform a web search",
    "parameters": {
        "query": {"type": "string", "description": "The search query"},
        "region": {"type": "string", "description": "Search region"},
        "timelimit": {"type": "string", "description": "Time limit for search results"},
        "max_results": {"type": "integer", "description": "Maximum number of results"}
    }
}
```

## Adding New Tools

1. Define the tool schema in `tools_schema.py`.
2. Implement the tool in `tools.py`.
3. Update the assistant's function calls in `agent.py` to include the new tool.

## Contributing

Contributions are welcome! Please create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
