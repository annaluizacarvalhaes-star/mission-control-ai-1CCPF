
print("============================================== ")
print ("MISSION CONTROL AI ")
print("============================================== ")
print("Missão: Orion Test Alpha \nEquipe: Equipe Apollo \nQuantidade de ciclos analisados: 6")
print("============================================== \n")

# temp, com, bat, oxig, estab
dados_missao = [
    [22, 90, 100, 96, 60], # linha 0 - ciclo 1
    [27, 78, 80, 92, 38],  # linha 1 - ciclo 2
    [31, 70, 76, 79, 70],  # linha 2 - ciclo 3
    [25, 40, 62, 89, 74],  # linha 3 - ciclo 4
    [30, 29, 58, 90, 89],  # linha 4 - ciclo 5
    [19, 80, 56, 90, 76]   # linha 5 - ciclo 6
]

pt_temp = 0
pt_comun = 0
pt_bat = 0
pt_oxig = 0
pt_estab = 0



def calcular_total():
    return pt_temp + pt_comun + pt_bat + pt_oxig + pt_estab

def classificar_total():
    total = calcular_total()
    if total <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= total < 6:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRITICA"


def analisar_temp(temp):
    global pt_temp
    if temp < 18:
        pt_temp = 2
        return "CRÍTICO", "Temperatura crítica"
    elif 18 <= temp <= 30:
        pt_temp = 0
        return "NORMAL", "Temperatura ideal"
    elif 30 < temp <= 35:
        pt_temp = 1
        return "ATENÇÃO", "Temperatura elevada"
    else:
        pt_temp = 2
        return "CRÍTICO", "Temperatura crítica"


def analisar_comunicacao(comun):
    global pt_comun
    if comun < 30:
        pt_comun = 2
        return "CRÍTICO", "Comunicação crítica"
    elif 30 <= comun < 60:
        pt_comun = 1
        return "ATENÇÃO", "Comunicação instável"
    else:
        pt_comun = 0
        return "NORMAL", "Comunicação estável"

def analisar_bateria(bat):
    global pt_bat
    if bat < 20:
        pt_bat = 2
        return "CRITICO"
    elif bat >= 20 and bat < 50:
        pt_bat = 1
        return "ATENCAO"
    else:
        pt_bat = 0
        return "NORMAL"


def analisar_oxigenio(oxig):
    global pt_oxig
    if oxig < 80:
        pt_oxig = 2
        return "CRÍTICO", "Oxigênio crítico"
    elif 80 <= oxig < 90:
        pt_oxig = 1
        return "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        pt_oxig = 0
        return "NORMAL", "Oxigênio ideal"


def analisar_estabilidade(estab):
    global pt_estab
    if estab < 40:
        pt_estab = 2
        return "CRÍTICO", "Instabilidade crítica"
    elif 40 <= estab < 70:
        pt_estab = 1
        return "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        pt_estab = 0
        return "NORMAL", "Estabilidade ideal"


def recomendacao():

    qld_temp = analisar_temp(temp)
    qld_comun = analisar_comunicacao(comun)
    qld_bat = analisar_bateria(bat)
    qld_oxig = analisar_oxigenio(oxig)
    qld_estab = analisar_estabilidade(estab)

    alertas = []

    if qld_temp == "ATENCAO" or qld_temp == "CRITICO":
        alertas.append("Verifique a temperatura") # append = adiciona a lista

    if qld_bat == "CRITICO" or qld_bat == "ATENCAO":
        alertas.append("Verifique a bateria")

    if qld_oxig == "CRITICO" or qld_oxig == "ATENCAO":
        alertas.append("Verifique o oxigênio")

    if qld_estab == "CRITICO" or qld_estab == "ATENCAO":
        alertas.append("Verifique a estabilidade")

    if qld_comun == "CRITICO" or qld_comun == "ATENCAO":
        alertas.append("Verifique a comunicação")

    if alertas:
        return " | ".join(alertas)
    else:
        return "Sistemas operando normalmente"



for i in range(len(dados_missao)):
    print(f"\n Ciclo {i+1}")

    temp = dados_missao[i][0]
    comun = dados_missao[i][1]
    bat = dados_missao[i][2]
    oxig = dados_missao[i][3]
    estab = dados_missao[i][4]


    print(f"  Temperatura: {temp}°C | {analisar_temp(temp)} | ")
    print(f"  Comunicação: {comun}% | {analisar_comunicacao(comun)} | ")
    print(f"  Bateria: {bat}% | {analisar_bateria(bat)} | ")
    print(f"  Oxigênio: {oxig}% | {analisar_oxigenio(oxig)} | ")
    print(f"  Estabilidade: {estab}% | {analisar_estabilidade(estab)} | ")
    print("-" * 30, "\n")

# ANÁLISE DE CICLO (COMPLETO)
    print("ANALISE DO CICLO ")
    print(f"Pontuação do ciclo: {calcular_total()}")
    print(f"Classificação do ciclo: {classificar_total()}")
    print(f"Recomendação: {recomendacao()}")


