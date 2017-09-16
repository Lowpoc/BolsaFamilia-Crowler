import wget
import os, errno
import json

# Matriz de Anos basta apenas configurar com o ano que deseja e ele ira buscar para o donwload
matriz = {}
matriz [2017] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz [2016] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz [2015] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz [2014] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz [2013] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
ano = {}

### Funcoes ###
def donwloadbBolsaFamiliaby(consulta):
    with open("./config/env.json") as env:
        data = json.load(env)
        url  = data["Bolsafamilia"]["url"]
    for ano in matriz:
        for mes in matriz[ano]:
            directory = "./Bolsafamilia/"+consulta+"/ANO/MES/"
            url = url.replace("{ano}",str(ano))
            url = url.replace("{mes}",mes)
            url = url.replace("{tipo}",consulta)            
            directory = directory.replace("ANO",str(ano))
            directory = directory.replace("MES",mes)
            arquivo = str(ano)+mes+consulta+".zip"
            try:  
                print " Novo Diretorio Criado :"+directory
                print "######Fazendo o donwload do arquivo do link("+url+")#######"
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise "Ja existe este diretorio : "+directory
            filename = wget.download(url,directory+arquivo)

def display_title_bar():
    # Banner inicial
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  CLi - Bolsa Familia (dados.gov.br)!  ***")
    print("\t**********************************************")
    
def get_resposta():
    # Perguntas 
    print("\n[1] Fazer donwload dos Pagamentos Bolsa Familia")
    print("[2] Fazer donwload dos Saques Bolsa Familia")
    print("[0] Sair.")
    
    return input("Escolha sua opcao?")

### Program ###
resposta = 9
display_title_bar()
while resposta != 0:    
    
    resposta = get_resposta()
    
    # Respond to the user's choice.
    display_title_bar()
    if resposta == 1:
        donwloadbBolsaFamiliaby("BolsaFamiliaFolhaPagamento")
    elif resposta == 2:
        donwloadbBolsaFamiliaby("BolsaFamiliaSacado")
    elif resposta == 0:
        print("\n Obrigado por usar nossa cli")
    else:
        print("\n Nao tem esta  opcao.\n")