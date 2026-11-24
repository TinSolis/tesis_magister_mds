**CLÍNICA DE ESCRITURA:**  
**TEXTUALIZAR EL PLAN DE INVESTIGACIÓN**

**Estudiante:** Agustín Sebastián Solís Meza  
**Profesor guía:** Valentin Clement Barriere  
**Profesora co-guía:** Franziska Christl Wagner

| PLAN DE INVESTIGACIÓN |  |
| :---: | ----- |
| **Título** | Análisis multimodal del discurso político y su relación con el voto parlamentario: postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa) |
| **Problema** **o** **justificación** | Los partidos comunican sus posiciones por varios canales (programas electorales, debate parlamentario, Twitter, televisión y radio) y sus diputados votan leyes y enmiendas, pero estas fuentes suelen estudiarse por separado. Saber de qué tema habla un partido no indica qué postura adopta, qué valores invoca ni si eso coincide con su voto. Además, los modelos que miden temas, argumentos, postura, valores y emociones fueron entrenados sobre todo en inglés y en otros dominios, por lo que no se sabe si funcionan sobre discurso político en francés ni sobre fuentes tan distintas como un programa, un tuit o un noticiero. Sin esa validación, las mediciones no pueden interpretarse. |
| **Pregunta** **de** **investigación** | ¿Qué modelos existentes permiten medir de forma confiable los temas, argumentos, posturas, valores y emociones del discurso político francés en fuentes textuales y audiovisuales, y qué revelan esas mediciones sobre la correspondencia entre lo que dicen y lo que votan los partidos y diputados de la XV legislatura (2017-2022)?<br><br>**Hipótesis de trabajo:** los modelos mantendrán un buen desempeño en texto estructurado (programas e intervenciones parlamentarias) y se degradarán en Twitter y en el material audiovisual; la correspondencia entre discurso y voto variará según el tema, el canal y la posición de gobierno u oposición. |
| **Objetivo** **General** | Desarrollar y evaluar una metodología multimodal de ciencia de datos que determine qué modelos existentes pueden aplicarse a fuentes textuales y audiovisuales del discurso político francés, y usar esas mediciones para estudiar el discurso y el voto de partidos y diputados de la XV legislatura de la Asamblea Nacional, así como la correspondencia entre ambos. |
| **Objetivos** **Específicos** | 1\. Construir una base de datos integrada y reproducible con programas electorales, Twitter, intervenciones en el hemiciclo, leyes, enmiendas, votos nominales y material audiovisual del INA, enlazados a una identidad común de diputado y partido.<br>2\. Extraer desde el texto el tema de cada unidad (taxonomía MARPOR), sus argumentos, su postura y los valores que expresa (Moral Foundations Theory y teoría de Schwartz).<br>3\. Caracterizar el material audiovisual del INA y determinar qué modelos de transcripción, atribución de hablante y reconocimiento de emociones pueden aplicarse según sus características.<br>4\. Construir conjuntos de evaluación revisados manualmente por fuente y tarea, y medir con ellos el desempeño de los modelos existentes, incluidos modelos de lenguaje de gran escala, para decidir cuáles son utilizables en cada fuente.<br>5\. Estudiar por separado el discurso de los partidos (temas, posturas, valores y emociones por canal) y su voto (cohesión interna, alineamientos y diferencias por tema).<br>6\. Diseñar e implementar medidas de correspondencia entre discurso y voto por partido, tema y canal, con estimación de su incertidumbre. |
| **Metodología** | Enfoque cuantitativo en seis etapas, con la evaluación de modelos como eje.<br>**1. Datos:** cohorte de diputados de la XV legislatura (datos abiertos de la Asamblea Nacional) enlazada con sus cuentas de Twitter (Regards Citoyens) y sus tuits (Zeeschuimer), programas de 2017 (Manifesto Project), intervenciones en el hemiciclo (Regards Citoyens), leyes, enmiendas y votos (Asamblea Nacional y Légifrance) y archivos del INA.<br>**2. Texto:** ManifestoBERTa para temas, con BERTopic como contraste, y modelos candidatos para argumentos, postura y valores identificados mediante una revisión sistemática en ACL Anthology.<br>**3. Audiovisual:** análisis exploratorio del material del INA y prueba de modelos de transcripción (Whisper), atribución de hablante y emociones desde la voz y la imagen.<br>**4. Evaluación:** muestras estratificadas anotadas manualmente; precisión, exhaustividad, F1 macro y acuerdo entre anotadores (kappa); modelos de lenguaje de gran escala como anotadores, contrastados con la muestra humana.<br>**5. Discurso y voto por separado:** temas, posturas, valores y emociones por partido y canal; cohesión y alineamientos en el voto; contraste con la encuesta de expertos CHES.<br>**6. Comparación:** medidas de correspondencia entre la postura y los valores expresados y la dirección del voto por tema, con remuestreo bootstrap. |
| **Resultados** **y** **Conclusiones** | Resultados esperados: una base de datos multimodal integrada con su pipeline reproducible; conjuntos de evaluación en francés para argumentos, postura y valores; una evaluación comparativa de qué modelos funcionan en cada fuente y cuánto se degradan al cambiar de dominio, idioma y modalidad, incluido un diagnóstico del material del INA; y una caracterización del discurso y el voto de los partidos que muestre dónde coinciden y dónde se separan.<br>Las conclusiones confirmarán o refutarán la hipótesis, establecerán qué mediciones automáticas del discurso político francés son confiables y en qué fuentes, y explicarán qué revelan sobre la coherencia entre discurso y voto. |

**PLANIFICACIÓN DE ÍNDICE**

1\. Introducción  
	1.1. Contexto y problema  
	1.2. Pregunta de investigación e hipótesis  
	1.3. Objetivos  
	1.4. Alcances

2\. Marco Teórico  
	2.1. Marco conceptual: texto como datos, taxonomía MARPOR, argumentos, postura, valores (MFT y Schwartz) y emociones  
	2.2. Estado del arte: modelos de clasificación temática, postura, detección de valores, transcripción y reconocimiento de emociones; modelos de lenguaje de gran escala como anotadores  
	2.3. Antecedentes: Asamblea Nacional y XV legislatura, partidos, proyecto PAROLES ET ACTES

3\. Datos y Metodología  
	3.1. Fuentes y construcción de la base integrada  
	3.2. Extracción de información desde el texto  
	3.3. Procesamiento del material audiovisual  
	3.4. Anotación manual y protocolo de evaluación  
	3.5. Análisis del discurso, del voto y medidas de correspondencia

4\. Resultados  
	4.1. Descripción de la base de datos integrada  
	4.2. Desempeño de los modelos por tarea y fuente  
	4.3. Diagnóstico del material audiovisual  
	4.4. Discurso y voto de los partidos  
	4.5. Correspondencia entre discurso y voto

5\. Discusión  
	5.1. Validez de los modelos fuera de su dominio  
	5.2. Interpretación política de los resultados  
	5.3. Limitaciones

6\. Conclusiones

7\. Trabajos futuros
