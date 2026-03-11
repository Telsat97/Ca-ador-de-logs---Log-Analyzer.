


# Dicionário para contar as falhas por IP
falhas_por_ip = {} # Reinicializa o dicionário para evitar contagem duplicada

# 1. Abrir o arquivo de log para leitura
with open('server_access.log', 'r') as arquivo: # Reabre o arquivo para uma nova leitura
    for linha in arquivo: 
        # 2. Verificar se a linha contém uma falha de login
        if "Login failed" in linha:
            # Extrair o IP (é a última parte da linha)
            ip = linha.split("IP: ")[1].strip()

            # 3. Contar a falha para esse IP
            falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1

# 4 Verificar se algum IP ultrapassou o limite de segurança ( ex: 3 tentativas)
print("--- RELATÓRIO DE SEGURANÇA ---")
for ip, contagem in falhas_por_ip.items():
    if contagem >= 3:
        print(f"[ALERTA CRÍTICO] O IP {ip} tentou invadir {contagem} vezes!")
    else:
        print(f"[INFO] IP {ip}: {contagem} FALHAS DETECTADAS. " )

        