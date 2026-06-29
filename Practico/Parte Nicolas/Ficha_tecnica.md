# Ficha técnica — Heatmap de capacidades de LLMs

**Visualización:** ¿Qué tan capaces son los LLMs? Rendimiento por benchmark (2026)

**Enlace:** https://public.flourish.studio/visualisation/29528338/

**Autor:** Nicolás González

**Tipo de gráfico:** Mapa de calor (heatmap / matriz)

**Herramienta:** Flourish (plantilla *Numeric heatmap*)

**Fuente de datos:** Artificial Analysis — https://artificialanalysis.ai (Consultado - junio 2026)


---

## Marca

La marca es el **rectángulo (celda)**. Cada celda representa la intersección de un modelo y un benchmark, es decir, un único puntaje. Es un área rellena: la unidad mínima de información es la celda.

## Canales

- **Posición espacial:** las columnas identifican el *modelo* y las filas el *benchmark*. La posición agrupa y ordena, pero no expresa magnitud.
- **Color (cuantitativo):** es el canal principal. La intensidad representa el puntaje (0–100 %): celdas más oscuras = puntaje más alto; celdas más claras = puntaje más bajo.

## Definición del lenguaje visual

| Elemento | Definición | Justificación |
|---|---|---|
| **Color** | Escala **secuencial** de claro a oscuro, con rango fijo **0–100**. | El dato es cuantitativo y ordenado, por lo que una escala secuencial lo representa sin sugerir categorías. El rango compartido 0–100 mantiene la comparabilidad entre todos los benchmarks. |
| **Texturas** | Sin texturas. | El heatmap se apoya en la intensidad del color; cualquier textura competiría con esa lectura. |
| **Tipografía** | Canva Sans; números legibles dentro/junto a cada celda. | Favorece la lectura rápida de etiquetas y valores. |
| **Líneas** | Bordes finos entre celdas; sin marcos gruesos. | Mantiene la grilla ordenada. |

## Lectura / conclusión

El heatmap muestra convergencia entre los modelos más populares (GPT-5, Claude Opus 4.5, Gemini 3 Pro, Grok 4) en los benchmarks de conocimiento, 
ciencia y matemáticas, donde se aprietan en valores altos. Las brechas reales se comienzan a aprecier en el benchmark *SWE-bench Verified* y, sobre todo, en *Humanity's Last Exam*, 
donde casi todos quedan bajos. También se ve el efecto del tamaño del modelo: variantes pequeñas como Qwen 3 1.7B y Llama 4 Maverick quedan claramente 
rezagadas en toda su columna.
