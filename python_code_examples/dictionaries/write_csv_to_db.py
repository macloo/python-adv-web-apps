"""
See https://www.sqlalchemy.org/ - SQLAlchemy must be installed in your virtualenv.
I used a PostgreSQL db on Heroku.
Your empty database table must already exist.
Table fieldnames must be set.
The environment variable "DATABASE_URL" must be set on the computer this runs on.
"""

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) # environment variable
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    # name of each field (column) in this csv - don't leave any out
    for isbn, title, author, year in reader:
        # SQL insert into table named books
        db.execute( "INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year} )
    db.commit()
    # close the file
    f.close()

if __name__ == "__main__":
  main()
