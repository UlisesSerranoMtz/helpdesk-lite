from app.core.db import db
from app.models.ticket import Ticket

def main():
    db.connect(reuse_if_open=True)
    db.create_tables([Ticket])
    db.close()
    print("Table created successfully")

if __name__ == "__main__":
    main()