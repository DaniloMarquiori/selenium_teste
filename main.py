# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time


def config_selenium():
    options = webdriver.ChromeOptions()
    # Descomentar linha abaixo caso queira rodar em background
    # options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Danilo Marquiori\Documents\Desenvolvimentos\Selenium\chromedriver\chromedriver.exe")

    return driver

driver = config_selenium()

driver.get('http://automationpractice.com/index.php')

valida_pagina_home = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'header_logo')))

if valida_pagina_home:
    busca_produto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search_query_top"]')))
    
    time.sleep(5)

    busca_produto.clear()
    busca_produto.send_keys('Blouse')

    busca_botao = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchbox"]/button')))
    busca_botao.click()

    validar_pagina_busca = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span')))
     
    time.sleep(2)

    # action = webdriver.ActionChains(driver)
    # imagem_produto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')))        
    # action.move_to_element(imagem_produto)
    # action.click(adiciona_carrinho).perform()
    # action.pause(3)
   
    imagem_produto = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="best-sellers_block_right"]/div/ul/li[3]/a/img')))
    imagem_produto.click()
    time.sleep(5)
    adiciona_carrinho = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add_to_cart"]/button')))
    adiciona_carrinho.click()
    
    valida_modal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'layer_cart')))

    if valida_modal:
        time.sleep(2)

        proceguir_carrinho = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')))
        proceguir_carrinho.click()            

        valida_pagina_finalizar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]')))

        if valida_pagina_finalizar:
            time.sleep(2)

            finalizar_carrinho = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
            finalizar_carrinho.click()
            time.sleep(2)

            valida_pagina_autentificacao = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="columns"]')))

            if valida_pagina_autentificacao:
                time.sleep(2)

                email_conta = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'email_create')))
                email_conta.send_keys('larissaleticia4@teste.com')
                registar_conta = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'SubmitCreate')))    
                registar_conta.click()

                valida_pagina_informacoes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-creation_form"]')))

                if valida_pagina_informacoes:
                    time.sleep(2)

                    cadastro_sexo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'id_gender2')))
                    cadastro_sexo.click()

                    cadastro_nome = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'customer_firstname')))
                    cadastro_nome.send_keys('Larissa')

                    cadastro_sobrenome = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'customer_lastname')))
                    cadastro_sobrenome.send_keys('Letícia Marli Lopes')

                    cadastro_senha = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'passwd')))
                    cadastro_senha.send_keys('lGUWB6ylM7y')

                    cadastro_dia = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'days')))
                    cadastro_dia.send_keys('27')

                    cadastro_mes = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'months')))
                    cadastro_mes.send_keys('January')

                    cadastro_ano = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'years')))
                    cadastro_ano.send_keys('1998')

                    cadastro_seguir = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'newsletter')))
                    cadastro_seguir.click()

                    cadastro_receber = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'optin')))
                    cadastro_receber.click()
                    
                    cadastro_companhia = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'company')))
                    cadastro_companhia.send_keys('Teste')

                    cadastro_ano = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'years')))
                    cadastro_ano.send_keys('1998')

                    cadastro_endereco = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'address1')))
                    cadastro_endereco.send_keys('Rua Sao Sebastiao')

                    cadastro_endereco2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'address2')))
                    cadastro_endereco2.send_keys('Casa')

                    cadastro_cidade = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'city')))
                    cadastro_cidade.send_keys('São José do Rio Preto')

                    cadastro_estado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'id_state')))
                    cadastro_estado.send_keys('New York')

                    cadastro_CEP = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'postcode')))
                    cadastro_CEP.send_keys('02550')

                    cadastro_pais = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'id_country')))
                    cadastro_pais.send_keys('United States')

                    cadastro_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'other')))
                    cadastro_info.send_keys('Trata-se de dados de teste')

                    cadastro_telefone = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'phone')))
                    cadastro_telefone.send_keys('17912345678')

                    cadastro_celular = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'phone_mobile')))
                    cadastro_celular.send_keys('17912345678')
                    
                    cadastro_titulo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'alias')))
                    cadastro_titulo.clear()
                    cadastro_titulo.send_keys('Meu Endereço')

                    cadastrar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'submitAccount')))
                    cadastrar.click()

                    checkout = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="center_column"]/form/p/button/span')))
                    checkout.click()

                    concordar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'cgv')))
                    concordar.click()

                    checkout2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/p/button/span')))
                    checkout2.click()

                    cartao = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
                    cartao.click()
                    
                    confirmar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart_navigation"]/button/span')))
                    confirmar.click()
                else:
                    print ("pagina informações não carregou")

            else:
                print ("pagina login/cadastro não carregou")

        else:
            print ("Pagina finalizar pedido não carregou")

    else:
        print ("pagina buscar produto não carregou") 

else:
    print ("Pagina não carregou")



driver.close()