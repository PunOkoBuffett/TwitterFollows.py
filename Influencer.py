import requests
import os
import sys


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def auth():
    #return "Bearer token string"
    return os.environ.get("BEARER_TOKEN")

def create_follower_url(influencer_id):
    # Replace with user ID below
    user_id = influencer_id

    return "https://api.twitter.com/2/users/{}/following".format(user_id)


def get_params():
    return {
        "max_results": 1000,
        "user.fields": "created_at"
    }


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def create_influencer_url(influencer):
    usernames = "usernames=" + influencer
    user_fields = "user.fields=description,created_at,public_metrics"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url

def get_following_ids(influencer_id):
    bearer_token = auth()
    url = create_follower_url(influencer_id)
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    output_dictionary = {}
    for x in json_response['data']:
        output_dictionary[x.get('id')] = x.get('username')
    if 'meta' in json_response:
        while 'next_token' in json_response['meta']:
            params['pagination_token'] = json_response['meta'].get('next_token')
            json_response = connect_to_endpoint(url, headers, params)
            for x in json_response['data']:
                output_dictionary[x.get('id')] = x.get('username')
    return output_dictionary

def get_influencer_id(influencer):
    bearer_token = auth()
    url = create_influencer_url(influencer)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers, '')
    return json_response['data'][0].get('id')


def get_follower_info(user_id, follower_operation, number):
    bearer_token = auth()
    url = create_influencer_url(user_id)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers, '')
    followers_count = json_response['data'][0].get("public_metrics").get("followers_count")
    if follower_operation == "follower_count_lt":
        return followers_count < number
    else:
        return followers_count > number

# System arguments
# Python3 Influencer.py <Search Criteria> <Number> <Twitter Handles>
# Search Critera (filter)
#    Options - follower_count_lt x - Follower Count less than x
#            - follower_count_gt x - Follower Count greater than x
# Twitter Handles
#       This script can accept any number of accounts to compare to buy there is an api limit
#       of 15,000 combined follows between them
# If you leave out a second person this script can analyze a single account to check follows greater or
# less than a certain follower count.
def main_function():
    x = 0
    influencer_list = []
    follower_operation = sys.argv[1]
    number = int(sys.argv[2])
    print("Operation is " + follower_operation)
    print("Number is " + str(number))
    for x in range(3, len(sys.argv)):
        influencer_list.append(sys.argv[x])
    print("Accounts are")
    print(influencer_list)
    influencer_following_dicts = []
    for influencer in influencer_list:
        influencer_id = get_influencer_id(influencer)
        influencer_following_dicts.append(get_following_ids(influencer_id))
    FinalDict = influencer_following_dicts[0]
    for x in range(1, len(influencer_following_dicts)):
        FinalDict = dict(FinalDict.items() & influencer_following_dicts[x].items())
    if len(FinalDict) == 0:
        print("No matches found")
        return 0
    final_dict = {k: v for (k, v) in FinalDict.items() if get_follower_info(v, follower_operation, number)}
    final_list = []
    for x in final_dict.values():
        final_list.append("@" + x)
    print(final_list)
    return 0

if __name__ == "__main__":
    main_function()
