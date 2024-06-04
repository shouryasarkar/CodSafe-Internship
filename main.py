from operation import add_contact, view_contacts, search_contact, update_contact, delete_contact

def main():
    while True:
        print("\n -------------------------------------- CONTACT MANAGEMENT SYSTEM ---------------------------------------- ")
        print("1. ADD CONTACT")
        print("2. VIEW CONTACT LIST")
        print("3. SEARCH CONTACTS")
        print("4. UPDATE CONTACT")
        print("5. DELETE CONTACT")
        print("6. EXIT")

        choice = input("Enter your choice: ")


        if choice == '1':
            store_name = input("Enter store name: ")
            phone_no = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter adress: ")
            add_contact(store_name,phone_no,email,address)
            return "Contact added successfully."
        
        elif choice == '2':
            contacts = view_contacts()
            for contact in contacts:
                print(contact)

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = search_contact(keyword)
            for result in results:
                print(result)
            
        elif choice == '4':
            contact_id = int(input("Enter contact id to update: "))
            store_name = input("Enter store name: ")
            phone_no = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter adress: ")
            update_contact(contact_id,store_name,phone_no,email,address)
            return "Contact updated successfully"
        
        elif choice == '5':
            contact_id = int(input("Enter the contact id to delete: "))
            delete_contact(contact_id)
            print("Contact deleted successfully.")
        
        elif choice == '6':
            break
        
        else:
            return "Invalid choice. Please try again."
    
if __name__ == "__main__":
    main()