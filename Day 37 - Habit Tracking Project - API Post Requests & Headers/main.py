import requests
import datetime  as dt

USERNAME = "subhash"
TOKEN = "qwertyuiop"
GRAPHID = "graph1"


pixela_enpoint = "https://pixe.la/v1/users"

# Create a new account on Pixela
user_params = {
"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor": "yes"
}

# response = requests.post(url=pixela_enpoint, json=user_params)
# print(response.text)

# Create a graph on Pixela
graph_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "Min",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post value to the graph
pixel_creation_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPHID}"

data = {
    "date": str(dt.datetime.now().date()).replace("-", ""),
    "quantity": input("How many minutes did you code today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=data, headers=headers)
print(response.text)

# Update value to the graph
pixel_updation_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPHID}/20231208"
update_data = {
    "quantity":"90"
}

# response = requests.put(url=pixel_updation_endpoint, json=update_data, headers=headers)
# print(response.text)


# Delete value from the graph
# pixel_deletion_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPHID}/20231208"
# response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# print(response.text)
