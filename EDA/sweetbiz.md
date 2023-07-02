# Libreria sweetbiz [(https://pypi.org/project/sweetviz/)]

Herramienta toma dataframes de pandas y crea un informe HTML autónomo que se puede ver solo en un navegador o integrarse en cuadernos.

Además de crear visualizaciones interesantes y hermosas con solo dos líneas de código, proporciona un análisis que llevaría mucho más tiempo generar manualmente.

## Analisis del informe sweetviz_report.html (File Size:65.1 MB)
### Primer vistazo a estado de los datos que pueden requerir transformacion para un analisis mas acertado.

### 1. Overview

#### 1.1 Aspectos a destacar

1.1.1 Columnas 27 de las cuales:
- Variables Numericas :        10
- Variables de Texto:          13
- Variables Categoricas:        4

Nota: sweetbiz no reconoce el campo released_date como date sino como texto

1.1.2 Filas duplicadas:         0

### 2. Variables

#### 2.1 Id (Id de pelicula).             Numérico

Identificador Unico ya que presenta 45436 valores diferentes. No hay valores repetidos.

#### 2.2 title (Titulo de pelicula).     Texto

Existen 3150 registros que aparecen mas de una vez. Entre los titulos que mas se repiten de mayor a menor son:

- Cinderella:             11
- Hamlet:                  9
- Alice in Wonderland      9
- Beauty and the Beast     8
- Les Miserables           8
- Treasure Island          7
- The Three Musketeers     7

Nota: Revisar el porque de la diferencia y si tiene algun efecto en las solicitudes de la API y en el modelo de Machine Learning

2.3 overview (pequeño resumen).        Texto

