def gerar_contrato(texto_modelo, dados):
    """
    Recebe:
    - texto_modelo (string): conteúdo do arquivo .txt do contrato
    - dados (dict): dados do usuário para substituir no contrato

    Retorna:
    - contrato final (string)
    """

    for chave, valor in dados.items():
        texto_modelo = texto_modelo.replace(f"{{{{{chave}}}}}", valor)

    return texto_modelo
