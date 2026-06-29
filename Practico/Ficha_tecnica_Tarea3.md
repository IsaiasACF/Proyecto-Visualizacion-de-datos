# Ficha técnica — Heatmap de capacidades de LLMs

**Visualización:** Mapa de puntos — Infraestructura física del cómputo.

**Autor:** Nicolás González.

**Tipo de gráfico:** Mapa de puntos (símbolos proporcionales sobre mapa).

**Herramienta:** Datawrapper.

**Fuente de datos:** Epoch AI (Frontier Data Centers), AI Data Center Index, m-ric, TechCrunch, Sherwood News, Neowin, Rystad Energy, Blackridge Research (consultado junio 2026).

---

## Marca
La marca es el símbolo puntual (círculo) ubicado sobre el mapa. Cada punto representa un centro de datos.

## Canales
- **Posición geográfica (cuantitativa, lat/long):** ubica cada centro de datos en su localización real sobre el mapa.
- **Tamaño – área del círculo (cuantitativo):** Codifica la capacidad eléctrica del campus en MW.
- **Color – matiz (nominal):** Identifica al *operador* (Google, Microsoft, Amazon, Meta, OpenAI/Oracle, xAI, Alibaba, Tencent, etc.).

## Definición del lenguaje visual
| Elemento | Definición | Justificación |
|---|---|---|
| **Color** | Paleta **categórica** por operador, sobre un mapa base gris neutro. | Los operadores son categorías nominales; el fondo neutro evita competir con las burbujas. |
| **Texturas** | Sin texturas; círculos de relleno semitransparente para ver solapamientos. | La transparencia permite leer agrupaciones densas (p. ej. EE.UU.) sin que un punto oculte a otro. |
| **Tipografía** | Canva Sans. | Lectura clara de etiquetas y leyenda. |
| **Líneas** | Bordes finos en los círculos y fronteras de país suaves. | Delimitan puntos y países sin sobrecargar el mapa. |

## Lectura
La infraestructura de cómputo está fuertemente concentrada: EE.UU. reúne gran parte de los campus y los de mayor escala; Europa aparece un escalón abajo y China de forma parcial. La capacidad la controla un grupo reducido de operadores.
