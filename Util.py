""" Utility for saving files """

import os
from tinydb import TinyDB, Query
from flask import jsonify

def database_upload(data):
    db = TinyDB("db.json")

    for d in data:
        db.insert({
            d: data[d].read().decode("latin-1")
        })

    print()
    print("Files uploaded to database.")

def local_upload(data):
    current_path = os.path.dirname(os.path.abspath(__file__))
    location = current_path + "/local_storage/"

    for d in data:
        save_location = location + d
        with open(save_location, 'w') as f:
            f.write(data[d].read().decode("latin-1"))

    print()
    print("Files saved to local storage.")

def print_to_screen(data):
    print()
    print("Printing data to screen...")

    for d in data:
        print("File:", d)
        print("Data:\n", data[d].read().decode("latin-1"))