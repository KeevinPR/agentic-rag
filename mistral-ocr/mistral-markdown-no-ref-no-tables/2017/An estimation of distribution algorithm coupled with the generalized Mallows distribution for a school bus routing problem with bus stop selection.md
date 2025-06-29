# Revista Iberoamericana de Automática e Informática Industrial 

Revista Iberoamericana de Automática e Informática industrial 14 (2017) 288-298

## Un Algoritmo de Estimación de Distribuciones copulado con la Distribución Generalizada de Mallows para el Problema de Ruteo de Autobuses Escolares con Selección de Paradas

Ricardo Pérez-Rodríguez ${ }^{\mathrm{a}, *}$, Arturo Hernández-Aguirre ${ }^{\mathrm{b}}$<br>${ }^{a}$ CONACYT - Centro de Investigación en Matemáticas CIMAT, A.C. Fray Bartolomé de las Casas 314, Barrio la Estación, C.P. 20259, Aguascalientes, Ags. México.<br>${ }^{\text {b }}$ Centro de Investigación en Matemáticas CIMAT, A.C. Callejón de Jalisco s/n, Mineral de Valenciana, C.P. 36240, Guanajuato, Gto, México.

## Resumen

Aunque los algoritmos de estimación de distribuciones fueron originalmente diseñados para resolver problemas con dominio de valores reales o enteros, en esta contribución se utilizan para la resolución de un problema basado en permutaciones. El ruteo de autobuses escolares con selección de paradas es resuelto utilizando la distribución generalizada de Mallows como un intento para describir y obtener una distribución de probabilidad explícita sobre un conjunto de rutas de autobuses escolares. Además, un operador de mutación es considerado para mejorar la estimación de la permutación central, un parámetro de la distribución de Mallows. Diferentes y diversas instancias sirvieron como parámetro de entrada y prueba para mostrar que problemas basados en permutaciones tales como el ruteo de autobuses escolares con selección de paradas pueden ser resueltos por medio de un modelo de probabilidad, y mejorar la estimación de la permutación central ayuda al desempeño del algoritmo.

## Palabras Clave:

Algoritmo de estimación de distribuciones, distribución de Mallows, problema de ruteo de vehículos, problema de ruteo de autobuses escolares.

## 1. Introducción

Básicamente, el problema del ruteo de autobuses escolares con selección de paradas SBRP (por sus siglas en inglés School Bus Routing Problem) consiste en encontrar una eficiente secuencia de rutas para una flota de autobuses escolares que recogen estudiantes en diversas paradas y los dejan en su escuela satisfaciendo varias restricciones tales como capacidad máxima del autobús, tiempo máximo para recoger a los estudiantes, y el tiempo límite para llegar a la escuela. Por lo tanto, el SBRP es un tema de investigación logística y puede ser considerado como un problema combinatorio realista.

Una variante del SBRP llamada SBRP con selección de paradas SBRPBSS (por sus siglas en inglés School Bus Routing Problem with Bus Stop Selection), se tiene cuando hay un conjunto de paradas potenciales de autobús, de tal manera que cada estudiante vive a $r$ metros de al menos alguna de ellas. Así, determinar el conjunto de paradas de autobús que realmente se deben visitar es una parte del problema (Schittekat et al., 2013).

El SBRPBSS puede ser visto como un caso especial del problema de ruteo de vehículos con capacidad finita CVRP (por

[^0]sus siglas en inglés Capacitated Vehicle Routing Problem), un problema NP-hard (por sus siglas en inglés Non-deterministic Polynomial-time), donde un conjunto de $n$ nodos o vértices (las paradas a visitar) está dado con una demanda específica (los estudiantes) los cuales deben ser atendidos por una flota de vehículos (los autobuses escolares) con capacidad limitada. Sin embargo se discute que existe un conjunto de paradas potenciales en este artículo, de las cuales se debe definir cuáles de ellas en realidad su ocuparan.

En esencia, el SBRPBSS tiene tres aspectos distintos pero relacionados entre sí: (1) determinar el conjunto de paradas a visitar, (2) establecer para cada estudiante a qué parada deberá dirigirse a esperar un autobús, y (3) diseñar rutas con las paradas de autobuses elegidas, tal que la distancia total de viaje es minimizada.

La mayoría de las técnicas de solución desarrolladas para el SBRPBSS son caracterizadas por un enfoque secuencial. Es decir, un procedimiento de selección de paradas y un procedimiento de ruteo son realizados uno después de otro. Ya sea que el procedimiento de selección de paradas es ejecutado inicialmente y después el procedimiento de ruteo o viceversa. En cualquier caso, el procedimiento de ruteo es en sí mismo un problema de optimización basado en permutaciones. Por lo tanto en esta investigación, vamos más profundo en el uso de un algoritmo basado en poblaciones, más específicamente, un algoritmo de estimación de distribuciones EDA (por sus siglas en inglés Estimation of Distribution Algorithm) para este tema de


[^0]:    * Autor en correspondencia.

    Correos electrónico. ricardo.perez@cimat.ma (Ricardo PérezRodríguez), artha@cimat.ma (Arturo Hernández-Aguirre),

    URL: http://mmop.cimat.ma/ea/planta-docente-mmop (Ricardo Pérez-Rodríguez)

investigación logística. El EDA es un tipo de algoritmo de optimización basado en poblaciones que utiliza un modelo de probabilidad para producir nuevos descendientes en el proceso evolutivo. El modelo de probabilidad es construido en cada generación con información de las mejores soluciones. Aunque los EDAs fueron originalmente diseñados para resolver problemas con dominio de valores reales o enteros, estos no pueden producir un individuo factible de un modelo de probabilidad construido sobre un conjunto de permutaciones (Larrañaga and Lozano, 2002). En este contexto, un individuo factible en un tour para el SBRPBSS y un conjunto de permutaciones es un conjunto de tours de la población seleccionada. Además, el EDA requiere ser adaptado para la resolución con problemas basados en permutaciones por medio de una modificación en el proceso del algoritmo. Entonces, implementar un modelo de probabilidad específico para este tópico de investigación debería ser más competitivo contra otros modelos. Nuestro objetivo es utilizar la distribución generalizada de Mallows GMD (por sus siglas en inglés Generalized Mallows Distribution) como una forma de estimar una distribución de probabilidad explícita sobre el dominio de las permutaciones (Ceberio et al., 2014). Un primer intento de adaptar los EDAs a problemas basados en permutaciones se encuentra en Ceberio et al., (2011).

Contrario a la investigación actual donde diversas técnicas tales como búsqueda tabu (Pacheco et al., 2013), búsqueda adaptativa ávida aleatorizada (Schittekat et al., 2013), algoritmo de ramificación y acotamiento (Riera-Ledesma and SalazarGonzález, 2012), algoritmo genético (Díaz-Parra et al., 2013) y algoritmo basado en colonia de hormigas (Euchi and Mraihi, 2012) han sido propuestos para resolver el problema examinado, este artículo contribuye al estado del arte en lo siguiente: a) introducir la GMD, detallada en la investigación de Fligner and Verducci (1986), al SBRPBSS como una manera de estimar una distribución de probabilidad explícita sobre el dominio de las permutaciones. b) aplicar la GMD copulado con un EDA, llamado GMDEDA, para resolver el SBRPBSS. c) proponer una hibridación en el proceso del GMDEDA, llamado HGMDEDA, usando un operador de mutación para encontrar aún mejores soluciones para el SBRPBSS.

Existe muy poco trabajo relacionado sobre el EDA aplicado en el SBRPBSS. Por ejemplo, Pérez and Hernández (2016) proponen el enfoque más simple para estimar la distribución de probabilidad conjunta de los individuos seleccionados en cada generación. La distribución de probabilidad conjunta mencionada es factorizada como un producto de distribuciones marginales univariantes. Cada distribución marginal univariante es estimada con respectivas frecuencias marginales. Aunque el algoritmo propuesto por Pérez and Hernández (2016) es útil para el SBRPBSS, este no está en la misma dirección de esta investigación. Se busca una distribución de probabilidad explícita sobre un conjunto de rutas de autobuses escolares.

## 2. Revisión de la literatura

Aun cuando el SBRP fue formulado décadas antes, este es aún un tema de investigación significativa debido a su importante impacto en logística. Diversos estudios contienen una gran variedad de estrategias para resolver el SBRP. Una revisión de literatura reciente puede encontrarse en Park and Kim (2010). Avances en metaheurísticas ofrecen a la comunidad de investigadores nuevas técnicas para abordar problemas de
optimización combinatoria tales como el SBRPBSS. Kwan et al., (1999) describen un algoritmo genético para el problema de la programación de conductores de autobuses. El algoritmo propuesto construye a un programa para diversos vehículos el cual refleja la operación global y evoluciona a producir las mejores soluciones al explotar los rasgos combinatorios del problema. Suiter and Cooley (2001) proponen un algoritmo genético para el diseño eficiente de rutas de autobuses municipales. Los autores consideran atributos tales como los tipos de pasajeros, las distancias, los impedimentos en ciertos lugares, y la importancia de los sitios visitados para encontrar mejores rutas. Un análisis de sensibilidad es realizado al modificar la importancia de los atributos mencionados. Yoshihara (2003) presenta una aplicación de un algoritmo genético con heurísticas para programar un sistema de administración de autobuses a fin de satisfacer todas las condiciones de trabajo de los conductores, reducir el número de conductores tanto como sea posible, y disminuir la extensión de la jornada laboral entre todos los conductores. Los puntos débiles de las heurísticas son compensados por el algoritmo genético propuesto. Kliewer et al., (2006) discuten el problema de programación de autobuses con múltiples paraderos y flotas heterogéneas. Los autores utilizan una red basada en tiempo-espacio en vez de redes basadas en conexiones de las paradas para modelar el problema mencionado. El modelo propuesto resuelve instancias reales con miles de viajes programados al aplicar directamente software de optimización estándar. Otra investigación que usa la misma formulación de red tiempo-espacio es encontrada en Gintner et al., (2008) la cual intenta resolver el problema de programación de conductores en un caso de transporte público. Thangiah et al., (2008) presentan heurísticas para resolver un SBRP rural complejo usando redes de caminos digitalizados. La investigación considerada en Thangiah et al., (2008) es una flota mixta, con múltiples paraderos, y entregas parciales. Euchi and Mraihi (2012) resuelven el SBRP en áreas urbanas, como un caso de estudio en la ciudad de Tunez. Los autores utilizan un algoritmo basado en colonia de hormigas para hacer frente a este problema. Díaz-Parra et al., (2013) proponen la aplicación de un algoritmo bio-inspirado para el SBRP con características de una sola escuela, servicio urbano, carga mixta, estudiantes con condiciones especiales y flota homogénea de vehículos. Un conjunto de instancias de prueba para el SBRP fue desarrollado por los autores y dichas instancias fueron resueltas por medio del algoritmo genético propuesto. Schittekat et al., (2013) desarrollan un meta heurística para el SBRPBSS. La meta heurística propuesta, llamada búsqueda adaptativa ávida aleatorizada, usa un algoritmo de tipo exacto para resolver de forma óptima el subproblema de asignar estudiantes a paradas cuando las rutas ya están predefinidas. Los resultados de esta meta heurística sobre instancias generadas artificialmente son comparados con soluciones obtenidas por un método secuencial, con soluciones obtenidas al implementar un modelo de programación entera mixta en un software comercial, y con soluciones obtenidas con un enfoque de generación de columnas. Minocha and Tripathi (2014) describen un problema real del SBRP. Los autores desarrollan un plan de ruta para el servicio de autobuses escolares localizado en la ciudad de Rajasthan en la India, de manera que es capaz de servir a los estudiantes eficientemente con la máxima utilización de la capacidad de los autobuses utilizando un algoritmo genético híbrido para ello. Widuch (2012) propone un algoritmo correctivo de etiquetas para resolver el SBRP. La meta del algoritmo es encontrar una ruta que minimice el tiempo y el

costo del viaje simultáneamente. Esta investigación plantea un problema de optimización multicriterio MOP (por sus siglas en inglés Multicriteria Optimization Problem), donde la solución es un conjunto de soluciones no dominadas. El algoritmo hace posible encontrar todas las rutas que pertenecen al conjunto de soluciones no dominadas. Widuch (2013) propone un algoritmo correctivo de etiquetas con el almacenamiento de soluciones parciales para resolver el SBRP. Los resultados se comparan con los resultados para el SBRP donde el objetivo es reducir al mínimo sólo el tiempo y los costos de viaje y la longitud de la ruta no se toma en consideración.

Finalmente, la mayoría de los enfoques de solución mencionados anteriormente usan una representación con un conjunto de números. Cada número representa una parada de autobús. El orden de los números muestra un recorrido factible en el procedimiento de ruteo. En toda esta investigación actual, las paradas de autobús son independientes entre sí. Esto significa que cualquier parada de autobús se puede reubicar a otra posición en la secuencia con el fin de obtener mejores soluciones (mejores tours). Sin embargo, los artículos publicados consideran que el resto de las paradas de autobús no necesariamente se ven afectadas (influidas) por los procesos de reubicación comunes en las metaheurísticas. Para hacer frente a esta situación, este documento presenta un método para producir y mejorar el procedimiento de ruteo para el SBRPBSS por medio de una distribución de probabilidad explícita en el dominio de las rutas de transporte escolar.

## 3. Planteamiento del problema

El SBRP analizado sólo contiene una escuela, un solo tipo de estudiante, con autobuses escolares idénticos, cada uno con capacidad finita. La distancia total recorrida por todos los autobuses escolares es el objetivo a minimizar. La siguiente formulación, basada en Schittekat et al., (2013) y construida sobre la formulación de Toth and Vigo (2001), representa un modelo de optimización.
$\min \sum_{i \in V} \sum_{j \in V} d_{i j} \sum_{k=1}^{n} X_{i j k}$
s.a.

$$
\begin{array}{ll}
\sum_{j \in V} \boldsymbol{X}_{i j k}=\sum_{j \in V} \boldsymbol{X}_{j i k}=\boldsymbol{y}_{i k} & \forall i \in V, k=1, \ldots, n \\
\sum_{i, j \in E} \boldsymbol{X}_{i j k} \leq|E|-1 & \forall E \subseteq V \backslash\left\{v_{0}\right\}, \forall k \\
\sum_{k=1}^{n} \boldsymbol{y}_{i k} \leq 1 & \forall l \in S, \forall i \in V \\
\sum_{k=1}^{n} \boldsymbol{z}_{i l k} \leq \boldsymbol{z}_{i l} & \forall l \in S, \forall i \in V \\
\sum_{i \in V} \sum_{l \in S} \boldsymbol{z}_{i l k} \leq C & k=1, \ldots, n \\
\boldsymbol{z}_{i l k} \leq \boldsymbol{y}_{i k} & \forall i, l, k \\
\sum_{i \in V} \sum_{k=1}^{n} \boldsymbol{z}_{i l k}=1 & \forall l \in S
\end{array}
$$

$$
\begin{array}{ll}
\boldsymbol{y}_{i k} \in\{0,1\} & \forall i \in V, k=1, \ldots, n \\
\boldsymbol{X}_{i j k} \in\{0,1\} & \forall i, j \in V, i \neq j, k=1, \ldots, n \\
\boldsymbol{z}_{i l k} \in\{0,1\} & \forall i, j \in V, i \neq j, l \in S
\end{array}
$$

Los símbolos utilizados en el modelo matemático son
$C$ Capacidad del autobús escolar
$V$ Conjunto de paradas potenciales, con $|V|=n$
$E$ Conjunto de arcos entre paradas
$S$ Conjunto de estudiantes
$d_{i j}$ Distancia de traslado entre la parada $i$ y la parada $j$
$i=0$ Índice de la escuela
$x_{i j k}=1$ Si el autobús $k$ se traslada de la parada $i$ a $j, 0$ de otra forma
$y_{i k}=1$ Si el autobús $k$ visita la parada $i, 0$ de otra forma
$z_{i l k}=1$ Si el estudiante $l$ es recogido por el autobús $k$ en la parada $i, 0$ de otra forma
$x_{i l}=1$ Si el estudiante $l$ puede llegar a la parada $i, 0$ de otra forma

La función objetivo (1) minimiza la distancia total recorrida por todos los autobuses. Las restricciones (2) obligan a que si la parada $i$ es visitada por el autobús $k$, entonces un arco debe ser atravesado por el autobús $k$ ingresando a la parada $i$ y dejando la parada $i$, mientras que en (3) se impone la conectividad de la ruta realizada por el autobús $k$. Estas restricciones sirven para eliminar sub-tours. En (4) se garantiza que cada parada es visitada una vez como máximo, excepto por la parada que corresponde a la escuela. En (5) se asegura que cada estudiante es recogido en una parada la cual el(o ella) puede llegar. En (6) se confirma que la capacidad de los autobuses no es violada. En (7) se impone que el estudiante $l$ no es recogido en la parada $i$ por el autobús $k$ si dicho autobús $k$ no visita la parada mencionada $i$. En (8) se hace cumplir que cada estudiante es recogido una sola vez. Por último, las restricciones (9)-(11) establecen que todas las variables de decisión son binarias. Algunos supuestos están implícitos, e.g., una parada solamente es visitada por un solo autobús, lo que significa que el número de estudiantes no puede exceder la capacidad del autobús. También implica que los estudiantes que van a una parada no pueden ser divididos en grupos donde cada grupo tome un diferente autobús. Otro supuesto es que los autobuses tienen igual capacidad. Además, cada autobús ejecuta una sola ruta y cada estudiante cuenta como una unidad de demanda.

## 4. EDA para el SBRPSS

### 4.1. Procedimiento de selección de paradas

La primera instancia de Schittekat et al., (2013) contiene cinco paradas potenciales de autobús, siendo un total de seis paradas si

se considera la locación de la escuela, con veinticinco estudiantes a recoger, un límite de distancia a caminar de tan sólo cinco minutos por estudiante y una capacidad máxima de veinticinco estudiantes por autobús. Las ubicaciones de las paradas y de los estudiantes en la instancia mencionada se detallan a continuación en la Tabla 1 y 2 respectivamente.

Tabla 1: Ubicaciones de paradas en instancia 1 de Schittekat et al., (2013)


Tabla 2: Ubicaciones de estudiantes en instancia 1 de Schittekat et al., (2013)

El primer paso es la asignación de los estudiantes a las posibles paradas de autobús a través de un proceso iterativo en el que se asigna a cada estudiante a la primera parada de autobús del conjunto de posibles paradas y el número de estudiantes asignados se actualiza por cada parada para evitar exceder la capacidad de cualquier autobús escolar. Una parada de autobús se considera potencial cuando la restricción de distancia se satisface para cada estudiante. Por lo tanto, una parada de autobús puede ser potencial para un estudiante y no serlo para otros. El proceso iterativo se explica a continuación.

## Define DISTANCE

Define CAPACITY
for each student i do
for each student j do
length:=distance_between(location student $i$, bus stop location $j$ );
if(length $\leq$ DISTANCE $)$
feasible_matrix $(i, j):=1$;
else
feasible_matrix $(i, j):=0$;
endif
endfor
endfor
for each bus stop j do
load $(j):=0$;
endfor
for each student i do
Assigned $\approx 1$;
for each stop j do
If (feasible matrix $(i, j)==1$ ) and (load $(j)<$ CAPACITY)
Assigned $\approx j$;
break;
endif
endfor
load (Assigned): $=$ load (Assigned) $+1$;
endfor
Una asignación factible usando el proceso iterativo detallado anteriormente puede ser

Ejemplo 1
1111122222333334444455555
donde cada número representa la parada de autobús asignado a cada estudiante, es decir, parada de autobús 1 para el estudiante 1 , parada de autobús 1 para el estudiante 2 , y así sucesivamente.

### 4.2. Procedimiento de ruteo

El segundo paso es la construcción de rutas factibles. El procedimiento se detalla a continuación.

## Representación de la solución

Se adopta una representación basada en permutaciones, como en la mayoría de los algoritmos genéticos GA (por sus siglas en inglés Genetic Algorithm) para el problema del agente viajero TSP (por sus siglas en inglés Travelling Salesman Problem). La representación mencionada es un vector, que muestra un recorrido por todas las paradas de autobús previamente seleccionadas. En cada posición dentro del vector, un número de tipo entero representa una parada de autobús específica. Un vector es simplemente una secuencia de paradas de autobús (una permutación) $\sigma$ sin delimitadores en la ruta. Se puede interpretar como el orden en el que un autobús escolar debe visitar todas las paradas de autobús seleccionadas, si el mismo autobús escolar lleva a cabo todas las rutas de una en una. La aptitud $F(\sigma)$ de $\sigma$ es la distancia total recorrida.

De acuerdo con el procedimiento de selección descrito anteriormente, una representación puede ser

Ejemplo 2

donde el autobús escolar va a la parada de autobús número cuatro en el comienzo, después se va a la parada de autobús número dos, y así sucesivamente hasta que se retorna a la escuela (parada número cero), que no se muestra en la representación de la solución de esta investigación.

## Generación de la población inicial

La población se implementa como un conjunto de $M$ vectores de tamaño $n$ paradas de autobús. Cada vector se inicializa como una permutación aleatoria de las paradas de autobús previamente seleccionadas. A continuación se muestran algunos vectores

Ejemplo 3,


## Regla de selección

Todos $\operatorname{los} M$ vectores se consideran con el fin de construir el modelo de probabilidad. En consecuencia, la población seleccionada es una matriz de $N$ vectores de tamaño $n$ paradas de autobús, donde $N=M$.

## Modelo de probabilidad

El modelo Mallows fue propuesto inicialmente por Mallows (1957), y posteriormente mejorado por Fligner and Verducci (1986) a través de la GMD. El modelo Mallows y la GMD se pueden utilizar para resolver problemas de optimización basados en permutaciones. Recientemente, Ceberio et al., (2014) contribuyen con una aplicación inicial de la GMD para resolver el problema de programación de trabajos en configuración jobshop usando EDAs.

Formalmente, el modelo de Mallows es definido como

$$
P(\sigma)=\psi(\theta)^{-1} e^{-\theta D\left(\sigma, \sigma_{0}\right)}
$$

donde $\theta$ es un parámetro de forma, y $D\left(\sigma, \sigma_{0}\right)$ es la distancia de una permutación dada $\sigma$ a la permutación central representada por $\sigma_{0}$, y donde $\psi(\theta)$ es una constante de normalización. En el presente estudio, la métrica de distancia Kendall-tau es con la cual el modelo de Mallows es copulado.

La GMD es una extensión del modelo de Mallows (Fligner and Verducci, 1986). La GMD es descrita como sigue
$P(\sigma)=\psi(\theta)^{-1} e^{\sum_{j=1}^{N-1} \theta_{j} V_{j}\left(\sigma, \sigma_{0}\right)}$
donde $V_{j}\left(\sigma, \sigma_{0}\right)$ es el número de posiciones a la derecha de $j$ con valores más pequeños que la posición actual en la permutación $\left(\sigma, \sigma_{0}\right)$. Una amplia explicación de la GMD y sus características se encuentra en Fligner and Verducci (1986) y en Fligner and Verducci (1988). Basado sobre la investigación de los artículos citados, es posible obtener cualquier permutación $\left(\sigma, \sigma_{0}\right)$ con $n-1$ enteros $V_{1}\left(\sigma, \sigma_{0}\right), \ldots, V_{n-1}\left(\sigma, \sigma_{0}\right)$ en la cual la distancia Kendall-tau $D_{c}\left(\sigma, \sigma_{0}\right)$ se descompone. Bajo la distribución uniforme, las variables $V_{j}\left(\sigma, \sigma_{0}\right)$ que definen una permutación son independientes (Fligner and Verducci, 1986) y, como consecuencia, la distribución de probabilidad de las variables aleatorias $V_{j}\left(\sigma, \sigma_{0}\right)$ bajo la GMD está dada por la ecuación (13).

La constante de normalización $\psi(\theta)$ en la GMD puede ser simplificada como el producto de $n-1$ términos
$\psi(\theta)=\prod_{j=1}^{n-1} \psi_{j}\left(\theta_{j}\right)=\prod_{j=1}^{n-1} \frac{1-e^{-\theta_{j}(n-j+1)}}{1-e^{-\theta_{j}}}$
donde $n$ es el total de elementos en la permutación. Cuando la GMD considera la distancia Kendall-tau, entonces la GMD puede ser expresada como un modelo clasificador de múltiples etapas (Fligner and Verducci, 1988). Por lo tanto, la distribución de probabilidad de una permutación dada $\sigma$ es
$P(\sigma)=\prod_{j=1}^{n-1} P\left(V_{j}\left(\sigma, \sigma_{0}\right)=r_{j}\right)$
donde $r_{j}$ es un valor posible para la posición $j$ en la permutación.

Proceso de muestreo (generación de nuevos individuos)

## Estimación de la permutación central

La primera etapa consiste en calcular una aproximación a la permutación central. Utilizamos el algoritmo de Borda (1784). El algoritmo calcula la permutación media de una muestra dada que es, de hecho, un estimador consistente de la permutación central (Fligner and Verducci, 1986). Su pseudo-código se detalla a continuación.
from the population of $N$ permutations $\left\{\sigma_{1}, \ldots, \sigma_{N}\right\}$ for $j \equiv 1$ to $n$

$$
\pi(j):=\frac{\sum_{i=1}^{N} \sigma_{i}(j)}{N}
$$

endfor

$$
\begin{aligned}
& \text { visited }:=\{\varnothing\} \\
& \text { for } j \approx 1 \text { to } n \\
& \quad \min \leftarrow \arg \min _{i}\{\pi(i) \mid i \notin \text { visited }\} \\
& \quad \sigma_{0}(\min ) \approx j ; \\
& \quad \text { visited } \leftarrow \text { visited } \cup \min \\
& \text { endfor }
\end{aligned}
$$

## Mejorando la permutación central

Aunque el comportamiento del algoritmo propuesto depende del vector $\theta$ que determina la forma de la distribución en el GMDEDA, consideramos que el algoritmo mejora su desempeño con algún tipo de mutación sólo aplicada a la permutación central $\sigma_{0}$. Cada iteración del procedimiento de mutación analiza todos los posibles pares de distintas paradas de autobús $(u, v)$. Para cada par, donde $x$ e $y$ son los sucesores de $u$ y $v$, los siguientes movimientos son aplicados.

Remove $u$ then insert it after $v$,
Swap $u$ and $v$,
Swap $(u, x)$ and $v$,
Swap $(u, x)$ and $(v, y)$.
Si hay una mejora en algunos de los movimientos detallados anteriormente, la permutación central es entonces modificada. En el mejor de nuestro conocimiento, una modificación en el parámetro descrito no se ha desarrollado a través de este tipo de algoritmos. Ceberio et al., (2014) utilizan un mecanismo de reinicio cuando la aptitud de todos los individuos es la misma. El mecanismo de reinicio genera nueva población mediante cinco movimientos de inserción al azar sobre el mejor individuo. A diferencia de la investigación de Ceberio et al., (2014), en esta investigación se desea evitar la pérdida de la diversidad a través de la modificación de la permutación central, no en el mejor individuo.

## Estimación del vector de forma $\theta$

Una vez que la permutación central $\sigma_{0}$ es aproximada y mejorada, la segunda etapa consiste en estimar el vector parámetro de forma de la distribución $\theta_{j}$ al resolver
$V_{j}=\frac{1}{e^{\theta_{j}}-1}-\frac{n-j+1}{e^{\theta_{j}(n-j+1)}-1}, j=1: n-1$
donde
$V_{j}=\frac{1}{N} \sum_{i=1}^{N} V_{j}\left(\sigma_{i} \sigma_{0}^{-1}\right)$

Finalmente, el proceso de generar nuevos descendientes es aplicando la GMD, y decodificando los vectores $V\left(\sigma, \sigma_{0}\right)$ a través del uso del algoritmo de Meila et al., (2007).

De esta forma, el modelo de probabilidad describe las características exhibidas por los padres como una distribución del espacio de soluciones. Por lo tanto, en el algoritmo propuesto no es necesario mantener los miembros de la población para realizar un seguimiento y heredar las características mencionadas en cada generación. Las características persisten por todos los miembros de la población en el progreso evolutivo gracias al modelo de probabilidad.

## Criterio de partición para las rutas

Teniendo la secuencia de paradas de autobús (permutación) $\sigma_{s}$ obtenida por la GMD, ahora llamada simplemente $\pi$ de tamaño $n$, un procedimiento debe realizarse con el fin de obtener las rutas viables para todos los vehículos necesarios. Debido a que una secuencia se puede dividir en muchas rutas diferentes, Prins (2004) propuso un procedimiento de partición que puede encontrar una división óptima, es decir, un delimitador de viaje de modo que la distancia total recorrida se reduce al mínimo. Una modificación del procedimiento de Prins (2004) se utiliza en esta investigación. Sin pérdida de generalidad, sea $\pi=\{1,2,3, \ldots, n\}$ una secuencia dada. Considere un grafo auxiliar $H=(V, E)$ donde $V=\{0,1,2 \ldots n\}$. Un arco $(i, j) \in E$. Dos etiquetas $V_{j}$ y $P_{j}$ para cada vértice $j$ en $\pi$ son estimados. $V_{j}$ es la distancia total recorrida de la trayectoria más corta desde el nodo 0 al nodo $j$ en $H$, y $P_{j}$ es el vértice predecesor de $j$ sobre dicha trayectoria. La distancia total de recorrido se da al final de $V_{n}$. Para cualquier vértice $i$, el incremento de paradas
$j$ en dicha ruta se detiene cuando la capacidad $Q$ del autobús es excedida. La modificación del procedimiento de Prins (2004) se describe como sigue.

$$
\begin{aligned}
V_{0} & \approx 0 \\
\text { for } i & \approx 1 \text { to } n \text { do } \\
V_{i} & \approx+\infty
\end{aligned}
$$

endfor
for $i \approx 1$ to $n$ do
traveled_distance $\approx 0$; load $\approx 0 ; j \approx i$;
repeat
load $\approx \operatorname{load}+q_{\pi_{j}}$;
if $(i==j)$ then
traveled_distance $\approx d_{0, \pi_{j}}+d_{\pi_{j}, 0}$;
else
traveled_distance $\approx$ traveled_distance $\cdot d_{\pi_{j-1}, 0}+d_{\pi_{j-1}, \pi_{j}}+d_{\pi_{j}, 0}$;
endif
if (load $<Q$ ) then
if $\left(V_{i-1}+\right.$ traveled_distance $\left.<V_{j}\right)$ then
$V_{j} \approx V_{i-1}+$ traveled_distance;

$$
P_{j} \approx i-1
$$

endif
$j \approx j+1$;
endif
until $(j>n)$ or (load $>Q$ )
endfor
donde $q_{\pi_{j}}$ significa el número de estudiantes asignados a la $\pi_{j}$ posición (parada) en la permutación. $d_{0, \pi_{j}}$ significa la distancia de la escuela (parada 0 ) a la $\pi_{j}$ posición en la permutación. $d_{\pi_{j}, 0}$ lo opuesto. $d_{\pi_{j-1}, \pi_{j}}$ es la distancia de la parada previa $\pi_{j-1}$ a la actual $\pi_{j} . Q$ es la capacidad del autobús.

El vector de etiquetas $P_{j}$ es mantenido junto con la secuencia para extraer la solución del problema bajo estudio, i.e., el SBRPBSS. El procedimiento construye $t$ rutas. Cada ruta es una lista de paradas. La función insertqueue adjunta una parada al final de la ruta. El procedimiento de partición de Prins (2004) es mostrado a continuación.

```
for \(i \approx 1\) to \(n\) do
    route(i) \(\approx 0\);
endfor
\(t \approx 0\)
\(j \approx n\)
repeat
    \(t \approx t+1 ;\)
    \(i \approx P_{j}\)
    for \(k \approx i+1\) to \(j\) do
        insertqueue(route(t), \(\pi_{k}\) )
    endfor
    \(j \approx i\)
until \(i==0\)
```


## Criterio de paro y tamaño de población

El número de generaciones es considerado como criterio de paro, basado en la investigación de Chakraborty and Dastidar (1993). Cien generaciones son establecidas en esta investigación y mil vectores son usados como tamaño de población. El algoritmo propuesto es detallado a continuación.
$D_{0} \leftarrow$ Generar $M$ individuos basado en el 4.1
$D_{0} \leftarrow$ Generar $M$ individuos basado en permutaciones aleatorias considerando las paradas elegidas previamente
$g \leftarrow 1$
Hacer $\{$
$D_{g-1} \leftarrow$ Evaluar individuos (calcular distancia total)
$D_{g-1}^{S e} \leftarrow$ Seleccionar $N=M$ individuos a partir de $D_{g-1}$
$\sigma_{0} \leftarrow$ Estimar la permutación central a partir de $D_{g-1}^{S e}$

$$
\begin{aligned}
& \sigma_{0} \leftarrow \text { Mejorar } \sigma_{0} \text { (hibridación) } \\
& \theta \leftarrow \text { Estimar el vector de forma } \\
& D_{g} \leftarrow \text { Muestrear } M \text { individuos a partir de } p\left(\sigma \mid D_{g-1}^{S e}, \sigma_{0}, \theta\right) \\
& D_{g} \leftarrow \text { Decodificar } D_{g} \\
& D_{g} \leftarrow \text { Partir } D_{g} \text { en } t \text { rutas basado en el 4.2.6 } \\
& g \leftarrow g+1 \\
& \text { \{ Hasta que el número de generaciones es alcanzado }
\end{aligned}
$$

## 5. Resultados y comparación

Las instancias de Schittekat et al., (2013) sirvieron como parámetro de entrada y prueba para producir y mejorar el procedimiento de ruteo en el SBRPBSS por medio de una distribución de probabilidad explícita en el dominio de las rutas de transporte escolar. Las instancias mencionadas anteriormente consideran desde 5 paradas con 25 estudiantes a 80 paradas con 800 estudiantes. Además, se consideran cuatro distancias máximas para caminar por parte de los estudiantes como restricción: 5, 10, 20 y 40 min . La distancia máxima para caminar determina en gran medida el número de paradas que el estudiante promedio es capaz de caminar. Las Tablas 3 - 7 proporcionan detalles sobre las instancias y muestra para cada instancia nueve columnas: instancia (columna id), el número de paradas (columna stop), el número de alumnos (columna stud), la capacidad del autobús (columna cap) y la distancia máxima a caminar (columna wd). Las Tablas mencionadas también detallan los resultados de un algoritmo genético (columna GA) y el algoritmo de estimación de distribuciones marginal univariado (columna UMDA por sus siglas en inglés Univariate Marginal Distribution Algorithm). Estos algoritmos se proponen como punto de referencia para la comparación con el esquema del EDA (columna GMDEDA). Además, las Tablas mencionadas muestran los resultados del EDA propuesto haciendo uso de la etapa de hibridación (columna HGMDEDA), es decir, la mejora a la permutación central obtenida por el algoritmo Borda (1784). Todos estos algoritmos, i.e., GA, UMDA, GMDEDA y HGMDEDA se obtuvieron mediante la programación y ejecución de los autores utilizando el lenguaje $\mathrm{C}++$.

Para dar cuenta de la naturaleza estocástica del problema, se realizan 30 ensayos para todos los algoritmos en todos los casos.

En general, el esquema del HGMDEDA produce resultados competitivos basados en la aptitud obtenida, como se muestra en 98 de los 112 casos indicados en negrita en Tablas 3 - 7. Un resultado competitivo significa que el HGMDEDA consigue un mejor valor u obtiene el mismo mejor valor que encuentran los otros algoritmos, i.e., GA, UMDA y GMDEDA. En Tablas 3 - 7 se puede apreciar cómo el modelo de probabilidad utilizado en ambos algoritmos, i.e., la GMDEDA y la HGMDEDA, son capaces de detectar secuencias competitivas para el SBRPBSS.

En Tabla 3, donde el número de paradas potenciales es 5, el HGMDEDA encuentra una aptitud competitiva en 22 de los 24 casos en comparación con los algoritmos propuestos como punto de referencia. Cuando el número de paradas posibles es 10 , entonces 21 de los 24 casos el HGMDEDA consigue una aptitud competitiva en comparación con el GA, UMDA y GMDEDA. Véase Tabla 4. Además, el GMDEDA consigue un resultado competitivo (19 de 24 casos) en el mismo número de posibles paradas de autobús. Si el número de paradas posibles es 20 , el

HGMDEDA encuentra resultados competitivos en 22 de los 24 casos, mientras que el GMDEDA lo obtiene en 20 de los 24 . Véase Tabla 5. Cuando el número de paradas es de 40, la HGMDEDA produce resultados idóneos en 20 de los 24, mientras que el GMDEDA los produce solamente en 9 de 24. Véase Tabla 6. Finalmente, para 80 paradas, la HGMDEDA produce buenos resultados en 13 de los 16 casos, mientras que el GMDEDA lo hace sólo en 8 de 16. Véase Tabla 7. A pesar de que el desempeño de los algoritmos propuestos como punto de referencia es aceptable, el HGMDEDA continúa logrando resultados competitivos contra estos algoritmos aun cuando el número de paradas es mayor que 20. Esto significa que cuando el número de paradas aumenta de 20 a 80, el HGMDEDA es capaz de identificar una mejor posición para cada parada de autobús en la secuencia para reducir la distancia recorrida por los autobuses. Por otra parte, 11 resultados del HGMDEDA (de un total de 48 casos) están solamente un 20 por ciento por encima del resultado del algoritmo de Schittekat et al., (2013) cuando el número de paradas es de 5 a 10 . Si el número de paradas es de 20, 40 y 80 , entonces 49 resultados HGMDEDA (de un total de 64 casos) están solamente un 20 por ciento por encima del resultado del algoritmo de Schittekat et al., (2013). Esta situación se explica por el aumento de número de paradas y porque todas las instancias están utilizando el mismo modelo de probabilidad. Los autores creen que la identificación de relaciones de orden superior ayudará a reducir el valor actual de la distancia recorrida por los autobuses hasta ahora obtenido para cada instancia por medio de un modelo de probabilidad más avanzado. Sin embargo, los resultados obtenidos por el GMDEDA y el HGMDEDA demuestran que la aplicación de una distribución de probabilidad explicita en el dominio de las rutas de autobuses escolares también puede mejorar la aptitud significativamente frente al GA y el UMDA. Por otra parte, se evita perdida de diversidad por medio del procedimiento de mutación que contribuye a una reducción adicional del valor de la distancia recorrida por los autobuses.
![img-0.jpeg](img-0.jpeg)

Figura 1: Prueba de Dunnett para comparación múltiple.

Además, la calidad de las soluciones ofrecida por el HGMDEDA es estable con respecto a los otros algoritmos. Para mostrarlo, se realiza una prueba de comparación múltiple sobre la diferencia de medias que ofrece el HGMDEDA con respecto a los demás algoritmos. La Figura 1 detalla la prueba de Dunnett. A partir de la Figura 1 se puede visualizar que no existe diferencia estadísticamente significativa entre la calidad de las soluciones usando el HGMDEDA y los algoritmos utilizados en la comparativa.
![img-1.jpeg](img-1.jpeg)

Figura 2: Robustez y sensibilidad de los resultados obtenidos frente a incertidumbres del tráfico.

Ahora bien, sobre la robustez y sensibilidad de los resultados obtenidos frente a incertidumbres del tráfico, las instancias se modifican sobre los tiempos de traslado para cada caso en hasta un $25 \%$ del tiempo original. Esto con el fin de conocer qué implicaciones puede tener la incertidumbre del tráfico con respecto a la calidad de las soluciones obtenidas usando el HGMDEDA. La Figura 2 la prueba de Dunnett donde se aprecia que no hay diferencia estadísticamente significativa con respecto a las soluciones ofrecidas por el HGMDEDA aun cuando la incertidumbre está presente. Nuevamente se considera estable el algoritmo propuesto.

Tabla 3: Resultados comparativos en 5 paradas potenciales con instancias de Schittekat et al., (2013)


Tabla 4: Resultados comparativos en 10 paradas potenciales con instancias de Schittekat et al., (2013)


Tabla 5: Resultados comparativos en 20 paradas potenciales con instancias de Schittekat et al., (2013)


Tabla 6: Resultados comparativos en 40 paradas potenciales con instancias de Schittekat et al., (2013)

Tabla 7: Resultados comparativos en 80 paradas potenciales con instancias de Schittekat et al., (2013)

Tabla 7: Resultados comparativos en 80 paradas potenciales con instancias de Schittekat et al., (2013)


## 6. Discusión y trabajo futuro

Basados en los resultados descritos en la sección previa no es necesario reparar las soluciones como otros algoritmos que se han utilizado para problemas de optimización basados en permutaciones. El GA y el UMDA emplean operadores específicos para mantener la diversidad en el progreso evolutivo. Estos operadores son útiles en problemas de optimización basados en permutaciones, pero no son capaces de construir una distribución de probabilidad explícita en el dominio de las rutas de transporte escolar. Podemos considerar que una ventaja del GMDEDA y del HGMDEDA es que toman en consideración la GMD para resolver esta situación. Gracias al uso de la GMD es posible estimar la probabilidad de que la parada $i$ sea elegida en la posición $j$ de la secuencia; sin embargo, para construir secuencias más amplias, i.e., mayor número de vértices, la GMD sin hibridación podría ser una desventaja.

Aunque los algoritmos utilizados en esta investigación no son capaces de manejar entradas inválidas o inesperadas, y el método propuesto se encuentra actualmente en la fase de prototipo para los usuarios, se espera que los profesionales y/o académicos encuentren el EDA beneficioso para sus escuelas cuando esté listo para su utilización debido a que el EDA puede ser modificado con el fin de obtener un módulo para los usuarios en entornos escolares.

Los trabajos de investigación futura deben considerar un módulo para usuarios, y deben incluir el tiempo computacional y aspectos económicos. Los tiempos de cálculo y los costos no fueron considerados en esta investigación debido a que el algoritmo propuesto se encuentra actualmente en la fase de

prototipo. Por último, esta investigación se centra solamente en las instancias de Schittekat et al., (2013). Sin embargo, el número de paradas de autobús parece variar significativamente en múltiples entornos escolares. La asignación dinámica de la correcta parada de autobús a la posición correcta en la secuencia también afecta el valor de aptitud, y esto sigue siendo un tema para futuras investigaciones. Además, esta investigación debe ampliarse para tener en cuenta otros factores de retraso, tales como el tránsito, ausentismos en los conductores, y otros cambios que pueden abordarse mediante el desarrollo de una versión dinámica del EDA y así regular el flujo vehicular de los autobuses basados en simulaciones partiendo de la investigación de Aquino et al., (2009).

La investigación a futuro puede tratar con una extensión del EDA que utilice modelos de probabilidad de orden superior para representar las interacciones más complejas o las relaciones entre las variables del problema enunciado. Se requieren módulos eficaces para usuarios específicos en las escuelas, y aprender acerca de los modelos probabilísticos sería útil para mejorar el modelado del problema mencionado. Por último, la literatura aun no considera la interacción que existe entre las paradas de autobús con otros temas de planeación relacionados, por medio de un modelo de probabilidad, y valdría la pena proporcionar un enfoque diferente, que integre las decisiones sobre estos temas de planeación con el fin de reducir al mínimo la distancia total recorrida.

## 7. Conclusiones

Este artículo trata sobre el problema de ruteo de autobuses escolares con selección paradas, donde se tienen tres cuestiones separadas pero relacionadas entre sí: (1) determinar el conjunto de paradas a visitar, (2) establecer para cada estudiante a qué parada deberá dirigirse a esperar un autobús, y (3) diseñar rutas con las paradas de autobuses elegidas, tal que la distancia total de viaje es minimizada. Para solucionar este problema se propone la aplicación del HGMDEDA. Por medio de experimentos numéricos se mostró que este enfoque genera mejores soluciones a los generados por una GA, UMDA y GMDEDA. La implementación de estas soluciones puede mejorar el servicio al cliente mediante la entrega a los estudiantes a tiempo y evitando retrasos en otras etapas del proceso. El HGMDEDA puede detectar las relaciones o interacciones entre las paradas de autobús y puede mejorar significativamente el desempeño por medio de un modelo de probabilidad explícito. Desde que el HGMDEDA presenta estabilidad basados en Figura 1 y 2, parece muy adecuado para su aplicación en software para fines prácticos. Los resultados actuales incluyen varias instancias que detallan el potencial del enfoque HGMDEDA para resolver el SBRPBSS. Los resultados fomentan el desarrollo de un método de optimización eficaz basado en un modelo de probabilidad para resolver problemas de transporte escolar del mundo real, que por lo general se producen en entornos dinámicos donde la eficiencia es prevalente.

## English Summary

An estimation of distribution algorithm coupled with the generalized Mallows distribution for a school bus routing problem with bus stop selection.

## Abstract

Although the estimation of distribution algorithms were originally designed for solving integer or real-valued domains, this contribution applies the algorithms mentioned to deal with a permutation-based problem, called school bus routing problem with bus stop selection, using the generalized Mallows distribution as an attempt to describe and obtain an explicit probability distribution over a set of school bus routes. In addition, a mutation operator is considered for improving the estimation of the central permutation, a parameter of the Mallows distribution. Different and diverse instances served as input and test parameters in order to show that permutation-based optimization problems such as the school bus routing problem with bus stop selection can be solved by means of a probability model, and improving the estimation of the central permutation helps the performance of the algorithm.

## Keywords:

Estimation of distribution algorithm, Mallows distribution, vehicle routing problem, school bus routing problem.

## Agradecimientos

Un agradecimiento a los revisores de este artículo por sus valiosas aportaciones.

## Referencias

Afifi S., Dang D.-C., Moukrim, A., 2015. Heuristic solutions for the vehicle routing problem with time windows and synchronized visits. Optimization Letters, DOI 10.1007/s11590-015-0878-3.
Aquino-Santos R., González-Potes A., Villaseñor-González L.A., Crespo A., Sánchez J., Gallardo J.R., 2009. Simulación de Algoritmos para regular el Flujo Vehicular y la Comunicación entre Vehículos Móviles Autónomos utilizando Redes Ad Hoc. RIAI 6(1), 75-83.
Barbucha D., 2014. Team of A-Teams Approach for Vehicle Routing Problem with Time Windows. In Terrazas G., Otero F., Masegosa A., (Eds.), Nature Inspired Cooperative Strategies for Optimization (NICSO 2013), Springer International Publishing, Vol. 512, pp. 273-286.
Berghida M., Boukza A., 2015. UBBO: an enhanced biogeography-based optimization algorithm for a vehicle routing problem with heterogeneous fleet, mixed backhauls, and time windows. The International Journal of Advanced Manufacturing Technology 77(9-12), 1711-1725.
Borda J., 1784. Memoire sur les elections au scrutin. Histoire de l'Academie Royale des Science.
Ceberio J., Irurozki E., Mendiburu A., Lozano J., 2014. A distance-based ranking model estimation of distribution algorithm for the flowshop scheduling problem. IEEE Transaction on evolutionary computation 18(2), 286-300.
Ceberio J., Mendiburu A., Lozano J., 2011. Introducing the Mallows Model on Estimation of Distribution Algorithms. In Bao-Liang L., Liquig Z., Kwok J., (Eds.), Neural Information Processing. 18th International Conference ICONIP 2011, Shanghai China, Berlin: Springer Berlin Heidelberg, pp. 461-470.
Chakraborty, U.K., Dastidar, D.G., 1993. Using reliability analysis to estimate the number of generations to convergence in genetic algorithms. Information Processing Letters. 46, 199-209.
Cruz-Ramirez N., Martinez-Morales M., 1997. Un algoritmo para generar redes Bayesianas a partir de datos estadísticos. Primer Encuentro Nacional de Computación, ENC 97. Querétaro, México.

de Armas J., Melián-Batista B., 2015. Constrained dynamic vehicle routing problems with time windows. Soft Computing, DOI 10.1007/s00500-0141574-4.
Díaz-Parra O., Ruiz-Vanoye J., Buenabad-Arias M., Canepa-Saenz A., 2013. Vertical Transfer Algorithm for the School Bus Routing Problem. In Gavrilova M., Tan C., Abraham A., (Eds.), Transactions on Computational Science XXI, Springer Berlin Heidelberg, Vol. 8160, pp. 211-229.
Euchi J., Mraibi R., 2012. The urban bus routing problem in the Tunisian case by the hybrid artificial ant colony algorithm. Swarm and Evolutionary Computation 2, 15-24.
Fligner M., Verducci J., 1986. Distance based ranking models. J. Royal Stat. Soc. 48(3), 359-369.
Fligner M., Verducci J., 1988. Multistage ranking models. J. Amer. Stat. Assoc. 83(403), 892-901.
Gan X., Kuang J., Niu B., 2014. Multi-type Vehicle Routing Problem with Time Windows. In Huang D.-S., Jo K.-H., Wang L., (Eds.), Intelligent Computing Methodologies, Springer International Publishing, Vol. 8589, pp. 808-815.
Gintner V., Kliewer N., Suhl L., 2008. A Crew Scheduling Approach for Public Transit Enhanced with Aspects from Vehicle Scheduling. In Hickman M., Mirchandani P., Voß S., (Eds.), Computer-aided Systems in Public Transport, Springer Berlin Heidelberg, Vol. 600, pp. 25-42.
Kliewer N., Mellouli T., Suhl L., 2006. A time-space network based exact optimization model for multi-depot bus scheduling. European Journal of Operational Research 175(3), 1616-1627.
Kwan A., Kwan R., Wren A., 1999. Driver Scheduling Using Genetic Algorithms with Embedded Combinatorial Traits. In Wilson N., (Ed.), Computer-Aided Transit Scheduling, Springer Berlin Heidelberg, Vol. 471, pp. 81-102.
Larrahaga P., Lozano J., 2002. Estimation of distribution algorithms: a new tool for evolutionary computation. Kluwer Academic Publishers.
Li J., Li Y., Pardalos P., 2014. Multi-depot vehicle routing problem with time windows under shared depot resources. Journal of Combinatorial Optimization, DOI 10.1007/s10878-014-9767-4.
Mallows C., 1957. Nonnull ranking models. Biometrika 44(1-2), 114-130.
Meila M., Phadnis K., Patterson A., Bilmes J., 2007. Consensus ranking under the exponential model. Proc. 22nd Conf. Uncertainty Artif. Intell., Vancouver, pp. 285-294.
Minocha B., Tripathi S., 2014. Solving School Bus Routing Problem Using Hybrid Genetic Algorithm: A Case Study. In Babu B., Nagar A., Deep K., Pant M., Bansal J., Ray K., Gupta U., (Eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving SocProS 2012, Springer India, Vol. 236, pp. 93-103.
Nalepa J., Blocho M., 2015. Adaptive memetic algorithm for minimizing distance in the vehicle routing problem with time windows. Soft Computing, DOI 10.1007/s00500-015-1642-4.
Niu H., 2013. Application of Genetic Algorithm to Optimize Transit Schedule under Time-Dependent Demand. In Wang W., Wets G., (Eds.), Computational Intelligence for Traffic and Mobility, Atlantis Press, Vol. 8, pp. 71-88.
Pacheco J., Caballero R., Laguna M., Molina J., 2013. Bi-Objective Bus Routing: An Application to School Buses in Rural Areas. Transportation Science 47(3), 397-411.

Park J., Kim B., 2010. The school bus routing problem: A review. European Journal of Operational Research 202(2), 311-319.
Pérez-Rodríguez R., Hernández-Aguirre A., 2016. Probability model to solve the school bus routing problem with stops selection. International Journal of Combinatorial Optimization Problems and Informatics 7(1), 30-39.
Prins C., 2004. A simple and effective evolutionary algorithm for the vehicle routing problem. Computers \& Operations Research 31(12), 1985-2002.
Riera-Ledesma J., Salazar-González J., 2012. Solving school bus routing using the multiple vehicle traveling purchaser problem: A branch-and-cut approach. Computers \& Operations Research 39(2), 391-404.
Schittekal P., Kinable J., Sörensen K., Sevaux M., Spieksma F., Springad J., 2013. A metaheuristic for the school bus routing problem with bus stop selection. European Journal of Operational Research 229(2), 518-528.
Schwarze S., Voß S., 2015. A Bicriteria Skill Vehicle Routing Problem with Time Windows and an Application to Pushback Operations at Airports. In Dethloff J., Haasis H.-D., Kopfer H., Kotzab H., Schönberger J., (Eds.), Logistics Management (Vols. Products, Actors, Technology - Proceedings of the German Academic Association for Business Research, Bremen, 2013), Springer International Publishing, pp. 289-300.

Soonpracha K., Mungwattana A., Manisri T., 2015. A Re-constructed MetaHeuristic Algorithm for Robust Fleet Size and Mix Vehicle Routing Problem with Time Windows under Uncertain Demands. In Handa H., Ishibuchi H., Ong Y.-S., Tan K.-C., (Eds.), Proceedings of the 18th Asia Pacific Symposium on Intelligent and Evolutionary Systems, Springer International Publishing, Vol. 2, pp. 347-361.
Suiter J., Cooley D., 2001. Optimal Municipal Bus Routing Using a Genetic Algorithm. In Kůrková V., Neruda R., Kárný M., Steele N., (Eds.), Artificial Neural Nets and Genetic Algorithms, Springer Vienna, pp. 312315.

Thangiah S., Fergany A., Wilson B., Pituga A., Mennell W., 2008. School Bus Routing in Rural School Districts. In Hickman M., Mirchandani P., Voß S., (Eds.), Computer-aided Systems in Public Transport, Springer Berlin Heidelberg, Vol. 600, pp. 209-232.
Toth P., Vigo D., (Eds.), 2001. The Vehicle Routing Problem. Philadelphia, PA, USA: SIAM Monographs on Discrete Mathematics and Applications. Society for Industrial and Applied Mathematics.
Widuch J., 2012. A label correcting algorithm for the bus routing problem. Fundamenta Informaticae 118(3), 305-326.
Widuch J. 2013. A label correcting algorithm with storing partial solutions to solving the bus routing problem. Informatica 24(3), 461-484.
Yang C., Guo Z.-x., Liu, L.-y., 2015. Comparison Study on Algorithms for Vehicle Routing Problem with Time Windows. In Qi E., Shen J., Dou R., Proceedings of the 21st International Conference on Industrial Engineering and Engineering Management 2014, Atlantis Press, pp. 257-260.
Yoshihara I., 2003. Scheduling of Bus Drivers' Service by a Genetic Algorithm. In Ghosh A., Tsutsui S., (Eds.), Advances in Evolutionary Computing, Springer Berlin Heidelberg, pp. 799-817.Able, B., 1945. Nombre del artículo. Nombre de la revista 35, 123-126. DOI: 10.3923//jbc.2010.190.202