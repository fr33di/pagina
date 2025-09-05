def ejemplo_largo():
    texto = '''Este es un texto largo
que ocupa varias líneas
y queremos que tenga scroll
para que no se expanda todo
en la página y solo se mueva
dentro del bloque de código'''
    for i in range(20):
        print(f"Línea {i}: {texto}")

ejemplo_largo()
