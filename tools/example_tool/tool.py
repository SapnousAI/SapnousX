# Example Tool Wrapper

def run(args):
    print(f"Example tool running with args: {args}")

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
