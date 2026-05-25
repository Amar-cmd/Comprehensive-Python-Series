# Library Management System (Console Based) - OOP Project
# Uses: dataclass where it makes sense + standard __init__ where needed
# Menu uses: match-case (Python 3.10+)

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    total_copies: int
    __available_copies: int = field(init=False, repr=False)  # private (encapsulation)

    def __post_init__(self):
        if self.total_copies <= 0:
            raise ValueError("total_copies must be positive")
        self.__available_copies = self.total_copies

    def get_available(self) -> int:
        return self.__available_copies

    def issue_copy(self) -> bool:
        if self.__available_copies > 0:
            self.__available_copies -= 1
            return True
        return False

    def return_copy(self) -> bool:
        if self.__available_copies < self.total_copies:
            self.__available_copies += 1
            return True
        return False

    def display_book(self):
        print(
            f"[{self.book_id}] {self.title} by {self.author} | "
            f"Total: {self.total_copies}, Available: {self.get_available()}"
        )


@dataclass
class Member:
    member_id: str
    name: str
    issued_books: List[str] = field(default_factory=list)

    ISSUE_LIMIT: int = field(init=False, default=0, repr=False)  # overridden by subclasses

    def can_issue_more(self) -> bool:
        return len(self.issued_books) < self.ISSUE_LIMIT

    def display_member(self):
        print(
            f"[{self.member_id}] {self.name} ({self.__class__.__name__}) | "
            f"Issued: {self.issued_books} | Limit: {self.ISSUE_LIMIT}"
        )


class StudentMember(Member):
    ISSUE_LIMIT = 2


class TeacherMember(Member):
    ISSUE_LIMIT = 5


class Library:
    total_issues = 0  # class attribute (counter)

    # Standard __init__ is better here
    def __init__(self):
        self.books: Dict[str, Book] = {}       # book_id -> Book
        self.members: Dict[str, Member] = {}   # member_id -> Member

    @classmethod
    def get_total_issues(cls) -> int:
        return cls.total_issues

    def add_book(self, book: Book):
        if book.book_id in self.books:
            print("Book ID already exists. Cannot add.")
            return
        self.books[book.book_id] = book
        print("Book added successfully.")

    def add_member(self, member: Member):
        if member.member_id in self.members:
            print("Member ID already exists. Cannot add.")
            return
        self.members[member.member_id] = member
        print("Member added successfully.")

    def issue_book(self, member_id: str, book_id: str):
        member = self.members.get(member_id)
        if not member:
            print("Member not found.")
            return

        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
            return

        if not member.can_issue_more():
            print("Member reached max issue limit.")
            return

        if book.issue_copy():
            member.issued_books.append(book_id)
            Library.total_issues += 1
            print("Book issued successfully.")
        else:
            print("No copies available.")

    def return_book(self, member_id: str, book_id: str):
        member = self.members.get(member_id)
        if not member:
            print("Member not found.")
            return

        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
            return

        if book_id not in member.issued_books:
            print("This member has not issued this book.")
            return

        member.issued_books.remove(book_id)

        if book.return_copy():
            print("Book returned successfully.")
        else:
            print("Return failed (already at total copies).")

    def search_book(self, keyword: str):
        keyword = keyword.strip().lower()
        if not keyword:
            print("Enter a valid search keyword.")
            return

        found = [
            b for b in self.books.values()
            if keyword in b.title.lower() or keyword in b.author.lower()
        ]

        if not found:
            print("No matching books found.")
            return

        print("\nSearch Results:")
        for b in found:
            b.display_book()

    def show_all_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("\nAll Books:")
        for b in self.books.values():
            b.display_book()

    def show_all_members(self):
        if not self.members:
            print("No members in library.")
            return
        print("\nAll Members:")
        for m in self.members.values():
            m.display_member()


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main():
    lib = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Add Member (Student/Teacher)")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book (title/author)")
        print("6. Show All Members")
        print("7. Show All Books")
        print("8. Total Issues Counter")
        print("9. Exit")

        choice = read_int("Enter choice: ")

        match choice:
            case 1:
                book_id = input("Book ID: ").strip()
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                total = read_int("Total copies: ")
                try:
                    lib.add_book(Book(book_id, title, author, total))
                except ValueError as e:
                    print("Error:", e)

            case 2:
                member_id = input("Member ID: ").strip()
                name = input("Name: ").strip()
                mtype = input("Type (S for Student / T for Teacher): ").strip().upper()

                if mtype == "S":
                    lib.add_member(StudentMember(member_id, name))
                elif mtype == "T":
                    lib.add_member(TeacherMember(member_id, name))
                else:
                    print("Invalid member type.")

            case 3:
                member_id = input("Member ID: ").strip()
                book_id = input("Book ID: ").strip()
                lib.issue_book(member_id, book_id)

            case 4:
                member_id = input("Member ID: ").strip()
                book_id = input("Book ID: ").strip()
                lib.return_book(member_id, book_id)

            case 5:
                keyword = input("Enter title/author keyword: ")
                lib.search_book(keyword)

            case 6:
                lib.show_all_members()

            case 7:
                lib.show_all_books()

            case 8:
                print("Total Issues so far:", Library.get_total_issues())

            case 9:
                print("Exiting... Bye!")
                break

            case _:
                print("Invalid choice. Try again.")


# run directly (no if __name__ == "__main__")
main()
