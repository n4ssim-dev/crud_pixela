from http.client import responses
import os
from dotenv import load_dotenv
import requests
from datetime import datetime

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

load_dotenv()

ACCOUNT_ENDPOINT = 'https://pixe.la/v1/users'

date_now = ''.join(str(datetime.now()).split(" ")[0].split("-"))

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_parameters = {
    'id': GRAPH_ID,
    'name': 'BookGraph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'ichou'
}

pixel_parameters = {
    "date": date_now,
    "quantity": '15'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

def create_user():
    response = requests.post(url=ACCOUNT_ENDPOINT, json=user_parameters)
    print(response.text)

def create_graph():
    graph_endpoint = f'{ACCOUNT_ENDPOINT}/{user_parameters["username"]}/graphs'
    response = requests.post(url=graph_endpoint, json=graph_parameters,headers=headers)
    print(response.text)

def create_pixel():
    pixel_endpoint = f'{ACCOUNT_ENDPOINT}/{user_parameters["username"]}/graphs/{graph_parameters["id"]}'
    response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
    print(response.text)

def update_pixel():
    pixel_endpoint = f'{ACCOUNT_ENDPOINT}/{user_parameters["username"]}/graphs/{graph_parameters["id"]}/{pixel_parameters["date"]}'
    response = requests.put(url=pixel_endpoint,json=pixel_parameters,headers=headers)
    if response.status_code == requests.codes.ok:
        print("Successfully updated !")
    else:
        print("Error: ", response.status_code, response.text)

def delete_pixel():
    pixel_endpoint = f'{ACCOUNT_ENDPOINT}/{user_parameters["username"]}/graphs/{graph_parameters["id"]}/{pixel_parameters["date"]}'
    response = requests.delete(url=pixel_endpoint, headers=headers)
    print(response.text)