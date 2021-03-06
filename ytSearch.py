# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import argparse
import sys


scopes = ["https://www.googleapis.com/auth/youtube"]
'''
def main():

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "desktopClientSecret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)



    #Seperate this into a method that can pass a custom query
    
    request = youtube.search().list(
        part="snippet",
        channelType="any",
        maxResults=3,
        q= "query"
    )
    response = request.execute()
    
    
    data = json.loads(response)

    return(data)
''' 


def youtube_query(query):

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "desktopClientSecret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        channelType="any",
        maxResults=1,
        q= query
    )
    response = request.execute() #This is apparently already a dictionary
    #data = json.loads(response)
    #data = json.dumps(response) #debug line to grab and format json data

    return response["pageInfo"]["totalResults"]
"""
def main(args):
    parser = argparse.ArgumentParser(description="Add query")
    parser.add_argument("-x", "--xcenter", type=float, default= 2, required=False)
"""

if __name__ == "__main__":
    youtube_query(sys.argv[1])
"""
def main():
    print(youtube_query("hello"))

main()
"""
