import requests
import json
import logging
from sample_rules import create_rules


def create_headers(bearer_token):
    headers = {"connection":"close","Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,

    )
    if response.status_code != 200:
        logging.error("Cannot get rules (HTTP {}): {}".format(response.status_code, response.text))
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    logging.info(json.dumps(response.json()))
    return response.json()



def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        logging.error("Cannot delete rules (HTTP {}): {}".format(response.status_code, response.text))
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    logging.info(json.dumps(response.json()))




def set_rules(headers):

    payload = {"add": create_rules()}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        logging.error("Cannot add rules (HTTP {}): {}".format(response.status_code, response.text))
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    logging.info(json.dumps(response.json()))