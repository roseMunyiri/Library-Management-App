# Library Management System

## Description

This app allows a librarian to perfom CRUD operations on books and library members. It utilizes the Frappe API
to import books to the library

## Installation

1. Create a virtual environment

```
python -m venv venv

```

2. Activate the Virtual Environment

```
source venv/bin/activate

```

3. Install Dependencies

```
pip install -r requirements.txt

```

4. Set Environment Variables. Create a .env file in the project root directory

```
SECRET_KEY=YourSecretKey
DEBUG=True
DATABASE_URI=sqlite:///library.db

```

5. Initialize the Database . Create the initial database and apply migrations.

```
flask db init
flask db migrate
flask db upgrade
```

## Usage

### `app/` Directory

- **`routes/`**: This directory contains Python files that define different routes and views for your application.

  - **`book.py`**: Manages routes and views for book-related operations.
    Imports book using the Frappe API, adds book to the library database, allows Librarian
    to search for books, updates book details, deletes book details, and view all books
  - **`member.py`**: Handles routes and views for library member-related operations.
    Allows the librarian to search for members, update member details, view members,
    delete members and view all members
  - **`transaction.py`**: Contains routes and views for handling book transactions (borrowing and returning).
    Allows the librarian to issues ooks, return books, and view transactions

  - **`auth.py`**: Handles user-related routes and views (authentication, registration, homepage.).

-**`templates/'**: Stores HTML templates for rendering different pages.

- **`book/`**
  Contains:
- add_books.html for adding books to library
- import_books.html for importing books using the frappe API
- delete_books.html for deleting books from the library
- search_books.html for searching books in the library
- update_books.html for updating book details

- **`member/`**
  Contains:
- add_members.html for adding members to the library
- all_members.html for viewing all members in the library
- delete_members.html for delting members from the library
- search_members.html for searching for members in the library
- update_members.html for updating member details

- **`transaction/`**
  Contains:
- issue_book.html for issuing books to members
- return_book.html for returning books to library
- view_trandactions.html for viewing all transations

- **`auth/`**
  Contains:

  - home.html for viewing the homepage
  - register.html for user registration
  - login.html for member login
 
    ![login](https://github.com/roseMunyiri/Library-Management-App/assets/101321558/2084a338-8fea-495d-a819-c8f9ecc28a19)


- **`static/`**
  Contains:
  - styles.css
### `models.py`
Defines the database models for the application, including models for books, members, and  transactions.


