# Context — hub de contexto de la tesis de Magíster (MDS)

Reúne todo el contexto de la tesis de Magíster en Ciencia de Datos en un solo lugar. Sirve para retomar el trabajo, pasarle contexto a otro chat/IA o entender el proyecto de cero.

> **Regla de encuadre (leer siempre primero):** en todo lo que se escriba para el MDS (propuesta, manuscrito, presentaciones), el trabajo de datos y análisis se presenta como parte de **esta** tesis. No se menciona la memoria de Ingeniería Civil ni se presenta nada como "ya hecho". Detalle en el §1 de `1_contexto_tesis_magister.md`.

## Por dónde empezar

1. **`1_contexto_tesis_magister.md`**: el documento principal. Encuadre, datos básicos (guías, programa, proyecto INA), análisis que pide Valentin, alcance, plazos del seminario, preguntas abiertas, riesgos, próximos pasos e historial.
2. **`0_como_trabajo/preferencias_y_estilo.md`**: cómo trabajo y cómo me gusta que me ayuden (tono, convenciones LaTeX, formato de entregables).
3. **`2_pipeline_datos_y_analisis/`**: detalle técnico de cada módulo de `french_deputies/` (datos, métodos, cifras), en orden del pipeline.

## `2_pipeline_datos_y_analisis/`

| Archivo | Módulo (`french_deputies/…`) | Qué cubre |
|---|---|---|
| `0_proyecto_completo.md` | todo | Síntesis integradora: arquitectura del pipeline, corpus, métodos, resultados y limitaciones |
| `1_datos_diputados.md` | `datos_diputados/` | Cohorte de 668 diputados (ancla de identidad) |
| `2_manifiestos.md` | `manifestos/` | Programas electorales 2017 (MARPOR) |
| `3_twitter.md` | `twitter_zeeschuimer/` | Captura de tuits con Zeeschuimer y cruce con la cohorte |
| `4_hemiciclo.md` | `hemicycle/` | Intervenciones en el hemiciclo (Regards Citoyens) |
| `5_leyes_y_votos.md` | `lois_votes/` | Leyes, enmiendas y votos por diputado |
| `6_bertopic.md` | `bertopic_analysis/` | Topic modeling no supervisado |
| `7_manifestoberta.md` | `manifestoberta_analysis/` | Clasificación supervisada MARPOR |
| `8_validacion_ches.md` | `ches_analysis/` | Validación RILE vs CHES 2019 |
| `9_party_analysis.md` | `party_analysis/` | Agenda declarada, revelada y el cruce |

> Estos documentos técnicos (y `0_como_trabajo/`) vienen del hub de la memoria (`../1_Memoria_Ing_Civil/Context/`) y citan rutas como `memoria/…`. Son notas internas de trabajo: sirven para cifras y decisiones del pipeline, **no** para copiar su encuadre al manuscrito del MDS. Si una cifra cambia en el magíster, se actualiza aquí y no en la copia de la memoria.
