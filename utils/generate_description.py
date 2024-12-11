from openai import OpenAI

def generate_description(api_key, db_structure, propmt):

    client = OpenAI(api_key=api_key)
    
    try:
        print('haciendo consulta a openai')
        prompt = f"{propmt}:\n\n{db_structure}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en bases de datos que explica estructuras de manera clara y concisa."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating description with GPT: {e}")
        return None