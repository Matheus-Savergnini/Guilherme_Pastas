#versao 0.0.2
#problemas futuros [maioria dos problemas resolvidos]

##anos bissextos
##2020	2024	2028	2032	2036
##2040	2044	2048	2052	2056
##2060	2064	2068	2072	2076
##2080	2084	2088	2092	2096
##if statment que compara o proximo ano bissexto
##e acrescenta 1 dia caso true.

##Ordem dos meses	Mês	Dias
##1	Janeiro	tem 31 dias
##2	Fevereiro	tem 28 dias (29 dias nos anos bissextos)
##3	Março	tem 31 dias
##4	Abril	tem 30 dias
##5	Maio	tem 31 dias
##6	Junho	tem 30 dias
##7	Julho	tem 31 dias
##8	Agosto	tem 31 dias
##9	Setembro	tem 30 dias
##10 Outubro	tem 31 dias
##11 Novembro	tem 30 dias
##12 Dezembro	tem 31 dias

import datetime
import os

# diretório atual
base_path = os.getcwd()

#ano atual
ano_atual_int = datetime.datetime.now().year
ano_atual = str(ano_atual_int)
ano = [ano_atual]
ano_bissexto = False

if ano_atual_int == 2024:
    ano_bissexto = True
elif ano_atual_int == 2028:
    ano_bissexto = True
elif ano_atual_int == 2032:
    ano_bissexto = True
elif ano_atual_int == 2036:
    ano_bissexto = True


#pasta ano
path_pasta_ano = os.path.join(base_path, ano_atual)

#pasta mes
def pasta_mes(arg):
    global path_pasta_mes
    path_pasta_mes = os.path.join(path_pasta_ano, arg)
    try:
        os.mkdir(path_pasta_mes)
    except OSError as error:
        print(error)


def pasta_dia(dia, mes):
    if int(dia) < 10:
        path = f"0{dia}.{mes}.{ano_atual}"
    else:
        path = f"{dia}.{mes}.{ano_atual}"
    path_pasta_dia = os.path.join(path_pasta_mes, path)
    try:
        os.mkdir(path_pasta_dia)
    except OSError as error:
        print(error)


#12 meses do ano
meses = ["01.janeiro", "02.fevereiro", "03.março", "04.abril", "05.maio", "06.junho", "07.julho", "08.agosto", "09.setembro", "10.outubro", "11.novembro", "12.dezembro"]
meses_in_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

dict = {"01.janeiro": "01",
        "02.fevereiro": "02",
        "03.março": "03",
        "04.abril": "04",
        "05.maio": "05",
        "06.junho": "06",
        "07.julho": "07",
        "08.agosto": "08",
        "09.setembro": "09",
        "10.outubro": "10",
        "11.novembro": "11",
        "12.dezembro": "12"
        }

#dias do ano
dias_31 = list(range(1, 32))
dias_30 = list(range(1, 31))
dias_29 = list(range(1, 30))
dias_28 = list(range(1, 29))


#função que executa tudo
for i in ano:
    #cria a pasta ano
    try:
        os.mkdir(path_pasta_ano)
    except OSError as error:
        print(error)
    #cria as pastas meses
    for g in meses:
        pasta_mes(g)
        #retorna path_pasta_mes como variáveis globais
        #cria pastas dias
        if g == "01.janeiro":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "02.fevereiro":
            if ano_bissexto == True:
                for m in dias_29:
                    meses_formatados = dict.get(g)
                    pasta_dia(str(m), meses_formatados)
            elif ano_bissexto == False:
                for m in dias_28:
                    meses_formatados = dict.get(g)
                    pasta_dia(str(m), meses_formatados)

        elif g == "03.março":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "04.abril":
            for m in dias_30:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "05.maio":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "06.junho":
            for m in dias_30:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "07.julho":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "08.agosto":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "09.setembro":
            for m in dias_30:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "10.outubro":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "11.novembro":
            for m in dias_30:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)

        elif g == "12.dezembro":
            for m in dias_31:
                meses_formatados = dict.get(g)
                pasta_dia(str(m), meses_formatados)