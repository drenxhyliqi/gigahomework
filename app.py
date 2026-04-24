import sys
from cli import run_cli
from cli import run_menu

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            run_cli()
        else:
            run_menu()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
