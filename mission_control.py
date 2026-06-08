print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão: Orion Test Alpha")
print("Equipe: Equipe Apollo")
print("Quantidade de ciclos analisados: 6")
print("=" * 60)

# temp, comun, bat, oxig, estab
dados_missao = [
    [24, 92, 88, 96, 90],  # ciclo 1
    [27, 80, 72, 94, 85],  # ciclo 2
    [31, 65, 58, 91, 70],  # ciclo 3
    [36, 42, 38, 87, 55],  # ciclo 4
    [39, 28, 19, 78, 35],  # ciclo 5
    [34, 55, 32, 82, 50],  # ciclo 6
]

# Acumuladores por área (somam ao longo dos ciclos 1 até N-1)
pt_temp  = 0
pt_comun = 0
pt_bat   = 0
pt_oxig  = 0
pt_estab = 0


# ANÁLISE DOS CICLOS

def analisar_temp(temp):
    if temp < 18:
        return "CRÍTICO", "Risco de congelamento", 2
    elif temp <= 30:
        return "NORMAL", "Temperatura estável", 0
    elif temp <= 35:
        return "ATENÇÃO", "Temperatura elevada", 1
    else:
        return "CRÍTICO", "Risco de superaquecimento", 2


def analisar_comunicacao(comun):
    if comun < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico", 2
    elif comun < 60:
        return "ATENÇÃO", "Comunicação instável", 1
    else:
        return "NORMAL", "Comunicação estável", 0


def analisar_bateria(bat):
    if bat < 20:
        return "CRÍTICO", "Bateria em nível crítico", 2
    elif bat < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado", 1
    else:
        return "NORMAL", "Energia estável", 0


def analisar_oxigenio(oxig):
    if oxig < 80:
        return "CRÍTICO", "Oxigênio em nível crítico", 2
    elif oxig < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal", 1
    else:
        return "NORMAL", "Oxigênio adequado", 0


def analisar_estabilidade(estab):
    if estab < 40:
        return "CRÍTICO", "Estabilidade operacional crítica", 2
    elif estab < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida", 1
    else:
        return "NORMAL", "Estabilidade operacional adequada", 0


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco < 6:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def recomendacao_ciclo(risco, st_temp, st_comun, st_bat, st_oxig, st_estab):
    if risco == 0:
        return "Manter operação normal e continuar monitoramento."

    tem_critico = "CRÍTICO" in (st_temp, st_comun, st_bat, st_oxig, st_estab)

    if tem_critico:
        return ("Ativar modo de segurança e priorizar suporte à vida,\n"
                "energia e comunicação.")


    if st_temp == "ATENÇÃO":
        return "Verificar controle térmico da missão."

    return ("Monitorar sistemas em atenção e preparar plano de\n"
            "contingência.")


def calcular_media(coluna):
    return sum(d[coluna] for d in dados_missao) / len(dados_missao)


def calcular_tendencia(riscos):
    metade = len(riscos) // 2
    media_inicio = sum(riscos[:metade]) / metade
    media_fim    = sum(riscos[metade:]) / metade
    if media_fim > media_inicio:
        return "A missão apresentou tendência de piora."
    elif media_fim < media_inicio:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão manteve tendência estável."


def classificar_final(risco_medio):
    if risco_medio <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco_medio < 6:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def area_mais_afetada(pt_t, pt_c, pt_b, pt_o, pt_e):
    areas = {
        "Temperatura interna":      pt_t,
        "Comunicação com a base":   pt_c,
        "Sistema de energia":       pt_b,
        "Suporte de oxigênio":      pt_o,
        "Estabilidade operacional": pt_e,
    }
    return max(areas, key=areas.get)


def conclusao_final(classificacao, tendencia):
    if classificacao == "MISSÃO ESTÁVEL":
        return ("A missão transcorreu dentro dos parâmetros normais. "
                "Todos os sistemas operaram de forma adequada e nenhuma "
                "intervenção crítica foi necessária.")
    elif classificacao == "MISSÃO EM ATENÇÃO":
        if "piora" in tendencia:
            return ("A missão apresentou instabilidade relevante durante a operação. Apesar da\n"
                    "tentativa de recuperação no último ciclo, ainda existem sistemas em atenção\n"
                    "e a equipe deve manter o plano de contingência ativo.")
        else:
            return ("A missão apresentou instabilidade em alguns ciclos, mas demonstrou\n"
                    "tendência de recuperação. Recomenda-se manter monitoramento contínuo.")
    else:
        return ("A missão atingiu níveis críticos em múltiplos sistemas. "
                "Intervenção imediata é necessária e o protocolo de emergência "
                "deve ser ativado.")



riscos_por_ciclo = []
total_ciclos = len(dados_missao)

for i in range(total_ciclos):
    temp  = dados_missao[i][0]
    comun = dados_missao[i][1]
    bat   = dados_missao[i][2]
    oxig  = dados_missao[i][3]
    estab = dados_missao[i][4]

    st_temp,  desc_temp,  pts_temp  = analisar_temp(temp)
    st_comun, desc_comun, pts_comun = analisar_comunicacao(comun)
    st_bat,   desc_bat,   pts_bat   = analisar_bateria(bat)
    st_oxig,  desc_oxig,  pts_oxig  = analisar_oxigenio(oxig)
    st_estab, desc_estab, pts_estab = analisar_estabilidade(estab)

    risco = pts_temp + pts_comun + pts_bat + pts_oxig + pts_estab
    riscos_por_ciclo.append(risco)


    if i < total_ciclos - 1:
        pt_temp  += pts_temp
        pt_comun += pts_comun
        pt_bat   += pts_bat
        pt_oxig  += pts_oxig
        pt_estab += pts_estab

    print("-" * 60)
    print(f"CICLO {i + 1}")
    print("-" * 60)
    print(f"Temperatura: {temp} °C | {st_temp} | {desc_temp}")
    print(f"Comunicação: {comun}% | {st_comun} | {desc_comun}")
    print(f"Bateria: {bat}% | {st_bat} | {desc_bat}")
    print(f"Oxigênio: {oxig}% | {st_oxig} | {desc_oxig}")
    print(f"Estabilidade: {estab}% | {st_estab} | {desc_estab}")
    print(f"Pontuação de risco do ciclo: {risco}")
    print(f"Classificação do ciclo: {classificar_ciclo(risco)}")
    print(f"Recomendação: {recomendacao_ciclo(risco, st_temp, st_comun, st_bat, st_oxig, st_estab)}")
    print("\n")


# RELATÓRIO FINAL

ciclo_critico_idx = riscos_por_ciclo.index(max(riscos_por_ciclo))
maior_risco       = max(riscos_por_ciclo)
risco_medio       = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
ciclos_criticos   = sum(1 for r in riscos_por_ciclo if r >= 6)
tendencia         = calcular_tendencia(riscos_por_ciclo)
classificacao_fim = classificar_final(risco_medio)
area_afetada      = area_mais_afetada(pt_temp, pt_comun, pt_bat, pt_oxig, pt_estab)
conclusao         = conclusao_final(classificacao_fim, tendencia)

print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)
print("Missão: Orion Test Alpha")
print("Equipe: Equipe Apollo \n")
print(f"QUANTIDADE DE CICLOS ANALISADOS: {total_ciclos}\n")
print(f"Média de temperatura: {calcular_media(0):.2f} °C")
print(f"Média de comunicação: {calcular_media(1):.2f}%")
print(f"Média de bateria: {calcular_media(2):.2f}%")
print(f"Média de oxigênio: {calcular_media(3):.2f}%")
print(f"Média de estabilidade: {calcular_media(4):.2f}%\n")
print(f"Ciclo mais crítico: Ciclo {ciclo_critico_idx + 1}")
print(f"Maior pontuação de risco: {maior_risco}\n")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
print(f"Tendência da missão:\n{tendencia}\n")
print("PONTUAÇÃO ACUMULADA POR ÁREA:")
print(f"  Temperatura interna: {pt_temp} pontos")
print(f"  Comunicação com a base: {pt_comun} pontos")
print(f"  Sistema de energia: {pt_bat} pontos")
print(f"  Suporte de oxigênio: {pt_oxig} pontos")
print(f"  Estabilidade operacional: {pt_estab} pontos\n")
print(f"Área mais afetada:\n  {area_afetada} \n")
print(f"Classificação final da missão:\n  {classificacao_fim}\n")
print(f"CONCLUSÃO:\n{conclusao}")