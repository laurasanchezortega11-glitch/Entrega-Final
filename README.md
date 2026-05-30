# Pipeline Bioinformático para Identificación de Familias Pfam

## Descripción

Este proyecto implementa un pipeline bioinformático en Python para identificar las familias de proteínas Pfam a las que pertenecen un conjunto de proteínas obtenidas desde UniProt.

El pipeline descarga las secuencias proteicas, construye una base de datos reducida de Pfam utilizando únicamente las familias solicitadas en la tarea, ejecuta búsquedas mediante HMMER y genera un resumen final con las familias detectadas para cada proteína.

---

## Estructura del proyecto

```text
Entrega-Final/
├── pipeline/
│   ├── main.py
│   ├── protein.py
│   ├── downloader.py
│   ├── build_pfam.py
│   ├── scan_proteins.py
│   └── summarize_results.py
│   └── proteins.txt   
│
│
├── README.md
└── .gitignore
```

---

## Requisitos

- Python 3
- HMMER 3.x
- requests

### Instalar HMMER

```bash
sudo apt update
sudo apt install hmmer
```

### Instalar requests

```bash
pip install requests
```

---

## Flujo del pipeline

### 1. Descarga de proteínas

A partir de los identificadores UniProt almacenados en `proteins.txt`, se descargan las secuencias FASTA.

```bash
python3 downloader.py
```

---

### 2. Construcción de la base Pfam reducida

A partir de las familias definidas en `families.txt` se genera una base de datos reducida llamada `miniPfam.hmm`.

```bash
python3 build_pfam.py
```

Posteriormente se indexa la base:

```bash
hmmpress miniPfam.hmm
```

---

### 3. Búsqueda de familias Pfam

Se ejecuta HMMER sobre cada proteína FASTA.

```bash
python3 scan_proteins.py
```

Los resultados se almacenan en:

```text
data/results/
```

---

### 4. Generación del resumen final

Se procesan los resultados obtenidos y se genera:

```text
data/protein_families.csv
```

Ejecutar:

```bash
python3 summarize_results.py
```

---

## Programación Orientada a Objetos

El proyecto implementa una clase `Protein` para representar proteínas mediante programación orientada a objetos.

La clase almacena información relacionada con cada proteína y facilita su manipulación dentro del pipeline.

---

## Resultado final

El pipeline genera un archivo CSV con las familias Pfam identificadas para cada proteína analizada.

Ejemplo:

```csv
Protein,Family
P01111,Ras
P98160,EGF
P40763,SH2
P29353,SH2
```

---

## Resumen del flujo de trabajo

```text
Lista de proteínas (UniProt)
          ↓
Descarga FASTA
          ↓
Construcción de miniPfam
          ↓
hmmpress
          ↓
hmmscan
          ↓
Archivos .tbl
          ↓
protein_families.csv
```

---

## Autora

Laura Sánchez

Proyecto desarrollado para la identificación de familias proteicas mediante perfiles HMM de Pfam utilizando Python y HMMER.