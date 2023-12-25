import re
import numpy as np
import csv
from message_parser import parse_message

categories = {
    1: "Rent",
    2: "Utilities",
    3: "Telephone",
    4: "Household",
    5: "Food",
    6: "Transport",
    7: "Tax",
    8: "Subscriptions",
    9: "Travel",
    10: "Insurance",
    11: "Medical",
    12: "Other"
}

def get_category(place):
    return None

def process_spending(payload):
    return None

def process_fetching(payload):
    return NotImplementedError

def process_analytics(payload):
    return NotImplementedError

def write_to_sheet(date, amount, category):
    return None

def write_to_csv(date, amount, desc, category):
    return None

def send_error(code):
    return None

def process_message(message):
    """Recieves message from Flask API and processes it. If the message cannot 
    be parsed into one of the 3 message types, sends back a help message.

    Args:
        message (string): Messenger message
    """
    type, payload = parse_message(message)
    if type == 1:
        process_spending(payload)
    else:
        send_error()
