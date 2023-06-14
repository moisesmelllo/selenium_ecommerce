import os
from selenium import webdriver
from constantes import *


class Ecommerce(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\moise\OneDrive\Área de Trabalho\SELENIUMDRIVER\chromedriver.exe",
                 teardow=False):
        self.preco = None
        self.nome = None
        self.dados = []
        self.driver_path = driver_path
        self.teardow = teardow
        os.environ['PATH'] += driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging']
        )
        super(Ecommerce, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardow:
            quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def crawling_products(self):
        celulares = self.find_elements('xpath', "//div[@class='single-shop-product']")
        for celular in celulares:
            print('Guardando valores da pagina atual...')
            self.nome = celular.find_element('xpath', './/h2/a').get_attribute('innerHTML')
            self.preco = celular.find_element(
                'xpath', ".//div[@class='product-carousel-price']/ins").get_attribute('innerHTML')
            self.dados.append([self.nome, self.preco])

    def next_page(self):
        print('Indo para a proxima pagina')
        botao_prox_pagina = self.find_element('xpath', '//a[@aria-label="Next"]')
        botao_prox_pagina.click()

    def save_to_excel(self):
        with open('dados.csv', 'a', encoding='utf-8', newline='') as file:
            file.write(f'{"Marca"}, {"Preço"}, {os.linesep}')
            for dado in self.dados:
                file.write(f'{dado[0]}, {dado[1]}, {os.linesep}')
            file.close()

