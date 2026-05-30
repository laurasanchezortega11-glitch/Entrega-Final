# Pipeline Bioinformático para Identificación de Familias Pfam

## Descripción

Este pipeline bioinformático tiene como objetivo identificar las familias de proteínas de Pfam asociadas a un conjunto de proteínas obtenidas desde UniProt.

El pipeline automatiza el proceso de:

1. Lectura de identificadores UniProt.
2. Descarga automática de secuencias FASTA.
3. Organización de archivos biológicos.
4. Comparación de proteínas contra perfiles HMM de Pfam utilizando HMMER.
5. Identificación de familias proteicas asociadas.

---

# Estructura del proyecto

```bash
Entrega-Final/
│
├── pipeline/
│   ├── main.py
│   ├── downloader.py
│   ├── protein.py
│   └── proteins.txt
│
├── data/
│   └── fasta/
│
├── PFAMdescargas/
│
├── README.md
└── .gitignore
```

---

# Funcionamiento general del pipeline

## 1. Lectura de proteínas

El archivo `proteins.txt` contiene los identificadores UniProt de las proteínas a analizar.

Ejemplo:

```text
P00519
P42684
P12931
```

---

## 2. Descarga automática de secuencias

El pipeline utiliza la API REST de UniProt para descargar automáticamente las secuencias en formato FASTA.

Las secuencias descargadas se almacenan en:

```bash
data/fasta/
```

---

## 3. Análisis con HMMER

Las proteínas descargadas son comparadas contra perfiles HMM de Pfam mediante la herramienta `hmmscan` de HMMER.

Este análisis permite identificar:

- dominios conservados,
- familias proteicas,
- similitud evolutiva.

---

## 4. Resultados esperados

El pipeline permitirá asociar cada proteína con una o varias familias Pfam, tales como:

- Protein_kinase
- SH2
- Ras
- DEAD
- HSP70
- WD40

entre otras.

---

# Tecnologías utilizadas

- Python 3
- HMMER
- Pfam
- UniProt REST API
- Git/GitHub
- Linux/Ubuntu (WSL)

---

# Objetivo bioinformático

Este proyecto busca automatizar la identificación de familias proteicas utilizando perfiles ocultos de Markov (HMM), permitiendo reconocer dominios funcionales y relaciones evolutivas entre proteínas.

---

# Ejecución del pipeline

Desde la carpeta `pipeline/` ejecutar:

```bash
python3 main.py
```
````
ga-Final
Este repositorio contiene un pipeline que analiza a que familias de proteínas  pertenecen algunas secuencias 
