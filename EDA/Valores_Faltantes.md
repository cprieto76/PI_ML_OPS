# Valores Faltantes

Una de los metodologias en que se basa el analisis de valores faltantes es la de **reconocer el patron** que siguen basados en la siguiente clasificación:

## MCAR (Missing Completely at Random):
"Datos Faltantes Completamente al Azar". En este caso, la ausencia de datos no está relacionada ni influenciada por los valores reales de los datos o cualquier otra variable en el conjunto de datos. En otras palabras, la probabilidad de que un dato falte es independiente de los valores observados y no observados en el conjunto de datos.
En un escenario MCAR, los datos faltantes se deben a causas completamente aleatorias o impredecibles, como errores en la recolección de datos o fallas técnicas. Esto implica que los datos faltantes no introducen ningún sesgo sistemático en el análisis de los datos y no se necesita considerar su patrón específico al realizar análisis estadísticos o imputación de valores faltantes.

## MAR (Missing at Random):
"Datos Faltantes al Azar". En este caso, la probabilidad de que un dato falte puede depender de los valores observados en el conjunto de datos, pero no de los valores no observados. En otras palabras, aunque hay datos faltantes, la falta de estos datos se puede explicar o predecir a partir de las variables observadas en el conjunto de datos.
En un escenario MAR, los datos faltantes pueden estar relacionados con ciertas características o variables observadas, pero no con los valores reales de los datos faltantes en sí mismos. Esto permite la posibilidad de modelar y predecir la falta de datos utilizando variables existentes en el conjunto de datos.

## MNAR (Missing Not at Random):
MNAR significa "Missing Not at Random" o "Datos Faltantes No al Azar". En este caso, la falta de datos está relacionada con los valores no observados en el conjunto de datos. La probabilidad de que un dato falte depende de la información contenida en los valores faltantes, lo que implica que los datos faltantes están sistemáticamente relacionados con la variable o atributo que falta.
En un escenario MNAR, la ausencia de datos puede estar influenciada por factores desconocidos o no medidos en el conjunto de datos, lo que puede introducir sesgos en los análisis posteriores si no se manejan adecuadamente.

*Determinar si los datos faltantes siguen un patrón MCAR, MAR o MNAR puede ser un desafío en la práctica, ya que requiere conocimiento del dominio y análisis detallados de los datos y su recolección. Sin embargo, comprender estos conceptos puede ser útil para abordar y manejar los datos faltantes de manera adecuada al realizar análisis estadísticos o modelado en conjuntos de datos incompletos.*





Regenerate response
