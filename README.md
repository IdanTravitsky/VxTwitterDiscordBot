# VxTwitterDiscordBot

## Introduction

VxTwitterDiscordBot is a simple Discord bot that automatically replaces "twitter.com" links with "vxtwitter.com" in messages, improving the embeds displayed on Discord.

## Prerequisites
   * Python 3.7 or higher installed on your system.
   * A Discord account with administrative privileges for the server where you want to add the bot.
   * A bot token obtained from the Discord Developer Portal.

## Installation

   1. Clone or download the VxTwitterDiscordBot repository to your local machine.

   2. Install the required dependencies by running the following command in the project directory:

`pip install -r requirements.txt` 

or 

`pip install discord`

## Setting Up the Bot

To set up the bot and invite it to your Discord server, follow these steps:

   1. Go to the Discord Developer Portal and create a new application.

   2. Navigate to the "Bot" tab in your application and click on "Add Bot".

   3. Under the "Token" section, click on "Copy" to copy your bot token.

   4. Open the bot.py file in a text editor and replace "YOUR_BOT_TOKEN" with the bot token you copied in the previous step.

   5. Save the changes to the bot.py file.

   6. Launch a terminal or command prompt and navigate to the project directory.

   7. Start the bot by running the following command:

`python bot.py`

   8. The bot should now be running. Leave the terminal or command prompt open for the bot to stay active.

   9. Open a web browser and go to the following URL, replacing YOUR_CLIENT_ID with the Client ID of your Discord application:


`https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot`

   10. Select the server where you want to invite the bot and click "Authorize" to add it to your server.

## Usage

Once the bot is added to your Discord server, it will automatically replace any "twitter.com" links with "vxtwitter.com" in messages. The bot works in real-time and does not require any additional commands to function.
