#!/usr/bin/env python3
"""Rellena Inscripcion_tema_de_tesis.xls. Ejecutar: ~/.venvs/pptx/bin/python fill_inscripcion_xls.py"""
from pathlib import Path

import xlrd
import xlwt
from xlutils.copy import copy

DIR = Path(__file__).resolve().parent
SRC = DIR / "Inscripcion_tema_de_tesis.xls"
OUT = DIR / "Inscripcion_tema_de_tesis_AGUSTIN_SOLIS.xls"

TITULO = (
    "Análisis multimodal del discurso político y su relación con el voto parlamentario: "
    "postura y valores en texto y archivos audiovisuales (Asamblea Nacional francesa)"
)

RESUMEN = """Antecedentes. En las democracias representativas los partidos comunican sus posiciones por programas electorales, redes sociales, el debate parlamentario y medios audiovisuales, mientras sus representantes votan leyes y enmiendas. Comparar discurso y voto exige integrar fuentes heterogéneas, extraer argumentos, postura y valores, y validar las mediciones computacionales (Grimmer y Stewart, 2013). Existen modelos para clasificación temática (MARPOR, ManifestoBERTa), detección de postura, extracción de argumentos y valores (MFT y Schwartz), y análisis audiovisual, pero fueron entrenados mayoritariamente fuera del discurso político en francés. La tesis aborda la XV legislatura de la Asamblea Nacional francesa (2017-2022), en el marco del proyecto PAROLES ET ACTES (INA le lab 2026-2027), con dos focos: determinar qué modelos sirven en cada fuente y estudiar discurso y voto de los partidos, por separado y en conjunto.

Objetivos. Objetivo general: desarrollar y evaluar una metodología multimodal que determine qué modelos pueden aplicarse a fuentes textuales y audiovisuales del discurso político francés para extraer temas, argumentos, posturas, valores y emociones, y usar esas mediciones para estudiar el discurso y el voto de partidos y diputados y su correspondencia. Objetivos específicos: (1) construir una base integrada y reproducible; (2) clasificar temáticamente con MARPOR y validar; (3) extraer argumentos, postura y valores (MFT y Schwartz); (4) caracterizar el material del INA y seleccionar modelos audiovisuales viables; (5) evaluar modelos con muestras anotadas manualmente; (6) analizar discurso y voto por separado; (7) medir correspondencia discurso-voto por partido, tema y canal.

Metodología. Seis etapas: (1) recolección e integración de cohorte de diputados, manifiestos, Twitter, hemiciclo, leyes, enmiendas, votaciones y material INA; (2) extracción desde texto con ManifestoBERTa, BERTopic, argument mining, stance y valores; (3) estudio exploratorio del audiovisual y prueba de modelos de transcripción, diarización y emociones; (4) evaluación por fuente con precisión, exhaustividad, F1 macro y kappa; (5) análisis del discurso y del voto de partidos; (6) comparación discurso-voto con medidas de correspondencia y bootstrap. Variables: tema MARPOR, postura, valores, emoción y dirección del voto nominal.

Resultados esperados. Base de datos multimodal documentada y pipeline reproducible; conjuntos de evaluación en francés; comparación de desempeño de modelos por tarea y fuente; diagnóstico de modelos audiovisuales aplicables al INA; caracterización del discurso y del voto por partido y canal; análisis de coincidencias y discrepancias entre lo expresado y lo votado."""

# Completar RUT antes de subir si el formulario lo exige
RUT = ""


def main() -> None:
    rb = xlrd.open_workbook(str(SRC), formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)

    wrap = xlwt.XFStyle()
    wrap.alignment.wrap = 1

    ws.write(6, 2, "Agustín Sebastián Solís Meza")
    ws.write(6, 17, RUT)
    ws.write(7, 2, "Magíster en Ciencia de Datos")
    ws.write(8, 2, "Ciencia de Datos")
    ws.write(9, 2, "No")
    ws.write(10, 2, TITULO, wrap)
    ws.write(13, 2, RESUMEN, wrap)
    ws.write(39, 2, "Valentin Clement Barriere")
    ws.write(39, 15, "Franziska Christl Wagner")

    wb.save(str(OUT))
    print(f"OK -> {OUT}")
    if not RUT:
        print("Nota: RUT vacío en celda (fila 7, col 18). Complétalo en Excel antes de subir.")


if __name__ == "__main__":
    main()
