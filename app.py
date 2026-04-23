
import os
import sys
import psycopg
from dotenv import load_dotenv
from cli import run_menu

load_dotenv()

if __name__ == "__main__":
    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
