
import matplotlib.pyplot as plt

def rename_df_columns(df):
    df.rename(columns={
    'DT_NOTIFIC': 'Data_Notificacao',
    'NU_ANO': 'Ano',
    'ID_UNIDADE': 'Unidade',
    'CS_GESTANT': 'TriGestacional',
    'CS_RACA': 'Raca',
    'CS_ESCOL_N': 'Escolaridade',
    'CS_ZONA': 'Residencia',
    'TPTESTE1': 'TipoTeste',
    'TPESQUEMA': 'Tratamento',
    'TRATPARC': 'TratamentoParceiro'
    }, inplace=True)


def Nan_or_empty_rows(df):
    return df.columns[df.isna().any()].tolist()


def Count_null_values(df):
    return df.isnull().sum().to_dict()

def tratando_Nan(df):
    df['TPMOTPARC'].fillna('Não Informado', inplace=True)


def multiple_series_line_Chart(titulo, DataFrame):
    # Prepare the data for plotting
    years = [2019, 2020, 2021, 2022, 2023]
    categories = DataFrame[f'{titulo}'].dropna().unique()

    # Initialize the plot
    plt.figure(figsize=(12, 6))

    # Plot each category as a separate line
    for category in categories:
        proportions = []
        for year in years:
            proportion = DataFrame[(DataFrame['Ano'] == year) & (DataFrame[f'{titulo}'] == category)][f'{titulo}'].count() / DataFrame[DataFrame['Ano'] == year][f'{titulo}'].count() * 100
            proportions.append(proportion)
        plt.plot(years, proportions, marker='o', label=f'{titulo} {category}')

    # Customize the plot
    plt.title(f'Proporção de {titulo} das Gestantes por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Proporção (%)')
    plt.xticks(years)  # Set x-axis to change year by year
    plt.legend(title=f'{titulo}')
    plt.grid(True)
    plt.show()


def categorizar_raca(x):
    if x == 1:
        return 'Branca'
    elif x == 2:
        return 'Preta'
    elif x == 3:
        return 'Amarela'
    elif x == 4:
        return 'Parda'
    elif x == 5:
        return 'Indígena'
    elif x == 9:
        return 'Ignorado'
    else:
        return 'Outro'


# df['Categoria_Raca'] = df['CS_RACA'].apply(categorizar_raca)
# Funções para as perguntas binárias
def notificada_depois_segundo_mes(cs_gestant):
    """Pergunta 1: Notificação após o segundo mês?"""
    # Considerando que CS_GESTANT > 2 indica após o segundo trimestre (mês 4+)
    return 1 if cs_gestant > 2 else 0

def tratamento_penicilina_gestante(tpesquema):
    """Pergunta 2 e 4: Tratamento com penicilina na gestante?"""
    return 1 if tpesquema in [1, 2, 3] else 0

def tratamento_penicilina_parceiro(tratparc):
    """Pergunta 3: Tratamento com penicilina no parceiro?"""
    return 1 if tratparc in [1, 2, 3] else 0

def cor_negra_parda(cs_raca):
    """Pergunta 5: Cor da pele é negra ou parda?"""
    return 1 if cs_raca in [2, 4] else 0

# Exemplo de aplicação em um DataFrame
def aplicar_transformacoes(df):
    df['NOTIFICADA_DEPOIS_SEGUNDO_MES'] = df['CS_GESTANT'].apply(notificada_depois_segundo_mes)
    df['TRATAMENTO_PENICILINA_GESTANTE'] = df['TPESQUEMA'].apply(tratamento_penicilina_gestante)
    df['TRATAMENTO_PENICILINA_PARCEIRO'] = df['TRATPARC'].apply(tratamento_penicilina_parceiro)
    df['COR_NEGRA_PARDA'] = df['CS_RACA'].apply(cor_negra_parda)
    return df

# Exemplo de uso:
# df_transformado = aplicar_transformacoes(df_original)