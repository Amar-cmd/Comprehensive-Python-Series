#! ==============+
#! JOURNAL ENTRY |
#! ==============+
import os.path

JOURNAL_DIR = "journal_entries"

def display_menu():
    print("\n=== Journal Menu ===")
    print("1) Add entry")
    print("2) List entries")
    print("3) View one entry")
    print("4) Delete entry")
    print("5) Exit")


# Helper Functions
def make_sure_folder_exists():
    if not os.path.exists(JOURNAL_DIR):
        os.makedirs(JOURNAL_DIR)


def get_all_entry_ids():
    """
    Look at all files in the journal folder and collect the IDs.
    Returns: a sorted list of IDs (as integers).
    """
    make_sure_folder_exists()
    ids = []

    # entry_0001.txt
    for filename in os.listdir(JOURNAL_DIR):
        # We only care about files that look like: entry_0001.txt
        if filename.startswith('entry_') and filename.endswith('.txt'):
            # Take the numeric part: "0001"
            number_part = filename[len("entry_"):-len(".txt")]

            # Check if it's really digits, then convert to int
            if number_part.isdigit():
                ids.append(int(number_part))
    ids.sort()
    return ids


def get_next_id():
    """
    Find the next entry ID.
    If no entries exist, start at 1.
    Otherwise, 1 + the highest existing ID.
    """

    ids = get_all_entry_ids()
    if not ids:
        return 1
    return ids[-1] + 1


def get_entry_filename(entry_id):
    return os.path.join(JOURNAL_DIR, f"entry_{entry_id:04d}.txt")


def save_entry(entry_id, title, body):
    """
    Save one entry to a file in this simple format:
        ID: <number>
        Title: <text>
        ----
        <body text (can be many lines)>
    """
    make_sure_folder_exists()
    filename = get_entry_filename(entry_id)

    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"ID: {entry_id}\n")
        f.write(f"Title: {title}\n")
        f.write("----\n")
        f.write(body)


def load_entries(entry_id):
    """
    Read one entry file and return a dictionary:
    {
      "id": ...,
      "title": ...,
      "body": ...
    }
    If the file does not exist, return None.
    """

    filename = get_entry_filename(entry_id)

    if not os.path.exists(filename):
        return None

    # Read all lines from the file
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.read().splitlines()

    # If the file is too short, treat it as invalid
    if len(lines) < 3:
        return None

    # Line 0: "ID: <number>"
    id_line = lines[0]
    if id_line.startswith("ID:"):
        try:
            actual_id = int(id_line[3:].strip())
        except ValueError:
            actual_id = entry_id
    else:
        actual_id = entry_id

    # Line 1: "Title: <text>"
    title_line = lines[1]
    if title_line.startswith("Title:"):
        title = title_line[6:].strip()
    else:
        title = ""

    # Line 2 should be "----" (separator)
    # Body starts after that. If it's not "----", just start from line 3 safely.

    if len(lines) >= 3 and lines[2].strip() == "----":
        body_start_index = 3
    else:
        body_start_index = 2

    body = "\n".join(lines[body_start_index:])

    return {
        "id": actual_id,
        "title": title,
        "body": body
    }
















def load_all_entries():
    """
    Load all entries from disk and return them as a list of dictionaries.
    """
    entries = []
    ids = get_all_entry_ids()

    for entry_id in ids:
        entry = load_entries(entry_id)
        if entry is not None:
            entries.append(entry)
    return entries


def print_entry_summary(entry):
    title = entry.get("title", "").strip()
    if title == "":
        title = "(no title)"
    print(f"{entry.get('id'):>4} | {title}")



def print_entry(entry):
    print("-" * 50)
    print(f"ID   : {entry.get('id')}")
    print(f"Title: {entry.get('title')}")
    print("Body :")
    print(entry.get("body", ""))
    print("-" * 50)


# Main Functions



def add_entry():
    title = input("Title: ").strip()

    print("Write your entry. Type END on a new line to finish:")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    body = "\n".join(lines)
    entry_id =get_next_id()
    save_entry(entry_id, title, body)

    print(f"\nEntry {entry_id} saved.")




def list_entries():
    """Show all entries with IDs and titles."""
    entries = load_all_entries()

    if not entries:
        print("\nNo entries yet.")
        return

    print("\nID   |  Title")
    print("-" * 50)
    for entry in entries:
        print_entry_summary(entry)




def view_one_entry():
    user_input = input("Enter the ID to view: ").strip()

    if not user_input.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    entry_id = int(user_input)
    entry = load_entries(entry_id)

    if entry is None:
        print(f"No entry with ID {entry_id} found.")
    else:
        print_entry(entry)


def delete_entry():
    user_input = input("Enter the ID to delete: ").strip()

    if not user_input.isdigit():
        print("Invalid ID. Please enter a number.")
        return

    entry_id = int(user_input)
    filename = get_entry_filename(entry_id)

    if not os.path.exists(filename):
        print(f"No entry with ID {entry_id} found.")
    else:
        os.remove(filename)
        print(f"Entry {entry_id} deleted.")


while True:
    display_menu()
    choice = input("Choose: ").strip()
    match choice:
        case "1": add_entry()
        case "2": list_entries()
        case "3": view_one_entry()
        case "4": delete_entry()
        case "5": print("Goodbye!"); break
        case _: print("Invalid choice. Please try again.")