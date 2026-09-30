import json
import os

# Configuration: The name of the file where data will be saved
DATA_FILE = "student_records.json"

def load_data():
    """Loads records from the JSON file. If file doesn't exist, returns empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(records):
    """Saves the current list of records to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def add_record():
    records = load_data()
    print("\n--- Add New Student Record ---")
    
    try:
        # Taking inputs
        student_id = input("Enter Student ID (e.g., 101): ")
        
        # Check if ID already exists
        for r in records:
            if r['id'] == student_id:
                print("Error: A student with this ID already exists!")
                return

        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Course/Major: ")

        # Creating a record dictionary
        new_record = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        records.append(new_record)
        save_data(records)
        print("Record added successfully!")

    except ValueError:
        print("Invalid input! Age must be a number.")

def view_records():
    records = load_data()
    print("\n--- List of All Records ---")
    if not records:
        print("No records found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Age':<10} {'Course':<20}")
    print("-" * 60)
    for r in records:
        print(f"{r['id']:<10} {r['name']:<20} {r['age']:<10} {r['course']:<20}")

def search_record():
    records = load_data()
    search_id = input("\nEnter Student ID to search: ")
    
    found = False
    for r in records:
        if r['id'] == search_id:
            print("\nRecord Found:")
            print(f"ID: {r['id']}\nName: {r['name']}\nAge: {r['age']}\nCourse: {r['course']}")
            found = True
            break
    
    if not found:
        print("Record not found.")

def update_record():
    records = load_data()
    search_id = input("\nEnter Student ID to update: ")
    
    for r in records:
        if r['id'] == search_id:
            print(f"Current Name: {r['name']}")
            r['name'] = input("Enter New Name (leave blank to keep current): ") or r['name']
            
            try:
                age_input = input("Enter New Age (leave blank to keep current): ")
                if age_input:
                    r['age'] = int(age_input)
                
                r['course'] = input("Enter New Course (leave blank to keep current): ") or r['course']
                
                save_data(records)
                print("Record updated successfully!")
                return
            except ValueError:
                print("Invalid age entered. Update failed.")
                return

    print("Record not found.")

def delete_record():
    records = load_data()
    search_id = input("\nEnter Student ID to delete: ")
    
    # Filter the list to exclude the record with the given ID
    original_count = len(records)
    records = [r for r in records if r['id'] != search_id]
    
    if len(records) < original_count:
        save_data(records)
        print("Record deleted successfully.")
    else:
        print("Record not found.")

def main_menu():
    """The main loop for the application interface."""
    while True:
        print("\n==============================")
        print(" STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_record()
        elif choice == '4':
            update_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main_menu()