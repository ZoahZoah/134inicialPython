# Função de login
import pytest # Biblioteca principal para testes
from selenium import webdriver # Import necessário pro webdriver
from selenium.webdriver.common.by import By
import time

# Configuração
    # Dados de entrada
nome_conta = 'Ivan Mendonca'
e_mail = 'ivantestado@teste.com.br'
senha = 'teste123'

# Executa
class TestLogin:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(
            '../../vendors/drivers/chromedriver102.exe'
        )

    def test_testlogin(self):
        # Definindo o site de testes
        self.driver.get('http://automationpractice.com/index.php')

        # Acessando loginPage
        self.driver.find_element(By.CSS_SELECTOR, 'div.header_user_info').click()

        # Preenchendo os campos de LogIn
        self.driver.find_element(By.ID, 'email').send_keys(f'{e_mail}')
        self.driver.find_element(By.ID, 'passwd').send_keys(f'{senha}')
        self.driver.find_element(By.CSS_SELECTOR, '#SubmitLogin > span').click()

        # Valida
        assert self.driver.find_element(By.CSS_SELECTOR, '.account > span').text == f'{nome_conta}'
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'b')
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, 'li > .btn > span')
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.logo')
