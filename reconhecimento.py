import pandas as pd

try:
    # Leia a planilha diretamente usando pandas
    df = pd.read_excel('Pasta1.xlsx', sheet_name='Planilha1', header=0)

    # Filtra os valores NaN na coluna 'img' e, em seguida, extrai os números e palavras usando a barra (/) como separador
    numeros_e_palavras = df['img'].dropna().astype(str).str.split('/')

    # Crie uma nova coluna 'numero' para os números e uma nova coluna 'palavra' para as palavras
    df['numero'] = numeros_e_palavras.apply(lambda x: int(x[0]))
    df['palavra'] = numeros_e_palavras.apply(lambda x: x[1])

    # Ordena o DataFrame com base nos números
    df_ordenado = df.sort_values(by='numero', ascending=False)

    # Imprime os números e palavras em ordem decrescente
    for index, row in df_ordenado.iterrows():
        print(f"{row['numero']}/{row['palavra']}")

except Exception as e:
    print(f"Erro: {e}")