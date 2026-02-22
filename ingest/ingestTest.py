import pandas as pd

# 1. EXTRAÇÃO (Extract) - Lendo um ficheiro CSV hipotético
# df = pd.read_csv('vendas_brutas.csv')
data = {
    'cliente': ['  joão SILVA  ', 'maria brito', ' ANA costa '],
    'data_venda': ['2025-01-15', '15/01/2025', '2025.01.16'],
    'valor_bruto': [100.0, 250.5, 80.0]
}
df = pd.DataFrame(data)

# 2. TRANSFORMAÇÃO (Transform) - Limpeza e padronização
# a) Normalizar nomes: remover espaços e colocar em Maiúsculas
df['cliente'] = df['cliente'].str.strip().str.title()

# b) Padronizar datas: converter formatos variados para o padrão YYYY-MM-DD
df['data_venda'] = pd.to_datetime(df['data_venda'], dayfirst=False, errors='coerce')

# c) Criar nova métrica: calcular valor líquido (ex: retirar 10% de taxa)
df['valor_liquido'] = df['valor_bruto'] * 0.9

# 3. CARGA (Load) - Salvar o resultado limpo para uso posterior
# df.to_csv('vendas_limpas.csv', index=False)

print("Dados Transformados:")
print(df)
