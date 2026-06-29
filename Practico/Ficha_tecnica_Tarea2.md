# Fichas técnicas — Visualizaciones de tareas anteriores

**Visualización:** Diagrama de Sankey — Frecuencia de uso y propósitos.

**Autor:** Nicolás González

**Tipo de gráfico:** Diagrama de Sankey (diagrama de flujo)

**Herramienta:** Flourish

**Fuente de datos:** Encuesta grupal sobre uso de herramientas LLM — UTFSM, mayo 2026 (formulario digital exportado a CSV).

---


## Marca

Hay dos marcas: los **nodos (rectángulos)**, que representan categorías, y las **bandas de enlace (links)**, que conectan un nodo de origen con uno de destino. La marca portadora del dato cuantitativo es la **banda de enlace**.

## Canales
- **Posición (nominal):** los nodos de la izquierda representan la *frecuencia de uso* (Todos los días, 3–5 veces, 1–2 veces, Rara vez) y los de la derecha el *propósito* (Estudio, Resumen, Programación, Redacción, Trabajo, Ocio, Otro).
- **Grosor del enlace (tamaño, cuantitativo):** el ancho de cada banda codifica el *volumen de menciones* de esa combinación frecuencia→propósito.
- **Color – matiz (nominal):** distingue los flujos según su origen/categoría.

## Definición del lenguaje visual
| Elemento | Definición | Justificación |
|---|---|---|
| **Color** | Paleta **categórica** por nodo de origen, con bandas semitransparentes. | Permite seguir cada flujo desde su frecuencia de origen; la transparencia ayuda a leer los cruces sin que un flujo tape a otro. |
| **Texturas** | Sin texturas; bandas y nodos de relleno plano. | El Sankey se lee por grosor y trayectoria; las texturas restarían claridad a los cruces. |
| **Tipografía** | Sans serif limpia, coherente con el grupo. | Lectura clara de las etiquetas de nodos a ambos lados. |
| **Líneas** | Nodos como rectángulos finos; enlaces sin borde, solo relleno. | Mantiene el foco en el flujo y evita ruido visual. |

## Lectura
Los flujos más gruesos nacen en las frecuencias altas ("Todos los días", "3–5 veces") y van hacia Estudio y Resumen: los LLMs se usan sobre todo como apoyo académico y de síntesis, con Programación alimentada por usuarios de alta frecuencia.
