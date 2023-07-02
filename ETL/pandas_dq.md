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

### 2. Fix_DQ class

Es un transformador scikit_learn que puede detectar problemas de calidad en los datos y limpiarlos todos en una línea de código

Fix_DQ es una excelente manera de limpiar un conjunto de datos de entrenamiento completo y aplicar los mismos pasos en un MLOps (Metodologia Machine Learning Operations) a un conjunto de datos de prueba. **Fix_DQ** se puede usar para detectar la mayoría de los problemas en sus datos (similar a find_dq pero sin los pasos relacionados con el objetivo) en un solo paso (durante el método `fit`). Este transformador se puede guardar (o "decapar") para aplicar los mismos pasos en los datos de prueba al mismo tiempo o más tarde.
