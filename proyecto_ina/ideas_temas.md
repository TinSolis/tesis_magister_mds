Idées 

La base (INA a deja ce qu’il faut): 
Transcripts avec le paralinguistics: Crisper
Simple speaker diarization: pyannote
Audiovisual speaker diarization? Pour associer un visage à chaque speaker? Pour mieux diariser? 

Propositions d’extractions supplementaires:  
Prosodie et qualité de voix: openSMILE, eGeMAPS
Non-semantic speech embedding type BYOL-A
Expressions faciales et gestes: OpenFace (AUs, head pose, gaze)
Squelettes: MediaPipe
Scenes: Pyscene (permet de savoir quand on change de plan)
Emotions (Arousal, valence, dominance; a priori plus précis pour debats politiques): audeering wav2vec2  
Autres? Pourrait-on avoir l’ironie/sarcasme, indignation, condescendance. Via un LLM? 

Problemes que l’on pourra rencontrer pour associer le speaker a son ID apres diarisation: 
Comment retrouver le député en question? 
Idée: faire une diarization, 
utiliser des samples identifiés avec sa voix, et faire un matching dans la conversation
Resultats-POC de David D. → Threshold 0.5 Rappel de .894, Precision de 0.850; 0.6 Rappel de 0.846 Precision de 0.902
 Superposition de parole? 

https://www.cepremap.fr/depot/2025/01/2025-01-Fievre-Parlementaire.pdf
mauvais “article” de Yann Algan, mais si 

données dispo :

Arthur Lezer
Arthur Lezer
2:39 PM Nov 16
je connaissais pas mais je note ! pas vu d'info sur les perfs en français mais je vais creuser
Arthur Lezer
Arthur Lezer
2:53 PM Nov 16
on peut avoir facilement
Val Barriere
Val Barriere
5:05 PM Nov 12
https://www.alphaxiv.org/abs/2509.15476v1
Val Barriere
Val Barriere
5:23 PM Nov 12
En gros pour le pas avoir un rappel ridicule (et jeter tous les exemples), il faut se placer au moins à un threshold de 0.2 ou 0.3 voir 0.4
Soyons prudents, disons 0.2

Ca voudrait dire qu'on ne peut retrouver les locuteurs que pour 23% des archives.
Ca voudrait dire aussi que 6% des locuteurs trouvés seraient des erreurs.
Semble ok en cas d'intervention manuelle, pas ok si besoin d'un cadre full automatique

Des méthodes où on présente manuellement des exemples des locuteurs cibles seraient plus préférables.
C'est du boulot, mais sachant qu'on l'a fait pour 2000, c'est rentable si on a de bonnes raisons de vouloir le faire

0.0 nan 0.0
0.1 1.0 0.043227665706051875
0.2 0.9418604651162791 0.2334293948126801
0.3 0.9259259259259259 0.4322766570605187
0.4 0.9227941176470589 0.723342939481268
0.5 0.8939393939393939 0.8501440922190202
0.6 0.845945945945946 0.9020172910662824
0.7 0.8121827411167513 0.9221902017291066
0.8 0.8121827411167513 0.9221902017291066
0.9 0.8121827411167513 0.9221902017291066