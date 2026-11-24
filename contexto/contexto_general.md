# Contexto de la tesis de Magíster (MDS, Universidad de Chile)

Documento vivo con todo lo relativo a la tesis de Magíster en Ciencia de Datos. Sirve para retomar el trabajo, pasarle contexto a otro chat/IA y registrar decisiones a medida que se avanza.

Para el detalle técnico del pipeline (datos, módulos, cifras) ver `contexto/pipeline/`, en especial `contexto/pipeline/00_resumen_pipeline.md`. Para preferencias de estilo y forma de trabajo ver `contexto/preferencias_y_estilo.md`.

**Estado de la memoria de Ingeniería Civil:** defendida el 16-nov-2026 y aprobada por la comisión (título de Ingeniero Civil en Computación obtenido). Su repo quedó cerrado en `../memoria_ing_civil/`. Desde ahora el foco es solo el magíster.

---

## 1. Regla de encuadre (la más importante)

La tesis de magíster **continúa y engloba** todo el trabajo de la memoria de Ingeniería Civil en Computación. El informe final de magíster va a incluir **todo lo anterior más lo nuevo**. El MDS no sabe de la memoria previa y no hay que mencionarla como trabajo previo: todo se presenta como trabajo de esta tesis. Lo que cambia es la profundidad: los guías esperan un análisis mejor y más detallado, más orientado a ciencia de datos (nuevas técnicas, evaluación de modelos y, según lo que permita el proyecto INA, datos audiovisuales).

Por eso, al escribir la propuesta, presentaciones o el informe:

- **No decir que algo "ya está hecho"** ni presentar el trabajo previo como antecedente cerrado. Todo se presenta como trabajo de esta tesis, en tiempo futuro o como parte del plan.
- Ejemplo correcto: "se recolectarán los tuits de los diputados mediante Zeeschuimer". Ejemplo incorrecto: "se usarán los datos de Twitter ya recolectados".
- Lo mismo para la cohorte de diputados, manifiestos, hemiciclo, leyes, enmiendas y votos, la clasificación MARPOR con ManifestoBERTa, BERTopic, la validación con CHES y los análisis declarado vs. revelado: todo es parte del trabajo de la tesis.
- Motivo: decir que está hecho hace que la tesis parezca menos trabajo, y todo ese trabajo sí se usa y forma parte de esta tesis.

**Criterio de alcance en propuestas y presentaciones.** Es una propuesta, así que está bien plantear un alcance amplio. No hay que recortarlo ni decir menos de lo que es: en la tesis final se puede terminar haciendo menos que lo propuesto. En las primeras instancias (propuesta, Presentación 1) el nivel es general, no hace falta tener todo investigado ni especificado. El recorte de alcance del §9 es una conversación interna con el guía, no algo que vaya en la propuesta.

---

## 2. Datos básicos

| Campo | Valor |
|---|---|
| Programa | Magíster en Ciencia de Datos (MDS), Universidad de Chile |
| Curso actual | Seminario de Tesis I, IA7305-1, Primavera 2026 |
| Profesor guía | Valentin Clement Barriere |
| Profesora co-guía | Franziska Christl Wagner |
| Doble título | No |
| Proyecto asociado | No es FONDEF ni FONDECYT. Se relaciona con el proyecto «PAROLES ET ACTES» (INA le lab 2026-2027, dirigido por Valentin Barriere) |
| Organización | Universidad de Chile, Departamento de Ciencias de la Computación (FCFM), y CENIA |
| Fuente de datos audiovisuales | INA (Institut national de l'audiovisuel, Francia). Ojo: es INA, no INRIA |

Proyecto de Valentin en INA le lab: «PAROLES ET ACTES: Cross-Modal Analysis of Political Rhetoric and Parliamentary Voting Using Audiovisual Archives».

- Lista de laureados: https://inalelab.hypotheses.org/10701
- Convocatoria (describe datos y herramientas disponibles: transcripciones Whisper de noticieros TV/radio desde 2011, ~497 M de tuits 2014-2023, análisis de rostro/voz, etc.): https://inalelab.hypotheses.org/10344

---

## 3. Decisiones confirmadas

- **Marco temporal**: XV legislatura de la Asamblea Nacional francesa (2017-2022). No se extiende a un periodo más reciente.
- **Datos INA**: llegarían a fin de año (2026). Si se atrasan, se avanza con los datos de texto.
- **Qué se analiza** (Valentin, 14-sep-2026): una mezcla.
  - En texto: extracción de argumentos con postura y valores (pueden usarse ambos marcos, MFT y Schwartz).
  - En audiovisual: análisis de emociones.
- **Parte más importante**: evaluar si los modelos existentes se adaptan a nuestros datos.

---

## 4. Propuesta entregada (Entrega 1, Seminario de Tesis I)

Planilla entregada: https://docs.google.com/spreadsheets/d/140VGDLgMe5zoftWWg3bkJPgEyGgaRfkyYvfPl9XMrxY/edit?usp=sharing

El feedback del seminario fue que el tema no quedaba del todo claro. Eso llevó a preguntarle a Valentin qué análisis concreto sería (ver §5).

**Nombre del tema.** Análisis multimodal del discurso político y su relación con el voto parlamentario: postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa).

**Descripción del tema.** La tesis analizará la relación entre el discurso público de los partidos políticos franceses y su comportamiento en el parlamento. Para ello, se integrarán programas electorales, publicaciones en Twitter, intervenciones parlamentarias, leyes, enmiendas, votaciones y material audiovisual del INA.

Se utilizarán modelos de ciencia de datos para identificar los temas, posturas y valores presentes en estas fuentes. El objetivo será estudiar si lo que los partidos y diputados comunican coincide con las decisiones que toman al votar.

**Antecedentes.** Los partidos políticos comunican sus posiciones mediante programas electorales, redes sociales, debates parlamentarios y apariciones en medios audiovisuales. Sin embargo, estas fuentes suelen estudiarse por separado, lo que dificulta comparar el discurso público con el comportamiento parlamentario.

La tesis se apoyará en métodos de procesamiento de lenguaje natural, clasificación temática, detección de postura, análisis de valores y aprendizaje multimodal. También se relacionará con el proyecto «PAROLES ET ACTES», dirigido por Valentin Barriere y apoyado por el INA, que permitirá trabajar con archivos audiovisuales políticos franceses.

**Problema a resolver.** Conocer los temas sobre los que habla un partido no permite determinar qué postura adopta, qué valores expresa ni si esas posiciones coinciden con sus votaciones.

El problema consiste en integrar distintas fuentes de información política y desarrollar una metodología que permita comparar el discurso de partidos y diputados con su comportamiento parlamentario, considerando tanto información textual como audiovisual.

**Objetivo general.** Desarrollar una metodología multimodal para analizar el discurso político francés y estudiar su relación con el comportamiento de voto de los partidos y diputados.

**Objetivos específicos.**

1. Construir una base integrada de diputados, programas electorales, Twitter, intervenciones parlamentarias, leyes, enmiendas, votaciones y material audiovisual.
2. Clasificar los temas presentes en las distintas fuentes.
3. Identificar las posturas y los valores expresados mediante modelos existentes.
4. Evaluar la calidad de los modelos mediante datos anotados manualmente.
5. Diseñar medidas para comparar el discurso político con las votaciones.
6. Analizar las coincidencias y diferencias entre partidos, fuentes y formas de comunicación.

---

## 5. Definición del análisis según Valentin (14-sep-2026)

Respuesta textual:

> Sobre lo que hay que analizar, seria una mezcla: extraccion de argumentos con postura y valores en el texto (pueden ser ambos MFT y Schwartz Theory), analisis de emociones en los datos AV. El mas interesante me parece de los valores de scwhartz y de la MFT, pero va a ser mas dificil porque hay menos trabajos sobre estos temas. Te recommendo de hacer una revision de literatura en las conferencias de ling tipo en https://aclanthology.org/. Tengo un ejemplo de codigo por usar la API: https://github.com/valbarriere/ACL_anthology/tree/master
>
> Por todos los modelos habra que evaluar los que existen para ver si se adaptan a tus datos. Eso es la parte mas importante creo. En los manifestos y en la asemblea el texto es bastante bien estructurado y va a ser simple de extraer informacion. En twitter va a ser mas contextual y dificil y hay que validar eso. En el AV no tengo una idea, tendra que mirar a los datos una vez que los van a entregar.

(AV = audiovisual.)

**Cómo se interpreta:**

- **Texto**, tres capas encadenadas:
  1. Extracción de argumentos (argument mining): identificar qué se afirma y con qué justificación, no solo el tema.
  2. Postura (stance): a favor o en contra.
  3. Valores: bajo qué marco moral se justifica. Se pueden usar ambos, Moral Foundations Theory (MFT) y la teoría de valores de Schwartz.
- **Audiovisual**: análisis de emociones (cómo se dice, no qué se dice).
- **Aporte central**: evaluar y validar si los modelos existentes se adaptan a cada fuente (adaptación de dominio y de idioma). No es solo aplicar modelos.
- **Dificultad esperada por fuente**:

| Fuente | Qué espera Valentin |
|---|---|
| Manifiestos y hemiciclo | Texto bien estructurado, simple de extraer información |
| Twitter | Más contextual y difícil, hay que validar |
| Audiovisual | Sin idea todavía, hay que mirar los datos cuando lleguen |

- **Lo más interesante**: valores de Schwartz y MFT. También lo más difícil, porque hay menos trabajos.

---

## 6. Alcance completo de la tesis (lo anterior más lo nuevo)

Según la regla del §1, todo esto se presenta como trabajo de la tesis.

**Construcción de datos**

- Cohorte de diputados de la XV legislatura (open data de la Asamblea Nacional) enlazada con sus cuentas de Twitter.
- Recolección de tuits de los diputados con Zeeschuimer.
- Descarga de manifiestos 2017 desde la API del Manifesto Project (MARPOR).
- Intervenciones en el hemiciclo (Regards Citoyens).
- Leyes (texto oficial vía Légifrance/PISTE), enmiendas y votaciones nominales.
- Material audiovisual del INA (cuando llegue): transcripción y enlace con diputados y partidos.

**Análisis temático**

- Clasificación MARPOR con ManifestoBERTa y exploración con BERTopic.
- Validación contra la codificación humana de MARPOR y contra CHES 2019 (RILE).
- Agenda declarada por canal, agenda revelada por el voto y cruce declarado vs. revelado.

**Lo nuevo del magíster**

- Extracción de argumentos, postura y valores (MFT y Schwartz) en texto.
- Análisis de emociones en audiovisual.
- Evaluación de modelos existentes en cada fuente, con datos anotados manualmente.
- Medidas que comparen postura y valores del discurso con la dirección del voto.

---

## 7. Plazos del Seminario de Tesis I (Primavera 2026)

| Entrega | Plazo | Estado |
|---|---|---|
| Entrega 1: Propuesta de 1 a 3 temas | 1-sep-2026 | Entregada |
| Presentación 1: Propuesta de tema de tesis | 27-sep-2026, 23:59 | Entregada |
| Entrega 2: Inscripción del tema de tesis | 6-oct-2026, 23:59 | Entregada |
| Entrega 3: Avance del manuscrito a la fecha (1 PDF; al menos portada y secciones enunciadas, se pueden incluir borradores) | 19-nov al 3-dic-2026, 23:59 | Pendiente |
| Presentación 2: Avance de tesis (subir 1 archivo; presentación presencial entre el 7 y el 11-dic-2026) | 19-nov al 3-dic-2026, 23:59 | Pendiente |

Carpetas de cada entrega: `seminario_1/0X_*/`. El manuscrito LaTeX (Overleaf) vive en `manuscrito/`.

---

## 8. Preguntas abiertas enviadas a Valentin (sin respuesta aún)

Mensaje enviado después de su respuesta del 14-sep:

1. **Validación en Twitter**: como no hay tuits políticos franceses etiquetados con valores o MFT, habría que etiquetar a mano una muestra. ¿De qué tamaño? ¿Un solo anotador o un segundo para reportar acuerdo (kappa)? ¿Se puede usar un LLM como anotador para escalar, validándolo contra la muestra humana?
2. **Guías de anotación**: ¿adaptar un esquema existente de alguna tarea compartida (por ejemplo, detección de valores de Schwartz en SemEval/Touché) o armar guías propias?
3. **Idioma**: casi todos los recursos de MFT y valores están en inglés. ¿Modelos multilingües directo, traducir, o buscar recursos en francés?
4. **Alcance**: si el tiempo se aprieta, priorizar valores y postura sobre dos fuentes (una fácil, manifiestos o hemiciclo, y Twitter como caso difícil), con el audiovisual como parte exploratoria. ¿Le parece?

Anotar aquí las respuestas cuando lleguen.

---

## 9. Notas de factibilidad y riesgos

- **Cuello de botella**: la anotación manual, no correr los modelos. Hay que escribir guías, anotar cientos de ejemplos por tarea y fuente e, idealmente, tener un segundo anotador.
- **Idioma**: los datos están en francés y la mayoría de los recursos de MFT y Schwartz están en inglés. Eso agrega transferencia entre idiomas encima de la transferencia de dominio.
- **Twitter**: ironía, hilos y contexto implícito hacen que un modelo entrenado en texto formal falle. Ahí es donde se espera la caída de desempeño y el hallazgo más interesante.
- **Audiovisual**: alta incertidumbre (formato, cobertura y fecha de entrega desconocidos).
- **Alcance completo**: cuatro tareas por varias fuentes por varios modelos es demasiado para 6 meses. Hay que recortar por tarea y por fuente (ver pregunta 4 del §8).
- **Pista para revisar primero**: la tarea compartida SemEval-2023 Task 4 (ValueEval, Touché) trata de detectar valores humanos de Schwartz detrás de argumentos, lo que calza con "argumentos con postura y valores". Por verificar en la revisión de literatura.
- **Recursos MFT a revisar** (por verificar): Moral Foundations Dictionary, Moral Foundations Twitter Corpus y modelos entrenados sobre ellos.

---

## 10. Próximos pasos

**Pendiente ahora (Seminario de Tesis I, cierre):**

1. Entrega 3, avance del manuscrito (plazo 3-dic-2026, 23:59, 1 PDF): portada y secciones enunciadas como mínimo, más los borradores que haya. Se escribe en `manuscrito/` (LaTeX, plantilla `umemoria` con `\tesis{Magíster en Ciencia de Datos}`) y se sube a Overleaf. Detalle en `seminario_1/entrega_3_avance_manuscrito/README.md`.
2. Presentación 2, avance de tesis (subir 1 archivo hasta el 3-dic-2026; presentación presencial entre el 7 y el 11-dic-2026). Carpeta `seminario_1/presentacion_2_avance_tesis/`.
3. Definir con Valentin qué datos del proyecto INA se pueden conseguir y qué temas propone (`proyecto_ina/`).
4. Crear el repo nuevo de GitHub para el magíster y el repo del manuscrito para Overleaf (ver `README.md` de la raíz del repo).

**Hecho (registro):**

1. Presentación 1 (plazo 27-sep), presentada en la semana 8 (28-sep al 2-oct, presencial, unos 7 minutos). Archivo: `seminario_1/presentacion_1_propuesta_tema/presentacion_1_propuesta_tema.pptx`, generado con `build_ppt.py` en la misma carpeta (se regenera con `~/.venvs/pptx/bin/python build_ppt.py`; el PDF y `preview/` salen con LibreOffice y pypdfium2). Orden: portada, motivación y problema, datos disponibles, antecedentes, objetivos, metodología, cierre. Contenido pedido por el curso: nombre del tema, profesores, antecedentes, objetivos, metodología y datos disponibles. Los objetivos de la presentación ya incorporan la definición de Valentin (argumentos, postura, valores MFT y Schwartz, emociones en audiovisual).
2. Revisión de literatura en ACL Anthology usando el repo de Valentin: https://github.com/valbarriere/ACL_anthology/tree/master. Palabras clave: moral foundations, Schwartz values, human value detection, stance detection, argument mining, political text, French, emotion recognition speech.
3. Hacer un inventario de modelos y datasets candidatos por tarea (argumentos, postura, MFT, Schwartz, emociones).
4. Entrega 2 (inscripción, 6-oct): dos archivos. (a) Formulario `inscripcion_tema_de_tesis_agustin_solis.xls`, que Agustín llena a mano. (b) Informe de 3 a 5 páginas firmado por guía y co-guía, en PDF, con nombre `AGUSTIN_SOLIS.pdf`. Sigue la plantilla oficial `plantillas/formato_inscripcion_tema_de_tesis_mds.docx` (máximo 5 páginas). El texto fuente es `seminario_1/entrega_2_inscripcion_tema/propuesta_tesis.md`, el PDF entregado es `informe_inscripcion_agustin_solis.pdf` y la versión llenada de la plantilla era `AGUSTIN_SOLIS.docx` (5 páginas, el PDF lo saca Agustín). Escrito como propuesta de tesis, en prosa, con foco en ciencia de datos. Secciones de la plantilla: Antecedentes (incluye los conceptos teóricos), Objetivos (general y 7 específicos), Metodología (seis etapas, con variables y métricas), Resultados esperados, Plan de trabajo (tabla tipo Gantt oct-2026 a jul-2027), Resultados preliminares, Bibliografía (5 referencias) y firmas. **Excepción a la regla del §1, autorizada por Agustín:** en Resultados preliminares sí se presentan como avance la cohorte de diputados (668, 587 con Twitter), la recolección de Twitter (533 cuentas, 244.244 publicaciones, 170.217 únicas) y los manifiestos 2017 del Manifesto Project (10, 3.801 cuasi-frases); el resto sigue en futuro. Hay dos focos que deben quedar explícitos: (a) estudiar los datos y determinar qué modelos sirven y cuáles no en cada fuente; en lo audiovisual esto se decide según cómo vengan los datos del INA, que primero se caracterizan; (b) estudiar el discurso y el voto de los partidos primero por separado, y después compararlos para buscar discrepancias. Es la base para ir ajustando la propuesta durante el curso.

**Preferencias de formato para entregables escritos:** solo markdown, sin generar PDF, Word ni imágenes de vista previa salvo que se pida (es trabajo extra). Ajustarse estrictamente a lo que pide cada entrega.

---

## 11. Estilo para mensajes al profesor

- Español informal, directo, en el tono de siempre ("Hola Profe, como esta?").
- Mensajes cortos y compactos, sin rayas largas (—) y que suenen naturales.
- Preguntas concretas, ordenadas de la más simple a la más estratégica.

---

## 12. Historial

| Fecha | Evento |
|---|---|
| 28-ago-2026 | Huddle con Valentin: pidió un plan de tesis con marco temporal, datos, fenómenos a extraer del audiovisual y plazos. Compartió los links de INA le lab |
| 1-sep-2026 | Entrega 1 (propuesta de tema) subida al seminario. Enviado el plan a Valentin |
| 7-sep-2026 | Feedback del seminario: el tema no queda claro. Pregunta a Valentin sobre qué análisis sería |
| 14-sep-2026 | Respuesta de Valentin (§5). Enviadas las preguntas del §8 |
| 27-sep-2026 | Se crea este documento. Se genera la Presentación 1 (7 slides, unos 7 min; se quitó la slide de plan de trabajo) |
| 6-oct-2026 | Se escribe el informe de la Entrega 2 en `propuesta_tesis.md` (5 referencias). Se descarta un borrador anterior por quedar muy parecido a la presentación. Luego aparece la plantilla oficial y se adapta a ella: `AGUSTIN_SOLIS.docx`, 5 páginas, con plan de trabajo y resultados preliminares |
| 13-oct-2026 | Taller de escritura, sesión 1: clínica del plan de investigación (`seminario_1/taller_escritura/`) |
| 16-nov-2026 | Defensa de la memoria de Ingeniería Civil en Computación, aprobada. Desde aquí el foco es solo el magíster |
| 24-nov-2026 | Se reordena la carpeta `Tesis/`: un repo por grado, contexto propio para el magíster, seminario ordenado por entrega y esqueleto del manuscrito |
