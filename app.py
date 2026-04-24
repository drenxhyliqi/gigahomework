import sys
from cli import run_cli

if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
