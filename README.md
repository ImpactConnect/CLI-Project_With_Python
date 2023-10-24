# Library Management CLI Application

This CLI application allows you to manage a library database efficiently. You can add new books, list existing books, and initialize the database with ease. This project demonstrates the use of Python, SQLAlchemy ORM, and Click library for creating a command-line interface.

## Getting Started

Follow these instructions to clone the repository, install the required dependencies, and run the CLI application on your local machine.

### Prerequisites

- Python 3.6 or higher installed on your system
- Pipenv installed for managing Python packages and virtual environments

### Clone the Repository


```bash
git clone https://github.com/ImpactConnect/CLI-Project_With_Python.git
cd CLI-Project 
```

### Install Dependencies

```bash
pipenv install
```

### Initialize the Database

```bash
python cli.py init_db
```

This command initializes the SQLite database required for the application.

## Usage

### Add a New Book

To add a new book, use the following command:

```bash
python cli.py add_book "Book Title" "Author Name" "Genre"
```

Replace `"Book Title"`, `"Author Name"`, and `"Genre"` with the actual book information.

### List All Books

To list all books in the library, use the following command:

```bash
python cli.py list_books
```

## Additional Commands

- `pipenv run python cli.py init_db`: Initializes the database.
- `pipenv run python cli.py list_books`: Lists all books in the library.

## Contributing

Feel free to open issues and pull requests to contribute to this project. We welcome any suggestions, bug reports, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the contributors of Click, SQLAlchemy, and other libraries used in this project.

Thank you for using the Library Management CLI Application! If you encounter any issues or have questions, please don't hesitate to reach out. Happy coding!
```
