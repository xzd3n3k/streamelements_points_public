# imports
import requests
import json


def main():
    # all neccesary variables
    channel_id = ''
    users = {}

    # iterating users
    for user in users:
        # making get request to fetch user data (on specified channel)
        get_response = requests.get(f"https://api.streamelements.com/kappa/v2/points/{channel_id}/{user}")

        if get_response.status_code == 200:
            response = json.loads(get_response.text)    # load data

            # declare variables and save data
            pts = response['points']
            usr = response['username']

            num_of_spaces = 40 - len(usr)

            print(70*"-")
            print("Username:", response['username'], num_of_spaces*" ", "Points:", pts)

        else:
            print(get_response.status_code)


if __name__ == '__main__':
    main()
