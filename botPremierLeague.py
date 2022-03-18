import requests # importamos as blibliotecas
from lxml import html #Importamos as bibliotecas
txt = '' #Variavel criada com '' (vazia) para armazenar os testos pegos no html
requisiçao = requests.get('https://www.terra.com.br/esportes/futebol/internacional/inglaterra/campeonato-ingles/tabela/') #link do site que iremos minerar (.get para obter as informaçoes do site)

tree = html.fromstring(requisiçao.content)#aqui estamos ultilizando um método para requisiçao pro html através da bilioteca requests

contador = 1 #contador iniciando em 1 para pegar as informaçoes
linha = 1  #linha = 1 para pegar cd informaçao da tabela uma por uma

print ('Times           P J V E D GP GC SG %') # print para organizar as informaçoes obtidas

while linha < 21: #laço de repetiçao < 21 para pegar todos os times (o contador inicia em 0 e percorre o laço 21 vezes até trazer todos os times)
    times = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[3]/text ()' %contador) # aqui pegando o elemento xpath da pagina html e adicionados um [%d] pois sera o contador que somara todas as informçaoes da tabela
    pontos = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[5]/text ()' %contador) #text() é para pegar a informaçao em forma de texto (string) e o %contador para contar cada requisiçao feita na pagina
    jogos = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[6]/text ()' %contador)
    vitorias = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[7]/text ()' %contador)
    empates = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[8]/text ()' %contador)
    derrotas = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[9]/text ()' %contador)
    gols_pro = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[10]/text ()' %contador)
    gols_contra = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[11]/text ()' %contador)
    saldo_de_gols = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[12]/text ()' %contador)
    aproveitamento = tree.xpath('//*[@id="mod-603-standings-round-robin"]/div[1]/div[1]/table/tbody/tr[%d]/td[13]/text ()' %contador)

    txt =  txt + (str(times) +' | '+str(pontos)+' | '+str(jogos)+' | '+str(vitorias)+' | '+str(empates)+' | '+str(derrotas)+' | '+str(gols_pro)+' | '+str(gols_contra)+' | '+str(saldo_de_gols)+' | '+str(aproveitamento)+' | \n') #str quer dizer string, | para separar as informaçoes, + pq eu quero pegar ex: jogos + pontos
    #txt recebe todas as variaveis +str para obter todas as informaçoes da pagina em formato de string

    linha = linha + 1 #contabilizador para cada requisiçao da tabela
    contador = contador + 1 #somador que contabiliza todos os times obtidos
print(txt.replace(chr(93), '').replace(chr(91), '').replace(chr(39), '')) #estamos adicionando uma | atráves do replace com numeros de acordo com a tabela ASC

print ('.:: FIM DO BOOT ::.') # print indicando o fim do bot