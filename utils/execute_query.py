from utils.generate_query import generate_query
import mysql.connector

def execute_query(config, query, api_key, db_structure, user_query):
    print('ejecutando query')
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(query)

        # Fetch all results if it's a SELECT query
        if query.lower().startswith('select'):
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            results = [dict(zip(columns, row)) for row in rows]
            return results if results else "No results found"
        
        # Commit changes if it's an UPDATE/INSERT/DELETE query
        conn.commit()
        return "Query executed successfully"
    
    except mysql.connector.Error as e:
        print('error query', e)
        message = f"Ocurrio el siguiente error {e} \n Con la  consulta {query} que generaste\n analiza el error y responde con el formato de respuesta que te brindo más abajo. "

        return generate_query(api_key, db_structure, user_query, message)

    finally:
        cursor.close()
        conn.close()
