"""Genera la Presentación 1 (Propuesta de Tema de Tesis) del Seminario de Tesis I.

Uso: python build_ppt.py  ->  Presentacion1_Propuesta_Tema.pptx
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

OUT = Path(__file__).with_name("Presentacion1_Propuesta_Tema.pptx")

AZUL = RGBColor(0x1F, 0x38, 0x64)
ACENTO = RGBColor(0x2E, 0x75, 0xB6)
GRIS = RGBColor(0x40, 0x40, 0x40)
CLARO = RGBColor(0xE8, 0xEF, 0xF7)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
TOTAL = 7


def texto(slide, x, y, w, h, lineas, size=20, color=GRIS, bold=False,
          align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, linea in enumerate(lineas if isinstance(lineas, list) else [lineas]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run()
        run.text = linea
        run.font.size = Pt(size)
        run.font.color.rgb = color
        run.font.bold = bold
    return box


def viñetas(slide, x, y, w, h, items, size=20, espacio=10):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        nivel = 1 if item.startswith("  ") else 0
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(espacio)
        run = p.add_run()
        run.text = ("•  " if nivel == 0 else "–  ") + item.strip()
        run.font.size = Pt(size - 2 * nivel)
        run.font.color.rgb = GRIS
        if nivel:
            p.level = 1
    return box


def slide_base(titulo, n, notas):
    s = prs.slides.add_slide(BLANK)
    barra = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.15))
    barra.fill.solid()
    barra.fill.fore_color.rgb = AZUL
    barra.line.fill.background()
    texto(s, 0.6, 0.18, 12, 0.8, titulo, size=30, color=BLANCO, bold=True,
          anchor=MSO_ANCHOR.MIDDLE)
    texto(s, 11.8, 6.95, 1.2, 0.4, f"{n}/{TOTAL}", size=12, align=PP_ALIGN.RIGHT)
    s.notes_slide.notes_text_frame.text = notas
    return s


def tabla(slide, filas, x, y, w, h, anchos, size=14, destacar_col0=False):
    t = slide.shapes.add_table(len(filas), len(filas[0]), Inches(x), Inches(y),
                               Inches(w), Inches(h)).table
    for j, ancho_col in enumerate(anchos):
        t.columns[j].width = Inches(ancho_col)
    for i, fila in enumerate(filas):
        for j, valor in enumerate(fila):
            c = t.cell(i, j)
            c.text = valor
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid()
            c.fill.fore_color.rgb = AZUL if i == 0 else (CLARO if i % 2 else BLANCO)
            for par in c.text_frame.paragraphs:
                for run in par.runs:
                    run.font.size = Pt(size)
                    run.font.bold = i == 0 or (destacar_col0 and j == 0)
                    if i == 0:
                        run.font.color.rgb = BLANCO
                    elif destacar_col0 and j == 0:
                        run.font.color.rgb = AZUL
                    else:
                        run.font.color.rgb = GRIS
    return t


def caja(slide, x, y, w, h, titulo, cuerpo, fill=CLARO, size_t=16, size_b=13,
         anchor=MSO_ANCHOR.TOP, con_viñetas=False):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y),
                                 Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = ACENTO
    tf = shp.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(6)
    r = p.add_run()
    r.text = titulo
    r.font.size = Pt(size_t)
    r.font.bold = True
    r.font.color.rgb = AZUL
    for linea in cuerpo:
        q = tf.add_paragraph()
        q.alignment = PP_ALIGN.LEFT if con_viñetas else PP_ALIGN.CENTER
        q.space_after = Pt(8 if con_viñetas else 4)
        rr = q.add_run()
        rr.text = ("•  " + linea) if con_viñetas else linea
        rr.font.size = Pt(size_b)
        rr.font.color.rgb = GRIS
    return shp


# 1. Portada
s = prs.slides.add_slide(BLANK)
fondo = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(4.2))
fondo.fill.solid()
fondo.fill.fore_color.rgb = AZUL
fondo.line.fill.background()
texto(s, 0.8, 0.8, 11.7, 1.8,
      "Análisis multimodal del discurso político y su relación con el voto parlamentario",
      size=32, color=BLANCO, bold=True)
texto(s, 0.8, 2.75, 11.7, 1.2,
      "Postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa)",
      size=22, color=BLANCO)
texto(s, 0.8, 4.6, 11.7, 2.4,
      ["Agustín Sebastián Solís Meza",
       "Profesor guía: Valentin Clement Barriere",
       "Profesora co-guía: Franziska Christl Wagner",
       "Magíster en Ciencia de Datos · Seminario de Tesis I (IA7305-1) · Primavera 2026"],
      size=20)
s.notes_slide.notes_text_frame.text = (
    "(20 s) Presentarse, el tema y los profesores. Mencionar que se trabaja con "
    "el DCC y CENIA, en relación con el proyecto PAROLES ET ACTES del INA.")

# 2. Motivación y problema
s = slide_base("Motivación y problema", 2,
               "(1 min) Idea central: los partidos hablan por muchos canales y votan en el "
               "parlamento, pero eso se estudia por separado. Saber el tema no basta: "
               "interesa la postura, los valores y cómo se dice. Cerrar con la pregunta.")
viñetas(s, 0.8, 1.6, 11.8, 3.6, [
    "Los partidos comunican sus posiciones por muchos canales: programas electorales, "
    "redes sociales, debate parlamentario y medios audiovisuales.",
    "Estos canales suelen estudiarse por separado, lo que dificulta compararlos con "
    "lo que los representantes votan.",
    "Saber de qué tema habla un partido no dice qué postura adopta, qué valores "
    "defiende ni con qué emoción lo comunica.",
], size=22)
q = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.3),
                       Inches(11.8), Inches(1.3))
q.fill.solid()
q.fill.fore_color.rgb = CLARO
q.line.color.rgb = ACENTO
tf = q.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.CENTER
r = p.add_run()
r.text = ("Pregunta: ¿lo que los partidos y diputados expresan en su discurso "
          "coincide con lo que votan en el parlamento?")
r.font.size = Pt(22)
r.font.bold = True
r.font.color.rgb = AZUL

# 3. Datos disponibles
s = slide_base("Datos disponibles", 3,
               "(1 min) Recorrer la tabla rápido. Todo se enlaza con la misma cohorte de "
               "diputados de la XV legislatura (2017-2022). Los datos audiovisuales del INA "
               "llegan vía el proyecto PAROLES ET ACTES y se incorporarán cuando estén "
               "disponibles, previsto hacia fin de 2026.")
filas = [
    ("Fuente", "Contenido", "Origen"),
    ("Diputados XV legislatura (2017-2022)", "Identidad, grupo parlamentario y cuenta de Twitter",
     "Open data Asamblea Nacional, Regards Citoyens"),
    ("Programas electorales 2017", "Textos codificados por expertos (MARPOR)",
     "API del Manifesto Project"),
    ("Twitter", "Publicaciones de los diputados", "Recolección con Zeeschuimer"),
    ("Intervenciones en el hemiciclo", "Turnos de palabra en sesión", "Regards Citoyens"),
    ("Leyes, enmiendas y votaciones", "Texto oficial y voto nominal por diputado",
     "Open data Asamblea Nacional, Légifrance"),
    ("Material audiovisual", "Televisión y radio con transcripciones",
     "INA, vía PAROLES ET ACTES"),
    ("Referencia de expertos", "Posiciones de los partidos", "Chapel Hill Expert Survey 2019"),
]
tabla(s, filas, 0.6, 1.45, 12.1, 5.3, (3.9, 4.6, 3.6))

# 4. Antecedentes
s = slide_base("Antecedentes", 4,
               "(1 min 15 s) Recorrer la tabla fila por fila: qué es cada enfoque y para qué "
               "se usa. Remarcar que valores (MFT y Schwartz) es lo más novedoso porque hay "
               "pocos trabajos, sobre todo en francés.")
tabla(s, [
    ("Enfoque", "Qué es", "Para qué se usa en la tesis"),
    ("Temas (MARPOR)",
     "Clasificación del texto en 56 categorías temáticas del Manifesto Project, "
     "con modelos como ManifestoBERTa",
     "Saber de qué habla cada partido en cada fuente"),
    ("Extracción de argumentos",
     "Identificar dentro de un texto qué se afirma y con qué justificación",
     "Separar qué propone cada partido y por qué lo propone"),
    ("Postura (stance)",
     "Determinar si un texto está a favor o en contra de un tema",
     "Comparar la dirección del discurso con la dirección del voto"),
    ("Valores",
     "Marcos que describen los principios morales detrás de un argumento, como "
     "cuidado, justicia, autoridad, seguridad o tradición",
     "Ver con qué valores justifica cada partido sus posiciones"),
    ("Emociones",
     "Reconocimiento de emociones en la voz y la imagen",
     "Analizar cómo se comunica en televisión y radio"),
], 0.6, 1.45, 12.1, 5.1, (2.9, 5.2, 4.0), size=15, destacar_col0=True)

# 5. Objetivos
s = slide_base("Objetivos", 5,
               "(1 min 30 s) Leer el general y resumir los específicos en tres bloques: "
               "construir los datos, analizar el discurso (temas, argumentos, postura, "
               "valores, emociones) y evaluar los modelos y compararlos con el voto.")
caja(s, 0.8, 1.45, 11.8, 1.3, "Objetivo general",
     ["Desarrollar y evaluar una metodología multimodal para analizar el discurso político "
      "francés (temas, argumentos, postura, valores y emociones) y estudiar su relación "
      "con el voto parlamentario de partidos y diputados."],
     size_t=18, size_b=16, anchor=MSO_ANCHOR.MIDDLE)
texto(s, 0.8, 2.9, 11.8, 0.5, "Objetivos específicos", size=20, color=AZUL, bold=True)
viñetas(s, 0.8, 3.4, 11.8, 3.6, [
    "Construir una base integrada de diputados, programas electorales, Twitter, "
    "intervenciones parlamentarias, leyes, enmiendas, votaciones y material audiovisual.",
    "Clasificar los temas presentes en cada fuente.",
    "Extraer argumentos e identificar su postura y los valores que expresan (MFT y Schwartz).",
    "Analizar las emociones en el material audiovisual.",
    "Evaluar si los modelos existentes se adaptan a cada fuente mediante datos anotados a mano.",
    "Comparar el discurso con las votaciones y analizar diferencias entre partidos y canales.",
], size=17, espacio=6)

# 6. Metodología
s = slide_base("Metodología", 6,
               "(1 min 30 s) Explicar el flujo de izquierda a derecha. Remarcar que la parte "
               "clave es la evaluación: verificar si los modelos existentes funcionan en cada "
               "fuente. Manifiestos y hemiciclo son texto estructurado; Twitter es más "
               "contextual y requiere más validación.")
pasos = [
    ("1. Recolección e integración",
     ["Reunir programas, tuits, intervenciones, leyes, votos y audiovisual del INA",
      "Enlazar todo a una misma cohorte de diputados y partidos"]),
    ("2. Análisis de texto",
     ["Clasificar el tema de cada texto (MARPOR)",
      "Extraer argumentos y su postura",
      "Identificar los valores (MFT y Schwartz)"]),
    ("3. Análisis audiovisual",
     ["Transcribir lo que se dice",
      "Reconocer emociones en la voz y la imagen"]),
    ("4. Evaluación de modelos",
     ["Revisión y clasificación de muestras de cada fuente",
      "Medir si los modelos existentes funcionan en cada fuente"]),
    ("5. Discurso y voto",
     ["Comparar lo que dice cada partido con cómo vota",
      "Ver coincidencias y diferencias por tema y canal"]),
]
ancho, sep, x0 = 2.3, 0.25, 0.42
for i, (t, cuerpo) in enumerate(pasos):
    x = x0 + i * (ancho + sep)
    caja(s, x, 2.0, ancho, 4.2, t, cuerpo, size_t=18, size_b=15,
         anchor=MSO_ANCHOR.MIDDLE, con_viñetas=True)
    if i < len(pasos) - 1:
        fl = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + ancho + 0.02),
                                Inches(3.95), Inches(0.21), Inches(0.3))
        fl.fill.solid()
        fl.fill.fore_color.rgb = ACENTO
        fl.line.fill.background()
# 7. Cierre
s = prs.slides.add_slide(BLANK)
fondo = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
fondo.fill.solid()
fondo.fill.fore_color.rgb = AZUL
fondo.line.fill.background()
texto(s, 0.8, 2.6, 11.7, 1.2, "Gracias", size=44, color=BLANCO, bold=True,
      align=PP_ALIGN.CENTER)
texto(s, 0.8, 3.8, 11.7, 1.0, "¿Preguntas?", size=28, color=BLANCO, align=PP_ALIGN.CENTER)
s.notes_slide.notes_text_frame.text = "Cierre y preguntas."

prs.save(OUT)
print(f"OK -> {OUT}")
