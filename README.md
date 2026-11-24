# Tesis de Magíster en Ciencia de Datos — Discurso político y voto parlamentario (Asamblea Nacional francesa, 2017-2022)

**Tema:** Análisis multimodal del discurso político y su relación con el voto parlamentario: postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa).

| | |
|---|---|
| Estudiante | Agustín Sebastián Solís Meza |
| Programa | Magíster en Ciencia de Datos (MDS), Universidad de Chile |
| Profesor guía | Valentin Clement Barriere |
| Profesora co-guía | Franziska Christl Wagner |
| Proyecto asociado | PAROLES ET ACTES (INA le lab 2026-2027) |
| Curso actual | Seminario de Tesis I, IA7305-1, Primavera 2026 |

La tesis integra programas electorales, Twitter, intervenciones parlamentarias, leyes, enmiendas, votaciones nominales y material audiovisual del INA para extraer temas, argumentos, posturas, valores (MFT y Schwartz) y emociones; evaluar qué modelos existentes funcionan en cada fuente; y comparar el discurso de partidos y diputados con su voto.

## Estructura

```
2_Tesis_Magister_MDS/
├── README.md                  ← estás aquí
├── REFERENCIAS.md             ← papers, modelos y recursos, con su rol en la tesis
├── Context/                   ← hub de contexto (empezar por Context/README.md)
├── seminario_1/               ← Seminario de Tesis I, una carpeta por entrega
├── proyecto_INA/              ← proyecto PAROLES ET ACTES y datos audiovisuales
├── french_deputies/           ← pipeline de datos y análisis (código, READMEs, datos livianos)
└── manuscrito/                ← (repo aparte, ignorado aquí) LaTeX de la tesis, sincronizado con Overleaf
```

## Pipeline `french_deputies/`

| Carpeta | Qué hace |
|---|---|
| `datos_diputados/` | Cohorte de 668 diputados de la XV legislatura enlazada con Twitter |
| `manifestos/` | Programas electorales 2017 (Manifesto Project) |
| `twitter_zeeschuimer/` | Recolección de tuits con Zeeschuimer |
| `hemicycle/` | Intervenciones en el hemiciclo (Regards Citoyens) |
| `lois_votes/` | Leyes, enmiendas y votaciones nominales |
| `bertopic_analysis/` | Modelado de tópicos exploratorio |
| `manifestoberta_analysis/` | Clasificación MARPOR (56 categorías) |
| `ches_analysis/` | Validación contra CHES 2019 |
| `party_analysis/` | Agenda declarada, revelada y su cruce |
| `kg-gen/` | Prueba de extracción de grafos de conocimiento |

Detalle en [`french_deputies/README.md`](french_deputies/README.md) y en [`Context/2_pipeline_datos_y_analisis/`](Context/2_pipeline_datos_y_analisis/). Los datos pesados (capturas, JSON crudos, resultados de modelos) no se versionan; se regeneran con los scripts (ver `.gitignore`). Las credenciales de `lois_votes/.env` tampoco.

## Primer push a GitHub

El repo ya está inicializado con un primer commit. Para publicarlo:

1. Crear en GitHub un repo vacío y **privado** (por ejemplo `TinSolis/tesis-mds-discurso-voto`), sin README ni `.gitignore`.
2. Desde esta carpeta:
   ```
   git remote add origin git@github.com:TinSolis/tesis-mds-discurso-voto.git
   git push -u origin main
   ```

El manuscrito tiene su propio repo: ver [`manuscrito/README.md`](manuscrito/README.md).
