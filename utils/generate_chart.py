from openai import OpenAI

def generate_chart(api_key, json, prompt, graph_type):
    print("Ejecutando creador de gráficas")

    
    client = OpenAI(api_key=api_key)

    try:
        prompt = (
            f"A partir de la siguiente estructura JSON \n {json} \n crea una gráfica de tipo {graph_type} debes de utilizar HTML, CSS y JS y la libreria 3D JS."
            f"Adicional a ello toma en consideración estas instrucciones {prompt}."
            f"Muy importante, debes de retornarme solo código HTML el cual debe de tener un elemento section como contenedor, omit toda la estructura inicial del HTML"
            f"Ejemplo de respuesta: <section> ...codigo generado para crear la gráfica </section>"

            f"Algunas consideraciones más: tu resultado se agregará a un elemento HTML mediante el atributo 'dangerouslySetInnerHTML' que proporciona ReactJS "
            f"Si escribes código script los eventos que uses deben de funcionar con el punto anterior"
            f"La librería D3JS ya la tengo importada en mi web así que no hay necesidad de que la importes"
            f"La gráfica debería de renderizarce al momento de que cargue el HTML en mi web. asegurate de agregar el evento correcto"
            )
        
        print(prompt)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en bases de datos y creación de gráficas con HTML, CSS y JS."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating chart with GPT: {e}")
        return None

