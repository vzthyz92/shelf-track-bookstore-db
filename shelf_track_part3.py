import sqlite3

#Create a SQLite database file
def connect_db():
    return sqlite3.connect("ebookstore.db")

def create_tables(cursor):

     # Create a table called book if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book(
        id INTEGER PRIMARY KEY,
        title TEXT,
        authorID INTEGER,
        qty INTEGER
    )
    ''')

    # Create a table called author if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS author(
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT
    )
    ''')

def populate_tables(cursor):

    book_data = [
        (3001, 'A Tale of Two Cities', 1290, 30),
        (3002, 'Harry Potter and the Philosophers Stone', 8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
        (3004, 'The Lord of the Rings', 6380, 37),
        (3005, 'Alices Adventures in Wonderland', 5620, 12)
    ]

    authors = [
        (1290, 'Charles Dickens', 'England'),
        (8937, 'J.K. Rowling', 'England'),
        (2356, 'C.S. Lewis', 'Ireland'),
        (6380, 'J.R.R. Tolkien', 'South Africa'),
        (5620, 'Lewis Carroll', 'England')
    ]

    #insert data into tables or ignore if already populated
    cursor.executemany(
        "INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)", book_data)
    cursor.executemany(
        "INSERT OR IGNORE INTO author VALUES (?, ?, ?)", authors)

def menu():

    print("""
Would you like to:
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View details of all books
0. Exit
""")

    try:
        return int(input("Enter selection: "))
    
    except ValueError:
        print("Invalid input.")
        return -1
    
def add_book(cursor):

    try:
        book_id = int(input("Enter book id: "))
        title = input("Enter title: ")
        author_id = int(input("Enter author ID: "))
        qty = int(input("Enter quantity: "))

        cursor.execute(
            "INSERT INTO book VALUES (?, ?, ?, ?)", (book_id, title, author_id, qty) )

        print("\nBook successfully added.\n")

    except sqlite3.IntegrityError:
        print("Error: That book ID already exists in the database.")    

    except ValueError:
        print("Invalid input. ID and quantity must be integers.")

# helper function to reduce repetition when updating fields
def update_field(cursor, field, value, book_id):
    cursor.execute(f"UPDATE book SET {field} = ? WHERE id = ?", (value, book_id))

# Update book details
def update_book(cursor):
  
    try:
        book_id = int(input("Enter the id of the book you wish to update: \n"))

        cursor.execute("SELECT * FROM book WHERE id = ?", (book_id,))
    
        #incase no book exists in database
        if not cursor.fetchone():
            print("Book not found!")
            return
        
        #display menu to guide the user update
        print("""
What attribute would you like to update?
1. Quantity
2. Title
3. Author ID
4. Author details (name & country)
""")

        selection = int(input("Enter your choice: \n"))

        # update quantity
        if selection == 1:
            new_qty = int(input("Enter the new quantity: \n"))
            cursor.execute(''' UPDATE book SET qty = ? WHERE id = ? ''', (new_qty, book_id))
            update_field(cursor, "qty", new_qty, book_id)
            print("Quantity successfully updated!")

        # update title
        elif selection == 2:
            new_title = input("Enter the new title: ")
            cursor.execute(''' UPDATE book SET title = ? WHERE id = ? ''', (new_title, book_id))
            update_field(cursor, "title", new_title, book_id)
            print("Title successfully updated!")

        # update author ID
        elif selection == 3:
            new_author_id = int(input("Enter the new author ID: "))
            cursor.execute(''' UPDATE book SET authorID = ? WHERE id = ? ''', (new_author_id, book_id))
            update_field(cursor, "authorID", new_author_id, book_id)
            print("Author ID successfully updated!")

        # update author name & country (Part 2 requirement)
        elif selection == 4:

            cursor.execute('''
            SELECT book.title, author.id, author.name, author.country
            FROM book
            INNER JOIN author
            ON book.authorID = author.id
            WHERE book.id = ?
            ''', (book_id,))

            result = cursor.fetchone()

            if result:
                title, author_id, name, country = result

                print("\nCurrent details:")
                print(f"Book Title: {title}")
                print(f"Author Name: {name}")
                print(f"Author Country: {country}")

                new_name = input("Enter new author name (press Enter to keep current): ")
                new_country = input("Enter new author country (press Enter to keep current): ")

                if new_name == "":
                    new_name = name
                if new_country == "":
                    new_country = country

                cursor.execute('''UPDATE author SET name = ?, country = ? WHERE id = ?''', (new_name, new_country, author_id)                )

                print("Author details successfully updated!")

            else:
                print("Book not found!")

        else:
            print("Invalid update option!")

    except ValueError:
        print("Invalid input!")


def delete_book(cursor):

    try:
        book_id = int(input("Enter book id to delete: "))
        cursor.execute("SELECT * FROM book WHERE id = ?", (book_id,))

        #incase the book does not exist
        if not cursor.fetchone():
            print("Book not found!")
            return

        cursor.execute("DELETE FROM book WHERE id = ?", (book_id,) )
        print("\nBook deleted.\n")

    except ValueError:
        print("Invalid ID.")

def search_book(cursor):

    title = input("Enter the title of the book to search for: ")

    #incase of user capitalization or spelling errors
    cursor.execute(
        '''
        SELECT book.id, book.title, author.name, author.country, book.qty
        FROM book 
        INNER JOIN author
        On book.authorID = author.id
        WHERE LOWER(book.title) LIKE LOWER(?)
        ''',
        ('%'+ title + '%',)
        )
    
    results = cursor.fetchall()

    if not results:
        print("No matching entries found! ")
    
    else:
        print("\nResults:\n")
        for book in results:
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Country: {book[3]} | Qty: {book[4]}")

def view_books(cursor):

    #join book and author table
    cursor.execute("""
    SELECT book.title, author.name, author.country
    FROM book
    INNER JOIN author
    ON book.authorID = author.id
    """)

    results = cursor.fetchall()

    if not results:
        print("No books found.")
        return

    for title, name, country in results:
        print("----------------------------------")
        print(f"Title: {title}")
        print(f"Author: {name}")
        print(f"Country: {country}")

def main():
#main menu function calls

    with connect_db() as db:

        cursor = db.cursor()

        create_tables(cursor)
        populate_tables(cursor)

        while True:

            choice = menu()

            if choice == 1:
                add_book(cursor)

            elif choice == 2:
                update_book(cursor)

            elif choice == 3:
                delete_book(cursor)

            elif choice == 4:
                search_book(cursor)

            elif choice == 5:
                view_books(cursor)

            elif choice == 0:
                print("Application closed.")
                break

            db.commit()

if __name__ == "__main__":
    main()