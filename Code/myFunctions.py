
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
    'TRATPARC': 'TratamentoParceiro',
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

