def create_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print("File created successfully!")
    except Exception as e:
        print("Error creating file:", e)


def write_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        print("Data written successfully")
    except Exception as e:
        print("Error writing to file:", e)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("File Content:")
        print(content)
    except Exception as e:
        print("Error reading file:", e)


def append_file(filename, data):
    try:
        with open(filename, 'a') as f:
            f.write(data)
        print("Data appended successfully")
    except Exception as e:
        print("Error appending file:", e)
