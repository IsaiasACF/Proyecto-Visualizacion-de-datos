# Sección Informe

## 1. Texto para el informe

### Visualización nueva: Anatomía de los fallos de agentes LLM

**Autor:** Benjamín Olguín Pozo  
**Tipo de visualización:** Voronoi Treemap ponderado (jerárquico, dos niveles)  
**Herramienta utilizada:** Python (`numpy`, `pandas`, `shapely`, `matplotlib`)  
**Fuente de datos:** Kaggle — LLM Agent Failure Analysis Benchmark. https://www.kaggle.com/datasets/sunil123kumar/ai-agent-failure-benchmark-dataset  
**Archivo base:** `benchmark_1500.csv`  
**Imagen generada:** `voronoi_fallos_agentes.png`

#### Contexto y objetivo

Esta visualización fue desarrollada como una nueva pieza para el trabajo práctico final, manteniendo el tema central del proyecto: el análisis del ecosistema de los Large Language Models (LLMs). A diferencia de las visualizaciones previas del grupo, centradas en la evolución temporal de los modelos, su rendimiento o su distribución geográfica, esta pieza desplaza la mirada hacia una pregunta cada vez más relevante a medida que los LLMs se integran como **agentes autónomos**: no *qué tan buenos son*, sino **cómo y cuán gravemente fallan**.

El objetivo principal es responder la siguiente pregunta:

> ¿Cuáles son los modos de fallo más frecuentes de los agentes LLM y cuán graves son? ¿Coincide lo que más falla con lo más peligroso?

Para ello se utilizó un benchmark de 1.500 casos de fallos de agentes, clasificados por tipo de fallo (`failure_type`), dominio de la tarea (`domain`) y severidad (`failure_severity`). La severidad se mapeó a una escala numérica (Low = 1, Medium = 2, High = 3, Critical = 4) para poder promediarla y codificarla por color.

> **Nota de transparencia (relevante para periodismo de datos):** el conjunto es un **benchmark sintético** —los casos fueron generados artificialmente y los 300 casos exactos por dominio confirman su naturaleza construida—, por lo que los **conteos** no constituyen una medición empírica del mundo real. Sin embargo, la **taxonomía de tipos de fallo** que emplea (Reasoning, Tool Use, Grounding, Hallucination, Safety & Alignment, etc.) sí está anclada en la literatura académica reciente sobre fallos de flujos agénticos (arXiv:2509.23735; conjuntos AgentFail y Who&When). Por ello, la visualización es válida como **panorama conceptual ilustrativo** de los modos de fallo de los agentes LLM, no como estadística poblacional.

#### Descripción de la visualización

El gráfico corresponde a un **Voronoi treemap ponderado** de dos niveles, dispuesto dentro de un disco. En el nivel externo, cada celda de bordes orgánicos representa un **tipo de fallo**, y su **área es estrictamente proporcional a la frecuencia** de ese fallo (la convergencia del algoritmo alcanza un error máximo de área del 0,62 %). Cada celda se subdivide, en un segundo nivel, según el **dominio** de la tarea (Coding, Mathematics, RAG/QA, Planning, Customer Support), con área proporcional a la frecuencia local.

El **color** de cada subcelda codifica la **severidad media** mediante una escala secuencial cálida (`YlOrRd`): del amarillo claro (Low) al rojo profundo (Critical). Cada tipo de fallo se identifica con un **badge numérico (1–12, ordenado por frecuencia)** ligado a una leyenda lateral que indica nombre, número de casos y severidad media; el dominio se rotula con su abreviatura y una fuente proporcional al tamaño de la subcelda.

#### Ficha técnica

**Marca geométrica**

- **Marca principal:** el **área** — el polígono (celda de Voronoi) de bordes irregulares.
- **Marca secundaria:** **texto y número** — badge numérico de cada tipo y abreviatura del dominio.

**Canales visuales**

| Canal | Variable codificada | Detalle |
|---|---|---|
| **Tamaño (área)** | Frecuencia | Nivel externo: área ∝ nº de casos del tipo de fallo. Nivel interno: área ∝ nº de casos del par tipo×dominio. |
| **Color / saturación** | Severidad | Escala secuencial `YlOrRd` normalizada de 1 (Low) a 4 (Critical), sobre la severidad media de la celda interna. |
| **Anidamiento (contención)** | Jerarquía | La pertenencia de una celda de dominio a un tipo de fallo se codifica por contención espacial, reforzada por un borde negro grueso. |
| **Texto / número** | Identidad | Badge numérico (1–12, por frecuencia) con leyenda lateral; abreviatura del dominio (Cod, Mat, RAG, Plan, CS). |
| **Posición (x, y)** | — *(sin codificación de datos)* | En un Voronoi treemap la posición resulta del empaquetado del algoritmo y **no** representa ninguna variable. Se declara explícitamente para no inducir lecturas espurias. |

**Definición del lenguaje visual**

La información se codifica en una teselación completa de un disco. Cada tipo de fallo ocupa una celda cuya superficie es proporcional a su frecuencia; dentro de ella, una segunda teselación pondera los dominios. El color mapea la severidad media: cuanto más rojo y oscuro, más grave. El lector decodifica, por tanto, *cuánto* falla cada categoría por el tamaño y *cuán grave* es por el tono, en una sola lectura. La tensión entre ambos canales —celdas grandes y pálidas frente a celdas pequeñas y oscuras— es el núcleo narrativo de la pieza.

**Nota de implementación.** Dado que no existe una librería mantenida en Python para el Voronoi treemap ponderado (el ecosistema maduro reside en JavaScript, `d3-voronoi-treemap`), el algoritmo se implementó manualmente en `voronoi_fallos_agentes.py`: (1) **diagrama de potencia** mediante intersección de semiplanos recortados contra el polígono contenedor (`shapely`); (2) **relajación de Lloyd** desplazando cada sitio al centroide de su celda; y (3) **ajuste iterativo de pesos** por la razón `√(área_objetivo / área_actual)`, hasta converger a las frecuencias objetivo.

#### Lectura / conclusión

La visualización revela una **disociación entre frecuencia y gravedad** que un ranking simple ocultaría:

- **Lo que más falla es de gravedad media, no crítica:** *Reasoning* (215 casos), *Tool Use* (195) y *Context* (179) son las celdas más grandes pero de tono pálido (severidad media ≈ 2,2–2,3). Son los errores cotidianos del agente: molestos pero rara vez catastróficos.
- **Lo más peligroso es raro pero intensamente oscuro:** *Safety & Alignment* (44 casos) es una celda pequeña del rojo más profundo (severidad 4,0; 100 % de casos graves), seguida de *Grounding* (84; 100 % graves) y *Planning* (110; 82 % graves).
- **Existen fallos casi benignos:** *Knowledge* (74 casos, 0 % graves) e *Instruction Following* (165 casos, severidad ≈ 1,5).

La implicancia es directa para la mitigación: el **tamaño** indica dónde invertir en robustez general, mientras que el **color** señala dónde colocar salvaguardas estrictas. Optimizar solo por frecuencia dejaría desatendidos justamente los riesgos más severos.

#### Responsabilidad individual

El desarrollo de esta visualización —selección y verificación del dataset, procesamiento de los datos, implementación manual del algoritmo de Voronoi treemap ponderado en Python, diseño del lenguaje visual y redacción de esta ficha técnica— fue realizado íntegramente por **Benjamín Olguín Pozo**.

---

## 2. Texto para la infografía

### Título corto recomendado

**Anatomía de los fallos de agentes LLM**

### Bajada o subtítulo

Lo que más falla no es lo más peligroso.

### Texto breve para acompañar el gráfico

Cada celda es un tipo de fallo de un agente LLM: su tamaño indica qué tan frecuente es y su color, qué tan grave. Los fallos más comunes (razonamiento, uso de herramientas, contexto) son grandes pero de gravedad media; los más críticos (seguridad y alineamiento, fundamentación) son pequeños pero intensamente rojos.

### Microconclusión para la infografía

Gestionar la confiabilidad de un agente no es reducir el fallo más común, sino equilibrar la atención entre lo frecuente y lo grave.

### Fuente para colocar bajo el gráfico

Fuente: Kaggle — LLM Agent Failure Analysis Benchmark (1.500 casos, dataset sintético). Taxonomía anclada en literatura de fallos agénticos (arXiv:2509.23735).

### Ubicación sugerida dentro de la narrativa visual

Hacia el cierre de la infografía, como pieza de síntesis sobre los **riesgos** del ecosistema LLM: después de mostrar qué modelos existen, cuán potentes son y dónde se concentran, esta visualización responde *qué puede salir mal cuando se les delega autonomía*.

### Frase puente para conectar con las demás visualizaciones

"Tras ver el poder y el alcance de los LLMs, queda la pregunta incómoda: cuando actúan por sí solos, ¿cómo y cuán gravemente fallan?"

### Recomendación visual para integrarlo

Conservar el disco completo con su leyenda numerada lateral y la barra de severidad; ubicarlo sobre fondo claro y neutro para no competir con la escala de color cálida. Si el espacio es reducido, puede recortarse la leyenda a las cinco entradas más relevantes (las tres más frecuentes y las dos más graves) y referir el resto al informe.
