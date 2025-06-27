# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Mexican public security data analysis project using ENSU (Encuesta Nacional de Seguridad Pública Urbana) survey data from INEGI. The project analyzes security perceptions, victimization, and institutional trust by state and gender using urban survey data from 18+ population in Mexico.

## Data Structure

The repository contains three main types of data files:

### Survey Microdata (CSV files)
- `conjunto_de_datos_ensu_cb_0325.csv` - Basic questionnaire (15.5MB): Security perceptions, victimization, institutional trust (~330k records)
- `conjunto_de_datos_ensu_cs_0325.csv` - Sociodemographic questionnaire (19.8MB): Demographics for all household members (~500k records)  
- `conjunto_de_datos_ensu_viv_0325.csv` - Housing questionnaire (4.6MB): Geographic and household context (~120k records)

### Quarterly Archives
- `conjunto_de_datos_ensu_2024_*t_csv.zip` - Quarterly survey data archives (Q1-Q4 2024)

## Data Processing Notes

### File Format Issues
- CSV files use CR line terminators (old Mac format)
- Very long lines (up to 1485 characters in CB file)
- Files require pandas for proper processing due to format complexity

### Data Relationships
- Files are linked by `ID_VIV` (household ID) and `ID_PER` (person ID)
- Geographic data comes from VIV file (states, municipalities, cities)
- Demographics from CS file (age, sex, education, employment)
- Security metrics from CB file (perceptions, victimization, trust)

### Key Variables
- **Geographic**: `NOM_ENT` (state), `NOM_MUN` (municipality), `NOM_CD` (city)
- **Demographics**: `SEXO` (1=Male, 2=Female), `EDAD` (age), `A_ESC` (education)
- **Security**: `BP1_*` (perceptions), `BP2_*` (victimization), `BP3_*` (institutional trust)
- **Weighting**: `FAC_VIV` (household factor), `FAC_SEL` (selected person factor)

## Development Environment

### Python Requirements
- Python 3.10.12 available
- pandas required for data processing (not currently installed)
- Data processing follows pandas merge workflow as documented in README.md

### Typical Data Processing Commands
```python
# Load and merge data as shown in README.md
import pandas as pd
cb = pd.read_csv("conjunto_de_datos_ensu_cb_0325.csv", low_memory=False)
viv = pd.read_csv("conjunto_de_datos_ensu_viv_0325.csv", low_memory=False) 
cs = pd.read_csv("conjunto_de_datos_ensu_cs_0325.csv", low_memory=False)

# Merge workflow: CB -> VIV (geography) -> CS (demographics)
df = cb.merge(viv, on="ID_VIV", how="left")
df = df.merge(cs, on=["ID_VIV", "ID_PER"], how="left")
```

## Data Source
- ENSU public microdata from INEGI 
- Creative Commons BY 4.0 license
- Q1 2025 data (code "0325") currently available
- Contact: Krishna Sandoval Cambranis