# Tesis de Magíster en Ciencia de Datos

*Análisis multimodal del discurso político y su relación con el voto parlamentario: postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa).*

En este repo está el desarrollo de mi tesis del Magíster en Ciencia de Datos de la Universidad de Chile: los datos, el código de análisis, mis notas de trabajo y las entregas del Seminario de Tesis I. El manuscrito lo escribo en LaTeX en otro repo, [tesis_magister_mds_manuscrito](https://github.com/TinSolis/tesis_magister_mds_manuscrito), que tengo sincronizado con Overleaf.

Mi profesor guía es Valentin Barriere y mi profesora co-guía es Franziska Wagner. La tesis está asociada al proyecto PAROLES ET ACTES de INA le lab (2026-2027).

## De qué se trata

Quiero estudiar si lo que dicen los partidos y los diputados de la Asamblea Nacional francesa (XV legislatura, 2017-2022) se refleja en cómo votan. Para eso uso programas electorales, tuits, intervenciones en el hemiciclo, leyes, enmiendas y votaciones nominales, y más adelante el material audiovisual del INA. Sobre esos datos extraigo temas, argumentos, posturas, valores (MFT y Schwartz) y emociones, evalúo qué modelos funcionan bien en cada fuente y comparo el discurso de cada partido con su voto.

## Cómo está organizado

- `contexto/`: mis notas para retomar el trabajo. Siempre parto por `contexto/contexto_general.md`.
- `seminario_1/`: una carpeta por cada entrega del Seminario de Tesis I (IA7305-1, Primavera 2026).
- `proyecto_ina/`: lo del proyecto con el INA y las ideas de análisis audiovisual que hemos ido conversando con el equipo.
- `french_deputies/`: el pipeline de datos y análisis.
- `manuscrito/`: mi clon local del repo del manuscrito. Este repo lo ignora.
- `archivo/`: respaldos locales, que tampoco se suben.

## El pipeline

`french_deputies/` tiene una carpeta por fuente de datos y otra por cada análisis:

| Carpeta | Qué hay |
|---|---|
| `datos_diputados/` | Los 668 diputados de la XV legislatura, enlazados con sus cuentas de Twitter |
| `manifestos/` | Programas electorales de 2017 (Manifesto Project) |
| `twitter_zeeschuimer/` | Tuits que recolecté con Zeeschuimer |
| `hemicycle/` | Intervenciones en el hemiciclo (Regards Citoyens) |
| `lois_votes/` | Leyes, enmiendas y votaciones nominales |
| `bertopic_analysis/` | Modelado de tópicos exploratorio |
| `manifestoberta_analysis/` | Clasificación en las 56 categorías MARPOR |
| `ches_analysis/` | Validación contra CHES 2019 |
| `party_analysis/` | Agenda declarada, agenda revelada y el cruce entre ambas |
| `kg_gen/` | Prueba de extracción de grafos de conocimiento |

Cada carpeta tiene su README, y en [`french_deputies/README.md`](french_deputies/README.md) explico cómo se conectan entre sí. Los datos pesados (capturas, JSON crudos, resultados de modelos) no están en el repo porque se regeneran con los scripts. Las credenciales de `lois_votes/.env` tampoco.
