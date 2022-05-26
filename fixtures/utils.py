import json


def is_json(possible_json):
    try:
        json.loads(possible_json)
    except ValueError as e:
        return False
    return True
