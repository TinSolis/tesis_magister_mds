# contexto — hub de contexto de la tesis de Magíster (MDS)

Reúne todo el contexto de la tesis de Magíster en Ciencia de Datos en un solo lugar. Sirve para retomar el trabajo, pasarle contexto a otro chat/IA o entender el proyecto de cero.

> **Regla de encuadre (leer siempre primero):** en todo lo que se escriba para el MDS (propuesta, manuscrito, presentaciones), el trabajo de datos y análisis se presenta como parte de **esta** tesis. No se menciona la memoria de Ingeniería Civil ni se presenta nada como "ya hecho". Detalle en el §1 de `contexto_general.md`.

## Estructura (igual en la memoria y en el magíster)

| Archivo o carpeta | Qué es |
|---|---|
| `README.md` | Este índice |
| `contexto_general.md` | **Empezar aquí.** Documento principal y vivo: encuadre, datos básicos (guías, programa, proyecto INA), análisis que pide Valentin, alcance, plazos del seminario, preguntas abiertas, riesgos, próximos pasos e historial |
| `preferencias_y_estilo.md` | Cómo trabajo y cómo me gusta que me ayuden (tono, convenciones LaTeX, formato de entregables) |
| `referencias.md` | Papers, modelos y recursos, con el rol que cumple cada uno en la tesis |
| `pipeline/` | Detalle técnico de cada módulo de `french_deputies/` (datos, métodos, cifras), en orden del pipeline |

### `pipeline/`

| Archivo | Módulo (`french_deputies/…`) | Qué cubre |
|---|---|---|
| `00_resumen_pipeline.md` | todo | Síntesis integradora: arquitectura del pipeline, corpus, métodos, resultados y limitaciones |
| `01_datos_diputados.md` | `datos_diputados/` | Cohorte de 668 diputados (ancla de identidad) |
| `02_manifiestos.md` | `manifestos/` | Programas electorales 2017 (MARPOR) |
| `03_twitter.md` | `twitter_zeeschuimer/` | Captura de tuits con Zeeschuimer y cruce con la cohorte |
| `04_hemiciclo.md` | `hemicycle/` | Intervenciones en el hemiciclo (Regards Citoyens) |
| `05_leyes_y_votos.md` | `lois_votes/` | Leyes, enmiendas y votos por diputado |
| `06_bertopic.md` | `bertopic_analysis/` | Topic modeling no supervisado |
| `07_manifestoberta.md` | `manifestoberta_analysis/` | Clasificación supervisada MARPOR |
| `08_validacion_ches.md` | `ches_analysis/` | Validación RILE vs CHES 2019 |
| `09_party_analysis.md` | `party_analysis/` | Agenda declarada, revelada y el cruce |

> Los documentos de `pipeline/` y `preferencias_y_estilo.md` parten de una copia del hub de la memoria (`../memoria_ing_civil/contexto/`) y a veces citan rutas viejas como `memoria/…`, `REFERENCIAS.md` o `kg-gen/`; las equivalencias están en `../memoria_ing_civil/contexto/README.md`. Son notas internas de trabajo: sirven para cifras y decisiones del pipeline, **no** para copiar su encuadre al manuscrito del MDS. Si una cifra cambia en el magíster, se actualiza aquí y no en la copia de la memoria.
