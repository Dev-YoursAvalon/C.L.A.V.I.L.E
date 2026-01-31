def classificar_contrato(tipo):
    if tipo == "1":
        with open("modelo/modelo_adm.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    elif tipo == "2":
        with open("modelo/modelo_trib.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    elif tipo == "3":
        with open("modelo/modelo_honorario.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    elif tipo == "4":
        with open("modelo/modelo_civel.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    elif tipo == "5":
        with open("modelo/modelo_prest_serv.txt", "r", encoding="utf-8") as arquivo:
            return arquivo.read()