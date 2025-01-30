from openai import OpenAI

# Inicializa el cliente OpenAI una vez para evitar inicializarlo en cada llamada
client = OpenAI(
    api_key="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"
)


def handle_thread(client, message_content, thread_id=None):
    """
    Maneja la lógica de creación de un thread y procesamiento de mensajes.
    """
    assistant_id = "asst_0NXHt3Rxeu2QUqU6ZcMSVQZP"

    # Crear thread si no se proporciona el thread_id
    if not thread_id:
        thread = client.beta.threads.create()
        thread_id = thread.id

    # Crear el mensaje en el thread
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message_content,
    )

    # Ejecutar y esperar la respuesta del asistente
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    # Verificar el estado del run
    if run.status == "completed":
        # Obtener mensajes del thread
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content[0].text.value, thread_id
    else:
        return f"Run status: {run.status}", thread_id
