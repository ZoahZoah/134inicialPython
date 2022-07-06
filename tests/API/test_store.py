# Done: 3 - criar uma venda de um pet para um usuário
# Done: 4 - consultar os dados do pet que foi vendido
import json
from datetime import datetime
import requests

url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

def test_vender_pet():
    #Configura
        # Dados de Entrada
        # Virão do arquivo store1.json

        # Resultado esperado
    status_code_esperado = 200
    id_pedido_esperado = 93100875
    pet_id_esperado = 1004219
    status_venda_esperado = 'placed'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('../../vendors/Json/store1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_resultado_obtido['status'] == status_venda_esperado
    corpo_resultado_obtido['shipDate'] = datetime.today()
    print(corpo_resultado_obtido['shipDate'])

def test_buscar_pet_store():
    # Configura
        # Dados de Entrada
        # Resultado Esperado

    # Executa

    # Valida