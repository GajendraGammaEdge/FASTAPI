from sqlalchemy import text
from sqlalchemy.orm import Session



def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    print("Init DB run")
    # default_data = db.query(Data).filter(Data.id == 1).first()
    # if not default_data:
    #        default_data = Data(id=data['id'],description=data['description'],type=data['type'],start_Date=str(date.today()))
    #         db.add(default_data)
    #         db.commit()
    try:
        with open('app/init.sql', 'r') as f:
            sql_commands = f.read()


        db.execute(text(sql_commands))
        db.commit()
        print("Data inserted successfully.")
    except Exception as e:
        # Handle any errors that occur during execution
        db.rollback()
        print("Error occurred while inserting data:", e)
