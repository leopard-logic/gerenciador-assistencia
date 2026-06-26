# 📊 Gerente de Assistência - Zetta IA e TI

Um aplicativo desktop moderno desenvolvido em Python para automatizar a gestão de Ordens de Serviço (O.S.) e o controle financeiro de fluxo de caixa em assistências técnicas de eletrônicos e TI.

O projeto evoluiu de um protótipo em Jupyter Notebook para um software independente com interface gráfica em modo escuro, facilitando a operação por qualquer usuário leigo.

## 🚀 Funcionalidades Principais

* **Interface Gráfica Moderna:** Desenvolvida com a biblioteca `CustomTkinter`, contando com visual limpo, cantos arredondados e suporte nativo a modo escuro.
* **Visão Contábil e Financeira:** O painel separa rigorosamente o faturamento de **Mão de Obra** (receita técnica) dos custos com **Peças de Reposição** (insumos), permitindo uma análise clara da margem de lucro de cada serviço.
* **Persistência de Dados Automatizada:** Salva instantaneamente cada registro em um banco de dados local estruturado em formato `.csv` (totalmente compatível com o Microsoft Excel), usando delimitadores seguros para evitar quebras de linhas.
* **Independência de Sistema (Executável):** Compilado para rodar diretamente como um aplicativo Windows `.exe` estável, sem necessidade de o usuário final possuir o Python instalado na máquina.

## 💻 Tecnologias e Bibliotecas Utilizadas

* **Linguagem Base:** Python 3
* **Interface Visual:** `CustomTkinter`
* **Manipulação de Arquivos:** `csv` e `os`
* **Compilação Externa:** `PyInstaller`

## 🛠️ Como Executar ou Compilar

### Requisitos para Desenvolvimento
Se quiser rodar o código-fonte original, instale as dependências necessárias no seu ambiente Python:
```bash
pip install customtkinter pyinstaller
