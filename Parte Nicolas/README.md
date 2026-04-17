### Criterios:
1. **Rendimiento por diminio:** Puntajes obtenidos en benchmarks estandarizados (GPQA, MATH, MMLU y HumanEval) correspondientes a diferentes dominios de estudio:
  * MATH: Preguntas matemáticas.
  * GPQA: Preguntas científicas a nivel de PhD.
  * MMLU: Preguntas y tareas cotidianas de conocimiento general.
  * HumanEval: Generación de código en base a lenguaje natural.
    
2. **Costo de inferencia:** Precio en $USD de uso de la API por cada millón de tokens (Input/Output).

### Justificación de los criterios
Se eligieron estos criterios porque permiten evaluar los Modelos de Lenguaje Grande (LLMs) desde una perspectiva 
de viabilidad práctica y comercial, más allá del avance tecnológico. El rendimiento técnico por sí solo 
no es suficiente para decidir qué modelo implementar en un entorno real; cruzarlo con el costo de inferencia 
permite identificar el verdadero retorno de inversión (ROI) de cada uno, revelando si pagar una tarifa 
premium garantiza necesariamente resultados superiores en todas las tareas.

### Conclusiones
* **Ausencia de correlación:** El gráfico demuestra que no existe una correlación estricta entre el precio y el rendimiento general.
Los modelos más costosos del mercado no dominan absolutamente todas las dimensiones técnicas, siendo superados en áreas específicas por alternativas más económicas.
* **Razonamiento experto especializado:** A pesar de la fuerte competencia en la gama baja de precios, alcanzar el rendimiento
tope en tareas de razonamiento experto a nivel de posgrado (GPQA) o de programación lógica compleja (HumanEval) aún requiere
invertir en los modelos de gama alta (como GPT-5 o Claude 3.5 Sonnet), marcando una clara segmentación en el mercado según la
exigencia del caso de uso.

**Fuente:** Datos recopilados de Artificial Analysis y Hugging Face (2026):
* https://artificialanalysis.ai
* https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/
  
**Gráfico:** Gráfico de Coordenadas Paralelas (Parallel Coordinates Plot).
