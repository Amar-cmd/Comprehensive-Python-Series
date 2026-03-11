#! =================
#! EXPENSE TRACKER
#! =================
# ------------------------------------------------------------
# - Stores all expenses in a single file: "expenses.tsv"
# - Each line in the file is one expense with fields:
#       id    date    category    amount_rupees    note
#   separated by TAB characters (\t).
#
# - Menu options:
#       1) Add expense
#       2) List all expenses
#       3) Edit an expense (by ID)
#       4) Delete an expense (by ID)
#       5) Delete entire file
#       6) Exit
#
# - Amount is stored as integer rupees (rounded from input).
# ============================================================

import os.path

FILE_NAME = "expenses.tsv"

def display_menu():
    """Show the main men options"""
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. List all expenses")
    print("3. Edit an expense")
    print("4. Delete an expense")
    print("5. Delete entire file")
    print("6. Exit")


#* Helper Functions
def ensure_file():
    """
    Make sure the data file exists.
    If it does not, create an empty one.
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8"):
            pass

def load_expense():
    """
    Read all expenses from the TSV file.

    Each non-empty line is expected to have:
        id<TAB>date<TAB>category<TAB>amount_rupees<TAB>note

    Returns:
        A list of dictionaries like:
        {
            "id": int,
            "date": str,
            "category": str,
            "amount_rupees": int,
            "note": str
        }

    """
    ensure_file()
    expenses = []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            expense_id, date, cat, amt, note = line.rstrip('\n').split("\t")
            expenses.append({
                "id": int(expense_id),
                "date": date,
                "category": cat,
                "amount_rupees": int(amt),
                "note": note
            })
    return expenses



def parse_amount_to_rupees(amount_in: str) -> int | None:
    """
    Convert user input (string) into an integer rupee amount.

    Examples:
    "1999" → 1999
    "1999.50" → 2000 (rounded)
    "abc" → None  (invalid)

    Returns:
        int  (if valid)
        None (if invalid)
    """
    try: return round(float(amount_in))
    except ValueError: return None

def next_id(expenses):

    return max((e["id"] for e in expenses), default=0) + 1

def sanitize_field(date_text):
    return date_text.replace("\t", " ")

def save_all(expenses):
    """
    Overwrite the file with the given list of expenses.
    Each expense is written as:
        id<TAB>date<TAB>category<TAB>amount_rupees<TAB>note
    """

    with open(FILE_NAME, "w", encoding='utf-8') as f:
        for e in expenses:
            f.write(f"{e["id"]}\t{e['date']}\t{e['category']}\t{e['amount_rupees']}\t{e['note']}\n")


def print_expense(e):

    print("-"*60)
    print(f"ID      : {e['id']}")
    print(f"Date    : {e.get('date','')}")
    print(f"Category: {e.get('category','')}")
    print(f"Amount  : {e.get('amount_rupees', 0)}")
    print("Note    :")
    print(e.get("note", ""))
    print("-"*60)



#* Main Functions

def add_expense():
    expenses = load_expense()
    date_text = input("Date (optional): ").strip()
    category = (input("Category (optional): ").strip() or "Uncategorized")
    amount_in = input("Amount in ₹(e.g., 1999 or 1999.50): ").strip()

    rupees = parse_amount_to_rupees(amount_in)
    if rupees is None:
        print("Invalid Amount")
        return
    note = input("Note (optional, single line): ").strip()

    e = {
        "id": next_id(expenses),
        "date": sanitize_field(date_text),
        "category": sanitize_field(category),
        "amount_rupees": rupees,
        "note": sanitize_field(note),
    }

    expenses.append(e)
    save_all(expenses)
    print("\nExpense Saved")
    print_expense(e)


def list_expenses():
    expenses = load_expense()
    if not expenses:
        print("\nNo Expenses Yet.")
        return

    print("\nID  | Date         | Category     | Amount | Note")
    print("-"*70)

    total = 0

    for e in sorted(expenses, key=lambda x: x['id']):
        print(f"{e['id']:>3} | {e['date'][:12]:<12} | {e['category'][:12]:<12} | {e['amount_rupees']:>6} | {e['note']}")
        total += e['amount_rupees']

    print("-" * 70)
    print(f"Total: ₹{total}")


def edit_expense():
    expenses = load_expense()
    if not expenses:
        print("\nNo expenses to edit")
        return
    try:
        eid = int(input("Enter ID to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    target = None
    for e in expenses:
        if e['id'] == eid:
            target = e
            break
    if not target:
        print(f"No expense with ID {eid}.")
        return

    print("\nPress ENTER to keep existing value.")
    new_date = input(f"Date [{target['date']}]: ").strip()
    new_cat = input(f"Category [{target['category']}]: ").strip()
    amt_in = input(f"Amount in [{target['amount_rupees']}]: ").strip()
    new_note = input(f"Note [{target['note']}]: ").strip()

    if new_date:
        target['date'] = sanitize_field(new_date)

    if new_cat:
        target['category'] = sanitize_field(new_cat)

    if amt_in:
        rupees = parse_amount_to_rupees(amt_in)
        if rupees is None:
            print("Invalid amount.")
            return
        target['amount_rupees'] = rupees

    if new_note:
        target["note"] = sanitize_field(new_note)


    save_all(expenses)
    print("\nUpdated expense:")
    print_expense(target)


def delete_expense():
    expenses = load_expense()
    if not expenses:
        print("\nNo expenses to delete.")
        return

    try:
        eid = int(input("Enter ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    new_expenses = [e for e in expenses if e['id'] != eid]
    if len(new_expenses) == len(expenses):
        print(f"No expense with ID {eid}.")
        return

    save_all(new_expenses)
    print(f"Deleted expense {eid}.")


def delete_entire_file():
    try:
        os.remove(FILE_NAME)
        print(f"{FILE_NAME} deleted successfully.")
    except FileNotFoundError:
        print("No file to delete.")



ensure_file()
while True:
    display_menu()
    choice = input("Choose:").strip()

    match choice:
        case "1": add_expense()
        case "2": list_expenses()
        case "3": edit_expense()
        case "4": delete_expense()
        case "5": delete_entire_file()
        case "6": print("Goodbye!"); break
        case _: print("Invalid Choice. Try Again.")









