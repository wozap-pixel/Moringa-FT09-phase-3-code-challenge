class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        # Validate title and content
        if not isinstance(self._title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(self._title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        if not isinstance(self._content, str):
            raise ValueError("Content must be a string.")
        if len(self._content) == 0:
            raise ValueError("Content cannot be empty.")

    # String representation for debugging
    def __repr__(self):
        return f'<Article {self.title}>'

    # User-friendly string representation
    def __str__(self):
        return f"Article: {self.title} (Author ID: {self.author_id}, Magazine ID: {self.magazine_id})"

    # Getter for id
    @property
    def id(self):
        return self._id

    # Getter and validation for title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after the Article is instantiated.")

    # Getter for content
    @property
    def content(self):
        return self._content

    # Setter for content (if editable later)
    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise ValueError("Content must be a string.")
        if len(value) == 0:
            raise ValueError("Content cannot be empty.")
        self._content = value
        # Update the database if necessary

    # Getter for author_id
    @property
    def author_id(self):
        return self._author_id

    # Getter for magazine_id
    @property
    def magazine_id(self):
        return self._magazine_id
