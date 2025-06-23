try:
    import pandas as pd
    spreadsheet_available = True
except ImportError:
    spreadsheet_available = False

def read_csv(path):
    if not spreadsheet_available:
        return 'pandas not installed.'
    return pd.read_csv(path).to_dict(orient='records')

def write_csv(path, data):
    if not spreadsheet_available:
        return 'pandas not installed.'
    pd.DataFrame(data).to_csv(path, index=False)
    return f'CSV written to {path}'
