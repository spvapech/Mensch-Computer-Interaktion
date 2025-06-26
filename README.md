# 👨‍💻 Mensch-Computer Interaktion (SoSe 2025) – Universität Duisburg-Essen

Dieses Repository enthält die Lösungen und Projektarbeiten aus dem Modul **Mensch-Computer Interaktion** im Sommersemester 2025 an der **Universität Duisburg-Essen**.

Die Inhalte decken verschiedene Themen der Mensch-Computer-Interaktion ab, darunter Fitts’s Law, papierbasierte und digitale Prototypen, Bildverarbeitung, Interaktion über Körperbewegung sowie Datenkompression.

---

## 📚 Inhaltsverzeichnis

- [🧪 Übung 1 & 2 – Fitts's Law GUI + Analyse](#-übung-1--2--fittss-law-gui--analyse)
- [🖼️ Übung 3 – HiFi-Prototyp](#️-übung-3--hifi-prototyp)
- [🖼🖌️ Übung 4.2 – SVG-Grafik – Landschaft bei Nacht](#️️-übung-42--svg-grafik--landschaft-bei-nacht)
- [🌳 Übung 4.3 – Green Screen Replacement](#-übung-43--green-screen-replacement)
- [🖼️ Übung 4.4 – Bildskalierung](#️-übung-44--bildskalierung)
- [📦 Übung 4.5 – LZSS-Kompression & -Dekompression](#-übung-45--lzss-kompression--dekompression)
- [🎮 Übung 5 – Mario-Spiel mit Körpersteuerung](#-übung-5--mario-spiel-mit-körpersteuerung)
- [⚙️ Installation & Setup](#️-installation--setup)
- [📦 requirements.txt](#-requirementstxt)

---

## 🧪 Übung 1 & 2 – Fitts's Law GUI + Analyse

### Teil 1 – GUI:
Ein grafisches Experiment zur Untersuchung von Fitts’s Law. In jedem Durchgang erscheinen zwei Kreise mit unterschiedlichem Durchmesser und Abstand, die der Nutzer anklicken muss. Die Zeit zwischen den Klicks wird gemessen. Insgesamt werden 27 Durchläufe (3 Durchmesser × 3 Distanzen × 3 Wiederholungen) durchgeführt.

### Teil 2 – Scatterplot-Auswertung:
Mit zwei verschiedenen Eingabegeräten (z. B. Maus & Touchpad) wird das Experiment durchgeführt. Die Ergebnisse (CSV) werden in einem gemeinsamen Scatterplot visualisiert:
- X-Achse: Index of Difficulty (ID)
- Y-Achse: Reaktionszeit (MT)
- Ausgleichsgeraden mit Gleichung & Legende für beide Eingabegeräte

---

## 🖼️ Übung 3 – HiFi-Prototyp

Erstellung von zwei Papierprototypen für eine Universitäts-App. Anschließend wird einer davon mit dem Webtool **Figma** in einen klickbaren HiFi-Prototypen überführt.


---

## 🖌️ Übung 4.2  SVG-Grafik – Landschaft bei Nacht

In dieser Übung soll eine einfache Vektorgrafik im SVG-Format erstellt werden, die eine Landschaft bei Nacht darstellt.

Die Grafik muss ausschließlich mit Standard-SVG-Formen (z. B. rect, circle, ellipse, line, polygon, path) umgesetzt werden.

Anforderungen – folgende Elemente müssen enthalten sein:
🌌 Dunkler Nachthimmel

☁️ Eine Wolke

🌙 Ein sichelförmiger Mond

🌍 Ein Bodenbereich

🌳 Mindestens ein Baum

🏠 Ein Haus mit:

einer Tür

zwei Fenstern

einem Spitzdach

---

## 🌳 Übung 4.3 – Green Screen Replacement

Ein Bild mit Greenscreen wird eingelesen und der grüne Hintergrund entfernt, anschließend durch ein Waldbild ersetzt.

**Ziel:**
- Extrahierte Person (grüne Pixel entfernt)
- Kombiniertes Bild mit Waldboden
- Ausgabe als `person_in_forest.png`

Nur `numpy` und `matplotlib` erlaubt – keine OpenCV-Tools.

---

## 🖼️ Übung 4.4 – Bildskalierung

Implementierung zweier Algorithmen zur Skalierung eines Bitmap-Bilds:

- `nearest_neighbor.py`: Nearest Neighbor Interpolation
- `bilinear.py`: Bilineare Interpolation

Das Skript `main.py` lädt ein Bild (`pixel.bmp`), wendet beide Verfahren an und speichert das Ergebnis in `results.png`.

---

## 📦 Übung 4.5 – LZSS-Kompression & -Dekompression

Implementierung des **LZSS-Kompressionsalgorithmus** (Variante von LZ77):

1. ASCII-Zeichen ↔ Binär (7-bit) via `ASCII_converter.py`
2. `lzss_encode()` und `lzss_decode()` in `LZSS_encoder.py`
3. Eingabedateien (`LZSS_to_encode.txt`, `LZSS_to_decode.txt`) → Ausgabedateien in `text_files/`

Ziel: Binärkompression ohne externe Bibliotheken (reines Python).

---

## 🎮 Übung 5 – Mario-Spiel mit Körpersteuerung

Ein modifiziertes Super Mario-Spiel wird mit Gesten über Webcam gesteuert. Steuerung durch Bewegung von Kopf, Händen oder Füßen – abhängig von der **letzten Ziffer deiner Matrikelnummer**.

**Zu implementieren:**

1. `custom_input_thread()` – Webcam-Feed einlesen
2. `getMarkerListAndShowMarkers()` – Marker erkennen & visualisieren
3. `custom_input_loop()` – Steuerung via Markerpositionen

**Bewegungssteuerung via:**
- `post_action(Action.LEFT / RIGHT / JUMP)`
- `Action.*_STOP` zum Beenden der Aktion

Verwendet: `OpenCV`, `mediapipe`, `pygame`, `PyTMX`

---

## ⚙️ Installation & Setup

### Voraussetzungen

- Python **3.10+**
- Virtuelle Umgebung empfohlen:

```bash

python -m venv venv
source venv/bin/activate  # Unter Windows: venv\Scripts\activate

````
---


## 📦 requirements.txt

Die Datei `requirements.txt` enthält alle benötigten Python-Bibliotheken für die einzelnen Übungen.  
Du kannst sie wie folgt verwenden:

### 📁 Inhalt der Datei:

```txt
# GUI & Matplotlib
tk

# Green Screen Replacement & Skalierung
numpy~=1.26.4
matplotlib~=3.9.0
pillow

# Spiel mit Körpersteuerung
pygame~=2.5.2
PyTMX~=3.32
opencv-python~=4.10.0.82
mediapipe~=0.10.14
