# Análisis de Flujo: Frecuencia de Uso y Propósitos de los LLMs

### Criterios:
1. **Frecuencia de Interacción:** Segmentación del hábito de uso basada en la frecuencia de uso reportada por los usuarios:
    * **Todos los días:** Uso integrado totalmente en la rutina diaria.
    * **3-5 veces por semana:** Uso recurrente, asociado habitualmente a días laborales o de estudio.
    * **1-2 veces por semana:** Uso ocasional o complementario para tareas específicas.
    * **Rara vez:** Uso esporádico o por curiosidad.

2. **Propósito de Uso:** Categorización de las tareas específicas realizadas con la herramienta, abarcando dimensiones académicas, técnicas y recreativas (Estudio, Programación, Resumen, Redacción, Trabajo, Ocio, otros).

3. **Volumen de Menciones:** Representación cuantitativa que mide la intensidad de la relación entre una frecuencia determinada y una tarea específica.

### Justificación de los criterios
Se eligió el Diagrama de Sankey como motor de visualización, ya que permite mapear la relación entre dimensiones 
cualitativas (Frecuencia y Uso) a través de una lógica de flujo direccional. A diferencia de los gráficos circulares 
o de barras, el Sankey utiliza el grosor de los conectores para representar la magnitud de los datos, facilitando la 
identificación inmediata de qué tareas capturan la mayor cantidad de atención según el perfil de hábito del usuario. 

### Conclusiones
* **Uso en el sector académico y de síntesis:** El flujo de mayor grosor en el diagrama nace en las frecuencias más altas ("Todos los días" y "3-5 veces") y se dirige hacia las categorías de **Estudio** y **Resumen**. Esto permite concluir que los LLMs se han consolidado principalmente como herramientas de apoyo al aprendizaje y procesamiento de información densa.
* **Fidelización técnica en Programación:** La tarea de **Programación** es alimentada casi exclusivamente por usuarios de alta frecuencia (diaria o recurrente). Esto indica que, al igual que en el punto anteior, los LLM's ya se han convertido en una herramienta más para los progamadores.
* **Distribuciones marginales:** El diagrama revela flujos notablemente delgados hacia categorías como **Ocio** o **Trabajo** general, lo que sugiere que, para la muestra analizada (considerando que son estudiantes), la percepción de valor de los LLMs está fuertemente inclinada hacia la utilidad académica sobre la recreativa y laboral.

**Fuente:** Datos recopilados de la *Encuesta sobre uso de herramientas LLM - Tarea 2 Visualización de datos*, UTFSM, Mayo 2026:
* https://docs.google.com/forms/d/e/1FAIpQLSdFZ46xKvJyotwesRccWVLClm3HGvVm5qQVnOe1rl9P-zitiQ/viewform

**Gráfico:** Diagrama de Sankey.
