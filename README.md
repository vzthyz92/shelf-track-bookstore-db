# Shelf Track - Part 1

## Overview

Shelf Track Part 1 is a command-line inventory management system developed using Python and SQLite. The application allows users to manage a bookstore inventory by storing and maintaining book records in a relational database.

This project demonstrates foundational database programming concepts, including creating tables, inserting records, updating data, deleting entries, and performing searches.

## Features

### Database Creation
- Creates an SQLite database (`ebookstore.db`)
- Automatically creates a `book` table if it does not exist
- Populates the database with predefined book records

### Inventory Management

#### Add Books
- Insert new books into the inventory
- Store:
  - Book ID
  - Title
  - Author ID
  - Quantity in stock

#### Update Books
- Modify book quantity
- Update book titles
- Change author IDs

#### Delete Books
- Remove books from the inventory using the book ID

#### Search Books
- Search for books by title
- Display matching records

## Technologies Used

- Python 3
- SQLite3


# Shelf Track - Part 2

## Overview

Shelf Track Part 2 expands the original bookstore inventory system by introducing author management and relational database concepts.

The application now maintains separate Book and Author tables connected through a foreign-key relationship, enabling richer inventory information and improved database design.

## Features

### Book Management
- Add books
- Update records
- Delete books
- Search books

### Author Management
- Store author details separately
- Update author names
- Update author countries

### Relational Database Design

Two linked tables:

#### Book Table
Stores:
- Book ID
- Title
- Author ID
- Quantity

#### Author Table
Stores:
- Author ID
- Author Name
- Country

### View Complete Inventory

Displays:

- Book title
- Author name
- Author country

using SQL JOIN operations.

## Technologies Used

- Python 3
- SQLite3
- SQL Joins

## Database Structure

### Book Table

| Field | Type |
|---------|---------|
| id | INTEGER |
| title | TEXT |
| authorID | INTEGER |
| qty | INTEGER |

### Author Table

| Field | Type |
|---------|---------|
| id | INTEGER |
| name | TEXT |
| country | TEXT |

## Key SQL Concepts Demonstrated

- CREATE TABLE
- INSERT
- UPDATE
- DELETE
- SELECT
- INNER JOIN


# Shelf Track - Part 3

## Overview

Shelf Track Part 3 is a fully refactored and enhanced bookstore inventory management system built with Python and SQLite.

This version introduces modular programming principles, improved validation, reusable functions, enhanced search capabilities, and cleaner code organization while maintaining all functionality from previous versions.

## Features

### Database Management

Automatically:

- Creates the SQLite database
- Creates Book and Author tables
- Populates starter data
- Maintains data persistence

### Book Management

#### Add Books
Create new inventory records.

#### Update Books
Modify:

- Quantity
- Title
- Author ID
- Author details

#### Delete Books
Remove books safely after validation.

#### Search Books

Search by title using:

- Partial matches
- Case-insensitive searching

### View Inventory

Displays complete book information including:

- Book title
- Author name
- Author country

using relational database joins.

## Technologies Used

- Python 3
- SQLite3
- SQL
- Modular Programming

## Project Structure

```text
shelf_track_part3.py

├── connect_db()
├── create_tables()
├── populate_tables()
├── menu()
├── add_book()
├── update_book()
├── delete_book()
├── search_book()
├── view_books()
└── main()



