def message_creator(text):
    respuesta = text
    if text == "computadora":
        respuesta = "con mi computadora puedo programar en python"
    elif text == "celular":
        respuesta = "En mi celular puedo aprender usando la app de Platzi"
    elif text == "cable":
        respuesta = "¡Hay un cable en mi bota!"
    else:
        respuesta =="Articulo no encontrado"
        
    return respuesta

text = 'computadora'
response = message_creator(text)
print(response)