import requests

def client():
  #token 34781dd3eb1df5b0717e710eb192b3a5642e30c0
    credentials = {"username": "testcaseone",
                    "email": "apsj@mail.com",
                    "password1": "APS_._113920a",
                    "password2": "APS_._113920a"}

    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
                            data=credentials)

    # response = requests.get('http://127.0.0.1:8000/api/profiles/',
    #                         headers=headers)

    print("status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
