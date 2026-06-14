
# Mapa de infraestructura física de cómputo para IA

Visualizacion: https://public.flourish.studio/visualisation/29369282/

## Descripción cualitativa del dataset

El dataset reúne los principales centros de datos y superclusters de GPUs/TPUs asociados al entrenamiento y operación de modelos de IA (LLMs) a nivel mundial. Fue construido a partir de fuentes especializadas en infraestructura de cómputo, complementadas con reportes de prensa (TechCrunch, Sherwood News, Neowin), análisis sectoriales (m-ric, Rystad Energy) y comunicados de proyecto (Blackridge Research).

Cada registro corresponde a un campus e incluye: operador, ciudad o zona, país, región, coordenadas geográficas, capacidad eléctrica (MW), estado (operacional, en construcción o planificado), uso (entrenamiento dedicado o mixto) y un indicador de confiabilidad (dato documentado o estimado).

El dataset debe interpretarse considerando tres limitaciones. Primero, existe una asimetría de transparencia: los sitios de Estados Unidos están ampliamente documentados, mientras que los de China son no, ya que ese país reporta su cómputo en EFLOPS y rara vez en MW, por lo que sus capacidades corresponden a estimaciones. Segundo, muchos campus se construyen por fases, de modo que la capacidad refleja el valor total proyectado y la variable estado distingue lo ya operativo de lo planificado. Tercero, algunos campus son de uso mixto (nube general + IA) y no exclusivamente de entrenamiento de LLMs.

## Tipo de mapa

La visualización corresponde a un mapa de puntos (símbolos proporcionales) realizado en Flourish. Cada punto representa un centro de datos; su tamaño codifica la capacidad eléctrica del campus en MW y su color identifica al operador. Se optó por un mapa de puntos, porque el fenómeno relevante ocurre a nivel de campus individual y no de país: este tipo de mapa permite mostrar clústeres dentro de un mismo territorio, como la fuerte concentración en Texas y el Medio Oeste de Estados Unidos.

## Pregunta que busca responder

La pregunta principal de la visualización es:
¿Dónde se encuentra la infraestructura física que entrena y opera los LLMs, quién la controla y a qué escala energética?
De forma secundaria, el mapa permite distinguir qué parte de esa infraestructura ya está operativa frente a la que aún se encuentra en construcción, y observar el grado de concentración geográfica y de operadores.

## Público objetivo

La visualización está dirigida a estudiantes y personas interesadas en inteligencia artificial, así como a analistas de infraestructura y energía, planificadores territoriales y tomadores de decisión en política pública que busquen comprender la dimensión que sostiene a los modelos de IA.

## Acción o decisión que podría apoyar

El mapa puede apoyar discusiones sobre el impacto energético y territorial de la IA, considerando que la capacidad involucrada equivale a la demanda eléctrica de ciudades enteras. También aporta a debates sobre soberanía tecnológica y dependencia de unas pocas regiones y operadores, y sobre la presión que estos campus ejercen sobre las redes eléctricas y el agua en las zonas donde se concentran. Asimismo, sirve de base para análisis académicos y para identificar la brecha de infraestructura entre regiones líderes y subrepresentadas.

## Fuentes de datos

La fuente específica de cada centro de datos está detallada fila por fila en el archivo de datos. Las fuentes utilizadas son:

- Epoch AI — Frontier Data Centers / Stargate: https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
- AI Data Center Index (Google, Alibaba): https://aidatacenterindex.com
- m-ric — "The 3 tiers of the AI compute race" (Europa y China): https://m-ric.com/blog/datacenter-buildout/
- TechCrunch (Meta Prometheus y Hyperion): https://techcrunch.com/2025/07/14/mark-zuckerberg-says-meta-is-building-a-5gw-ai-data-center
- Sherwood News (xAI Colossus): https://sherwood.news/tech/clash-of-the-titans-here-are-the-biggest-ai-data-center-projects/
- Neowin (Microsoft Fairwater, Amazon Project Rainier): https://www.neowin.net/news/these-are-the-biggest-ai-data-centers-owned-by-big-tech/
- Rystad Energy (contexto de China): https://www.rystadenergy.com/news/chinas-data-center-capacity-doubling-of-power
- Blackridge Research (Stargate UAE): https://www.blackridgeresearch.com/blog/facts-you-need-to-know-about-openai-stargate-ai-data-center-project-abilene-texas-united-states-us-united-arab-emirates-uae

## Conclusión principal

El mapa evidencia que la infraestructura física que sostiene a los LLMs está fuertemente concentrada. Estados Unidos reúne la mitad de los campus mapeados y, además, los de mayor escala individual (como Meta Hyperion, con 2 GW proyectados), con clústeres densos en Texas y el Medio Oeste. Europa aparece con proyectos reales, pero un orden de magnitud por detrás (cientos de MW frente a gigavatios), y China, pese a su acelerado desarrollo, solo puede observarse de forma estimada debido a su opacidad de datos. La capacidad de cómputo se reparte, además, entre un grupo reducido de operadores (Google, Microsoft, Amazon, Meta, OpenAI/Oracle, xAI, Alibaba y Tencent). Finalmente, buena parte de los campus de mayor tamaño aún se encuentra en construcción, lo que sugiere que la concentración actual podría intensificarse con la ola de megacentros proyectada para el período 2026–2029.
