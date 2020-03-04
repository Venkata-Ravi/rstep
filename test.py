import requests
from requests.exceptions import HTTPError

#This function takes url endpoint as parameter and sends request to that server
#It fetches the response from the server and returns the same to the caller
def getresource(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return (resp)

if __name__ == "__main__":

    #Base URL and End points defined in "urls.py" in the Django server
    BASE_URL = "http://127.0.0.1:8000/"
    ENDPOINT = "total/"

    #preparing the API end point
    url = BASE_URL+ENDPOINT

    # Calling the method getresource which actually calls the "GET" method in server.
    # Using try, except to handle the exceptions
    try:
        resp = getresource(url)
        resp.raise_for_status()
    except HTTPError as http_err:
        print (f"HTTP Error: {http_err}")
    except Exception as e:
        print (f"Exception: {e}")
    else:
        resp_data = resp.json()
        print(resp_data)
