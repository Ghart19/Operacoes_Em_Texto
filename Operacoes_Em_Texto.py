import os
import re

# Limpa a tela do terminal
def clear_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

# Retorna o número de caracteres no texto.
def count_characters(text):

    return len(text)

# Retorna o número de caracteres no texto sem contar espaços.
def count_characters_no_spaces(text):
    no_space = ''.join(text.split())
    return len(no_space)

# Retorna o número de espaços no texto.
def count_spaces(text):
    count = text.count(' ')
    return count

# Retorna o número de ocorrências de uma letra específica no texto.
def count_specific_letter(text, letter):
    count = text.count(letter)
    return count

# Retorna o número de ocorrências de uma frase específica no texto.
def count_specific_phrase(text, phrase):
    count = text.count(phrase)
    return count

# Retorna o número de letras maiúsculas no texto.
def count_uppercase_letters(text):
    count = sum(1 for c in text if c.isupper())
    return count

# Retorna o número de letras minúsculas no texto.
def count_lowercase_letters(text):
    count = sum(1 for c in text if c.islower())
    return count

# Retorna o número de números no texto.
def count_numbers(text):
    count = sum(1 for c in text if c.isdigit())
    return count

# Retorna o texto ordenado em ordem alfabética.
def sort_text(text):
    words = re.findall(r'\w+', text)
    sorted_words = sorted(words, key=str.lower)
    sorted_text = ' '.join(sorted_words)
    return sorted_text

# Imprime o menu principal do script.
def print_menu():
    print('-' * 20)
    print(f'Seu texto é: {input_text}')
    print('-' * 20)
    print('''
[1] Contar o texto todo
[2] Contar apenas as frases, sem espaços
[3] Contar apenas os espaços
[4] Limpar tela
[5] Contar letra em especifico
[6] Contar frase em especifico
[7] Contar letras maiusculas
[8] Contar letras minusculas
[9] Contar numeros no texto
[10] Ordenar o texto em ordem alfabética
[11] Sair do programa
''')
    print(' ')

# Programa principal
clear_terminal()
print('-' * 20)
input_text = input('Digite o seu texto: ')

while True:
    print_menu()
    choice_user = input('Sua escolha: ').lower()

    if choice_user == '1':
        count = count_characters(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} caracteres.')

    elif choice_user == '2':
        count = count_characters_no_spaces(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} caracteres, sem espaços.')

    elif choice_user == '3':
        count = count_spaces(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} espaços.')

    elif choice_user == '4':
        clear_terminal()

    elif choice_user == '5':
        letter = input('Digite a letra que deseja contar: ')
        count = count_specific_letter(input_text, letter)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} ocorrências da letra "{letter}".')

    elif choice_user == '6':
        phrase = input('Digite a frase que deseja contar: ')
        count = count_specific_phrase(input_text, phrase)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} ocorrências da frase "{phrase}".')

    elif choice_user == '7':
        count = count_uppercase_letters(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} letras maiúsculas.')

    elif choice_user == '8':
        count = count_lowercase_letters(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} letras minúsculas.')

    elif choice_user == '9':
        count = count_numbers(input_text)
        clear_terminal()
        print('-' * 20)
        print(f'O texto contém {count} números.')

    elif choice_user == '10':
        sorted_text = sort_text(input_text)
        clear_terminal()
        print('-' * 20)
        print('Texto ordenado em ordem alfabética:')
        print(sorted_text)

    elif choice_user == '11':
        clear_terminal()
        print('-' * 20)
        print('Programa encerrado.')
        break

    else:
        clear_terminal()
        print('-' * 20)
        print('Escolha inválida. Tente novamente.')
