# Discord Grinding Auto Chat

A Discord bot for auto-leveling with features for automatic message sending, supporting multiple accounts.

---

## Features
- Support for multiple accounts (tokens)
- Auto-deletion of messages after sending
- Detection of timeout channels
- Handling of rate limits and slow mode
- Comprehensive error handling
- Customizable delay between messages
- 54 random message variations

---

## Requirements
- Python 3.7+
- `discord.py` 1.7.3
- `asyncio`
- `colorama`

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/stephenahmeed/discord-grinding-bot.git
   cd discord-grinding-bot
   ```

2. Set up a virtual environment:
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Create a `token.txt` file and add your Discord tokens (one token per line):
   ```
   TOKEN1
   TOKEN2
   TOKEN3
   ```

2. Run the script:
   ```bash
   python jawa.py
   ```

3. Enter the required information when prompted:
   - Channel ID
   - Number of messages to send
   - Delay between messages (in seconds)

---

## How to Obtain a Discord Token
1. Open Discord in a browser.
2. Press `F12` to open Developer Tools.
3. Go to the "Network" tab.
4. Filter by "api."
5. Find a request with the `authorization` header.
6. Copy the token value.

---

## How to Obtain a Channel ID
1. Enable Developer Mode in Discord (User Settings > App Settings > Advanced > Developer Mode).
2. Right-click on a channel.
3. Select "Copy ID."

---

## Warnings
⚠️ **IMPORTANT**:
- Using self-bots violates Discord's Terms of Service.
- Use this bot at your own risk.
- It is recommended to set a minimum delay of 10 seconds between messages.
- Ensure the tokens you use are valid and fresh.

---

## Error Handling
The script handles various types of errors:
- Invalid/expired tokens
- Channel not found
- Channel timeout
- Rate limits
- Slow mode
- Missing permissions to send/delete messages
- Voice channel detection

---

## Usage Tips
- **Use a safe delay**:
  - Minimum of 10 seconds between messages.
  - Avoid spamming too many messages.
- **If errors occur**:
  - **Invalid token**: Update the token in `token.txt`.
  - **Rate limit**: The script will automatically wait.
  - **Timeout**: Wait for the timeout to finish.

### Join My Airdrop Channel For Upcoming Update: https://t.me/sabbirofficialairdrop
