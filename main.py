
elementos = {
    'H': {'nome': 'Hidrogênio', 'numero_atomico': 1, 'massa': 1.008},
    'He': {'nome': 'Hélio', 'numero_atomico': 2, 'massa':40086},
    'Li': {'nome': 'Lítio', 'numero_atomico': 3, 'massa': 6.941},
    'Be': {'nome': 'Berílio', 'numero_atomico': 4, 'massa': 9.012182},
    'B': {'nome': 'Boro', 'numero_atomico': 5, 'massa': 10.811},
    'C': {'nome': 'Carbono', 'numero_atomico': 6, 'massa': 12.0107},
    'N': {'nome': 'Nitrogênio', 'numero_atomico': 7, 'massa': 14.0067},
    'O': {'nome': 'Oxigênio', 'numero_atomico': 8, 'massa': 15.9994},
    'F': {'nome': 'Flúor', 'numero_atomico': 9, 'massa': 18.9984032},
    'Ne': {'nome': 'Neônio', 'numero_atomico': 10, 'massa': 20.1797}
}

def buscar_elementos(sigla):
    sigla = sigla.upper() 
    if sigla in elementos:
        elemento = elementos[sigla]
        print(f"Nome: {elemento['nome']}")
        print(f"Número atômico: {elemento['numero_atomico']}")
        print(f"Massa: {elemento['massa']}")
    else:
        print("Elemento não encontrado!")

sigla = input("Digite a sigla do elemento químico: ")


buscar_elementos(sigla)