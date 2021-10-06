import requests

token = "AQAAAAAzRd1pAAcVsRM3rju2pUZPtWbyIu82GsM"

URL = "https://cloud-api.yandex.net/v1/disk/resources"
authorization = {"Authorization": f"OAuth {token}"}
name_folder = "Folder_test"

result = requests.put(URL, headers=authorization, params={"path": f"/{name_folder}"})
result_get = requests.get(URL, headers=authorization, params={"path": f"/{name_folder}"})

