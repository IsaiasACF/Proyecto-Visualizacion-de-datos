import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. Cargar datos
df = pd.read_csv('dataset.csv')
df['Modelo_ID'] = range(len(df))

colores = px.colors.qualitative.Bold 
escala_colores = [[i / (len(df)-1), colores[i % len(colores)]] for i in range(len(df))]

# 3. Construir el gráfico
fig = go.Figure(data=
    go.Parcoords(
        line = dict(
            color = df['Modelo_ID'], 
            colorscale = escala_colores, 
            showscale = False 
        ),
        dimensions = list([
            dict(range = [0, len(df)-1],
                 tickvals = df['Modelo_ID'],
                 ticktext = df['Modelo'],
                 label = 'Modelo de IA (Leyenda)', 
                 values = df['Modelo_ID']),
            
            dict(range = [0, 1],
                 label = 'HumanEval (Código)', 
                 values = df['HumanEval']),
            
            dict(range = [0, 1],
                 label = 'MATH', 
                 values = df['MATH']),
            
            dict(range = [0, 1],
                 label = 'MMLU', 
                 values = df['MMLU']),
                 
            dict(range = [0, 0.9],
                 label = 'GPQA', 
                 values = df['GPQA']),
            
            dict(range = [0, df['Costo_Input'].max() + 1],
                 label = 'Costo Input ($/1M tokens)', 
                 values = df['Costo_Input']),
            
            dict(range = [0, df['Costo_Output'].max() + 5],
                 label = 'Costo Output ($/1M tokens)', 
                 values = df['Costo_Output'])
        ])
    )
)

fig.update_layout(
    annotations=[
        dict(
            x=0, y=-0.15, xref='paper', yref='paper', showarrow=False,
            text='Fuente: Datos recopilados de Artificial Analysis y Hugging Face (2026).',
            font=dict(size=10, color='gray')
        )
    ],
    title=dict(
        text="Análisis: Rendimiento vs Costo de LLMs",
        font=dict(size=20)
    ),
    font=dict(size=12),
    margin=dict(l=160, r=120, t=120, b=80)
)

fig.write_image("coordenadas_paralelas.png", width=1300, height=600, scale=2)