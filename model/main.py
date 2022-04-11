"""Main file to call all the utilities and controller file"""
import logging
from util import create_headers
from util import get_rules
from util import delete_all_rules
from util import set_rules
from controller import get_stream
from load_configuration import load_configuration_file


file_data = load_configuration_file()
twitter_handles = file_data['Handle']
bearer_token = file_data['cred']['bearer_token']


def main():
    """Calling all utilities and stream function"""
    logging.info("Creating headers...")
    headers = create_headers(bearer_token)
    logging.info("Done")
    logging.info("Getting rules...")
    rules = get_rules(headers, bearer_token)
    logging.info("Done")
    logging.info("Deleting all rules...")
    delete_all_rules(headers, bearer_token, rules)
    logging.info("Setting rules...")
    set_rules(headers)
    logging.info("Done")
    logging.info("Getting stream...")
    get_stream(headers)
