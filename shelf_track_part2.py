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
    ''')

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

db.commit()

# Create the table called author if it does not exist
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS author (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT
    )
    ''')

authors = [(1290, 'Charles Dickens', 'England'), 
                 (8937, 'J.K. Rowling', 'England'), 
                 (2356, 'C.S. Lewis', 'Ireland'), 
                 (6380, 'J.R.R. Tolkien', 'South Africa'), 
                 (5620, 'Lewis Carroll', 'England')]


# Insert multiple entries into the table
cursor.executemany(
    '''
    INSERT OR IGNORE INTO author(id, name, country)
    VALUES(?, ?, ?)
    ''',
    authors
)
db.commit()


# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    5. View details of all books
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

        cursor.execute('''SELECT book.title, author.id, author.name, author.country
                       FROM book
                       INNER JOIN author
                       ON book.authorID = author.id
                       WHERE book.id = ?
                       ''', (id2,))
        
        search_result = cursor.fetchone()

        if search_result:
            title, author_id, name, country = search_result    

            print("\nCurrent details:")
            print(f"Book Title: {title}")
            print(f"Author Name: {name}")
            print(f"Author Country: {country}\n")

        new_name = input("Enter new author name (Enter to skip): \n")
        new_country = input("Enter new author country (Enter to skip): \n")

        #if user hits enter, maintain existing data
        if new_name == "":
            new_name = name

        #if user hits enter, maintain existing data
        if new_country == "":
            new_country = country

        cursor.execute('''
        UPDATE author
        SET name = ?, country = ?
        WHERE id = ?
        ''', (new_name, new_country, author_id))

        db.commit()
        print("Author details successfully updated!")


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

   
    elif user_choice == 5:
    #To view details of all books
        #join two tables using primary key in author table
        cursor.execute('''SELECT book.title, author.name, author.country
                       FROM book
                       INNER JOIN author
                       ON book.authorID = author.id
                       ''')    
        
        results = cursor.fetchall()

        for title, name, country in results:
            print("--------------------------------------------------")
            print(f"Title: {title}")
            print(f"Author's Name: {name}")
            print(f"Author's Country: {country}")

        print("--------------------------------------------------")   
        
    
    elif user_choice == 0:
    # Add logic here to exit the application
        print("Application closed successfully!")
        break


    else:
        print("Oops - invalid input!")


db.close()
