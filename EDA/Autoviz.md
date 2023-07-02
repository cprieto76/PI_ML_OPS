# Libreria autoviz [(https://pypi.org/project/autoviz/0.0.6/)]

Realiza la visualizacion automatica de cualquier conjunto de datos, se le puede entregar cualquier archivo json, csv o un dataframe.
La maxima cantidad de filas por analizar es de 150.000 y la maxima de columnas es de 30

## Codigo para generar graficos ubicados en URL

#####   1     from autoviz.AutoViz_Class import AutoViz_Class
#####   2     AV = AutoViz_Class()
#####   3     dft = AV.AutoViz(
    "",
    sep=",",
    depVar="",
    dfte=df,
    header=0,
    verbose=1,
    lowess=False,
    chart_format="server",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
    save_plot_dir=None
)

Return:
-  5 variable(s) removed since they were ID or low-information variables
        List of variables removed: ['id', 'id_btc', 'name_btc', 'poster_btc', 'backdrop_btc']

- pair_scatters can be found in URL below:
Launching server at http://localhost:58734
- distplots can be found in URL below:
Launching server at http://localhost:58735
- violinplots can be found in URL below:
Launching server at http://localhost:58736
- No date vars could be found in data set
- heatmaps can be found in URL below:
Launching server at http://localhost:58737
- cat_var_plots can be found in URL below:
Launching server at http://localhost:58738
