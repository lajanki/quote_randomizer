#!/bin/sh

# execute test_quotes.sql to create a test database.
cat test_quotes.sql | sqlite3 test_quotes.db