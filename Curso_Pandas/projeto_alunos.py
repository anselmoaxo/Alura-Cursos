# -*- coding: utf-8 -*-
"""Projeto_Alunos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dqDgCXdlpaq0oyymnN2Ww4QZA_KdALnp
"""

import pandas as pd

url='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
df_alunos = pd.read_csv(url)
df_alunos.head()

df_alunos.head(7)

df_alunos.shape

df_alunos.info()

df_alunos.describe()

"""Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação."""

df_alunos.isnull().sum()
df_alunos = df_alunos.fillna(0)

df_alunos.isnull().sum()

"""2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados."""

filtro_nomes = df_alunos['Nome'].isin(['Alice', 'Carlos'])
remover_linhas = df_alunos[filtro_nomes].index
df_alunos.drop(remover_linhas, inplace=True)

df_alunos

"""3) Aplique um filtro que selecione apenas os alunos que foram aprovados."""

filtro = df_alunos['Aprovado'] == True
df_alunos = df_alunos[filtro]

"""Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv"."""

df_alunos.to_csv('alunos_aprovados.csv', index=False)

df_alunos

df_alunos = df_alunos.replace(7,8)

df_alunos

df_alunos.to_csv('alunos_aprovados.csv', index=False)

"""
1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.
"""

df_alunos = pd.read_csv(url)
df_alunos.head()

df_alunos['Pontos_extras'] = df_alunos['Notas'] * 0.4
df_alunos

"""2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras."""

df_alunos['Notas_finais'] = df_alunos['Notas'] + df_alunos['Pontos_extras']
df_alunos

"""3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
"""

df_alunos['Aprovados_final'] = df_alunos['Notas_finais'].apply(lambda x: True if x >= 6 else False)
df_alunos

"""4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras."""

selecao = (df_alunos['Notas'] < 6) & ( df_alunos['Notas_finais'] >= 6)
df_alunos[selecao]