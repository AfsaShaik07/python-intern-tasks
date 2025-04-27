#!/usr/bin/env python3
import os

CONTACTS_FILE = "contacts.txt"

def ensure_file():
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "w") as f:
            pass
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    with open(CONTACTS_FILE, "a") as f:
        f.write(f"{name},{phone},{email}\n")
    print("✅ Contact added.\n")

def view_contacts():
    print("\n---- All Contacts ----")
    with open(CONTACTS_FILE) as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print("No contacts found.\n"); return
    for idx, line in enumerate(lines, 1):
        name, phone, email = line.split(",", 2)
        print(f"{idx}. {name}  |  📞 {phone}  |  ✉️ {email}")
    print()

def search_contacts():
    term = input("Search by name/phone/email: ").strip().lower()
    print(f"\n-- Results for '{term}' --")
    found = False
    with open(CONTACTS_FILE) as f:
        for line in f:
            name, phone, email = line.strip().split(",", 2)
            if term in name.lower() or term in phone or term in email.lower():
                print(f"• {name}  |  {phone}  |  {email}")
                found = True
    if not found:
        print("No matches found.")
    print()

def main():
    ensure_file()
    menu = (
        "1) Add contact\n"
        "2) View all contacts\n"
        "3) Search contacts\n"
        "4) Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
