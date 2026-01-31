PROJETO - GERADOR DE CONTRATOS JUDICIAIS // NIVEL INICIANTE

GERADOR DE CONTRATOS JURIDICOS AUTOMATIZADO:
// Este projeto é um sistema inteligente desenvolvido em Python para automatizar a redação de contratos jurídicos. Ele utiliza uma estrutura de Árvore de Decisão para coletar dados específicos dependendo do ramo do Direito selecionado, gerando documentos personalizados e precisos de acordo com o desejo do usuario.

OBJETIVO:

//O objetivo principal é reduzir o erro humano e o tempo gasto na elaboração de contratos repetitivos, garantindo que cláusulas específicas (como CNPJ para empresas ou número de processo para contencioso) sejam incluídas apenas quando necessário.

FUNCIONALIDADE:

//Módulos Especializados: Perguntas dinâmicas para contratos Administrativos ou Tributarios

//Validação de Dados: Sistema de verificação para CPFs, CNPJs e opções de menu.

//Formatação Automática: Máscaras de texto para documentos (ex: 000.000.000-00).

//Geração de Documento: Exportação do texto final baseado em modelos .txt profissionais.

//Lógica de Honorários: Cálculo e descrição de pagamentos (Fixo, Êxito ou Híbrido).

COMO FUNCIONA:

// O sistema opera através de um terminal interativo seguindo estes passos:

// Coleta de Dados Básicos: Nome, CPF e Endereço das partes.

// Seleção de Especialidade: O usuário escolhe entre 2 tipos de contratos.

 //Bifurcação de Perguntas:

    ////Exemplo: No contrato Tributário, se escolher "Pessoa Jurídica", o sistema solicita o CNPJ e aplica a formatação. Se escolher "Contencioso", solicita o número do processo.

// Substituição de Tags: O motor do sistema localiza chaves como {{contratante}} no modelo e as substitui pelos dados coletados.

// Resultado: O contrato é exibido pronto para cópia ou salvo em arquivo.
 
TECNOLOGIAS UTILIZADAS:

//Linguagem: Python 3.11.9
// VSCode
// Gemini: Dicas, auxilio para duvidas, sugestões, detecção de erros no script.

// Lógica de Programação: Dicionários, Estruturas de Repetição (while), Condicionais Compostas (if/elif/else) e Modularização de funções.

Estrutura do Projeto

├── main.py              # Script principal e fluxo de perguntas
├── classificacao.py     # Lógica de seleção de modelos
├── gerador.py           # Mecanismo de substituição de tags
├── modelo/              # Pasta com arquivos .txt (templates)
│   ├── modelo_adm.txt
│   ├── modelo_trib.txt
|   
└── README.md            # Documentação do projeto
AUTOR:

////yours.avalon

// Desenvolvedor Iniciante focado em Python e Automação.

(ESTE PROJETO FOI FEITO COM O INTUITO EDUCACIONAL !!!)
