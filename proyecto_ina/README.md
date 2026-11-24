# Proyecto INA: PAROLES ET ACTES

*PAROLES ET ACTES: Cross-Modal Analysis of Political Rhetoric and Parliamentary Voting Using Audiovisual Archives* es un proyecto de INA le lab (2026-2027) que dirige Valentin. Nos da acceso a los archivos audiovisuales del Institut national de l'audiovisuel (INA), que son la parte multimodal de la tesis.

- Lista de proyectos seleccionados: https://inalelab.hypotheses.org/10701
- Convocatoria, con los datos y herramientas disponibles (transcripciones Whisper de noticieros de TV y radio desde 2011, unos 497 millones de tuits de 2014 a 2023, análisis de rostro y voz): https://inalelab.hypotheses.org/10344

Los datos deberían llegar a fines de 2026. Mientras tanto sigo avanzando con los datos de texto.

En `ideas_temas.md` tengo las notas que hemos ido juntando con Valentin y Arthur Lezer, en francés, sobre qué extraer de los archivos. Por ejemplo:

- transcripciones con paralingüística (Crisper) y diarización (pyannote)
- prosodia (openSMILE, eGeMAPS) y embeddings de voz (BYOL-A)
- expresiones faciales (OpenFace), esqueletos (MediaPipe) y cambios de plano (PySceneDetect)
- emociones con el wav2vec2 de audEERING

También está el problema de reconocer a cada diputado después de diarizar, con los umbrales de precisión y recall de la prueba de concepto.
