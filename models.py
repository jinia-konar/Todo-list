import sqlite3
from flask import jsonify

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):
        query = """CREATE TABLE IF NOT EXISTS "Todo" ( id INTEGER NOT NULL PRIMARY KEY, Title TEXT, Description TEXT, _is_done boolean DEFAULT 0, _is_deleted boolean DEFAULT 0, CreatedOn Date DEFAULT CURRENT_DATE, DueDate Date, UserId INTEGER FOREIGNKEY REFERENCES User(_id));"""

        print("table created")
        self.conn.execute(query)
        #print("Executed")

    def create_user_table(self):
        query = """CREATE TABLE IF NOT EXISTS "User" (Name TEXT, Email EMAIL, Id INTEGER PRIMARY KEY, CreatedOn Date default CURRENT_DATE);"""

        print("User table created")
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self, params):
        #print(text, description)
        print(params)
        query = f'insert into {self.TABLENAME}' \
        f'(Title, Description, DueDate, UserId)' \
        f'values ("{params.get("Title")}","{params.get("Description")}", "{params.get("DueDate")}", "{params.get("UserId")}")'

        print(query)
        result = self.conn.execute(query)
        return self.get_item_by_id(result.lastrowid)      

    def delete(self, item_id):
        print("inside delete")
        query = f'UPDATE {self.TABLENAME} ' \
                f'SET _is_deleted = {1} ' \
                f'WHERE id = {item_id} '

        self.conn.execute(query)
        print("delete executed")
        return self.list_items()

    def update(self, item_id, params):
        print("inside update")
        print(params)
        set_query = ", ".join([f'{key} = "{value}"' for key, value in params.items()])

        print(set_query)
        query = f'UPDATE {self.TABLENAME} ' \
                f'SET {set_query} ' \
                f'WHERE id = {item_id}'
        print(query)

        self.conn.execute(query)
        print("update done")
        return self.get_item_by_id(item_id)

    def list_items(self, where_clause=""):
        print("inside list_items")
        query = f'select id, Title, Description, DueDate, _is_done, CreatedOn ' \
                f'from {self.TABLENAME} WHERE _is_deleted != {1}' + where_clause

        result = self.conn.execute(query).fetchall()
        #print(result)
        output = [{column: row[i] for i, column in enumerate(result[0].keys())} for row in result]
        return output

    def get_item_by_id(self, item_id):
        print("inside get_item_by_id")
        where_clause = f' AND id = {item_id}'
        return self.list_items(where_clause)



class User:
    TABLENAME = "User" 

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def __del__(self):
        self.conn.commit()
        self.conn.close()  

    def create(self, params):
        query = f'insert into {self.TABLENAME}' \
                f'(Name, Email)' \
                f'values ("{params.get("Name")}", "{params.get("Email")}")'

        self.conn.execute(query)

