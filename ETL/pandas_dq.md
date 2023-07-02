# Libreria pandas_dq (https:/(https://pypi.org/project/pandas-dq/1.1/)

- Herramienta para analizar y limpiar sus datos en una sola línea de código con un transformador compatible con Scikit-Learn.

- **pandas_dq** es una nueva biblioteca de python para limpiar automáticamente su conjunto de datos sucios utilizando las funciones pandas scikit_learn. Puede analizar su conjunto de datos y corregirlos, ¡todo en una sola línea de código!

## pandas_dq tiene dos modulos importantes: find_dq y Fix_DQ.

### 1. Funcion find_dq

**find_dq** es una función que probablemente sea la forma más popular al usar **pandas_dq**. Realiza los siguientes pasos de análisis de calidad de datos:

- Detecta valores perdidos y sugiere imputarlos con la media, la mediana, la moda o un valor constante.
- Identifica categorías raras y sugiere agruparlas en una sola categoría o descartarlas.
- Encuentra valores infinitos y sugiere reemplazarlos con NaN o un valor grande.
- Detecta tipos de datos mixtos y sugiere convertirlos en un solo tipo o dividirlos en varias columnas.
- Detecta valores atípicos y sugiere eliminarlos o utilizar estadísticas robustas.
- Detecta características de alta cardinalidad y sugiere reducirlas utilizando técnicas de codificación o métodos de selección de características.
- Detecta características altamente correlacionadas y sugiere descartar una de ellas o usar técnicas de reducción de dimensionalidad.
- Detecta filas y columnas duplicadas y sugiere eliminarlas o conservar solo una copia.
- Detecta distribuciones sesgadas y sugiere aplicar transformaciones o técnicas de escalado.
- Detecta clases desequilibradas y sugiere utilizar técnicas de remuestreo o pesos de clase.
- Detecta la fuga de funciones y sugiere evitar el uso de funciones que no están disponibles en el momento de la predicción.
