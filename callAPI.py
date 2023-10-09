from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    authorization_string = client_id + ":" + client_secret
    authorization_bytes = authorization_string.encode("utf-8")
    authorization_base64 = str(base64.b64encode(authorization_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authorization_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    result_json = json.loads(result.content)
    access_token = result_json["access_token"]
    return access_token


def get_authorization_header(access_token):
    return {"Authorization": "Bearer " + access_token}


def search_for_new_releases(access_token, country):
    url = "https://api.spotify.com/v1/browse/new-releases"
    headers = get_authorization_header(access_token)
    request = f"?country={country}"
    request_url = url + request
    result = get(request_url, headers=headers)
    result_json = json.loads(result.content)["albums"]["items"]
    return result_json


def search_for_artist_info(access_token, artist_id):
    url = "https://api.spotify.com/v1/artists/"
    headers = get_authorization_header(access_token)
    request_url = url + artist_id
    result = get(request_url, headers=headers)
    result_json = json.loads(result.content)
    return result_json
