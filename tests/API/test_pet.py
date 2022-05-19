#Bibliotecas
import pytest
import requests

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
            data=open('C:\\Users\\ivana\\PycharmProjects\\134inicial\\vendors\\Json\\pet1.json')
        )
    #Válida
        print(resultado_obtido)
        corpo_resultado_obtido = resultado_obtido.json()
        print(corpo_resultado_obtido)

        assert resultado_obtido.status_code == status_code_esperado
        assert corpo_resultado_obtido['id'] == pet_id_esperado
        assert corpo_resultado_obtido['name'] == pet_nome_esperado
        assert corpo_resultado_obtido['category']['name'] == pet_nome_categoria
        assert corpo_resultado_obtido['tags'][0]['name'] == pet_nome_tag_nome
