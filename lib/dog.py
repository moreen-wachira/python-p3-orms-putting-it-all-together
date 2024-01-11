import sqlite3
import pytest
from dog import Dog, CONN, CURSOR

class TestDog:
    def setup_method(self, method):
        # Open the database connection before each test method
        CONN.connect('lib/dogs.db')
        CURSOR = CONN.cursor()

    def teardown_method(self, method):
        # Close the database connection after each test method
        CONN.close()

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "dogs" if it does not exist.'''
        # Drop the table before creating it to ensure a clean slate
        CURSOR.execute("DROP TABLE IF EXISTS dogs")
        
        # Call the create_table method
        Dog.create_table()

        # Verify that the 'dogs' table exists
        CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dogs'")
        result = CURSOR.fetchone()

        assert result is not None, "The 'dogs' table was not created."
