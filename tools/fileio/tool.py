import os

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return str(e)

def write_file(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        return str(e)

def list_dir(path):
    try:
        return os.listdir(path)
    except Exception as e:
        return str(e)
