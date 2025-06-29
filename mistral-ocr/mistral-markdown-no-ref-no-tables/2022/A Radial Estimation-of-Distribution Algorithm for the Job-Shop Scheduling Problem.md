# A Radial Estimation-of-Distribution Algorithm for the Job-Shop Scheduling Problem 

Ricardo Pérez-Rodríguez, National Council for Science and Technology, Mexico \& Autonomous University of Queretaro, Mexico*


#### Abstract

The job-shop environment has been widely studied under different approaches. Its practical characteristics make its research interesting. Therefore, the job-shop scheduling problem continues being attractive in developing new evolutionary algorithms. In this paper, the authors propose a new estimation of distribution algorithm coupled with a radial probability function. The aforementioned radial function comes from the hydrogen element. This approach is proposed in order to build a competitive evolutionary algorithm for the job-shop scheduling problem. The key point is to exploit the radial probability distribution to construct offspring and to tackle the inconvenient of the EDAs (i.e., lack of diversity of the solutions and poor ability of exploitation). Various instances and numerical experiments are presented to illustrate and to validate this novel research. The results, obtained from this research, permit the conclusion that using radial probability distributions is an emerging field to develop new and efficient EDAs.


## KEYWORDS

Estimation of Distribution Algorithm, Evolutionary Computing, Hydrogen Element, Job-Shop Scheduling Problem, Radial Probability Distribution

## 1. INTRODUCTION

Estimation of Distribution Algorithms (EDAs) have been widely published in more than two decades. These algorithms have shown to be efficient to solve optimization problems. In addition, these algorithms have been used to tackle combinatorial problems. It can be considered that there are two classifications for the EDAs, i.e., pure EDAs and hybrid EDAs.

Pure EDAs base their performance on a probability model to find new solutions from previous solutions meanwhile hybrid EDAs base their performance on an interaction between a probability model and some another technique or method to generate offspring or to improve the performance of the algorithm. As hybrid EDAs is considered the Peña et al's (2004) research for solving synthetic optimizations problems. The Zhang et al's (2006) algorithm for the quadratic assignment problem. The Liu et al's (2011) study for the permutation flow-shop scheduling problem. The Wang's (2012) method for the flexible job-shop scheduling problem. The Fang et al's (2015) algorithm for the stochastic resource-constrained project-scheduling problem, and the Wang et al's (2016) research for the distributed permutation ñowshop scheduling problems under machine breakdown. The articles mentioned above are current and representative of this group of hybrid EDAs.

Both pure EDAs and hybrid EDAs have been widely used to solve combinatorial problems. The development of EDAs does not finish in this point. Recently, new EDAs have been published. These EDAs have a new characteristic. These utilize permutation of elements-based representation as a solution to solve combinatorial optimization problems. That is, these algorithms propose specific probability models to integrate solutions as permutation-based representation. This category is named distance-based ranking models. The proposed EDA by Ceberio et al (2014) for flow-shop scheduling problem, the Pérez-Rodríguez et al's (2017) study for the school bus routing problem with bus stop selection, the Pérez-Rodríguez \& Hernández-Aguirre's (2018) algorithm for the flexible job-shop scheduling problem with process plan flexibility, and the Pérez-Rodríguez \& Hernández-Aguirre's (2019) technique for the vehicle routing problem with time windows, are currently published papers belonging to this category.

From the previous classification, it can be seen that recent authors have combined new and recognized methodologies to solve optimization problems such as the job-shop scheduling problem. Recently, other studies make comparisons between other algorithms, such as the genetic algorithm, the particle swarm optimization algorithm, multi-objective algorithms, and others. Currently, other researchers show the effectiveness and efficiency of the proposed methods as a part of their manuscripts. The published methods try to get new solutions to some benchmark problems. The cited methods carried out experiments on actual examples, i.e., actual data of real environments. Some examples of such methodologies are detailed below

Ning et al (2017) combines a permutation flow-shop scheduling problem and a non-permutation flow-shop scheduling problem with minimal and maximal time lag considerations. Sáenz-Alanís et al (2016) address a job-shop scheduling in the beer production context, where sequence-dependent setup times are related to the cleaning operations. Deep \& Singh (2015) study cellular manufacture systems where machines are grouped in machine cells able to process multiple operations at the same time.

Phanden \& Jain (2015) offer a simulation-based genetic algorithm approach to solve flexible job-shop scheduling problems with process plan flexibility. The authors assess the effect of flexible process plan of a part-type in a production order environment. The objective is to find the minimum makespan as a performance measure.

Li \& Gao (2016) propose an effective hybrid algorithm that hybridizes the genetic algorithm and tabu search, for the flexible job-shop scheduling problems with the objective of minimizing the makespan.

Xu et al. (2017) establish a mathematical model for job-shop scheduling problems, and an improved bat algorithm is proposed to solve the mathematical model mentioned. The objective is to seek an appropriate schedule that costs minimum time to complete all operations.

Pérez-Rodríguez \& Hernández-Aguirre (2018) propose a Pareto approach based on the hybridization of an estimation of distribution algorithm and the Mallows distribution in order to build better sequences for flexible job-shop scheduling problems with process plan flexibility and to solve conflicting objectives.

The development of new probability models continues being attractive for practitioners and researchers. The proposal of identifying new probability models, to be more efficient than the performance of the EDAs, is the aim and scope for any research in this field. Therefore, as contribution of this research, the development of a new probability model is presented. The proposed EDA generates new solutions based on a radial probability model. It means that an atomic orbital generation function is used to produce offspring. In quantum chemistry it is established that a function, of this type, makes it possible to describe the behavior of an electron in a space occupied by an atom to which the electron belongs. However, due to the random behavior of the electron, it is more useful to describe its behavior in terms of the probability to find the electron in a specific volume of the space occupied by the atom to which the electron belongs. In the current atom model, the electron is described in terms of a wave function E. The wave function is a math function that it describes the behavior of the electron in a specific space. This space is called atomic orbital. The function $\hat{E}^{2}$ is proportional to the probability

density of the electron in a specific point of the atomic space. If the values of $\hat{E}^{2}$ around of the core are considered, then it can define a contour surface (see Figure 1). This contour surface contains the volume where there exists a probability to find the electron. It permits to visualize the atomic orbital. In this research, the wave function of the hydrogen $(\mathrm{H})$ is used. This function is elected because it is exactly defined in math terms. In this sense, there exist four orbitals for the hydrogen. Then, four equations describe the radial probability function. The contribution of this research is to use such radial probability functions as probability model for the EDA scheme, and from these functions to generate offspring to solve the job-shop scheduling problem (JSSP). The performance of the proposed EDA, called REDA (Radial Estimation of Distribution Algorithm), is compared with those recent algorithms that efficiently solve the JSSP. Although diverse methods and strategies have been used to solve the JSSP, this paper contributes to the state of the art through utilization of the radial probability functions of the hydrogen, for the JSSP, as a probability model to enhance the performance of the EDA.

The results, obtained from this research, permit to conclude that using radial probability distributions is an emerging field to develop new and efficient EDAs.

# 2. PROBLEM STATEMENT 

Pinedo (2008) details the job-shop scheduling problem. The main constraints are detailed below

- For each job, the corresponding operations have to be processed in the given order, that is, the starting time for an operation must not be earlier than the point at which the preceding operation in the sequence of operations of the respective job is completed
- Each operation has to be assigned to exactly one machine
- Preemption is not allowed, i.e., each operation must be completed without interruption once it starts
- The operations assigned for each machine have to be subsequently established, that is, an operation is only allowed to be assigned to the sequence of a machine if the preceding position on the sequence is already established
- If the operations $i$ and $j$ are assigned to the same machine $k$ for consecutive positions $p-1$ and $p$, then the starting time of operation $j$ must not be earlier than the completion time of operation $i$ in order to prevent overlapping

An example is provided with four machines and three jobs. The data are given in Table 1.
Figure 2 depicts a schedule as a solution by Gantt chart.
Based on the schedule, depicted in Fig. 2, the makespan is 33. The goal is to find the best schedule in order to obtain the minimum makespan.

## 3. REDA FOR THE JSSP

### 3.1. Solution Representation

A solution for the JSSP should be an operation scheduling decision, and machine assignment. Thus, a solution can be expressed by the processing sequence of operations on the machines, and the assignment of operations on machines. In this paper, two vectors, i.e., an operation sequence vector, and machine assignment vector, represents a solution. For the operation sequence vector, the number of elements equals the total number of operations, where each element contains a continuous value. The aforementioned continuous value, indicates the distance, in picometers, between the electron and the core. In Figure 3, the representation of an operation sequence vector is illustrated.

Figure 1. Contour surface of an atom where an electron can be
![img-0.jpeg](img-0.jpeg)

The representation, elected in this research, is suitable to integrate the radial probability distribution as a probability model. Anyway, the operation sequence vectors must be decoded to represent valid schedules. The decoding process is detailed as follows:

A fixed integer number is assigned for each operation. Each fixed integer number is associated with a job. A sort on the continuous values of each operation sequence vector is done. Assigning each continuous value to the corresponding fixed integer number that belongs to each operation and setting each fixed integer number to a job to finish. Table 2 details the previous operation sequence vector, depicted in Figure 3, and its decoding.

For the machine assignment vector, each element represents the corresponding selected machine for each operation. An example is provided below

# 3.2. Fitness 

The makespan is computed for each member of the population. Using each decoded operations sequence vector, and each machine assignment vector, a makespan is obtained. The makespan is the length of time that elapses from the start of job to the end (that is, when all the jobs have finished processing). An illustration can be seen in Fig. 2. The makespan, for the Fig. 2., is 33 unit time.

### 3.3. Probability Model

The wave functions for the hydrogen atom are given a special name, atomic orbitals, because they play such an important role in the electronic structure of atoms. In general the word orbital is the

Table 1. Data example for the JSSP
Figure 2. A schedule solution for the JSSP example
![img-1.jpeg](img-1.jpeg)

Table 2. Representation of an operation sequence vector
name given to a wave function which determines the motion of a single electron. If the one-electron wave function is for an atomic system, it is called an atomic orbital. For the hydrogen atom, there are four different atomic orbitals and four different electron density distributions. The math expressions of the radial distribution function $P(r)$, for the hydrogen, in each atomic orbital are detailed as follows
$1^{\circ}$ atomic orbital

Table 3. Representation of an operation sequence vector to a valid schedule.
Table 4.

$P_{1}(r)=4\left(\frac{Z}{a_{0}}\right)^{3} e^{\left(\frac{2 Z r}{a_{0}}\right)} r^{2}$
where $Z$ represents the atomic number of the element, i.e., the hydrogen $Z=1 . a_{0}$ indicates the Bohr radius, and $r$ is the distance (radius), in picometers $(p m)$ of electron to the core.

The Bohr radius is defined as
$a_{0}=\frac{h^{2}}{\left(4 \pi^{2} m e\right)}=52.9 \mathrm{pm}, h$ is the Planck constant, $m$ is the mass of the electron, and $e$ its charge.

Figure 4 shows the radial distribution probability, for the $1^{\text {st }}$ atomic orbital, using the Eq. (1). As we can see, the function rapidly decays with respect to its distance to the core.

The next functions correspond to the $2^{\text {nd }}, 3^{\text {rd }}$, and $4^{\text {th }}$ atomic orbitals for the hydrogen
$P_{2}(r)=\frac{1}{8}\left(\frac{Z}{a_{0}}\right)^{3}\left(2-\frac{Z r}{a_{0}}\right) e^{\left(\frac{Z r}{a_{0}}\right)} r^{2}$

Figure 3. Radial distribution probability, for the $1^{\text {st }}$ atomic orbital
![img-2.jpeg](img-2.jpeg)

$$
\begin{aligned}
& P_{4}(r)=\frac{1}{243}\left(\frac{Z}{a_{0}}\right)^{3}\left(6-\frac{12 Z r}{3 a_{0}}+\frac{4 z^{2} r^{2}}{9 a_{0}{ }^{2}}\right) e^{-\left(\frac{2 Z r}{3 a_{0}}\right)} r^{2} \\
& P_{4}(r)=\frac{1}{9216}\left(\frac{Z}{a_{0}}\right)^{3}\left(24-\frac{18 Z r}{a_{0}}+\frac{3 Z^{2} r^{2}}{a_{0}{ }^{2}}-\frac{z^{3} r^{3}}{8 a_{0}{ }^{3}}\right) e^{-\left(\frac{Z r}{2 a_{0}}\right)} r^{2}
\end{aligned}
$$

With these radial distribution functions, a cumulative distribution should be built for each atomic orbital. The offspring can be generated using any cumulative radial distribution.

# 3.4. Sampling 

The process to obtain an offspring is computed operation per operation. Firstly, a random value should be generated for each operation. Then, each random value, is interpolated in a cumulative probability distribution, previously selected, to identify which distance, between the electron and the core, should be established. Figure 5 shows an example of this process.

### 3.5. Replacement

The offspring should be evaluated to obtain their fitness. Finally, the replacement process used in this study is by binary tournament between the parents and the offspring.

Figure 4. Sampling example
![img-3.jpeg](img-3.jpeg)

All the stages of the proposed algorithm have been defined. All of this, within a number of the generations. In this research, 100 generations and 1000 solutions per generation, were used. These are fixed parameters.

The REDA framework is provided below
The main differences between the REDA and the rest of EDAs is highlighted below

# 4. RESULTS AND COMPARISON 

### 4.1. Comparison Between Atomic Orbitals

The standard benchmarking datasets, for the JSSP, are used as input data for the mentioned comparison. The aforementioned datasets used in this research are the Adams, Balas \& Zawack (1988) instances; the Fisher \& Thompson (1963) instances; the Lawrence (1984) instances; the Applegate \& Cook (1991) instances; the Storer, Wu \& Vaccari (1992) instances; finally, the Yamada \& Nakano (1992) instances. All the details about the instances are depicted below

The experiments are executed in a Lanix Titan HX 4200 computer, Intel Core ${ }^{\mathrm{TM}} \mathrm{i} 7$ processor, 3.4 GHz, 8 GB of RAM, Windows 10 for 64 bits to run every instance. C++ language is used for the implementation for all the comparisons. To account for the stochastic nature of the REDA, we run 30 trials for each instance.

The relative percentage increase $(R P I)$ is computed in order to compare the performance of each atomic orbital. The $R P I$ is detailed as follows
$R P I\left(c_{i}\right)=\frac{c_{i}-c_{*}}{c_{*}}$
where $c_{i}$ is the best result, i.e., the minimum makespan found in each run by the REDA, and $c_{*}$ is the best result found and reported in the literature. The four atomic orbital functions, of the hydrogen, are compared in order to identify which atomic orbital is better to solve the JSSP.

Table 5.
Figure 6 includes four box plots: the $1^{\text {st }}$ atomic orbital, the $2^{\text {nd }}$ atomic orbital, and so on, after running all the instances, and all the trials. As we can see, there is no practically difference between the orbitals, i.e., any orbital is suitable for solving the JSSP instances used in the comparison.

# 4.2. Comparison Between Recent Algorithms 

In order to validate the scientific relevance of this paper, recent algorithms are proposed as a benchmark for comparison with the REDA scheme. The aforementioned recent algorithms are as follows

- The simulation-based genetic algorithm presented by Phanden \& Jain (2015),
- The improved bat algorithm proposed by Xu et al. (2017),
- The hybrid algorithm that hybridizes the genetic algorithm and tabu search detailed by Li \& Gao (2016),
- The genetic algorithm designed by Li et al. (2017),

Table 6.
Table 7.
Figure 5. Performance of the REDA in each radial distribution
![img-4.jpeg](img-4.jpeg)

- The hybrid estimation of distribution algorithm proposed by Pérez-Rodríguez \& Hernández-Aguirre (2018), called MEDA, and
- The hybrid approach that hybridizes an estimation of distribution algorithm and the moth-flame algorithm designed by Pérez-Rodríguez (2020), called HEDAMMF.

The experiments are executed in the same computer and language specification. As in the previous comparison, the relative percentage increase $(R P I)$ detailed in Eq. (5) is computed.

The distribution of the experimental results, in each interval, for the Adams, Balas \& Zawack (1988) instances, is presented in Table 3. It is clear from the table that the results of the REDA algorithm are comparatively concentrated, which is mainly in the range of $[0.04,0.08]$, whereas the main results of the other algorithms are concentrated in the range of [0.08, or more].

Figure 6 depicts seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, for the Adams, Balas \& Zawack (1988) instances, after running all the trials.

The distribution of the experimental results, in each interval, for the Fisher \& Thompson (1963) instances, is presented in Table 4. From the table, it is possible to identify that the overall performance of the REDA algorithm is competitive. Based on the results, the REDA algorithm can find efficiently the closest solutions to the optimal, 60 times in the range of $[0,0.04]$, whereas the main results of the other algorithms are far from this amount.

Figure 7 depicts seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, for the Fisher \& Thompson (1963) instances, after running all the trials.

The distribution of the experimental results, in each interval, for the Lawrence (1984) instances, is presented in Table 5. From the table, it is possible to identify that the overall performance of the REDA algorithm is again competitive. Based on the results, the REDA algorithm can efficiently find the closest solutions to the optimal, more times in the range of $[0,0.04]$, than any another algorithm used in the comparison.

Figure 8 depicts seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, for the Lawrence (1984) instances, after running all the trials.

The distribution of the experimental results, in each interval, for the Applegate \& Cook (1991) instances, is presented in Table 6. It is clear, from the table, that the performance of the REDA

Table 8. Distribution of the results for the Adams, Balas \& Zawack (1988) instances

Figure 6. Performance of the REDA, for the Adams, Balas \& Zawack (1988) instances
![img-5.jpeg](img-5.jpeg)
algorithm obtains the best results. Based on the results, the rest of the other algorithms are far from this performance. Therefore, the performance of the REDA algorithm is competitive.

Figure 9 depicts seven boxplots, one per each algorithm. As we can see, the REDA scheme obtain a competitive performance, for the Applegate \& Cook (1991) instances, after running all the trials.

The distribution of the experimental results, in each interval, for the Storer, Wu \& Vaccari (1992) instances, is presented in Table 12. From the table, it is possible to identify that the overall performance of the REDA algorithm is again competitive. Based on the results, the REDA algorithm can efficiently find the closest solutions to the optimal, more times in the range of $[0,0.04]$, than any another algorithm used in the comparison.

Figure 10 depicts seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, for the Storer, Wu \& Vaccari (1992) instances, after running all the trials.

Table 9. Distribution of the results for the Fisher \& Thompson (1963) instances

Figure 7. Performance of the REDA, for the Fisher \& Thompson (1963) instances
![img-6.jpeg](img-6.jpeg)

Table 10. Distribution of the results for the Lawrence (1984) instances

The distribution of the experimental results, in each interval, for the Yamada \& Nakano (1992) instances, is presented in Table 13. From the table, it is possible to identify that the overall performance of the REDA algorithm is again competitive. Based on the results, the REDA algorithm can efficiently find the closest solutions to the optimal, more times in the range of $[0,0.04]$, than any another algorithm used in the comparison.

Figure 11 depicts seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, for the Yamada \& Nakano (1992) instances, after running all the trials.

Figure 12 depicts the overall performance, with seven boxplots, one per each algorithm. As we can see, the REDA outperforms all the algorithms used in the comparison, after running all the instances, and all the trials.

Finally, a statistical test is executed in order to show that the REDA scheme outperforms all the algorithms used in the comparison for the all trails, and all the instances. Figure 13 depicts a Dunnett test. There is a statistically significant difference between the algorithms by means of the Dunnett test.

Based on the results detailed above, the radial probability distributions are suitable to identify the best performing ones. It is due to the solution representation used in this approach, by continuous values, permits to explore, and adapt any combination for the operation scheduling process. Having a wide and diverse operation scheduling vectors, obtained from the cumulative radial probability distribution, it is the key point to find competitive solutions.

- The setting of the parameters

The EDA scheme considers population size, replacement (also known as generation gap), and selection strategy as key parameters.

- The population size; in the current experiments, the population size ranged from 500 to 1000 solutions in increments of 500 .
- The replacement; the current experiments allowed to vary the percentage of the population to be replaced during each generation between $50 \%$ and $100 \%$, in increments of $50 \%$.
- The stopping criteria; the number of generations is defined as a stopping criteria, varying from 50 to 100 generations.

Figure 8. Performance of the REDA, for the Lawrence (1984) instances
![img-7.jpeg](img-7.jpeg)

A design of experiment is built to identify the best parameter of each parameter. Then parameter tuning is detailed below

Table 11. Distribution of the results for the Applegate \& Cook (1991) instances

Finally, the results of the parameter tuning is shown below. There is no statistically significant difference of any of the three controlled parameters (number of generations, initial population size, and replacement). Therefore, the parameters used are the same for all the algorithms.

# 5. CONCLUSION 

This paper discusses the job-shop scheduling problem, which considers different processing sequence of operations, for each job, as many industrial environments. To solve this problem, the REDA scheme is proposed. By means of wide and diverse numerical experiments and comparisons, the REDA offers a competitive performance.

This research concludes that radial probability functions can be coupled with the EDA scheme in order to solve combinatorial optimization problems, such as JSSP.

The computational results show that the different radial probability distributions, used for the JSSP, with large data sets are suitable.

The results, obtained from this research, permit to conclude that using radial probability distributions is an emerging field to develop new and efficient EDAs.

More radial probability distributions, from others elements not only the hydrogen, for the JSSP and others combinatorial problems, should be considered in future research.

Dynamic job-shop issues should be included, in light of these results, for building new evolutionary algorithms coupled with other radial probability functions.

Since the REDA presents stability, it appears very suitable for implementation in software systems for practical purposes. Further research directions may deal with an extension of the REDA for building effective modules for specific users in the industry. Finally, the REDA could be used in other types of job-shop systems, such as flow-shop scheduling, flexible job-shop scheduling, openshop scheduling, between others.

## ACKNOWLEDGMENT

A gratitude to all the reviewers for their comments in improving the manuscript.

Figure 9. Performance of the REDA, for the Applegate \& Cook (1991) instances
![img-8.jpeg](img-8.jpeg)

International Journal of Applied Metaheuristic Computing
Volume 13 ・ Issue 1

Table 12. Distribution of the results for the Storer, Wu \& Vaccari (1992) instances

Figure 10. Performance of the REDA, for the Storer, Wu \& Vaccari (1992) instances
![img-9.jpeg](img-9.jpeg)

International Journal of Applied Metaheuristic Computing
Volume 13 ・ Issue 1

Table 13. Distribution of the results for the Yamada \& Nakano (1992) instances

Figure 11. Performance of the REDA, for the Yamada \& Nakano (1992) instances
![img-10.jpeg](img-10.jpeg)

Figure 12. Performance of the REDA
![img-11.jpeg](img-11.jpeg)

Figure 13. Statistical test
![img-12.jpeg](img-12.jpeg)

Table 14. Criteria

Figure 14. Parameter tuning
![img-13.jpeg](img-13.jpeg)
