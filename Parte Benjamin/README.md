### Criterios:
1. **Desempeño relativo de LLM segun preferencia humana:**  Que tan bien se desempeña cada modelo cuando compite contra otros en comparaciones reales.
    
2. **Estructura de competencia entre modelos en enfrentamientos directos:** Analisís de que modelos comparan entre sí. Para no solo medir cuales ganan más, sino contra que modelos lo hacen.

### Justificación de los criterios
Estos criterios fueron seleccionados porque permiten un analisis de los LLM desde una dimension diferente al rendimiento tecnico tradicional y nos concentramos en comparaciones directas con evaluación humana. Esto nos acerca a un analisis más cercano a al uso practico de los LLM, observar cuales son preferidos por las personas y como se comportan en frente a competidores especificos.

### Conclusiones
* **El gráfico muestra que la preferencia humana no se distribuye de manera homogénea entre los modelos analizados:** Algunos modelos concentran una mayor cantidad de victorias, mientras que otros acumulan más derrotas, lo que sugiere diferencias claras de desempeño relativo en enfrentamientos directos.
* **Se observa una estructura competitiva jerárquica entre los modelos:** En particular, modelos como gpt-4-1106-preview y otros de la familia GPT-4 presentan un flujo importante de victorias, mientras que otros modelos, como claude-2.1, gpt-3.5-turbo-0613 o vicuna-33b, aparecen con una mayor concentración de derrotas. Esto indica que no todos los LLM compiten en igualdad de condiciones dentro del conjunto analizado.

**Fuente:** Datos recopilados de :
* Hugging Face Datasets: lmarena-ai/arena-human-preference-55k, dataset en formato CSV con aproximadamente 57.5 mil filas, que contiene comparaciones entre pares de modelos, prompts, respuestas y resultado de preferencia humana.
* Chiang et al. (2024): Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference, trabajo asociado al dataset y referenciado en la ficha oficial del mismo.
  
**Gráfico:** 

Gráfico:
**Sankey diagram de victorias entre modelos.**
Este gráfico representa el flujo de victorias entre los modelos con mayor presencia en el dataset. En el lado izquierdo se ubican los modelos ganadores y en el lado derecho los modelos derrotados. El grosor de cada flujo indica cuántas veces un modelo venció a otro, permitiendo visualizar simultáneamente el desempeño relativo y la estructura de competencia entre LLMs.