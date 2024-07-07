import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_contents(path, indent=""):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"{indent}{Fore.BLUE}{entry.name}")
                    print_directory_contents(entry.path, indent + "  ")
                else:
                    print(f"{indent}{Fore.GREEN}{entry.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission Denied: {path}")
    except FileNotFoundError:
        print(f"{indent}{Fore.RED}File Not Found: {path}")
    except Exception as e:
        print(f"{indent}{Fore.RED}Error: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <directory_path>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        sys.exit(1)
    
    if not path.is_dir():
        print(f"Error: The path '{path}' is not a directory.")
        sys.exit(1)

    print_directory_contents(path)

if __name__ == "__main__":
    main()
