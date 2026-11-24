# Proyecto INA — PAROLES ET ACTES

«PAROLES ET ACTES: Cross-Modal Analysis of Political Rhetoric and Parliamentary Voting Using Audiovisual Archives», proyecto de INA le lab 2026-2027 dirigido por Valentin Barriere. Da acceso a archivos audiovisuales del Institut national de l'audiovisuel (INA, no INRIA).

- Lista de laureados: https://inalelab.hypotheses.org/10701
- Convocatoria (datos y herramientas: transcripciones Whisper de noticieros TV/radio desde 2011, ~497 M de tuits 2014-2023, análisis de rostro y voz): https://inalelab.hypotheses.org/10344

Los datos llegarían a fin de 2026. Hasta entonces se avanza con los datos de texto.

| Archivo | Qué es |
|---|---|
| `ideas_temas.md` | Notas del equipo (Valentin Barriere, Arthur Lezer), en francés, sobre qué extraer de los archivos del INA: transcripciones con paralingüística (Crisper), diarización (pyannote), prosodia (openSMILE, eGeMAPS), embeddings de voz (BYOL-A), expresiones faciales (OpenFace), esqueletos (MediaPipe), cambios de plano (PySceneDetect), emociones (wav2vec2 de audEERING), y el problema de identificar a cada diputado después de diarizar (umbrales de precisión y recall del POC) |
