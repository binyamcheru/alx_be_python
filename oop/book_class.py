class Book:
    def __init__(self, title, author, year):
        """Initialize the Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string that could recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
