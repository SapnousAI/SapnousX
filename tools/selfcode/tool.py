import subprocess

def git_status():
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
