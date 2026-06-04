#!/usr/bin/env python3

# Book class represents a digital or physical book in the bookstore system
# It tracks title and page count and allows navigation through pages


class Book:
    # pass
    #!/usr/bin/env python3

    def __init__(self, title, page_count):
        # Initialize book with title and number of pages
        # Page count is validated to ensure data integrity
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        # Returns the number of pages in the book
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensures page count is always stored as a valid integer
        # Prevents invalid data like strings from being assigned
        if type(value) == int:
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Simulates reading behavior by flipping a page
        print("Flipping the page...wow, you read fast!")