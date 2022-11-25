## 2do Parcial FI - 1er Cuatrimestre 2022
A tener en cuenta:

* La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso de ser necesario y pushearlos a este repo que se te generó automáticamente.

* Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. Debés hacer un commit cada 5 min, de lo contrario tu entrega no será considerada válida. En todo momento debés estar conectado al zoom, con la cámara prendida.

* El tiempo recomendado de resolución será de 2 hora y media, pero se dará tiempo para entregar hasta el horario de finalización pautado según disposición del aula.

* Para rendir se podrán usar las computadoras disponibles de los laboratorios. Alternativamente, quien lo desee podrá traer y utilizar su propia computadora portátil.

* Durante el parcial estará permitido navegar en Internet para consultar los apuntes de la cátedra. No estará permitido bajo ningún concepto la comunicación con otra persona salvo el o la docente a cargo, presente o no en el aula, por cualquier tipo de medio, ya sea oral u escrito

* **Prohibido chatear**. Hacerlo será considerado una falta grave, que implicará la desaprobación automática del examen y estará sujeto a sanciones administrativas.

* Para aprobar el examen se deberá contar con al menos el 60% del mismo correcto

* El parcial es teórico-práctico, se evalúan tanto las habilidades adquiridas en programación y en Python específicamente, como la adquisición de los conceptos teóricos. 


### Consigna N°1

Dado el siguiente enlace "https://pokeapi.co/api/v2/pokemon/pikachu", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué content_type? Obtené la información correspondiente al campo "forms".

c) Averigüá cuántos Pokemones almacena la API.

d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2? ¿Qué métodos HTTP deberían asociarse a cada una?

f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

g) Describí la arquitectura cliente-servidor y los roles de cada parte

### Consigna N°2
Una empresa de internet está investigando distintas zonas por las afueras de una ciudad a fin de decidir si extender su servicio hacia estas zonas, por lo que se encarga de averiguar la cantidad de personas que hay. De estas personas se sabe las edades de las mismas (solo personas adultas), sus ingresos, sus gastos generales, si tiene familar/es a cargo, la accesibilidad a calle asfaltada, presencia de otra empresa de internet cercana, entre algunas otras cosas. La idea de esta empresa es realizar una oferta limitada en estas zonas, dándoles en principio el acceso de hasta 3 posibles velocidades de internet.

Dado el [siguiente dataset](https://raw.githubusercontent.com/FundamentosInformaticaUCEMA/FI_Parcial2_2022_T1/main/recursos/internet.csv?token=GHSAT0AAAAAABTQD3IXNKY7XLI74SXU6ZB2YWCJHAQ) ([link alternativo para descargar](https://ucema.edu.ar/webcampus3/mod/resource/view.php?id=66874)), responder las siguientes preguntas:

a) Cargá los datos en un data frame, inspeccionalo y caracterizalo.

b) ¿Cuáles son las variables que se encuentran relacionadas? ¿Cómo lo evaluarías gráficamente?

c) Usando un k=3 realizá el agrupamiento de los datos. Analizar y evaluar si el proceso de clustering fue correcto. 

d) Proponer un número de clusters (k) más apropiado, validarlo de forma gráfica. 

e) ¿Qué conclusión podés sacar de [este gráfico del codo](https://github.com/FundamentosInformaticaUCEMA/FI_Parcial2_2022_T1/blob/main/recursos/codo.jpg)?


<details>
  <summary>Código que te puede resultar útil</summary>
  
  > Bibliotecas
  ```python
  import pandas as pd
  import seaborn as sns
  from sklearn.preprocessing import StandardScaler
  from sklearn.cluster import KMeans, DBSCAN
  from sklearn.metrics import silhouette_samples, silhouette_score
  import matplotlib.pyplot as plt 
  import matplotlib.cm as cm 
  import numpy as np
  from scipy import stats
  ```
  
  > Distribución
  
  ```python
  sns.histplot(data = df, x = "columna", binwidth=10, kde = True)
  # el binwidth depende de la cantidad de datos, a mayor cantidad de datos, más grande el binwidth
  ``` 
  
  > Escalado

  ```python
  scaler = StandardScaler()
  df_escalado = scaler.fit_transform(df)
  ```
  
  > Inercias según número de grupos

  ```python
  def inercias_por_k():
    inercias = {}
    for i in range(1,11):
        kmeans = KMeans(n_clusters = i, init="random", n_init=10, max_iter=300, random_state=123457)
        kmeans.fit(df_escalado)
        inercias[i] = kmeans.inertia_
    return inercias
  ```

  > Gráfico de agrupación
  ```python
  import seaborn as sns
  colores = ["red", "green"]
  sns.scatterplot(x = datos_escalados[:,2], y = datos_escalados[:, 3], hue = kmeans.labels_, palette = colores, alpha = 0.5)
  sns.scatterplot(x = kmeans.cluster_centers_[:,2], y = kmeans.cluster_centers_[:,3], zorder = 10, palette = colores, hue = [0, 1], legend = False, marker=6, s=200)
  ```

  > Silhouette

  ```python
  silhouette_avg = silhouette_score(df_escalado, kmeans.labels_)
  sample_silhouette_values = silhouette_samples(df_escalado, kmeans.labels_)

  def graficarSilhouette (k, labels, sample_silhouette_values, silhouette_avg):
    fig, ax1 = plt.subplots(1, 1)
    y_lower = 10
    for i in range(k):
        ith_cluster_silhouette_values = \
            sample_silhouette_values[labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / k)
        ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax1.set_title("Plot del silhouette de cada cluster")
    ax1.set_xlabel("Coeficiente de silhouette")
    ax1.set_ylabel("Etiqueta del cluster")
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax1.set_yticks([])

    graficarSilhouette (k, kmeans.labels_, sample_silhouette_values, silhouette_avg)
  ```


</details>


### Consigna N°3

Retomando la consigna del punto 2, realizá un informe de lo observado para dicho data set, siguiendo el estilo propuesto a continuación:

![plantilla](/recursos/plantilla.png)

**REEMPLAZAR EL TEXTO Y LAS IMÁGENES CON LAS PRODUCCIONES PROPIAS OBTENIDAS EN EL PUNTO ANTERIOR**

b) ¿Qué es una etiqueta semántica y qué ventajas tienesu uso?

c) Explique los siguientes conceptos: página web, sitio web, aplicación REST