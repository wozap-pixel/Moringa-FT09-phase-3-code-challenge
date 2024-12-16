class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

        # Validation for name during initialization
        if not isinstance(self._name, str):
            raise ValueError("Name must be a string.")
        if len(self._name) == 0:
            raise ValueError("Name must be longer than 0 characters.")

    # String representation for better debugging
    def __repr__(self):
        return f'<Author {self.name}>'

    # Getter for id
    @property
    def id(self):
        return self._id

    # Getter for name
    @property
    def name(self):
        return self._name

    # Prevent name from being changed after instantiation
    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed after the Author is instantiated.")
