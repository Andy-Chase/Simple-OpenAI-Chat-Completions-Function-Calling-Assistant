tools = [
    {
        "type": "function",
        "function": {
            "description": "Fetches the text website <body> content using BeautifulSoup.",
            "name": "fetch_website_data",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "url"
                    }
                },
                "required": [
                    "url"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "description": "Fetches the transcript for a YouTube video given its URL",
            "name": "get_transcript",
            "parameters": {
                "type": "object",
                "properties": {
                    "video_url": {
                        "type": "string",
                        "description": "video_url"
                    }
                },
                "required": [
                    "video_url"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_to_file",
            "description": "accepts text content for multipe file types and saves it to a file with the specified file path and approapriate file extension",
            "parameters": {
                "type": "object",
                "properties": {
                    "text_content": {
                        "type": "string",
                        "description": "The markdown text to save to a file.",
                    },
                    "file_path": {
                        "type": "string",
                        "description": "The path where the markdown file should be saved. You must include the relevant extension following the file name. For example 'example_file_name.md', 'example_file_name.txt', 'example_file_name.html', 'example_file_name.py' etc.",
                    },
                },
                "required": ["text_content", "file_path"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "description": "Searches the web using DuckDuckGo and returns the top search results.",
            "name": "web_search",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "query"
                    },
                    "region": {
                        "type": "string",
                        "default": "wt-wt",
                        "description": "region: Australia, United States, United Kingdom, Worldwide, etc. Defaults to 'wt-wt' if not specified."
                    },
                    "timelimit": {
                        "type": "string",
                        "default": "7w",
                        "description": "timelimit: d, w, m, y. Defaults to None. To specify use number and d,m,y to resprest the period i.e 7 days = 7d, 1 week = 1w, 1 month = 1m, 1 year = 1y If user asks for the latest information, we can set the timelimit to 1w. Defaults to None if not specified."
                    },
                    "max_results": {
                        "type": "integer",
                        "default": 5,
                        "description": "max_results: max number of results. If None, returns results only from the first response. Defaults to 5"
                    }
                },
                "required": [
                    "query", "region", "timelimit", "max_results"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "description": "Searches the web for news results using DuckDuckGo news api and returns the top news results.",
            "name": "news_search",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "query"
                    },
                    "region": {
                        "type": "string",
                        "default": "wt-wt",
                        "description": "region: Australia, United States, United Kingdom, Worldwide, etc. Defaults to 'wt-wt' if not specified."
                    },
                    "timelimit": {
                        "type": "string",
                        "default": "7w",
                        "description": "timelimit: d, w, m, y. Defaults to None. To specify use number and d,m,y to resprest the period i.e 7 days = 7d, 1 week = 1w, 1 month = 1m, 1 year = 1y If user asks for the latest information, we can set the timelimit to 1w. Defaults to None if not specified."
                    },
                    "max_results": {
                        "type": "integer",
                        "default": 5,
                        "description": "max_results: max number of results. If None, returns results only from the first response. Defaults to 5"
                    }
                },
                "required": [
                    "query", "region", "timelimit", "max_results"
                ]
            }
        }
    }
]