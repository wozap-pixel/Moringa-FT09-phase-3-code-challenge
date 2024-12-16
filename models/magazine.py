class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    # String representation for better debugging
    def __repr__(self):
        return f'<Magazine {self.name}>'

    # Getter for id
    @property
    def id(self):
        return self._id

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value
        # Update the database here if necessary

    # Getter and setter for category
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if len(value) == 0:
            raise ValueError("Category cannot be empty.")
        self._category = value
        # Update the database here if necessary
