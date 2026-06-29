# Fichas técnica - Evolución de modelos LLM por organización.

**Visualización:** Streamgraph — Evolución de modelos LLM por organización  

**Autor:** Isaías Carte Figueroa

**Tipo de gráfico:** Streamgraph (gráfico de flujo apilado)

**Herramienta:** Python

**Fuente de datos:** Epoch AI — Notable AI Models. https://epoch.ai/data/ai-models?view=table&tab=notable

---

## Marca
La marca es el **área (banda de flujo)**. Cada banda representa una organización desarrolladora, y su forma fluye a lo largo del tiempo apilándose en torno a un eje central (rasgo propio del streamgraph).

## Canales
- **Posición horizontal (cuantitativa/ordinal):** el eje X codifica el *tiempo* (año de publicación, 2018–2025).
- **Grosor de la banda (tamaño, cuantitativo):** la altura de cada banda codifica la *cantidad de modelos* publicados por la organización en ese período.
- **Color – matiz (nominal):** cada organización (Google, OpenAI, Anthropic, Meta, Microsoft, NVIDIA, Alibaba, Baidu) recibe un color distinto.

## Definición del lenguaje visual
| Elemento | Definición | Justificación |
|---|---|---|
| **Color** | Paleta **categórica** (un matiz por organización). | Las organizaciones son categorías nominales sin orden; un matiz por categoría permite seguir cada flujo a lo largo del tiempo. |
| **Texturas** | Sin texturas; áreas de relleno sólido. | El streamgraph se lee por forma y grosor; las texturas dificultarían distinguir el espesor de cada banda. |
| **Tipografía** | Sans serif limpia, coherente con el grupo. | Lectura rápida de ejes, leyenda y etiquetas de organización. |
| **Líneas** | Bordes finos entre bandas para separarlas; sin marcos gruesos. | Delimitan los flujos manteniendo una lectura fluida. |

## Lectura
El desarrollo de LLMs se acelera desde 2022; Google y OpenAI concentran el mayor peso relativo, con Anthropic, Meta y Microsoft creciendo en el período reciente.


## Lectura
La infraestructura de cómputo está fuertemente concentrada: EE.UU. reúne gran parte de los campus y los de mayor escala; Europa aparece un escalón abajo y China de forma parcial (datos estimados). La capacidad la controla un grupo reducido de operadores.
