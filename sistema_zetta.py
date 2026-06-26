import customtkinter as ctk
import datetime
import csv
import os

# --- LÓGICA DO SISTEMA ---
class OrdemServico:
    def __init__(self, cliente, equipamento, defeito_relatado):
        self.id_os = datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.cliente = cliente
        self.equipamento = equipamento
        self.defeito_relatado = defeito_relatado
        self.status = "Em Análise"
        self.total_servico = 0.0
        self.total_pecas = 0.0

    def calcular_total(self):
        return self.total_servico + self.total_pecas

def registrar_os():
    cliente = entry_cliente.get()
    equipamento = entry_equipamento.get()
    defeito = entry_defeito.get()
    
    try:
        # Troca vírgula por ponto para evitar erro se alguém digitar "150,00"
        servico = float(entry_servico.get().replace(',', '.')) if entry_servico.get() else 0.0
        pecas = float(entry_pecas.get().replace(',', '.')) if entry_pecas.get() else 0.0
    except ValueError:
        label_resultado.configure(text="⚠️ Erro: Digite apenas números nos valores!", text_color="#ff5555")
        return

    if not cliente or not equipamento:
        label_resultado.configure(text="⚠️ Preencha Cliente e Aparelho!", text_color="#ff5555")
        return

    # Gera a O.S.
    nova_os = OrdemServico(cliente, equipamento, defeito)
    nova_os.total_servico = servico
    nova_os.total_pecas = pecas

    # Salva na Planilha
    nome_arquivo = 'banco_de_os.csv'
    arquivo_existe = os.path.isfile(nome_arquivo)

    with open(nome_arquivo, mode='a', newline='', encoding='utf-8') as planilha:
        escritor = csv.writer(planilha, delimiter=';')
        if not arquivo_existe:
            escritor.writerow(['ID da OS', 'Cliente', 'Equipamento', 'Defeito Relatado', 'Status', 'Mão de Obra (R$)', 'Peças (R$)', 'Total Geral (R$)'])
        
        escritor.writerow([
            nova_os.id_os, cliente, equipamento, defeito, nova_os.status,
            f"{servico:.2f}", f"{pecas:.2f}", f"{nova_os.calcular_total():.2f}"
        ])
    
    label_resultado.configure(text=f"✅ O.S. {nova_os.id_os} salva com sucesso no caixa!", text_color="#55ff55")
    
    # Limpa os campos para o próximo cliente
    entry_cliente.delete(0, 'end')
    entry_equipamento.delete(0, 'end')
    entry_defeito.delete(0, 'end')
    entry_servico.delete(0, 'end')
    entry_pecas.delete(0, 'end')

# --- INTERFACE GRÁFICA ---
ctk.set_appearance_mode("dark") # Tema escuro
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Zetta IA e TI - Recepção")
app.geometry("450x550")

# Título da Janela
ctk.CTkLabel(app, text="Nova Ordem de Serviço", font=("Arial", 22, "bold")).pack(pady=20)

# Campos de digitação
entry_cliente = ctk.CTkEntry(app, placeholder_text="Nome do Cliente", width=350, height=40)
entry_cliente.pack(pady=10)

entry_equipamento = ctk.CTkEntry(app, placeholder_text="Aparelho (Ex: TV Xion 50', iPhone 15)", width=350, height=40)
entry_equipamento.pack(pady=10)

entry_defeito = ctk.CTkEntry(app, placeholder_text="Defeito Relatado", width=350, height=40)
entry_defeito.pack(pady=10)

entry_servico = ctk.CTkEntry(app, placeholder_text="Valor Mão de Obra (Ex: 150.00)", width=350, height=40)
entry_servico.pack(pady=10)

entry_pecas = ctk.CTkEntry(app, placeholder_text="Valor das Peças (Ex: 80.00)", width=350, height=40)
entry_pecas.pack(pady=10)

# Botão de Salvar
btn_salvar = ctk.CTkButton(app, text="Registrar Sistema", command=registrar_os, fg_color="#28a745", hover_color="#218838", height=45, font=("Arial", 16, "bold"))
btn_salvar.pack(pady=25)

# Mensagem de sucesso/erro
label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 14))
label_resultado.pack(pady=5)

app.mainloop()