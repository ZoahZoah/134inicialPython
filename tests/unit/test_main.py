from main import somar, subtrair, multiplicar, dividir


class TesteContas:
    def test_somar(self):
        # 1 - Configura
        # 1.1 - Dados de Entrada
        numero_a = 3
        numero_b = 18

        # 1.2 - Resultados Esperados
        resultado_esperado = 21

        # 2 - Executa
        resultado_obtido = somar(numero_a, numero_b)

        # 3 - Valida
        assert resultado_esperado == resultado_obtido

    def test_subtrair(self):
        numero_a = 3
        numero_b = 18
        resultado_esperado = -15

        resultado_obtido = subtrair(numero_a, numero_b)
        assert resultado_esperado == resultado_obtido

    def test_multiplicar(self):
        numero_a = 3
        numero_b = 18
        resultado_esperado = 54

        resultado_obtido = multiplicar(numero_a, numero_b)
        assert resultado_esperado == resultado_obtido

    def test_dividir(self):
        numero_a = 18
        numero_b = 3
        resultado_esperado = 6

        resultado_obtido = dividir(numero_a, numero_b)
        assert resultado_esperado == resultado_obtido

    # TDD = Test Driven Development
    #       Desenvolvimento Direcionado por Teste
    #
    # - Criar todos os testes de unidade no começo?
    # - Executar todos os testes pelo menos 1 vez por dia
    #
    # Imagine que você no primeiro dia (nada pronto)
    # Você executa todos os testes - o que acontece?
    # Dia 01 - Falhou 100 - Passou 000
    # Dia 02 - Falhou 095 - Passou 005
    # Dia 03 - Falhou 090 - Passou 010
    # Dia 04 - Falhou 088 - Passou 012
    # Dia 05 - Falhou 081 - Passou 019
    # Dia 06 - Falhou 075 - Passou 025
    # Informação sobre o progresso
    # Insistir mais um dia        1 + 1 = 2?
    # Pedir ajuda                 1 + 2 = 3
    # Devolver e pegar outra      1 + 1 = 2!
    # Tudo certo!                 1 + 2 = 4
    # TDD: Teste é uma medida de progresso

    # CI: Continuous Integration
    # IC> Integração Continua

    # (Build) --> Suite de Testes -------> (Build)
    #             Automatizada     Passou
    # Ambiente                            Então, move >> Ambiente
    # de Desenvolvimento                                 de Teste

    # CD: Continuou Delivery
    # EC: Entrega Continua

    # (Build) -->  Suite  --> (Build) -------> (Build)
    #   Dev       de Teste     Teste   Muitos   Produção
    #                                  Testes
