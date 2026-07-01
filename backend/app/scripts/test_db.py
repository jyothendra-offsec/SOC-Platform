from sqlalchemy import text

from app.db.session import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))

        print("\n✅ Database connection successful!\n")

        for row in result:
            print(row[0])

except Exception as error:
    print("\n❌ Database connection failed!\n")
    print(error)
