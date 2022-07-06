#Bibliotecas
import json

import pytest
import requests

#Necessario fazer o caminho abaixo para importar pastas
from tests.utils.file_manager import ler_csv

# Variáveis publicas
url =   'https://petstore.swagger.io/v2/pet'
headers = {'Content-type': 'application/json'}

#Definições das funções (defs)

def test_incluir_pet():
    #Configura
        #Dados de entrada provém do pet1.json

        #Resultados esperados
        status_code_esperado = 200
        pet_id_esperado = 1004219
        pet_nome_esperado = "Maggienha"
        pet_nome_categoria = "Cachorros"
        pet_nome_tag_nome = "Vacinado"

    #Executa
        resultado_obtido = requests.post(
            url=url,
            headers=headers,
            data=open('../../vendors/Json/pet1.json')
        )
    #Válida
        print(resultado_obtido)
        corpo_resultado_obtido = resultado_obtido.json()
        print(json.dumps(corpo_resultado_obtido, indent=4))

        assert resultado_obtido.status_code == status_code_esperado
        assert corpo_resultado_obtido['id'] == pet_id_esperado
        assert corpo_resultado_obtido['name'] == pet_nome_esperado
        assert corpo_resultado_obtido['category']['name'] == pet_nome_categoria
        assert corpo_resultado_obtido['tags'][0]['name'] == pet_nome_tag_nome

def test_consultar_pet():
    # Configura
    pet_id = '1004219'

    status_code_esperado = 200
    pet_id_esperado = 1004219
    pet_nome_esperado = "Maggienha"
    pet_nome_categoria = "Cachorros"
    pet_nome_tag_nome = "Vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Válida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(corpo_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == pet_id_esperado
    assert corpo_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_resultado_obtido['category']['name'] == pet_nome_categoria
    assert corpo_resultado_obtido['tags'][0]['name'] == pet_nome_tag_nome

def test_alterar_pet():
    # Configura
    status_code_esperado = 200
    pet_id_esperado = 1004219
    pet_nome_esperado = "Maggienha"
    pet_nome_categoria = "Cachorros"
    pet_nome_tag_nome = "Vacinado"
    pet_status_esperado = "Indisponivel"

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('../../vendors/Json/pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == pet_id_esperado
    assert corpo_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_resultado_obtido['category']['name'] == pet_nome_categoria
    assert corpo_resultado_obtido['tags'][0]['name'] == pet_nome_tag_nome
    assert  corpo_resultado_obtido['status'] == pet_status_esperado

def test_excluir_pet():
    # Configura
        #Dados de Entrada
    pet_id = '1004219'

        #Resultados esperados
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '1004219'

    #Executa
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers
    )

    #Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert  resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['code'] == status_code_esperado
    assert corpo_resultado_obtido['type'] == type_esperado
    assert corpo_resultado_obtido['message'] == message_esperada

@pytest.mark.parametrize('pet_id, category_id, category_name, pet_name, tags_id, tag_names, status', ler_csv(
    '../../vendors/CSV/massa_incluir_pet.csv'))
def test_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tag_names, status):
    # 1. Configura
        # 1.1. Dados de Entrada
        # os dados de entrada proveem do arquivo massa_incluir_pet.csv
        # 1.1.1. Montagem do JSON dinâmico
    corpo_json = '  {   '
    corpo_json +=  f'    "id": {pet_id},  '
    corpo_json += '     "category": {   '
    corpo_json += f'    "id": {category_id}, '
    corpo_json += f'  "name": "{category_name}" '
    corpo_json += '  }, '
    corpo_json += f'  "name": "{pet_name}", '
    corpo_json += '  "photoUrls": [ '
    corpo_json += '  "string"   '
    corpo_json += '  ], '
    corpo_json += f'    "tags": [   '
    corpo_json += '  {   '
    corpo_json += f'  "id": {tags_id},   '
    corpo_json += f'      "name": "{tag_names}"   '
    corpo_json += '      }      '
    corpo_json += '     ],      '
    corpo_json += f'     "status": "{status}"    '
    corpo_json += '  }   '

        # 1.2. Resultado esperado
        # Como o resultado esperado é um eco, usaremos os dados de entrada como base
    status_code_esperado = 200

    # 2. Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )
    # 3. Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == int(pet_id)
    assert corpo_resultado_obtido['name'] == pet_name
    assert corpo_resultado_obtido['category']['name'] == category_name
    assert corpo_resultado_obtido['tags'][0]['name'] == tag_names
    assert corpo_resultado_obtido['status'] == status

def test_search_by_ID():
    # Configura
    pet_id = '44821902'
    status_code_esperado = 200
    category_id = 2
    category_name = 'gato'
    pet_name = 'Shoyu'
    tags_id = 3
    tag_names = 'castrado'
    status = 'disponivel'

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == int(pet_id)
    assert corpo_resultado_obtido['name'] == pet_name
    assert corpo_resultado_obtido['category']['id'] == category_id
    assert corpo_resultado_obtido['category']['name'] == category_name
    assert corpo_resultado_obtido['tags'][0]['name'] == tag_names
    assert corpo_resultado_obtido['status'] == status