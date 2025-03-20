# Chatbot Prototype

This project is a prototype chatbot designed to assist users in finding houses for rent or sale based on their specified criteria. The chatbot interacts with users, gathers their requirements, and searches the web for relevant listings.

## Project Structure

```
chatbot-prototype
├── src
│   ├── main.py               # Entry point of the application
│   ├── chatbot
│   │   ├── __init__.py       # Initializes the chatbot package
│   │   ├── bot.py            # Contains the ChatBot class for conversation management
│   │   └── search.py         # Contains the Search class for finding house listings
│   ├── utils
│   │   ├── __init__.py       # Initializes the utils package
│   │   └── web_scraper.py    # Contains the WebScraper class for web scraping functionality
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-prototype
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the chatbot, execute the following command:
```
python src/main.py
```

Follow the prompts to provide your criteria for houses you wish to buy or rent. The chatbot will then search for relevant listings and provide you with links to the houses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.