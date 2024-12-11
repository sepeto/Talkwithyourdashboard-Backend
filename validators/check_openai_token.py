from openai import OpenAI

# Función para validar la clave de OpenAI
def check_openai_token(api_key):
    client = OpenAI(api_key=api_key)

    try:
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a tester of connection."},
                {
                    "role": "user",
                    "content": "Confirme message"
                }
            ]
        )
        return True
    except Exception as e:
        print(f"OpenAI API Key validation error: {e}")
        return False