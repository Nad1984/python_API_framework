import json


def is_json(possible_json):
    try:
        json.loads(possible_json)
    except ValueError as e:
        return False
    return True


def get_json_value(data, field_path):
    item_names = field_path.split('/')
    print(item_names)

    field_value = data
    for i in item_names:

        if i.__contains__('[') and i.__contains__(']'):
            index = int(i.replace('[', '').replace(']', ''))
            field_value = field_value[index]
        else:
            field_value = field_value[i]

    return field_value
