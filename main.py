from classificacao import classificar_contrato
from gerador import gerar_contrato
# Formatação
def formatacao_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
def formatacao_cnpj(cnpj):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
# Definições
def obter_tipo():
    return {
        "1": "Contrato Administrativo",
        "2": "Contrato Tributário",
    }
def perguntas_administrativo():
    print("\n--- DADOS ESPECIFICOS DO CONTRATO ADMINISTRATIVO ---")
    
    # Pergunta Chave
    resp = input("O contratante é (1) Orgão Público ou (2) Empresa Privada?: ")
    
    # Validação de escolha
    while resp not in ["1", "2"]:
        resp = input("Opção INVÁLIDA. Tente novamente: ")
    
    # Definição de Tipo
    tipo = "Orgão Público" if resp == "1" else "Empresa Privada"
    print("Seu contratante é:",tipo)
    
    # Modalidade
    if resp == "1":
        modalidade = input("Modalidade: (1) Pregão (2) Dispensa): ").upper()
        while modalidade not in ["1", "2"]:
            modalidade = input("Opção INVÁLIDA. Tente novamente: ")
    else:
        modalidade = ("Contratação Direta")
    
    #Objeto
    objeto = input("Descrição resumida do serviço (Objeto): ").strip().upper()

    esfera = input("Esfera (Ex: Federal, Estadual, Municipal): ").upper() if resp == "1" else "N/A"
    licitacao = input("Nº da Licitação/Edital: ").upper() if resp == "1" else "N/A"
    
    #Perguntas Empresa
    if resp == "2":
        # Empresa Privada: perguntamos o CNPJ, fiscal e prazo
        cnpj = input("Digite o CNPJ da Empresa (apenas números): ")
        while len(cnpj) != 14 or not cnpj.isdigit():
            print("CNPJ inválido.")
            cnpj = input("Digite o CNPJ da Empresa (apenas números): ")
        # Formatação do CNPJ
        valor_id = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
        label_id = "CNPJ"
        fiscais = input("Nome do fiscal ou gestor do contrato: ").upper()
        prazo = input("Prazo de pagamento (em dias): ")
        prazo_pagamento = f"{prazo} DIAS"
    else:
        # Órgão Público: usamos CPF do contratante e valores padrão
        label_id = "CPF"
        valor_id = formatacao_cpf(cpf_contratante) # Usa o CPF global
        fiscais = "Conselho de Gestão" # Valor padrão para órgão público
        prazo_pagamento = "Conforme cronograma orçamentário"
    lei = "14.133/21" if resp == "1" else "13.303/16"
    
    return {
        "org_pessoa": tipo,
        # Orgão Público
        "esfera": esfera,
        "licitacao": licitacao,
        "modalidade": modalidade,
        "objeto": objeto,
        # Empresa Privada
        "label_identificador": label_id,
        "documento_identificador": valor_id,
        "fiscal_contrato": fiscais,
        "praz_pag": prazo_pagamento,
        "lei_base": lei,
    }
def perguntas_tributario():
    print("\n--- DADOS ESPECIFICOS DO CONTRATO TRIBUTÁRIO ---")
    
    # 1. Definição do Perfil do Cliente
    perfil = input("O contratante é (1) Pessoa Física ou (2) Pessoa Jurídica?: ")
    while perfil not in ["1", "2"]:
        perfil = input("Opção INVÁLIDA. Tente novamente: ")
    
    if perfil == "2":
        cnpj_bruto = input("Digite o CNPJ (apenas números): ")
        # Validação simples de tamanho para o CNPJ
        while len(cnpj_bruto) != 14 or not cnpj_bruto.isdigit():
            cnpj_bruto = input("CNPJ INVÁLIDO. Digite os 14 números: ")
        
        # Formatação do CNPJ
        documento_cliente = formatacao_cnpj(cnpj_bruto)
        label_documento = "CNPJ"
    else:
        documento_cliente = formatacao_cpf(cpf_contratante) 
        label_documento = "CPF"

    # 2. Tipo de Serviço
    serv = input("Qual o tipo de serviço? (1) Consultoria/Planejamento | (2) Contencioso/Defesa: ")
    while serv not in ["1", "2"]:
        serv = input("Opção INVÁLIDA. Tente novamente: ")

    tipo_servico = "CONSULTORIA/PLANEJAMENTO" if serv == "1" else "CONTENCIOSO/DEFESA"

    # 3. Detalhamento Técnico
    if serv == "1":
        opc_tributo = input("Especifique o tributo: (1) IRPJ | (2) ICMS | (3) ISS: ")
        mapa_tributos = {"1": "IRPJ", "2": "ICMS", "3": "ISS"}
        tributo_final = mapa_tributos.get(opc_tributo, "Outros")
        
        identificador = input("Finalidade do contrato (Ex: Recuperação de Créditos): ").upper()
        v_causa = "N/A"
    else:
        opc_orgao = input("Qual o Órgão atuador? (1) Receita Federal | (2) TJ | (3) CARF: ")
        mapa_orgaos = {"1": "RECEITA FEDERAL", "2": "TRIBUNAL DE JUSTIÇA", "3": "CARF"}
        tributo_final = mapa_orgaos.get(opc_orgao, "Outros")
        
        identificador = input("Qual o número do processo?: ").upper()
        v_causa = input("Valor da causa (em R$): ").upper()

    # 4. Honorários
    print("\n--- DEFINIÇÃO DE HONORÁRIOS ---")
    h_tipo = input("Tipo de honorários? (1) Fixo | (2) Êxito | (3) Híbrido: ")
    while h_tipo not in ["1", "2", "3"]:
        h_tipo = input("Opção INVÁLIDA: ")

    if h_tipo == "1":
        v_fixo = input("Qual o valor fixo (R$): ")
        honorarios_texto = f"R$ {v_fixo} (Valor Fixo)"
    elif h_tipo == "2":
        porcent = input("Qual a porcentagem de êxito (%): ")
        honorarios_texto = f"{porcent}% sobre o proveito econômico"
    else:
        v_fixo = input("Valor fixo de entrada (R$): ")
        porcent = input("Porcentagem de êxito final (%): ")
        honorarios_texto = f"R$ {v_fixo} (entrada) + {porcent}% (êxito)"

    return {
        "label_doc": label_documento,
        "doc_contratante": documento_cliente,
        "tipo_servico": tipo_servico,
        "tributo_orgao": tributo_final,
        "info_adicional": identificador,
        "valor_causa": v_causa,
        "honorarios": honorarios_texto
    }
    print("\n--- DADOS ESPECIFICOS DO CONTRATO DE DIREITO DE FAMÍLIA E SUCESSÕES ---")
    # Perguntas Chave
    return {}

# Script Principal
print("PROJETO: GERADOR DE CONTRATOS JURÍDICOS")
print("CRIADO POR: YANN KLEBER SANTANA DE OLIVEIRA")

# NOME
contratante = input("Nome do contratante: ").upper()

# NACIONALIDAE
nac_contratante = input("Nacionalidade do contratante: (1) Nato | (2) Naturalizado: ").upper()
while nac_contratante not in ["1", "2"]:
    nac_contratante = input("Opção INVÁLIDA. Tente novamente: ")

# CPF
cpf_contratante = input("CPF do contratante: ")
while len(cpf_contratante) != 11 or not cpf_contratante.isdigit():
    print("CPF inválido.")
    cpf_contratante = input("CPF do contratante: ")

# ESTADO CIVIL
est_civil_contratante = input("Estado Civil do contratante : (1) Solteiro | (2) Casado | (3) Divorciado | (4) Viúvo:").upper()
while est_civil_contratante not in ["1", "2", "3", "4"]:
    est_civil_contratante = input("Opção INVÁLIDA. Tente novamente: ")



#Endereço
endereco_contratante = input("Endereço do contratante: ").upper()


#Contratado
contratado = input("Nome do contratado: ").upper()
while True:
    oab_input = input("Numero OAB do contratado (Ex: SP123456): ").upper().strip()
    
    # Validação da OAB
    if len(oab_input) != 8:
        print("Erro: A OAB deve ter exatamente 8 caracteres.")
        continue
        
    # Validação da UF
    uf = oab_input[:2]
    if not uf.isalpha():
        print("Erro: Os 2 primeiros caracteres devem ser a UF (Ex: SP).")
        continue
        
    # Validação dos Números (seis últimos caracteres)
    numeros = oab_input[2:]
    if not numeros.isdigit():
        print("Erro: Os 6 últimos caracteres devem ser apenas números.")
        continue
    
    oab_final = oab_input
    break

# MENU TIPO DE CONTRATO
print("\nInsira o tipo de contrato de 1 ou 2:")
tipos_contrato = obter_tipo()
for chave, valor in tipos_contrato.items():
    print(f"{chave} - {valor}")

# Validação de escolha
contract_type = input("\nEscolha uma opção: ")
while contract_type not in tipos_contrato:
    contract_type = input("Opção INVÁLIDA. Tente novamente: ")

nome_selecionado = tipos_contrato[contract_type]
print(f"\nVocê selecionou: {nome_selecionado.upper()}")

# pega o modelo correto
modelo = classificar_contrato(contract_type)

# dados para substituição
dados = {
    "contratante": contratante,
    "contratado": contratado,
    "cpf_contratante": formatacao_cpf(cpf_contratante),
    "endereco_contratante": endereco_contratante,
    "OAB_contratado": oab_final,
    "est_civil_contratante": est_civil_contratante
}

if contract_type == "1":
    dados_adm = perguntas_administrativo()
    dados.update(dados_adm)
elif contract_type == "2":
    dados_trib = perguntas_tributario()
    dados.update(dados_trib)  

# Gerador de contrato
modelo = classificar_contrato(contract_type)
contrato_final = gerar_contrato(modelo, dados)

print("\n===== CONTRATO GERADO =====\n")
print(contrato_final)
