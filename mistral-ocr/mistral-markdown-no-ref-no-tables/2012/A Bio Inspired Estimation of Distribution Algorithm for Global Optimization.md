# A Bio Inspired Estimation of Distribution Algorithm for Global Optimization 

Omar S. Soliman and Aliaa Rassem<br>Faculty of Computers and Information, Cairo University, 5 Ahmed Zewal Street, Orman, Giza, Egypt<br>Dr.omar.soliman@gmail.com<br>aliaa.rassem@yahoo.com


#### Abstract

This paper introduces a new bio-inspired Estimation of Distribution Algorithm for global optimization that integrates the quantum computing concepts with the immune clonal selection, vaccination process and Estimation of Distribution Algorithm (EDA). EDA is employed in the vaccination process to improve the solutions diversity and maintain high quality solutions in addition to its ability to avoid falling in local optimum for multi modal problems. The proposed algorithm is implemented and evaluated using standard benchmark test problems. Experimental results are compared with the quantum inspired immune clonal algorithm (QICA) and the QICA- with vaccine algorithm, where the proposed algorithm is superior to both of them. The obtained results carried out, it is performing well in terms of the solutions quality and diversity, and it is superior to both of compared algorithms.


Keywords: Quantum Inspired Immune Clonal Algorithm (QICA), Estimation of Distribution Algorithm (EDA), Vaccine Operator, Global Optimization.

## 1 Introduction

Immune clonal algorithm (ICA) is inspired from the human immune systems clonal selection process over the B cells where the evolution process of the antibodies is a repeated cycle of matching, cloning, mutating and replacing. The best B cells are allowed through this process to survive which increases the attacking performance against the unknown antigens. Vaccination is another immunological concept that ICA applies through the vaccine operator to introduce some degree of diversity between solutions and increase their fitness values [1], [15].

The quantum-inspired immune clonal algorithm (QICA) is one of the Quantum inspired evolutionary algorithms QIEAs, based on the combination of quantum computing principles, like quantum bits, quantum superposition property and quantum observation process, with immune clonal selection theory. The quantum bit representation for antibodies and vaccines has the advantage of representing a linear superposition of states (classical solutions) in search space probabilistically. Quantum representation can guarantee less population size as

a few number of antibodies and vaccines can represent a large set of solutions through the space [16]. The quantum observation process plays a great role in projecting the multi state quantum antibodies into one of its basic states to help in the individuals evaluation. Quantum vaccine ICA algorithm(QICA-V) is an algorithm that applies quantum vaccines to inject the quantum antibodies in the search space to increase their fitness. This algorithm has a drawback in its obtained solutions because they have a lack in diversity. A new hybridization of QICA-V and Estimation of distribution Algorithm is proposed to obtain some degree of diversity between solutions and maintain low computational and time complexity.

The aim of this paper is to develop a bio-inspired algorithm based on the QICA and the vaccine operator with the aid of EDA to sample vaccines. The algorithm merges the quantum computing concepts with the vaccine operator and the EDA sampling to improve the diversity and save computational time. The rest of this paper is organized as follows: Section 2 introduces a brief of some related work that had been done using QIEA and a background about QICA and EDA algorithms. The proposed algorithm is presented in section 3. The experiments setup and results are presented in section 4, where the last section is devoted to conclusions and further researches.

# 2 Related Works and Background 

Quantum-Inspired Artificial Immune System algorithms had been applied extensively in virous real applications $[5,7,9,12,17]$. The vaccine operator was also used in many works with the AIS algorithms to enhance their exploration ability and increase their detection efficiency $[2,6,13,14,18]$.

### 2.1 Estimation of Distribution Algorithm

iterated density estimation evolutionary algorithms (IDEAs) are EAs that apply an explicit sampling procedure through using probabilistic models rep- resenting the solutions characteristics. Estimation of Distribution Algorithms (EDAs) are types of the IDEA and population based algorithms with a theoretical foundation of probability theory. They can extract the global statistical information about the search space from the search so far and builds a probability model of promising solutions $[1,4,9,15]$. The general procedure of EDA is described in algorithm 1 .

The EDA advantage is that it relies on the construction and maintenance of a probability model that generates satisfactory solutions for the problem solved. An estimated probabilistic model, to capture the joint probailties between variables, is constructed from selecting the current best solutions and then it is simulated for producing samples to guide the search process and update the induced model. Estimating the joint probability distribution associated with the data constitutes the bottleneck of EDA. Based on the complexity of the model used, EDAs are classified into different categories, without interdependencies,

```
Algorithm 1. Estimation of Distribution Algorithm
    Initialize the initial population.
    while termination condition is not satisfied do
        Select a certain number of excellent individuals.
        Construct probabilistic model by analyzing information of the selected
        individuals.
        Create new population by sampling new individuals from the constructed
        probabilistic model.
    end while
```

pair wise dependencies and multiply dependencies algorithms where detailed description is shown in [15].

# 2.2 Quantum Inspired Immune Clonal Algorithm 

Quantum-Inspired Artificial Immune System algorithms had been applied extensively in virous real applications $[5,7,9,12,17]$. The vaccine operator was also used in many works with the AIS algorithms to enhance their exploration ability and increase their detection efficiency $[2,6,13,14,18]$. Quantum inspired ICA (QICA), is the hybridization between QC and classical ICA to enhance the perfrmonace of the ICA and helpe in solving the problem of its ineffective performance in high dimensional problems. Inspired quantum concepts used in QICA include quantum bit (q-bit), quantum mutation gate and observation process $[16]$.

## 3 Proposed Algorithm

The proposed algorithm integrates the quantum computing and immune clonal selection principles with the vaccination and EDA sampling mechansim to improve the solutions fitness and degree of diversity. The quantum bit representation is used for antibodies and vaccines where the vaccine population is divided into two sub populations [9]. Genetic operators are used to evolve the first subpopulation and the EDA is applied in the second one to sample the fittest vaccines. The main steps of the proposed algorithm are described in algorithm 2.

The algorithm starts by initializing both the quantum antibody population $Q(t)$ and the quantum vaccine population $V(t)$ followed by cloning and mutataing antibodies to be then decoded for evlauation. Additional steps to the simple QICA, like vaccine decoding and sampling will be described in details. The quantum vaccine population $V(t)$ is initialized in the same way with $n$ quantum vaccines where $n$ is the number of grids that the decision space is divided to and $n=\left(D_{1} * D_{2} * \cdots * D_{d}\right)$ with $d$ which is the number of dimensions.

```
Algorithm 2. The proposed Algorithm (QICA-V with EDA)
    Initialize the quantum antibody and vaccine populations, \(\mathrm{Q}(\mathrm{t})\) and \(\mathrm{V}(\mathrm{t})\).
    Initialize \(\mathrm{t}=1\) as first iteration
    while termination condition is not satisfied do
        Apply the clonal and quantum mutation operators over the \(Q(t)\) to get
        \(Q^{\prime}(t)\)
        Produce \(B^{\prime}(t)\) by observing \(Q^{\prime}(t)\).
        Decode \(V(t)\) to get \(V_{2}\).
        Divide \(V_{2}\) into two subpopulations, \(V_{2}^{\prime}\) and \(V_{2}^{\prime \prime}\).
        Select the farthest vaccines from \(V_{2}^{\prime}\) as the current \(V_{b}\) est.
        Estimate probability distribution of the \(V_{b}\) est.
        Sample the distribution to get the new \(V_{2}^{\prime}\).
        Apply the genetic operators over the \(V_{2}^{\prime \prime}\) to get the new \(V_{2}^{\prime \prime}\).
        Build the new \(V_{2}\) by merging the new \(V_{2}^{\prime}\) and new \(V_{2}^{\prime \prime}\).
        Apply vaccination over \(B(t)\) using the new \(V_{2}\) to get \(B V(t)\).
        Apply clonal selection operator over \(B V(t)\) to get \(Q(t+1)\).
    end while
```

- Initialization: Quantum antibodies and vaccines populations are created where $V(t)$ is initialized with $n$ quantum vaccines where $n$ is the number of grids that the decision space is divided to. Quantum antibodies $Q(t)$ are cloned and mutated to get $Q^{\prime}(t)$ using the clonal operator $\theta$ where,

$$
\theta\left(Q_{t}\right)=\left[\theta\left(q_{1}\right), \theta\left(q_{2}\right), \ldots, \theta\left(q_{m}\right)\right]
$$

- Vaccine Selection and vaccination: Hamming distance is used to compute the distance between the vaccines and antibodies to evaluate the farthest vaccines. Vaccines with higher hamming distances from all antibodies are selected into $V_{b}$ est set. Vaccines in this set are used to apply the injection process over the mutated antibodies clones.
- Vaccine Sampling: EDA estimates the probability distribution of the next iterations best vaccines from the current $V_{b}$ est. It uses the mean and standard deviation (sd) of the vaccines in $V_{b}$ est to construct its model.
- Clonal selection: The best antibodies from the vaccined antibodies population and selected to form $\mathrm{Q}(\mathrm{t}+1)$ to proceed to a new iteration.


# 4 Experiemntal Results 

This section introduces the implementation and evaluation of the proposed algorithm. An intial number of the antibodies was set to 5 where 1000 iterations were done. Each antibody has a clone scale of 5 and a probabailty of mutation of 0.5 . The proposed algorithm is implemented and evaluated using eight benchmark test problems where the first four are unimodal and last four are multimodal

problems [9]. A set of four evaluation indicators are used in this paper where they are computed for the QICA-V with EDA over all the test functions. These indicators include the best (B) and worst solutions (W) found in addition to the average fitness (AF) and average standard deviation (AS) of all solutions. The results are then compared with their found in the literature for the QICA and the QICA-V algorithms as in table 1 Table 1 shows that the QICA-V with EDA performs better than QICA and QICA-V in all experiments except for the unimodal Shwefels and multi modal Shwefel functions. The algorithm is able to achieve the optimal solution of the problems with high degree of diversity represented in the high standard deviation values. The EDA sampling mechanism of the proposed algorithm proved its effectiveness over the vaccine operator of the QICA-V in reaching optimal solutions in multimodal problems and maintaining better performance with reduced complexity.

The error rate of the proposed algorithm and compared algorithms are recorded and visualized for all test problems. Due to limit pages Fig. 1(a) \& 1(b) show error rates for some benchmark test problems. The proposed algorithm performance is the best over the other algorithms in achieving optimal solutions at earlier iterations. Although the multimodal property of the Rastring problem, QICA-V with EDA was the best and the quickest to achieve optimality where QICA-V takes more iterations to achieve it. QICA has the worst performance where it failed to achieve the optimality in the multi modal Rastring problem and converges to it in Sphere problem. The population dynamics was also captured and visualized to check how the solutions are evolved through the evolutionary process. The population dynamics of the first 3000 evaluations of the QICA-V, QICA and our algorithm for a sample of multimodal and unimodal test problems are shown in Fig.2, $3 \& 4$.

As shown in Fig.2, 3 \&4, QICA-V with EDA was able to converge to optimal solutions through the first evluations for the multi modal problems although the QICA-V failed to do the same. Solutions have high degree of variation due to

Table 1. Experimental Results of all algorithms

![img-0.jpeg](img-0.jpeg)
(a) Error Rate for Rastring problem. (b) Error Rate for Sphere problem.

Fig. 1. Error Rate for Rastring \& Sphere function
![img-1.jpeg](img-1.jpeg)
(a) Pop. dynamics using QICA-V. (b) Pop. dynamics using proposed algorithm.

Fig. 2. Population dynamics of Ackely function
![img-2.jpeg](img-2.jpeg)
(a) Pop. dynamics using QICA-V. (b) Pop. dynamics using proposed algorithm.

Fig. 3. Population dynamics of Rastring function
the EDA sampling mechansim where low vaired solutions obtained by QICA-V using the genetic cross over and mutataion. For unimodal functions, QICA-V has better performance due to the simple problems structure but EDA sampling was again better. For simple two dimension problem, both algorithms behave almost the same either in convergence speed or solutions diversity.

![img-3.jpeg](img-3.jpeg)
(a) Pop. dynamics using QICA-V. (b) Pop. dynamics using proposed algorithm.

Fig. 4. Population dynamics of Sphere function

# 5 Conclusions 

In this paper, we proposed a new bio inspired algorithm that integrates quantum vaccine immune clonal algorithm with EDA (QICA-V with EDA). It employs immune concepts and the quantum computing principles with the aid of vaccine operator and EDA sampling mechanism. The quantum representation and vaccination helped in improving the search capabilities of the algorithm and the fitness of solutions. The EDA sampling helped in improving the diversity between solutions with reduced complexity and execution time. The performance of the proposed algorithm was analyzed and the results verified that it outperformed QICA and the QICA-V. It was able to produce high quality diversified solutions for both unimodal and multimodal benchmark problems. For further research, extensive experiments with detailed analysis are needed as well as an implementation of real applications.
