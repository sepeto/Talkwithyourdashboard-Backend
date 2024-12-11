import mysql.connector



# Función para validar la conexión a MySQL
def check_mysql_connection(db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            connection.close()
            return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    return False