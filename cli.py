import sqlite3
import click
from lib.database import create_tables, SessionLocal
from lib.models import Book

@click.group()
def cli():
    pass

# @cli.command()
@cli.command('init_db')

def init_db():
    """Create database tables."""
    create_tables()
    click.echo("Database initialized.")

@cli.command('add_book')
@click.argument("title")
@click.argument("author")
@click.argument("genre")
def add_book(title, author, genre):
    """Add a new book to the library."""
    db = SessionLocal()
    book = Book(title=title, author=author, genre=genre)
    db.add(book)
    db.commit()
    db.close()
    click.echo(f"Book '{title}' added to the library.")

@cli.command('list_books')
def list_books():
    """List all books in the library."""
    db = SessionLocal()
    books = db.query(Book).all()
    for book in books:
        click.echo(f"{book.id}: {book.title} - {book.author} - {book.genre}")
    db.close()

if __name__ == "__main__":
    cli()
