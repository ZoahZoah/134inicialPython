# Done: 1 - Criar um teste que adicione um usuário
# Done: 2 - Realizar o login e extrair o token da resposta
import json

import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

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