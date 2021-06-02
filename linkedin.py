#1 todas as importações 
from selenium import webdriver
from time import sleep 

#2 todos os parametros 
URL_LINKEDIN_DS = 'https://www.linkedin.com/jobs/search/?f_E=3&keywords=ci%C3%AAncia%20de%20dados&originalSubdomain=br'

#4 executando o código 
if __name__ == '__main__':
    #ACESSAR uma instancia do google Chrome pelo selenium 
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    #Acessar URL do linkedin
    driver.get(URL_LINKEDIN_DS)
    
    #pegar list de resultado de vagas de DS 
    resultados = driver.find_elements_by_class_name("result-card")
    lista_descricao = []
    
    #iniciar While loop em cima de todas os resultados
    
    while True:
        #for loop para coletar descrições de dados 
        for r in resultados[len(lista_descricao):]:
            r.click() # Clicar na descrição 
            sleep(1)
            try:
                #pegar elemento com as  descriçoes 
                descricao = driver.find_elements_by_class_name('description')
                #anexar o texto na lista 
                lista_descricao.append(descricao.text)
            except:
                print("erro")
                pass
            
            #critério de saida do while 
            if len(lista_descricao) == len(resultados):
                break 
        
        #salvar descrições de vagas 
        descricao_salvar = '\n'.join(lista_descricao)
        with open('descricoes_vagas.txt', 'w') as f:
            f.write(descricao_salvar)
        
        driver.quit()












