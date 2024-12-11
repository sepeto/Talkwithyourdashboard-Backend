import mysql.connector

def connect_to_db(config):
    try:
        conn = mysql.connector.connect(**config)
        print("Successfully connected to the database")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_db_structure(conn):
    try:
        cursor = conn.cursor()
        db_structure = {"tables": []}

        # Get list of tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0].decode('utf-8') if isinstance(table[0], bytes) else table[0]
            table_info = {"name": table_name, "columns": []}

            # Get columns for each table
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()

            for column in columns:
                column_info = {
                    "name": column[0].decode('utf-8') if isinstance(column[0], bytes) else column[0],
                    "type": column[1].decode('utf-8') if isinstance(column[1], bytes) else column[1],
                    "null": column[2].decode('utf-8') if isinstance(column[2], bytes) else column[2],
                    "key": column[3].decode('utf-8') if isinstance(column[3], bytes) else column[3],
                    "default": column[4].decode('utf-8') if isinstance(column[4], bytes) else column[4],
                    "extra": column[5].decode('utf-8') if isinstance(column[5], bytes) else column[5]
                }
                table_info["columns"].append(column_info)

            db_structure["tables"].append(table_info)

        cursor.close()
        return db_structure
    except mysql.connector.Error as e:
        print(f"Error getting database structure: {e}")
        return None


def check_db(config):
    conn = connect_to_db(config)
    if conn:
        structure = get_db_structure(conn)
        conn.close()
        return structure
    return None