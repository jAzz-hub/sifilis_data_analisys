
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
