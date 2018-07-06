import requests


class HttpService:

    @staticmethod
    def send_request(url, http_method='GET', params=None, payload=None):
        if not url:
            raise ValueError("No Url")

        headers = {
            "content-type": "application/json"
        }

        result = requests.request(http_method, url, params=params, json=payload, headers=headers)
        return result
