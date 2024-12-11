from openai import OpenAI

def generate_query(api_key, db_structure, user_query, error_message):
    
    client = OpenAI(api_key=api_key)
    try:
        prompt = (
            f"Utilizando la siguiente estructura de la base de datos, convierte la pregunta del usuario en una consulta MySQL válida:\n\n"
            f"Estructura de la base de datos: {db_structure}\n\n"
            f"Pregunta del usuario: {user_query}\n\n"
            f"{error_message} \n"
            "Por favor, proporciona una consulta MySQL que sea compatible con la estructura proporcionada. Da solo la consulta sin ningun dato mas ni introducción ni signos."
            "ejemplo>> -peticion: dime todas los datos de pacientes con 10 años. -respuesta: SELECT * FROM paciente WHERE edad = 10;"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en bases de datos y consultas SQL."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            temperature=0.5,
        )

        sql_query = response.choices[0].message.content
        return sql_query, prompt
    except Exception as e:
        print(f"Error generating SQL query with GPT: {e}")
        return None, prompt
