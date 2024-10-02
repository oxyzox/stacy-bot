# Stacy - Minecraft Server Status Bot

**Stacy** is a cute and cool Discord bot designed to fetch and display the status of Minecraft servers (Java or Bedrock) with a stylish embed. Powered by `mcstatus.io`, Stacy provides live updates on player counts, server versions, and online/offline status!

## 🚀 Features

- **Supports both Java and Bedrock Servers**: Easily switch between server types when checking status.
- **Stylish Embed Messages**: Get server information with a clean and colorful embed.
- **Live Player Count**: See how many players are currently online.
- **Version Information**: View the Minecraft server version.
- **Error Handling**: Stacy will let you know if there's a problem fetching server data.

## 🛠️ Setup

Follow these steps to get Stacy up and running on your own server.

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Discord Bot Token](https://discord.com/developers/applications)
- `requests` library

### Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/oxyzox/stacy-bot.git
   cd stacy-bot
    ```

2. **Install the required libraries:**

 ```pip install -r requirements.txt```


3. **Set up environment variables:**

    Create a ```.env``` file and add your Discord bot token:

```TOKEN=your-discord-bot-token-here```

4. **Run the bot:**

``` python main.py```


**Made with ❤️ by oxyzox**
