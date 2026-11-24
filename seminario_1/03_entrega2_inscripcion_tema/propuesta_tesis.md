# Análisis multimodal del discurso político y su relación con el voto parlamentario: postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa)

**Estudiante:** Agustín Sebastián Solís Meza
**Profesor(a) guía:** Valentin Clement Barriere
**Profesor(a) co-guía:** Franziska Christl Wagner
**Fecha:** 6 de octubre de 2026

# Antecedentes

En las democracias representativas, los partidos políticos comunican sus posiciones por múltiples canales: las fijan en sus programas electorales, las defienden en el debate parlamentario, las difunden en redes sociales y las repiten en televisión y radio. Al mismo tiempo, sus representantes toman decisiones observables cuando votan leyes y enmiendas. Estudiar qué dicen los partidos, cómo votan y si ambas cosas coinciden es relevante para comprender su comportamiento y evaluar la coherencia de la representación política.

Desde la ciencia de datos, este problema presenta tres desafíos. El primero es de integración: las fuentes son heterogéneas en formato, unidad de análisis y modalidad (texto, audio y video), y deben vincularse a una misma identidad de diputado y partido. El segundo es de extracción de información: no basta con saber de qué tema habla un actor, sino que es necesario identificar qué argumentos plantea, qué postura adopta y qué valores invoca. El tercero es de validez de la medición: el análisis computacional de textos políticos permite medir posiciones a gran escala, pero sus resultados deben validarse en cada aplicación antes de interpretarse (Grimmer y Stewart, 2013).

La literatura ofrece modelos para cada una de estas tareas. Para la clasificación temática, el Manifesto Project (MARPOR) define 56 categorías en siete dominios, sobre las que se entrenó el modelo multilingüe ManifestoBERTa (Burst et al., 2024). La detección de postura (a favor, en contra o neutral frente a un objetivo) cuenta con conjuntos de datos políticos multilingües (Barriere et al., 2022). La extracción de argumentos identifica las afirmaciones de un texto y las razones que las sostienen. Para los valores, la Moral Foundations Theory describe fundamentos morales como el cuidado, la justicia, la lealtad, la autoridad y la pureza (Graham et al., 2013), y la teoría de Schwartz describe valores básicos como la seguridad, la tradición o el universalismo; en procesamiento de lenguaje natural se formuló la tarea de identificar los valores humanos detrás de un argumento (Kiesel et al., 2022). En lo audiovisual, existen modelos de transcripción automática del habla y de reconocimiento de emociones a partir de la voz y la imagen. Sin embargo, estos modelos fueron entrenados mayoritariamente con datos en inglés y de dominios distintos al político, por lo que no se sabe si mantienen su desempeño sobre discurso político en francés ni sobre fuentes tan distintas como un programa, una intervención parlamentaria, un tuit o un noticiero. Además, los estudios suelen enfocarse en una sola fuente o dimensión del discurso, y rara vez integran estas mediciones con el voto nominal.

Esta tesis aborda esos desafíos en la Asamblea Nacional francesa durante la XV legislatura (2017-2022). El caso es adecuado por la disponibilidad de datos abiertos parlamentarios detallados y porque el trabajo se enmarca en el proyecto PAROLES ET ACTES (INA le lab 2026-2027), dirigido por el profesor guía, que dará acceso a archivos audiovisuales del Institut national de l'audiovisuel (INA). La tesis tiene dos focos: estudiar los datos y determinar qué modelos existentes pueden usarse sobre ellos, cuáles no y por qué; y usar las mediciones confiables para estudiar el discurso y el voto de los partidos, primero por separado y luego en conjunto, para identificar dónde coinciden y dónde se separan.

# Objetivos

## Objetivo General

Desarrollar y evaluar una metodología multimodal de ciencia de datos que determine qué modelos existentes pueden aplicarse a fuentes textuales y audiovisuales del discurso político francés para extraer sus temas, argumentos, posturas, valores y emociones, y usar esas mediciones para estudiar el discurso y el comportamiento de voto de partidos y diputados en la XV legislatura de la Asamblea Nacional, así como la correspondencia entre ambos.

## Objetivos Específicos

1. Construir una base de datos integrada y reproducible que reúna las fuentes textuales, el voto nominal y el material audiovisual, enlazados a una identidad común de diputado y partido.
2. Clasificar temáticamente cada fuente según la taxonomía MARPOR y validar la clasificación contra la codificación humana y contra una referencia de expertos.
3. Extraer los argumentos del discurso e identificar su postura y los valores que expresan, según la Moral Foundations Theory y la teoría de valores de Schwartz.
4. Caracterizar el material audiovisual que entregue el INA (tipo de programa, calidad de audio y video, cantidad de hablantes, presencia de diputados de la cohorte) y, según esas características, determinar qué modelos de transcripción, atribución de hablante y reconocimiento de emociones pueden aplicarse y cuáles no, a partir de su desempeño sobre muestras revisadas manualmente.
5. Construir conjuntos de evaluación revisados manualmente por fuente y por tarea, y medir con ellos el desempeño de los modelos existentes, incluidos modelos de lenguaje de gran escala, para decidir cuáles son utilizables en cada fuente.
6. Estudiar por separado el discurso y el voto de los partidos: qué temas priorizan, qué posturas, valores y emociones expresan según el canal, y cómo votan en términos de cohesión interna, alineamientos entre partidos y diferencias por tema.
7. Diseñar e implementar medidas de correspondencia entre discurso y voto por partido, tema y canal, con estimación de su incertidumbre, para identificar dónde coinciden y dónde se separan.

# Metodología

La metodología se organiza en seis etapas. La evaluación de los modelos es el eje, ya que de ella depende que las mediciones puedan interpretarse. Las variables principales serán, para cada unidad de discurso, su tema (categoría MARPOR), su postura, sus valores (multietiqueta, según MFT y Schwartz) y, en lo audiovisual, la emoción expresada; para el voto, la dirección del voto nominal de cada diputado (a favor, en contra o abstención).

**Etapa 1: recolección e integración de datos.** Como eje se armará la cohorte de diputados de la XV legislatura, incluidos los reemplazos, a partir de los datos abiertos de la Asamblea Nacional, enlazada con sus cuentas de Twitter mediante el registro de Regards Citoyens. Sobre esa cohorte se incorporarán los programas electorales de 2017 (API del Manifesto Project, con su codificación humana), las publicaciones en Twitter (recolectadas con Zeeschuimer), las intervenciones en el hemiciclo (Regards Citoyens), las leyes, enmiendas y votaciones nominales (datos abiertos de la Asamblea Nacional y Légifrance) y el material audiovisual del INA, cuya entrega está prevista hacia fines de 2026. Cada fuente se normalizará a una unidad de análisis comparable y se enlazará con el diputado y el partido mediante resolución de entidades, en un pipeline modular y reproducible.

**Etapa 2: extracción de información desde el texto.** Se clasificará el tema de cada unidad con ManifestoBERTa, usando modelado de tópicos (BERTopic) como contraste exploratorio. Luego se aplicarán tres tareas encadenadas: extracción de argumentos, detección de su postura y detección de los valores que expresan. Los modelos candidatos se identificarán mediante una revisión sistemática en ACL Anthology (consultada con su API), considerando modelos multilingües ajustados por tarea, transferencia entre idiomas y modelos de lenguaje de gran escala sin entrenamiento adicional o con pocos ejemplos.

**Etapa 3: estudio del material audiovisual y selección de modelos.** Como el contenido exacto del material del INA se conocerá al recibirlo, esta etapa comenzará con un análisis exploratorio de las características descritas en el objetivo 4, además de la duración y la disponibilidad de transcripciones o metadatos. En función de esas características se determinará qué tareas son factibles y qué modelos candidatos pueden aplicarse: transcripción automática (por ejemplo, Whisper), atribución de cada segmento a su hablante y reconocimiento de emociones a partir de la voz y, si la imagen lo permite, de las expresiones faciales. Cada modelo se probará sobre muestras revisadas manualmente, igual que en la etapa 4, y solo se usarán los que tengan un desempeño suficiente; los que no funcionen también se reportarán, indicando por qué fallan (superposición de voces, ruido, planos sin el hablante, entre otros).

**Etapa 4: evaluación de modelos.** Para cada tarea y fuente se seleccionará una muestra estratificada, revisada y clasificada manualmente con guías de anotación adaptadas de esquemas existentes. Con ella se medirá el desempeño de cada modelo (precisión, exhaustividad y F1 macro) y se analizará en qué casos y fuentes falla; cuando sea posible, se reportará el acuerdo entre anotadores con el coeficiente kappa. También se evaluarán modelos de lenguaje de gran escala como anotadores, contrastándolos con la muestra humana. El resultado será una comparación de cuánto se degrada cada modelo al cambiar de fuente, que permitirá decidir qué modelos usar en cada una y qué mediciones son confiables.

**Etapa 5: análisis del discurso y del voto de los partidos.** Con las mediciones validadas, se estudiará cada dimensión por separado. En el discurso, se caracterizará qué temas prioriza cada partido, qué posturas adopta, qué valores y emociones invoca, y cómo cambia esto según el canal y a lo largo de la legislatura. En el voto, se analizará la cohesión interna de cada partido, los alineamientos entre partidos, las diferencias por tema y el efecto de pertenecer al gobierno o a la oposición. Las posiciones estimadas se contrastarán con la encuesta de expertos Chapel Hill (CHES).

**Etapa 6: comparación entre discurso y voto.** Se contrastarán la postura y los valores expresados por cada partido y diputado según tema y canal con la dirección de su voto en las leyes y enmiendas asociadas a esos temas. Se diseñarán medidas de correspondencia que identifiquen en qué temas y canales discurso y voto coinciden y en cuáles se separan, considerando la posición de gobierno u oposición. La robustez de los resultados se evaluará mediante remuestreo bootstrap.

# Resultados Esperados

- Una base de datos multimodal, integrada y documentada, que reúna el discurso y el voto de los diputados de la XV legislatura francesa, junto con el código del pipeline para replicarla y extenderla a otras legislaturas o países.
- Conjuntos de evaluación en francés, revisados manualmente, para extracción de argumentos, postura y valores en distintas fuentes políticas.
- Una evaluación comparativa, con métricas de desempeño por tarea y fuente, de qué modelos funcionan y de cuánto se degradan al cambiar de dominio, idioma y modalidad.
- Un diagnóstico de qué modelos de análisis audiovisual pueden aplicarse al material del INA y cuáles no, según las características de esos datos.
- Una caracterización del discurso de los partidos (temas, posturas, valores y emociones por canal) y de su comportamiento de voto.
- Un análisis de las coincidencias y diferencias entre lo que partidos y diputados expresan y lo que votan, por tema, partido y canal.
# Plan de Trabajo

Plan tentativo entre octubre de 2026 y julio de 2027. E1 a E6 son las etapas de la metodología; las que dependen del INA se ajustarán a su fecha de entrega.

| Actividad | Oct | Nov | Dic | Ene | Feb | Mar | Abr | May | Jun | Jul |
|---|---|---|---|---|---|---|---|---|---|---|
| Revisión de literatura y modelos | X | X | X | | | | | | | |
| E1: fuentes textuales | X | X | X | | | | | | | |
| E1: material del INA | | | X | X | X | | | | | |
| E2: extracción desde el texto | | | X | X | X | X | | | | |
| E3: audiovisual y modelos | | | | X | X | X | X | | | |
| E4: anotación y evaluación | | | | | X | X | X | X | | |
| E5: discurso y voto | | | | | | | X | X | X | |
| E6: comparación | | | | | | | | X | X | |
| Escritura: antecedentes y datos | X | X | X | | | | | | | |
| Escritura: metodología y evaluación | | | | | | X | X | X | | |
| Escritura: resultados y conclusiones | | | | | | | | | X | X |
| Hitos: avance y entrega final | | X | | | | | | | | X |

# Resultados preliminares

Como avance de la etapa 1, se cuenta con la cohorte de diputados de la XV legislatura: 668 diputados, incluidos los reemplazos, de los cuales 587 tienen una cuenta de Twitter identificada en el registro de Regards Citoyens. Sobre esas cuentas se recolectaron con Zeeschuimer las publicaciones de 533 diputados: 244.244 publicaciones atribuidas, de las cuales 170.217 son tuits únicos por duplicados en la captura. Además, se dispone de los programas electorales de 2017 entregados por el Manifesto Project: 10 manifiestos segmentados en 3.801 cuasi-frases con su codificación temática humana. La exploración inicial muestra dos aspectos a resolver: la captura de Twitter cubre la línea de tiempo reciente de cada cuenta, por lo que excede la legislatura y deberá filtrarse o completarse, y 54 cuentas quedaron sin captura.

# Bibliografía

- Barriere, V., Jacquet, G. y Hemamou, L. (2022). CoFE: A new dataset of intra-multilingual multi-target stance classification from an online European participatory democracy platform. *Proceedings of AACL-IJCNLP 2022*.
- Burst, T., Lehmann, P., Franzmann, S. et al. (2024). *manifestoberta-xlm-roberta-56policy-topics-sentence-2024-1-1*. Manifesto Project.
- Graham, J., Haidt, J., Koleva, S., Motyl, M., Iyer, R., Wojcik, S. P. y Ditto, P. H. (2013). Moral foundations theory: The pragmatic validity of moral pluralism. *Advances in Experimental Social Psychology*, 47, 55-130.
- Grimmer, J. y Stewart, B. M. (2013). Text as data: The promise and pitfalls of automatic content analysis methods for political texts. *Political Analysis*, 21(3), 267-297.
- Kiesel, J., Alshomary, M., Handke, N., Cai, X., Wachsmuth, H. y Stein, B. (2022). Identifying the human values behind arguments. *Proceedings of ACL 2022*, 4459-4471.
