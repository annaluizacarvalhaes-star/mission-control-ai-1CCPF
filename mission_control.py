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
'''
pt_temp = []
pt_comun = []
pt_bat = []
pt_oxig = []
pt_estab = []


pt_total = pt_temp + pt_comun + pt_bat + pt_oxig + pt_estab
'''

def analisar_temp(temp):
    if temp < 18:
        return "CRÍTICO"
        pt_temp == 2
    elif temp >= 18 and temp <= 30:
        return "NORMAL"
        pt_temp == 0
    elif temp > 30 and temp <= 35:
        return "ATENCAO"
        pt_temp == 1
    else:
        return "CRITICO"
        pt_temp == 2

def analisar_comunicacao(comun):
    if comun < 30:
        return "CRITICO"
        pt_comun == 2
    elif comun >= 30 and comun < 60:
        return "ATENCAO"
        pt_comun == 1
    else:
        pt_comun == 0
        return "NORMAL"

def analisar_bateria(bat):
    if bat < 20:
        return "CRITICO"
        pt_bat == 2

    elif bat >= 20 and bat < 50:
        return "ATENCAO"
        pt_bat == 1

    else:
        return "NORMAL"
        pt_bat == 0

def analisar_oxigenio(oxig):
    if oxig < 80:
        return "CRITICO"
        pt_oxig == 2
    elif oxig >= 80 and oxig < 90:
        return "ATENCAO"
        pt_oxig == 1
    else:
        return "NORMAL"
        pt_oxig == 0

def analisar_estabilidade(estab):
    if estab < 40:
        return "CRITICO"
        pt_estab == 2
    elif estab >= 40 and estab < 70:
        return "ATENCAO"
        pt_estab == 1
    else:
        return "NORMAL"
        pt_estab == 0

# Análise dos ciclos
def analise_ciclo(num_ciclo, status_temp, status_comun, status_bat, status_oxig, status_estab):
    todos_status = [status_temp, status_comun, status_bat, status_oxig, status_estab]

    if "CRITICO" in todos_status:
        resultado = "MISSÃO CRÍTICA"
        recomendacao = "verificar"

    elif "ATENCAO" in todos_status:
        resultado = "MISSÃO CRÍTICA"
        recomendacao = "Verificar controle térmico da missão."


for i in range(len(dados_missao)):
    print(f"\n Ciclo {i+1}")


    temp = dados_missao[i][0]
    comun = dados_missao[i][1]
    bat = dados_missao[i][2]
    oxig = dados_missao[i][3]
    estab = dados_missao[i][4]

    print(f"  Temperatura: {temp}°C - Status: {analisar_temp(temp)}")
    print(f"  Comunicação: {comun}% - Status: {analisar_comunicacao(comun)}")
    print(f"  Bateria: {bat}% - Status: {analisar_bateria(bat)}")
    print(f"  Oxigênio: {oxig}% - Status: {analisar_oxigenio(oxig)}")
    print(f"  Estabilidade: {estab}% - Status: {analisar_estabilidade(estab)}")
    print("-" * 30, "\n")

    print("ANALISE DO CICLO ")
    print(f"Pontuação do ciclo: {pt_total}")
