#!/usr/bin/env python3

"""InstaTool

Tool designed to use for giveaways
- Read all the comments and get a list of unique usernames
- Pull viewer list from live stream
- Pick a username from a list in multiple fun methods

Usage: $ python3 instatool.py <_args_>

Arguments:
    -_param_ <type>: _description_
"""

### Import Statements ###

import instaloader

### Functions ###


def extract_data(user: str) -> None:
    """Gets simple profile data

    Args:
        user (str): username
    """
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, user)
    print(f"Username: {profile.username}")
    print(f"User ID: {profile.userid}")
    print(f"Number of Posts: {profile.mediacount}")
    print(f"Followers Count: {profile.followers}")
    print(f"Following Count: {profile.followees}")
    print(f"Bio: {profile.biography}")
    print(f"Extern URL: {profile.external_url}")


def get_follower_info() -> None:
    """Gets follower information"""
    user = input("Enter username: ")
    pwd = input(f"Enter password for {user}: ")
    if user and pwd:
        return
    bot = instaloader.Instaloader()
    bot.login(user, pwd)
    profile = instaloader.Profile.from_username(bot.context, user)
    follower_list = profile.get_followers()
    followee_list = profile.get_followees()
    print(f"Followers: {follower_list}")
    print(f"Followees: {followee_list}")


def function3(_param_: type) -> type:
    """_description_

    Args:
        _param_ (type): _description_

    Returns:
        type: _description_
    """
    return _param_


if __name__ == "__main__":
    get_follower_info()
