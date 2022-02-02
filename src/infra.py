import json


# function to add to JSON
def append_data_on_database(new_data, filename='database.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        print(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def read_database(filename='database.json'):
  with open(filename,'r') as file:
        # First we load existing data into a dict.
        file_data = json.loads(file.read())
        file.close()
        return file_data