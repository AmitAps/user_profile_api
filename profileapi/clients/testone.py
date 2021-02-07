import requests

def client():
    token = "Token 36a64ffd53f3b1aebdc1de547d0ccf9fdd1d3d34"
    credentials = {"username": "Aps", "password": "APS_._113920a"}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                         data=credentials)

    headers = {"Authorization": token}
    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                            headers=headers)

    print("status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
