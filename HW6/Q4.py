dict = {"firstName": "Mohamed", "lastName": "Farag", "birthYear": 1900, "nationality": "Egyptian"}
to_delete = {'a', 'b'}

def delete_keys(to_delete, dict):
    for key in to_delete:
        dict.pop(key)
    return ""

print(delete_keys(("lastName", "birthYear"), dict),dict)