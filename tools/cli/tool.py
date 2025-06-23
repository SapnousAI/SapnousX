import subprocess

def run_command(command: str):
    """Run a shell command and return its output and error."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip(),
            'returncode': result.returncode
        }
    except Exception as e:
        return {'stdout': '', 'stderr': str(e), 'returncode': -1}
