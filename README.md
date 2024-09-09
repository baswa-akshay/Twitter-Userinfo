# Twitter User Info

This Python script uses the Tweepy library to interact with the Twitter API. It provides functionality to retrieve and display information about a Twitter user and the authenticated user.

## Features

- **About Me**: Displays information about the authenticated Twitter user, including their name, username, and follower count.
- **User Lookup**: Retrieves and prints detailed information about a specific Twitter user based on their username. This includes their name, username, description, and follower, following, and tweet counts.

## Requirements

To run this script, you need:

- Python 3.x
- Tweepy library

Install the Tweepy library using pip:

```bash
pip install tweepy
```
## Setup
### 1.Obtain Twitter API Credentials
Create a Twitter Developer account and set up an app to get the necessary API keys and tokens:
- [Twitter Developer Portal](https://developer.x.com/en)

### 2.Configure the Script
Open main.py and replace the placeholders with your Twitter API credentials:
```python
client = tweepy.Client(
    bearer_token='',  # Your Bearer Token
    consumer_key='',  # Your Consumer Key
    consumer_secret='',  # Your Consumer Secret
    access_token='',  # Your Access Token
    access_token_secret='',  # Your Access Token Secret
)
```
## Usage
### 1. Run the Script
Execute the script using Python:
```bash
python main.py
```
### 2. About Me
This option displays information about the authenticated Twitter user. This information is printed automatically when you run the script.
### 3. User Lookup
When prompted, enter a Twitter username to retrieve and display information about that user.
## Error Handling
- If there are issues with retrieving user information, the script will print an error message.
- Make sure your API credentials are correct and that you have the necessary permissions.
## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/baswa-akshay/Twitter-Userinfo/blob/main/LICENSE) file for details.
## Author 
- [Baswa-Akshay](https://github.com/baswa-akshay)
