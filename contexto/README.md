# contexto

Aquí guardo mis notas de trabajo de la tesis. Las uso para retomar después de un tiempo sin tocarla o para darle contexto a quien me esté ayudando, sea una persona o una IA.

- `contexto_general.md` es el documento principal y el que voy actualizando. Tiene el encuadre, los datos básicos, lo que me pidió Valentin, el alcance, los plazos del seminario, las preguntas abiertas, los riesgos, los próximos pasos y un historial.
- `preferencias_y_estilo.md` explica cómo trabajo y cómo me gusta que me ayuden.
- `referencias.md` tiene los papers, modelos y recursos, y para qué uso cada uno.
- `pipeline/` tiene una nota técnica por módulo de `french_deputies/`, en el orden del pipeline.

Una regla que sigo en todo lo que escribo para el magíster (propuesta, manuscrito, presentaciones) es presentar el trabajo de datos y análisis como parte de esta tesis. La explico en el §1 de `contexto_general.md`.

## pipeline/

| Archivo | Módulo | De qué trata |
|---|---|---|
| `00_resumen_pipeline.md` | todos | Resumen del pipeline completo: corpus, métodos, resultados y limitaciones |
| `01_datos_diputados.md` | `datos_diputados/` | Los 668 diputados, que son la base para enlazar todo lo demás |
| `02_manifiestos.md` | `manifestos/` | Programas electorales 2017 (MARPOR) |
| `03_twitter.md` | `twitter_zeeschuimer/` | Captura de tuits con Zeeschuimer y cruce con los diputados |
| `04_hemiciclo.md` | `hemicycle/` | Intervenciones en el hemiciclo (Regards Citoyens) |
| `05_leyes_y_votos.md` | `lois_votes/` | Leyes, enmiendas y votos por diputado |
| `06_bertopic.md` | `bertopic_analysis/` | Topic modeling no supervisado |
| `07_manifestoberta.md` | `manifestoberta_analysis/` | Clasificación supervisada MARPOR |
| `08_validacion_ches.md` | `ches_analysis/` | Validación RILE contra CHES 2019 |
| `09_party_analysis.md` | `party_analysis/` | Agenda declarada, revelada y el cruce |

Algunas de estas notas las escribí antes de ordenar las carpetas y todavía citan rutas antiguas, como `kg-gen/` (hoy `kg_gen/`) o `REFERENCIAS.md` (hoy `referencias.md`). Las cifras y las decisiones siguen valiendo. Si una cifra cambia, la actualizo aquí.
