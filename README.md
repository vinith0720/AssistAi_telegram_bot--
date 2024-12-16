# Assist AI Telegram Bot

This is a Telegram bot designed to interact with users using Google Gemini for AI-powered responses. The bot provides basic commands like `/start`, `/website`, and `/help`, as well as the ability to send messages to Gemini and receive AI-generated responses.

## Features

- **/start**: Greets the user with a welcome message.
- **/website**: Provides the link to the Assist AI website.
- **/help**: Displays a list of available commands.
- **Gemini Integration**: Sends user messages to Gemini and replies with AI-generated responses.

## Prerequisites

- Python 3.7+ installed on your machine.
- A Telegram bot token. You can get one by creating a bot through [BotFather](https://core.telegram.org/bots#botfather).
- Access to Gemini API for AI-powered responses.

## Setup

### Step 1: Clone the repository

Clone this repository to your local machine using:

```bash
git clone <repository-url>
```
### Step 2: Install required dependencies
Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
### Step 3: Create a constant.py file
Create a file named constant.py and add your Telegram bot token in the following format:

```python
API_key = 'your-telegram-bot-api-key'
Replace 'your-telegram-bot-api-key' with your actual API key.
```

### Step 4: Configure Gemini API
Make sure you have access to the Gemini API, and add your Gemini API credentials or setup as needed in the gemini module.

### Step 5: Run the bot
Run the bot using the following command:

```bash
python bot.py
```
The bot should now be running and ready to interact with users on Telegram.
## Commands

- **/start**: Starts the bot and sends a welcome message.
- **/website**: Provides the website link.
- **/help**: Lists the available commands.

## Troubleshooting

If you encounter issues, ensure the following:

1. Your Telegram bot API key is correctly set in `constant.py`.
2. Your Gemini integration is set up and accessible.
3. All required dependencies are installed.

### License
```
This project is licensed under the MIT License - see the LICENSE file for details.
```
