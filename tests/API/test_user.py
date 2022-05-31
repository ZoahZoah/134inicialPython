# Done: 1 - Criar um teste que adicione um usuário
# Done: 2 - Realizar o login e extrair o token da resposta
import json

import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
username = 'jorjinho'

#Necessario fazer o caminho abaixo para importar pastas
from tests.utils.file_manager import ler_csv

def test_incluir_usuario():
    # Configura
        # Dados de Entrada
        # Virão do arquivo user1.json

        #Resultados esperados
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = '4219448'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\ivana\\PycharmProjects\\134inicial\\vendors\\Json\\user1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert corpo_resultado_obtido['message'] == message_esperado

def test_login():
    #Configura
        # Dados de entrada
    username = 'jorjinho'
    password = 'jorjinhoeluana'

        # Resultado_esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers,
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert message_esperado.find(corpo_resultado_obtido['message'])

    # Extrai
    mensagem_extraida = corpo_resultado_obtido.get('message')
    print(f'A mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23:36]  #o numero correspondete aos colchetes, é qual letra ele deseja pegar; [inicio:fim:passos]
    print(f'O token = {token}')

def test_logout():
    # Configura
        # Dados de entrada
        # Resultado esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = 'ok'

    # Executa
    resultado_obtido = requests.get(
        url=url +'/logout',
        headers=headers,
    )
    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert corpo_resultado_obtido['message'] == message_esperado

def test_delete_user():
    # Configura
        #Dados de Entrada
    username = 'jorjinho'
        # Resultado esperado
    status_code_esperado = 404
    message_code_esperado = 'Error: response status is 404'

    # Executa
    resultado_obtido = requests.delete(
        url=f'{url}/{username}',
        headers=headers,
    )
    #Valida
    print(resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado

def test_update_user():
    # Configura
        # Dados de Entrada
        # Dados de entrada virão do user2.json

        # Resultado esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = '4219448'

    # Executa
    resultado_obtido = requests.put(
        url=f'{url}/{username}',
        headers=headers,
        data=open('C:\\Users\\ivana\\PycharmProjects\\134inicial\\vendors\\Json\\user2.json')
    )

    # Válida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert corpo_resultado_obtido['message'] == message_esperado

@pytest.mark.parametrize('user_id, user_username, user_firstName, user_lastName, user_email, user_password, user_phone',
                         ler_csv('C:\\Users\\ivana\\PycharmProjects\\134inicial\\vendors\\CSV\\massa_incluir_user.csv'))
def test_incluir_usuario_csv(user_id, user_username, user_firstName, user_lastName, user_email, user_password, user_phone):
    # Configura
        # Dados de entrada
        # os dados proveem do csv
        # 1.1 Json dinamico
    corpo_json =     '  {   '
    corpo_json +=f'   "id": {user_id},    '
    corpo_json +=f'   "username": "{user_username}",    '
    corpo_json +=f'   "firstName": "{user_firstName}",     '
    corpo_json +=f'   "lastName": "{user_lastName}",    '
    corpo_json +=f'   "email": "{user_email}",   '
    corpo_json +=f'   "password": "{user_password}",    '
    corpo_json +=f'   "phone": "{user_phone}",  '
    corpo_json +='    "userStatus": 0  '
    corpo_json +=    ' }   '

        # Resultado Esperado
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = user_id



    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == status_code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert corpo_resultado_obtido['message'] == message_esperado
