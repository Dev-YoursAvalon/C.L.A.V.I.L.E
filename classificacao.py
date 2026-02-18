def classificar_contrato(tipo):
    if tipo == "1":
        with open("modelo/modelo_adm.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    elif tipo == "2":
        with open("modelo/modelo_trib.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    else:
        raise ValueError("Tipo de contrato inválido.")  