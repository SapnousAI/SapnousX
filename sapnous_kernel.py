import sys
from sapnous_kernel import planner, memory

# Tool imports
try:
    from tools.cli import tool as cli_tool
except ImportError:
    cli_tool = None
try:
    from tools.fileio import tool as fileio_tool
except ImportError:
    fileio_tool = None
try:
    from tools.websearch import tool as websearch_tool
except ImportError:
    websearch_tool = None
try:
    from tools.browser import tool as browser_tool
except ImportError:
    browser_tool = None
# ...add other tools as needed...

def print_help():
    print("""
SapnousX CLI Agent
Available commands:
  shell <command>                Run a shell command
  read <file>                    Read a file
  write <file> <content>         Write content to a file
  listdir <dir>                  List directory contents
  web <query>                    Web search
  browser <task>                 Browser automation
  help                           Show this help
  exit                           Quit
""")

def main():
    print("SapnousX CLI Agent. Type 'help' for commands.")
    while True:
        try:
            user_input = input("SapnousX> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting SapnousX.")
            break
        if not user_input:
            continue
        parts = user_input.split()
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd == 'exit':
            print("Goodbye!")
            break
        elif cmd == 'help':
            print_help()
        elif cmd == 'shell' and cli_tool:
            result = cli_tool.run_command(' '.join(args))
            print(result['stdout'] or result['stderr'])
        elif cmd == 'read' and fileio_tool:
            print(fileio_tool.read_file(args[0]))
        elif cmd == 'write' and fileio_tool:
            if len(args) < 2:
                print("Usage: write <file> <content>")
            else:
                print(fileio_tool.write_file(args[0], ' '.join(args[1:])))
        elif cmd == 'listdir' and fileio_tool:
            print(fileio_tool.list_dir(args[0] if args else '.'))
        elif cmd == 'web' and websearch_tool:
            results = websearch_tool.web_search(' '.join(args))
            for i, r in enumerate(results, 1):
                print(f"{i}. {r['title']} - {r['url']}")
        elif cmd == 'browser' and browser_tool:
            print(browser_tool.browser_demo(' '.join(args)))
        else:
            print("Unknown or unavailable command. Type 'help' for options.")

if __name__ == "__main__":
    main()
