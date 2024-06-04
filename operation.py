from database import create_connection


# Add a new contact
def add_contact(store_name, phone_no, email, address):
    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO contacts (store_name, phone_number, email, address) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (store_name,phone_no,email,address))
    conn.commit()
    cursor.close()
    conn.close()

# View all contacts 
def view_contacts():
    conn = create_connection()
    cursor = conn.cursor()
    query = "Select * from contacts"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# Search for a contact
def search_contact(keyword):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM contacts WHERE store_name LIKE %s OR phone_number LIKE %s"
    cursor.execute(query, (f"%{keyword}%', f'%{keyword}%"))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# Update a contact
def update_contact(store_name,phone_no,email,address,contact_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "UPDATE contacts SET store_name=%s, phone_number=%s, email=%s, address=%s WHERE id=%s"
    cursor.execute(query, (store_name,phone_no,email,address,contact_id))
    cursor.close()
    conn.close()

# Delete a contact
def delete_contact(contact_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    cursor.execute(query, (contact_id))
    cursor.close()
    conn.close()