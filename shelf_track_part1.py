import sqlite3

#Create a SQLite database file
db = sqlite3.connect('ebookstore.db')

#Cursor object to interact with the database
cursor = db.cursor()

# Create the table called book if it does not exist
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        authorID INTEGER,
        qty INTEGER
    )
    '''
)

# Commit the changes and save table creation
db.commit()

#enter given data for the table named book
book_data = [(3001, 'A Tale of Two Cities', 1290, 30), 
                 (3002, 'Harry Potter and the Philosophers Stone', 8937, 40), 
                 (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25), 
                 (3004, 'The Lord of the Rings', 6380, 37), 
                 (3005, 'Alices Adventures in Wonderland', 5620, 12)]


# Insert multiple entries into the table
cursor.executemany(
    '''
    INSERT OR IGNORE INTO book(id, title, authorID, qty)
    VALUES(?, ?, ?, ?)
    ''',
    book_data
)

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit 

    Enter selection: \n"""
        )
    )


    if user_choice == 1:
        # Add logic here to enter or add a new book
        id1 = int(input("Enter the unique book id: \n"))
        title1 = input("Enter the book title: \n")
        authorID1 = int(input("Enter the author ID: \n"))
        qty1 = int(input("Enter the quantity of books on hand: \n"))
        
        cursor.execute(
            '''
            INSERT INTO book(id, title, authorID, qty)
            VALUES(?, ?, ?, ?)
            ''',
            (id1, title1, authorID1, qty1)
            )
        
        db.commit()
        print(f"The book {title1} has been successfully added! ")
       

    elif user_choice == 2:
        # Add logic here to update an existing book qty in the table
        id2 = int(input("Enter the id of the book you wish to update: \n"))

        #display menu to guide the user update
        print("""
                What attribute would you like to update?
                1. Quantity
                2. Title
                3. Author ID
                \n""")
        
        selection = int(input("Enter your choice: \n"))

        #to update the books on hand quantity
        if selection == 1:
            qty2 = int(input("Enter the new quantity: \n"))
            cursor.execute(
                '''
                UPDATE book SET qty = ? WHERE id = ?
                ''', (qty2, id2)
            )
            print("Quantity successfully updated!")

        #to update the book title
        elif selection == 2:
            title2 = input("Enter the new title: ")
            cursor.execute(
                '''
                UPDATE book SET title = ? WHERE id = ?
                ''', (title2, id2)
            )
            print("Title successfully updated!")

        #to update the book author ID
        elif selection == 3:
            authorID2 = int(input("Enter the new author ID: "))
            cursor.execute(
                '''
                UPDATE book SET authorID = ? WHERE id = ?
                ''', (authorID2, id2)
            )
            print("Author ID successfully updated!")

        else:
            print("Invalid update option!")

        #save update
        db.commit()


    elif user_choice == 3:
        # Add logic here to delete a book from the table
        # Execute DELETE statement to remove student 
        choose_id = int(input("Please select the entry id to remove from the table: \n"))
        cursor.execute('''DELETE FROM book WHERE id = ?''', (choose_id,))
        db.commit()
        print("Entry successfully deleted! ")
            
    elif user_choice == 4:
        # Add logic here to search a book
        booktitle = input("Please enter the title of the book you are searching for: \n")

        cursor.execute('''
                       SELECT id, title, authorID, qty FROM book WHERE title = ?  
                       ''', (booktitle,)
                       )
        
        matches = cursor.fetchall()

        for book in matches:
           print(f"ID: {book[0]} | Title: {book[1]} | Author ID: {book[2]} | Qty: {book[3]}")
          
    elif user_choice == 0:
    # Add logic here to exit the application
        print("Application closed successfully!")
        break

    else:
        print("Oops - invalid input!")

db.close()
