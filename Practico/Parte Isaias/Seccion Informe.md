# Sección Informe

## 1. Texto para el informe

### Visualización nueva: Escala de entrenamiento de modelos LLM notables

**Autor:** Isaías Carte Figueroa  
**Tipo de visualización:** Ridgeline plot / Joyplot  
**Herramienta utilizada:** Python  
**Fuente de datos:** Epoch AI — Notable AI Models. https://epoch.ai/data/ai-models?view=table&tab=notable  
**Archivo base:** `Epoch Database - Notable Models.csv`  
**Archivo procesado:** `llm_training_compute_ridgeline_dataset.csv`  
**Imagen generada:** `ridgeline_training_compute.png`

#### Contexto y objetivo

Esta visualización fue desarrollada como una nueva pieza para el trabajo práctico final, manteniendo el tema central del proyecto: el análisis del ecosistema de los Large Language Models (LLMs). A diferencia del streamgraph, que muestra la evolución temporal de modelos por organización, y de los mapas, que presentan la concentración geográfica e infraestructural del fenómeno, esta visualización se enfoca en la escala computacional necesaria para entrenar los modelos.

El objetivo principal es responder la siguiente pregunta:

> ¿Cómo ha cambiado la escala de entrenamiento de los modelos LLM notables entre 2018 y 2025?

Para ello, se utilizó la variable `Training compute (FLOP)` del dataset de Epoch AI, filtrando modelos cuyo dominio contiene `Language`, publicados entre 2018 y 2025 y con dato disponible de cómputo de entrenamiento. Debido a que los valores de FLOP son extremadamente grandes, se aplicó una transformación logarítmica mediante `log10(FLOP)`, lo que permite comparar la magnitud del cómputo de forma más legible.

#### Descripción de la visualización

El gráfico corresponde a un ridgeline plot o joyplot. Cada curva representa un año entre 2018 y 2025, y muestra la distribución del cómputo de entrenamiento de los modelos LLM notables publicados en ese período. La posición horizontal representa el `log10(FLOP de entrenamiento)`, mientras que la posición vertical organiza las distribuciones por año.

Además, cada fila incluye una etiqueta `n=`, que indica la cantidad de modelos considerados para ese año, y una marca vertical corta que representa la mediana anual del cómputo de entrenamiento. Esta marca permite observar de forma más clara el desplazamiento general de la escala computacional a través del tiempo.

#### Ficha técnica

**Visualización:** Ridgeline Plot — Escala de entrenamiento de modelos LLM notables  

**Autor:** Isaías Carte Figueroa

**Tipo de gráfico:** Ridgeline plot / Joyplot

**Herramienta:** Python

**Fuente de datos:** Epoch AI — Notable AI Models. https://epoch.ai/data/ai-models?view=table&tab=notable

---

##### Marca

La marca principal es el **área de densidad**. Cada curva representa un año entre 2018 y 2025, mostrando la distribución del cómputo de entrenamiento de los modelos LLM notables publicados en ese período.

Como marca secundaria, se utiliza una **línea vertical corta** sobre cada distribución para señalar la mediana anual del cómputo de entrenamiento. Además, cada año incluye una etiqueta con la cantidad de modelos considerados en la distribución correspondiente.

##### Canales

- **Posición horizontal (cuantitativa):** el eje X codifica el cómputo de entrenamiento expresado como `log10(FLOP)`. Esta transformación permite representar valores de gran magnitud en una escala legible.
- **Posición vertical (ordinal):** cada fila corresponde a un año de publicación entre 2018 y 2025.
- **Forma / altura del área (cuantitativa):** la forma de cada curva muestra la concentración de modelos en determinados rangos de cómputo de entrenamiento.
- **Color – matiz (ordinal/categórico):** cada año recibe un color distinto para facilitar la separación visual entre distribuciones.
- **Etiqueta textual:** el valor `n=` indica la cantidad de modelos incluidos en cada año.

##### Definición del lenguaje visual

| Elemento | Definición | Justificación |
|---|---|---|
| **Color** | Paleta diferenciada por año. | Permite separar visualmente cada distribución anual y seguir la evolución temporal sin utilizar un gráfico de líneas tradicional. |
| **Texturas** | Sin texturas; áreas con relleno sólido y transparencia moderada. | La lectura depende de la forma de las distribuciones; las texturas podrían dificultar la comparación entre curvas. |
| **Tipografía** | Sans serif limpia, coherente con el resto del trabajo. | Facilita la lectura rápida del título, subtítulo, ejes, etiquetas de año y fuente. |
| **Líneas** | Líneas base horizontales por año y marcas verticales de referencia. | Las líneas base ordenan las distribuciones y las marcas verticales ayudan a comparar la mediana anual del cómputo de entrenamiento. |

#### Lectura / conclusión

La visualización evidencia que la evolución de los LLMs no solo se expresa en una mayor cantidad de modelos publicados, sino también en una creciente escala computacional asociada a su entrenamiento. En los años más recientes, especialmente desde 2022, las distribuciones se desplazan hacia valores más altos de `log10(FLOP)`, lo que sugiere que el desarrollo de modelos de lenguaje depende cada vez más de infraestructura especializada, capacidad energética y acceso a recursos avanzados de cómputo.

Este resultado complementa las visualizaciones anteriores del proyecto, ya que funciona como un puente entre la evolución temporal de los modelos y el análisis de infraestructura física. Primero se observa que aumentan los modelos; luego, que aumenta la escala computacional necesaria para entrenarlos; finalmente, los mapas de infraestructura permiten entender dónde se ubican los centros de datos y superclusters capaces de sostener esa demanda.

#### Responsabilidad individual

Isaías Carte Figueroa fue responsable de la construcción de la visualización ridgeline plot sobre la escala de entrenamiento de modelos LLM notables. Su trabajo incluyó la preparación del dataset de Epoch AI, el filtrado de modelos de lenguaje publicados entre 2018 y 2025, la transformación logarítmica del cómputo de entrenamiento, la generación del gráfico en Python y la redacción de la ficha técnica, lectura y conclusión asociada.

---

## 2. Texto para la infografía

### Título corto recomendado

**La escala que exige entrenar LLMs**

### Bajada o subtítulo

No solo aumentan los modelos: también crece el cómputo necesario para entrenarlos.

### Texto breve para acompañar el gráfico

Cada curva representa un año entre 2018 y 2025. El eje horizontal muestra el cómputo de entrenamiento en escala logarítmica (`log10(FLOP)`). A medida que pasan los años, las distribuciones se desplazan hacia la derecha, indicando que los modelos recientes tienden a requerir mayor escala computacional.

### Microconclusión para la infografía

Desde 2022, los LLMs se concentran en rangos más altos de cómputo. Esto ayuda a explicar por qué su desarrollo depende cada vez más de centros de datos, superclusters y grandes operadores tecnológicos.

### Fuente para colocar bajo el gráfico

Fuente: Epoch AI — Notable Models. Elaboración propia. Filtro: modelos de lenguaje publicados entre 2018 y 2025 con dato disponible de Training compute (FLOP).

### Ubicación sugerida dentro de la narrativa visual

Esta visualización debería ubicarse después del gráfico de evolución temporal y antes del mapa de infraestructura. De esta forma, la infografía mantiene una secuencia lógica:

1. **Crecen los modelos:** el streamgraph muestra la evolución temporal de la producción de LLMs.
2. **Crece la escala técnica:** el ridgeline muestra el aumento del cómputo de entrenamiento.
3. **Se necesita infraestructura:** el mapa de puntos muestra dónde se ubican los centros de datos que sostienen ese entrenamiento.

### Frase puente para conectar con el mapa de infraestructura

Si entrenar modelos exige cada vez más cómputo, entonces la infraestructura física deja de ser un elemento secundario y pasa a ser parte central del ecosistema LLM.

### Recomendación visual para integrarlo

- Mantener el gráfico en formato horizontal.
- Usar una caja de texto breve al costado derecho o debajo del gráfico.
- No saturar con explicación técnica: basta con aclarar que `log10(FLOP)` representa la escala del cómputo de entrenamiento.
- Conservar la fuente bajo el gráfico.
- Usar la misma familia tipográfica y estilo de títulos que el resto de la infografía.
- Si el gráfico se reduce mucho, priorizar que se lean el título, el eje horizontal y la tendencia general de las curvas.
