import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    '''adicionando a opção de nome composto com o 'replace' '''
    nome_sem_espaco = nome.replace(" ", "") 
    return nome_sem_espaco.isalpha()

def validate_rg(rg):
    return len(rg) == 9 

def validate_celular(celular):
    '''Verifica se o celular é válido'''
    '''expressões regulares'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' 
    '''re.findall é uma função de verificação do modelo criado'''
    resposta = re.findall(modelo, celular)
    return resposta
    