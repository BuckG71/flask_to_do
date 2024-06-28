from app import app, db

# Reflect the tables
with app.app_context():
    metadata = db.MetaData()
    metadata.reflect(bind=db.engine)

    # Print the table names
    print("Tables in the database:")
    for table_name in metadata.tables.keys():
        print(table_name)