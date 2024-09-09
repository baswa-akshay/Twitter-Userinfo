import tweepy


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


def lookup_user(client: tweepy.Client, username: str) -> None:
    """Retrieve and print information about a user by their username."""
    try:
        user = client.get_user(username=username, user_fields=[
                               "public_metrics", "description"])
        if user.data:
            print(f"User ID: {user.data.id}")
            print(f"Username: @{user.data.username}")
            print(f"Name: {user.data.name}")
            print(f"Description: {user.data.description}")
            print(f"Followers Count: {
                  user.data.public_metrics['followers_count']}")
            print(f"Following Count: {
                  user.data.public_metrics['following_count']}")
            print(f"Tweet Count: {user.data.public_metrics['tweet_count']}")
        else:
            print(f"No user found with username: {username}")
    except tweepy.errors.TweepyException as e:
        print(f"An error occurred while looking up the user: {e}")


if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token='',  # Get the client tokens and access keys from https://developer.x.com
        consumer_key='',
        consumer_secret='',
        access_token='',
        access_token_secret='',
    )

    print("=== About Me ===")
    about_me(client)
    print()

    print("=== User Lookup ===")
    username = str(input("enter username to lookup:  "))  # Example username
    lookup_user(client, username)
