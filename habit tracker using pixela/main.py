import requests
from datetime import datetime
USERNAME="santosh5444"
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="Pixela_api"
GRAPH_ID="graph1"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config= {
    "id":"graph1",
    "name":"running graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}

headers={
    "X-USER-TOKEN":TOKEN,
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
now=datetime.now().strftime("%Y%m%d")
print(now)
pixel_params={
    "date":now,
    "quantity":input("how many kilometers did u ran")

}
# response=requests.post(url=pixel_creation_endpoint,json=pixel_params,headers=headers)
# print(response.text)

update_end_point=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"

new_pixel_data={
    "quantity":"4.5",
}
# response=requests.put(url=update_end_point,json=new_pixel_data,headers=headers)
# print(response.text)

delete_end_point= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"
response=requests.delete(url=delete_end_point,headers=headers)
print(response.text)