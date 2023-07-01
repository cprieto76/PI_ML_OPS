# Libreria pandas_profiling (https://pypi.org/project/pandas-profiling/)

Gran herramienta para crear informes en formato HTML interactivo, fácil para entender y analizar datos.

## Analisis del informe report.html

### 1. Overview

#### 1.1 Aspectos a destacar

1.1.1 Gran cantidad de valores faltantes (missing values) 19.6 %
1.1.2 Columnas 27 de las cuales:
- Variables Numericas :        10
- Variables de Texto:          13
- Variables Categoricas:        3
- Variables de Fecha:           1


#### 1.2 Acciones a desarrollar

### 2. Alertas

#### 2.1 Correlacion Alta

a) popularity vs vote_count
b) vote_count vs revenue
c) budget vs revenue
d) budget vs return

#### 2.2 Desbalances

El status nos muestra el 97% de las peliculas con categoria released lo cual indica que el analisis total se va a hacer sobre peliculas estrenadas

#### 2.3 Valores faltantes

Los siguientes features presentan altos valores faltantes:

- overview:         946 (2.1%) 
- tagline:        24960 (55.0%)
- id_btc:         42183 (93.0%) 
- name_btc:       42183 (93.0%) 
- poster_btc:     42183 (93.0%) 
- backdrop_btc:   42183 (93.0%) 
- iso_639_1:       3792 (8.4%) 
- language_name:   3915 (8.6%) 
- companies_id:   12264 (27.0%) 
- companies_name: 12264 (27.0%) 
- countries_iso:   6213 (13.7%) 
- countries_name:  6213 (13.7%) 





