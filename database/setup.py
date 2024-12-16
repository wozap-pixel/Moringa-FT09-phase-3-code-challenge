from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) > 0)
        )
    ''')
    
    # Create magazines table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) BETWEEN 2 AND 50),
            category TEXT NOT NULL CHECK(length(category) > 0)
        )
    ''')
    
    # Create articles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL CHECK(length(title) BETWEEN 5 AND 255),
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE,
            FOREIGN KEY (magazine_id) REFERENCES magazines (id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()
