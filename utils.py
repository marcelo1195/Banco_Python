import re
from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def validar_formato_data():
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    while True:
        data_nascimento_str = input("Digite sua data de nascimento no formato DD/MM/YYYY: ")
        if re.match(pattern, data_nascimento_str):
            try:
                # Verificamos se a data é válida, mas retornamos a string
                datetime.strptime(data_nascimento_str, "%d/%m/%Y")
                return data_nascimento_str
            except ValueError:
                print("Data inválida. Por favor, insira uma data existente.")
        else:
            print("Formato de data inválido. Por favor, use o formato DD/MM/YYYY.")