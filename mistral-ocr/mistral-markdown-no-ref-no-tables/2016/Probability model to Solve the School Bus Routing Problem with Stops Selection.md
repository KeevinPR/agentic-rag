# Probability model to Solve the School Bus Routing Problem with Stops Selection 

Ricardo Pérez-Rodríguez, Arturo Hernández-Aguirre<br>Center for Mathematics Research CIMAT, AC<br>ricardo.perez@cimat.mx


#### Abstract

This paper describes the use of a new algorithm that solves the school bus routing problem with stops selection. The aim is to reduce the travel time of a set of buses that transport students to a school. The fundamental contribution of the authors is the use of a probability model to describe the feasible solution space distribution and thus to get the best solution. An estimation of distribution algorithm is used to address the combinatorial complexity of the problem statement. Different and better results are obtained with the proposed algorithm against a genetic algorithm. The contribution of this paper is to propose an alternative to solve permutation-based representation problems with logistics application.


Keywords: probability model; school bus routing; vehicle routing; genetic algorithm; estimation of distribution algorithm.

## 1 Introduction

The transportation of students is an important factor in the efficient management of the services offered by the different schools especially when such transportation complexity increases as the number of students to attend. A large number of transport companies and schools in different countries are faced with the transport situation every day for students. Various laws that regulate the way in which students are transported and to where the bus stops can be placed is discussed, approved and modified continuously. The school bus routing problem is a logistics issue that requires more accountability and better service by drivers and the companies that offer the service. Bus stops are constantly changing. As students move or change of degree, it may be necessary to move, add or delete any stop on the route. Security considerations also come into play with the location of stops, for example, whether the bus turns to the right for a pickup or students crossing the street can be critical in making decision the correct location of the stop bus. An additional requirement may be that a stop should be located at a distance of no more than n meters in the direction of each student.

Unlike traditional vehicle routing formulations where there is a set of nodes (vertices) already established, this research focuses on the school bus routing problem where a set of potential bus stops is known. Then, determining the set of bus stops really to use is a part of the formulation in this research. The objective of this problem is (1) finding the set of bus stops to visit, (2) determine for each student what bus stop should be addressed and (3) set the path for the chosen bus stops, so that the total travel time is minimized.

Minocha and Tripathi [1] describe a real school bus routing problem. The authors develop a roadmap for the bus service of a school located in Rajasthan, India, so it is able to serve students in an efficient manner with maximum capacity utilization of the buses using a hybrid genetic algorithm. In this research, the authors transform the school bus routing problem with the format of a vehicle routing problem with time windows. Therefore, the vertices of the graph are the stops where students board the bus. Schittekat et al. [2] solve a school bus routing problem with stops selection using a meta-heuristic. The meta-heuristic proposed called adaptive randomized greedy search procedure, based on a method of neighborhood, use an exact algorithm to solve optimally the problem of allocation of students to the stops when the routing is defined. This meta-heuristic starts from a solution in which all stops are visited on separate routes. Therefore, the solution is represented by numbers representing the buses. The results of the meta-heuristic approach was compared with solutions found by a sequential method, with solutions obtained by applying a mixed integer programming model using commercial software, and solutions obtained by a column generation approach.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

Niu [3] focuses on how to determine an operations schedule for an urban transportation company (a real case) for the peak hours during the morning. An operations schedule at irregular intervals intends to match the demands in terms of time and increase the use of vehicles. This program allows buses depart at times different from each other. In addition, a linear programming model is formulated to minimize the waiting time and costs incurred by the use of vehicles. Finally, a heuristic method based on a genetic algorithm is developed to generate feasible solutions. The representation of the solution is binary and indicates that a bus part or not in the corresponding time point.

Diaz-Parra et al. [4] proposed an application of a bio-inspired algorithm for a school bus routing problem with the features of a single school, urban services, mixed cargo, special students and homogeneous fleet. In this study, each chromosome is represented by a set of numbers. Each number represents a bus stop. The order of the numbers shows a feasible route. A set of test cases were developed by the authors and these cases were resolved by the proposed genetic algorithm.

Other contributions that are virtually in the same direction of current research are Euchi and Mraihi [5], Pacheco et al. [6] and a review of the problem mentioned can be found in Park and Kim [7]. Most of the methods developed for the school bus routing problem with stops selection are characterized by using a sequential approach [2], that is, a selection procedure for the bus stops is followed for a routing process or vice versa. In the first case (selection-routing), it has the drawback of generating more routes than the opposite case (routing-selection). Moreover, the trend of current research is to develop algorithms and iterative search procedures where the process of variation (represented by the cross and mutation operators on the algorithms based-population) has control of the solutions that are generated without having totally clear for the user as such solutions were obtained. The random nature of the process of variation makes changes to the existing solutions as a black box approach, whereas in this study the black box approach is avoided, that is, the search process is transparent.

The Estimation of Distribution Algorithms (EDA) is a relatively new paradigm in the field of evolutionary computing. Compared with other evolutionary algorithms, in the EDA the new population is reproduced without using traditional evolutionary operators. In the EDA, a probability model of the most promising area is built with statistical information based on the search experience, and then the probability model is used to generate new individuals. The EDA make use of a probability model to describe the solution space distribution. The updated process of the solution space distribution reflects the tendency of the evolution population (Wang et al. [8]). To describe the solution space distribution, the EDA tries to determine a relationship or interaction between the variables of the problem as its main objective. Traditional evolutionary operators are replaced by a probability model that is built with information about relationships and interactions between the variables of the problem. The main idea is to learn and benefit from interaction between variables by estimating the population distribution and sample new offspring from it. Although the interaction may or may not be present, usually, this is explicitly unknown even for the school bus routing problem. In this investigation, an EDA is proposed in order to improve the sequential selection-routing approach. Finally, although different algorithms have been proposed in order to solve the above problem successfully, in the best of our knowledge, probability models have not been used to address the problem described.

# 2 Experimental procedures 

### 2.1 Allocation

As the goal in this research is to improve the sequential approach for building solutions for the school bus routing problem with stops selection known as selection-routing, then the first decision is to assign students to the bus stops by means of an iterative process that assigns each student to a bus stop in the first possible stop within the set of potential stops and the number of students assigned to the bus stop mentioned is updated to avoid exceeding the capacity of any bus. A stop is considered potential when a student walk to the stop and the distance-time restriction is not violated. Therefore, a stop may be potential for a student, but it is not potential for other students. The code iterative procedure described below in Figure 1.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

```
Define distance-restriction
Define bus-capacity
for each student i do
for each stop j do
distance = (stop location j, student location i)
if distance & distance-restriction
    feasible matrix (i,j) = 1
else
    feasible matrix (i,j) = 0
endif
endfor
endfor
for each stop j do
capacities(j) = 0
for each student i do
assigned = 1
for each stop j do
    if feasible matrix (i,j) == 1 AND capacities(j)<bus-capacity
        assigned = j
        break
    endif
endfor
capacities (assigned) = capacities (assigned) +1
endfor
```

Fig. 1. A method of allocating student-stop.
As an example, Schittekat et al. [2]'s first test is used, which has 5 stops with 25 potential stops to assign students, and where the distance-time restriction is only 5 min . Then given the above procedure a feasible allocation is below

# 1111122222333334444455555 

Where each number represents the stop assigned to each student.
The second decision concerns the routing procedure. For this research a population of M vectors is initialized with size m , where m is the total number of selected stops. Each vector is initialized as a permutation of selected stops mentioned. A permutation is shown below according to the above example

## 4251

Where the first bus stop to attend is the 4 after the 2 and so on.
Once the permutation is generated, a feasible solution should be created so that the capacity of the vehicles is not exceeded based on the Prins [9] procedure. This is for each vector of the population.

### 2.2 Selection

A subset N of M parents is selected according to their fitness value by the method of the bubble. Fitness in this case is the total travel time.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

# 2.3 Probability model 

The proposed probability model uses the simplest approach for estimating the joint probability distribution of selected individuals in each generation, $\mathrm{p}_{\mathrm{i}}(\mathrm{x})$. This joint probability distribution is factored as a product of the univariate marginal distributions $\mathrm{p}_{\mathrm{i}}(\mathrm{x})=\mathrm{p}(\mathrm{x} \mid \mathrm{N})=\prod^{1} \mathrm{p}_{\mathrm{i}}\left(\mathrm{x}_{\mathrm{i}}\right)$. Each univariate marginal distribution is estimated with marginal frequencies $\mathrm{p}_{\mathrm{i}}\left(\mathrm{x}_{\mathrm{i}}\right)=\sum^{N} \delta_{\mathrm{i}}\left(\mathrm{X}_{\mathrm{i}}=\mathrm{x}_{\mathrm{i}} \mid \mathrm{N}\right) / \mathrm{N}$ where: $\delta_{\mathrm{i}}\left(\mathrm{X}_{\mathrm{i}}=\mathrm{x}_{\mathrm{i}} \mid \mathrm{N}\right)=1$, if the j -th case $\mathrm{N}, \mathrm{X}_{\mathrm{i}}=\mathrm{x}_{\mathrm{i}}$.
Figure 2 details an example where for the first position (first column) in the permutation are only six possible stops according to the individuals selected. Therefore, the possible values to choose for the first bus stop on the route (first column) are 2, 3, 4, 6, 7 and 9 and each has a $1 / 6$ chance of being chosen.

### 2.4 Sampling

To generate new offspring, each bus stop is selected with probability pj at each position of the route according to the selected individuals, see Figure 2. If a bus stop has already been chosen, it means that the bus stop cannot be selected again. Then, for each successor position of the route should not be considered the bus stops selected previously. This update mechanism considers previous assignments. Figure 3 depicts for the first position the bus stop 4 was selected. Then the bus stop 4 cannot be elected for the second position. The possible values to choose for the second position in the route (second column) are 5 and 7 and each has $1 / 2$ chance of being elected.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.
![img-0.jpeg](img-0.jpeg)

Fig. 2. Probability distribution generated for each bus stop.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Update on the probability distribution of the sample.

# 3 Results 

Schietekat et al. [2]'s test sets serve as input parameters to show that the sequential selection-routing approach can be improved. A better position to each bus stop in the sequence can be estimated by the probability model. The tests mentioned ranging from 5 stops and 25 students to 800 students and 80 stops. In addition, four maximum walking distances are considered: 5, 10, 20 and 40. The maximum walking distance-time determines the average number of stops that a student is able to walk. From Table 1 to Table 5 include seven columns: the instance (id column), the number of stops (stop column), the number of students (stud column), bus capacity (cap column), the maximum distance-time walk (column wd), the shortest travel time obtained with a genetic algorithm used as comparative (GA column), and the proposed EDA (EDA column). Table 1 provides details on the results for 5 potential stops. From Table 1 can see how the probability model is able of detecting competitive sequences than the genetic algorithm for the problem stated.

Table 1. Comparative results for 5 potential stops

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

Table 2 provides information on the results when there are 10 potential stops. From Table 2 can see how the probability model is able to detect competitive sequences and sometimes getting less time than the genetic algorithm.

Table 2. Comparative results for 10 potential stops

Table 3 details the results when there are 20 potential stops. According to the Table 3, the probability model is able to detect competitive sequences and many occasions getting less time than the genetic algorithm.

Table 3. Comparative results for 20 potential stops

Table 4 depicts on the results when there are 40 potential stops. Based on the results shown in the Table 4, the probability model is able to detect competitive sequences and the most cases getting less time than the genetic algorithm.

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

Table 4. Comparative results for 40 potential stops

Table 5 provides the results when there are 80 potential stops. From Table 5 can see how the probability model is able to detect competitive sequences and almost always getting less time than the genetic algorithm.

Table 5. Comparative results for 80 potential stops

Figure 4 shows the dispersion and symmetry for both algorithms for each number of potential stops. As the dispersion and symmetry observed between the values obtained is very similar, so it follows that both algorithms are equally stable in finding better sequences (routes).

Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Dispersion and symmetry between both algorithms.
Further, a hypothesis test is performed to determine whether the proposed EDA is better than the genetic algorithm. Table 6 describes when there is a statistically significant difference between the algorithms.

Table 6. Hypothesis testing between algorithms
Pérez-Rodríguez and Hernández-Aguirre / Probability model to solve the school bus routing problem with stops selection. IJCOPI, Vol. 7, No. 1, Jan-April 2016, pp. 30-39. ISSN: 2007-1558.

# 4 Conclusions 

Based on the above results, the contribution of this research to the solution of permutation-based representation problems such as the school bus routing problem with stops selection is confirmed. The probability model used is able to find better solutions to reduce the travel time for a set of school buses. The proposed model makes explicit the search, a situation that is random in the variation process on other algorithms. The construction mechanism of the solutions permits to determine the chance for a bus stop to be chosen on the route through the probability model. The method of allocating student-stop used in this research was no downside to reduce travel time by the model used.
