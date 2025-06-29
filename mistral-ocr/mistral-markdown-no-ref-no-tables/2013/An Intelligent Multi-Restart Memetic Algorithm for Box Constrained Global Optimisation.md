# An Intelligent Multi-Restart Memetic Algorithm for Box Constrained Global Optimisation 

J. Sun*<br>J.Sun@abertay.ac.uk<br>CPIB, School of Bioscience, The University of Nottingham,<br>Sutton Bonington, LE12 5RD, United Kingdom<br>J. M. Garibaldi<br>jmg@cs.nott.ac.uk<br>Department of Computer Science, The University of Nottingham,<br>Nottingham, NG8 1BB, United Kingdom<br>N. Krasnogor<br>nxk@cs.nott.ac.uk<br>Department of Computer Science, The University of Nottingham,<br>Nottingham, NG8 1BB, United Kingdom<br>Q. Zhang<br>qzhang@essex.ac.uk<br>Department of Computing and Electrical Systems, The University of Essex,<br>Colchester, CO4 3SQ, United Kingdom


#### Abstract

In this paper, we propose a multi-restart memetic algorithm framework for box constrained global continuous optimisation. In this framework, an evolutionary algorithm (EA) and a local optimizer are employed as separated building blocks. The EA is used to explore the search space for very promising solutions (e.g., solutions in the attraction basin of the global optimum) through its exploration capability and previous EA search history, and local search is used to improve these promising solutions to local optima. An estimation of distribution algorithm (EDA) combined with a derivative free local optimizer, called NEWUOA (M. Powell, Developments of NEWUOA for minimization without derivatives. Journal of Numerical Analysis, 28:649-664, 2008), is developed based on this framework and empirically compared with several well-known EAs on a set of 40 commonly used test functions. The main components of the specific algorithm include: (1) an adaptive multivariate probability model, (2) a multiple sampling strategy, (3) decoupling of the hybridisation strategy, and (4) a restart mechanism. The adaptive multivariate probability model and multiple sampling strategy are designed to enhance the exploration capability. The restart mechanism attempts to make the search escape from local optima, resorting to previous search history. Comparison results show that the algorithm is comparable with the best known EAs, including the winner of the 2005 IEEE Congress on Evolutionary Computation (CEC2005), and significantly better than the others in terms of both the solution quality and computational cost.


## Keywords

Global numerical optimisation, estimation of distribution algorithm, local search, memetic algorithm.

[^0]
[^0]:    *Corresponding Author.

# 1 Introduction 

In this paper, we consider the following box constrained optimisation problem:

$$
\min _{\mathbf{x}=\left(x_{1}, \cdots, x_{n}\right) \in \mathcal{D} \subset \mathbb{R}^{n}} f(\mathbf{x})
$$

where $\mathcal{D}$ is the search space with $x_{i} \in\left[a_{i}, b_{i}\right], 1 \leq i \leq n$ and $n$ is the dimensionality of the optimisation problem. From the 1970s, population-based modern global optimisation methods, such as evolutionary programming (Fogel, 1999; Yao and Liu, 1999; Lee and Yao, 2004), genetic algorithms (Michalewicz, 1996; Tsai et al., 2004; Tu and Lu, 2004; Wang and Dang, 2007; Leung and Wang, 2001; Zhong et al., 2004), estimation of distribution algorithms (Larrañaga and Lozano, 2002; Zhang et al., 2003), and many others have been proposed and achieved great success in theory and practice.

One of the main concerns in the design of evolutionary algorithms (EAs) is to balance the exploration and exploitation aspects (Bäck, 1996; Bäck et al., 1997; Torn and Zilinskas, 1989) for effective and efficient search. Among these EAs, memetic algorithms (MAs), that is, the combination of local search (LS) and EAs (Moscato, 1989), have been considered as a promising paradigm. MAs aim to improve the slow convergence of EAs to locate high-quality solutions by using LS to exploit the local fitness landscape. Readers are referred to Hart et al. (2005) for recent advances in MAs, and Krasnogor and Smith (2000) or Krasnogor and Smith (2005) for a comprehensive review of MAs in solving optimisation problems. Also, see Krasnogor (2009) for a more detailed discussion of the balance between exploration and exploitation in MAs.

To design an efficient MA, the trade-off between the intensities of EA and LS methods needs to be carefully tuned under a fixed computational budget. Various strategies have been proposed in the literature to address the trade-off, particularly for continuous optimisation. As summarised elsewhere (Nguyen, Ong, and Krasnogor, 2007; Nguyen et al., 2009), the basic issues addressed in these strategies include: (i) the LS frequency, or similarly, the LS probability, (i.e., how often the LS is applied); (ii) the LS intensity (i.e., for how long to apply the LS); (iii) the subset of individuals selected to carry out LS; and (iv) the selection of memes (i.e., local optimizers) to be used. The study in Nguyen, Ong, and Krasnogor (2007) showed that the LS frequency and intensity should be balanced under a fixed computational budget, and it is better to apply the LS to the best individuals. Theoretical analysis of convergence and search speed of MAs can be found in Sudholt (2006, 2009). Extensive studies on the selection of memes, such as adaptive MAs (Ong and Keane, 2004; Ong et al., 2006; Houck et al., 2004) and co-evolving MAs (Smith, 2003, 2007), have shown that the memes employed have a major influence on the search performance of the MAs. Interested readers are referred to Ong et al. (2006) and the references therein. In this paper, we focus on the development of a MA with a single LS.

Hart (1994) proposed several mechanisms to decide which solutions LS should be applied to, and the LS frequency, including a fixed frequency method, a fitness-based adaptive method, and a distribution-based adaptive method. In the fixed frequency method, LS is to be used in a fixed frequency of generations to all new offspring. The fitness-based adaptive method biases the application of LS to promising solutions with an LS probability. The distribution-based adaptive method applies LS only to solutions that are far away from each other, or without redundancy in the population.

In Bambha et al. (2004), simulated heating is applied to vary an LS parameter (which specifies the LS intensity) during the optimisation process. In Molina et al. (2005), the LS intensity and probability are decided according to the individual qualities in the

population at each generation. An MA based on LS chains is developed in Molina et al. (2010) where previous LS parameters are inherited for the application of LS to newly generated individuals with fixed LS intensity, and the percentage of evaluations spent on LS is fixed. In Nguyen, Ong, Lim, et al. (2007), an adaptive method has been proposed for the selection of proper individuals to undertake LS. The probabilistic memetic framework developed in Nguyen et al. (2009) estimates the LS intensity for each individual at each generation. In Zhang et al. (2003), cheap and expensive LS algorithms are applied intelligently to solutions in different search stages. Cheap LS is applied to all new solutions to improve them within a limited number of steps. Expensive LS is only applied to the best solutions in every generation. The cheap LS can improve exploration ability, while the expensive LS will finally locate a near-global optimum.

Usually, for continuous optimisation problems, the memes used are classical LS algorithms, such as those methods appearing in the Schwefel libraries (Schwefel, 1995). Researchers have also proposed to use deliberately designed crossover operators or even an EA to take the role of LS in continuous domain optimisation, such as XLS (Satoh et al., 1996), SPX (Tsutsui et al., 1999; Tsutsui and Goldberg, 2002; Noman and Iba, 2008), and crossover LS (Jones, 1995; O'Reilly and Oppacher, 1995; Satoh et al., 1996; Lozano et al., 2004), among otheres. In Molina et al. (2010), CMA-ES (Hansen and Ostermeier, 2001) is applied as the LS algorithm. Although these methods may perform well, it is doubtful whether these heuristic-based local optimizers are more effective and efficient than classical LS algorithms for local improvement.

Informally, an LS is coupled with an EA in any existing MA. Usually, the LS takes effect on selected individuals at frequent generations (sometimes every generation). This could lead (in some cases) to the MA placing too much emphasis on exploitation. In other words, the balance of exploration and exploitation may be shifted too much in favour of exploitation (Houck et al., 1997). To redress the balance, we believe that it may sometimes be preferable to reduce the relative contribution of LS within the MA. Moreover, the computational cost to add a new solution to the overall MA process by EA and LS may also be highly unbalanced. It is rather easy for EA reproduction operators to generate such a solution, while LS usually requires a higher cost (although the cost does vary considerably depending on the LS intensity). In existing MAs, the imbalance is redressed by tuning the LS frequency and intensity. This tuning could make the development of an efficient MA rather complex.

In this paper, we attempt to moderate these problems in existing MAs. To realize this goal, we propose to isolate LS from the evolutionary search but not vice versa. That is, LS will be applied to improve a limited number of very promising solutions found by an EA in full strength, not to all or part of the population as in previous hybridisation strategies. Hence, we do not need to explicitly tune the LS frequency and intensity. The underlying idea of the algorithm design is to clearly distinguish exploration and exploitation. The task of the EA is limited to exploring the search space for very promising solutions, which is its advantage and should be strengthened. The task of the LS is to improve the very promising solutions efficiently to local optima. The less efforts contributed to the exploration for very promising solutions, the better. The design issues that arise are how to design an EA with good exploration capability and how to speed up an EA's exploration under a fixed computational budget. These problems are addressed in this paper.

The proposed algorithmic framework is described and discussed in Section 2. Section 3 describes the components of the exemplar algorithm including the adaptive

![img-0.jpeg](img-0.jpeg)

Figure 1: (a) The flowchart of the proposed novel framework and (b) the traditional MA framework as described in Eiben and Smith (2003).
multivariate model, multiple sampling strategy, and the embedding of these components. Section 4 gives the experimental results on a diverse set of commonly used test problems including those in the 2005 IEEE Congress on Evolutionary Computation (CEC2005; Suganthan et al., 2005) and the comparison with some well-known EAs. The effects of the algorithmic components, including the adaptive multivariate model, the multiple sampling strategy, the selection operation, the population size, and the decoupling hybridisation strategy, on the performance of the developed algorithm, and the scalability property of the developed algorithm, are experimentally studied in this section. Important issues related to the algorithmic framework and the developed algorithm are discussed in Section 5. Section 6 concludes the paper.

# 2 The Algorithmic Framework 

Recall that one of the main merits of EAs is that they usually show good ability to explore the search space, while LSs are good at locating local optima. It is worth noting that the quality of the local optima found by LSs largely depends on the initial solutions they start from (although the parameters of the LS are also important, but basically it is the location of the initial solutions that decide the final solution quality). Imagine that if the exploration ability of an EA is extensively increased so that it can provide a very promising solution (e.g., a solution located in the attraction basin of a high-quality optimum, or the global optimum) in a short time, then a properly selected LS will improve the solution to the high-quality local optimum, or the global optimum, efficiently. If this idea can be realised, an efficient optimisation algorithm will be achieved.

The key design issues of an MA based on the above idea lies in the success of designing an EA that is able to quickly locate the very promising solution and the selection of a proper LS. However, it is not always guaranteed that an EA can find the near global optimum solution. Also, the EA's low exploration speed is not acceptable under a fixed computational budget.

In light of the above arguments, we propose a novel memetic framework, called intelligent multi-restart memetic algorithm (IMMA). Figure 1(a) displays the flowchart of the proposed framework. In the framework, LS and EA are untangled and committed to acting separately. That is, no LS is applied inside EA, which distinguishes the classical

```
Algorithm 1 The abstract IMMA algorithm framework
Input: The population size \(M\), the size of the selected population \(K\), and the restart criterion \(\mathcal{C}\)
Output: The best solution found \(\mathbf{x}^{*}\)
    Initialization
    Set \(t:=0, c=0\), restart \(:=0\). Set \(\mathbf{x}_{c}, \mathbf{x}^{*}\) and \(\mathbf{x}_{c}^{*}\) as empty;
    Diversification
    if restart \(=1\), set \(c:=c+1\) and restart \(:=0\).
    Randomly or heuristically generate a set of solutions as the initial population \(\mathcal{P}(t)\). Evaluate
    \(\mathcal{P}(t) \cdot\) Set \(\mathbf{x}_{c}\) as the best solution in \(\mathcal{P}(t)\).
    Selection
    Select \(K\) solutions from \(\mathcal{P}(t)\) by a selection method;
    Reproduction
    Create a set of offspring according to the \(K\) selected solutions;
    Replacement
    Replace partially or fully \(\mathcal{P}(t)\) by the created solutions;
    Best Solution Updating
    if the best solution in \(\mathcal{P}(t+1)\) has a better fitness than \(\mathbf{x}_{c}\), replace \(\mathbf{x}_{c}\) with the best solution;
    Set \(t:=t+1\);
    Check Search Status
    if the restart criterion \(\mathcal{C}\) has been satisfied,
        then perform LS taking \(\mathbf{x}_{c}\) as the initial point. Set the resultant local optimum as \(\mathbf{x}_{c}^{*}\).
            Set \(\mathbf{x}^{*}\) as the solution with the minimum objective function value among the \((c+1)\)
            solutions, and restart \(:=1\).
        else goto line 6 .
    Stop Criterion Check
    if the stop criterion has not been met, goto line 3 .
    else Stop and return \(\mathbf{x}^{*}\).
```

MA framework shown in Figure 1(b) where local search intertwines with EA operation. In the developed framework, local search comes into play only if an EA is considered to have found a very promising solution. The framework requires an EA with strong exploration ability and a fast exploration speed. If the termination criterion (e.g., fixed computational budget) has not been reached, the diversification scheme is applied so that the EA may escape from the local optima. This multi-restart strategy is used to increase the possibility of finding near global optimum solutions as opposed to the stochastic nature of EAs. Moreover, to enhance the efficiency of the new evolutionary search, it will be particularly useful if we can use knowledge obtained from previous visited solutions. The abstract algorithmic framework shown in Algorithm 1 describes the idea in more detail.

In the algorithmic framework, the loop from Selection to Check Search Status until convergence is called a cycle, that is, a typical run of an EA. The EA is considered to have converged if the restart criterion $\mathcal{C}$ is satisfied. The restart criterion $\mathcal{C}$ stops the EA's process of exploring for attraction basins of high quality solutions. After a cycle ends, local search is applied to improve the best solution found in the cycle. In Diversification, a new cycle begins following a finished cycle. We use $\mathbf{x}_{c}$ to record the best solution found in each cycle (called the cycle best), $\mathbf{x}_{c}^{*}$ is the local optimum resulting from the application of LS on $\mathbf{x}_{c}$, and $\mathbf{x}^{*}$ is the best solution among these local optima (called the global best).

In each cycle, the EA components can be specified at will, although the critical design issue is how to increase the exploration ability so that a promising solution can be found quickly. The restart criterion has an important role in deciding when a very promising solution is found. In our implementation, we consider the EA has found a possible very promising solution if in $T$ consecutive generations, $\mathbf{x}_{c}$ is not updated. This does not guarantee that the current $\mathbf{x}_{c}$ is truly very promising; it may just be that the evolutionary search has been trapped in a large attraction basin. To tell exactly whether $\mathbf{x}_{c}$ is promising or not depends on knowledge about the fitness landscape of the optimisation problem. Unfortunately, this is not usually available. However, to choose between two solutions for the LS application, a direct (yet heuristic) approach is to choose the one with a smaller objective function value. A previous study (Nguyen, Ong, and Krasnogor, 2007) has already shown that the LS improvement over best individuals can result in good algorithmic performance. Note that the EA is supposed to be developed with good exploration ability. Therefore, we may postulate that the current best solution is more possible to be located in the attraction basin of a high-quality optimum than the other visited solutions. The stagnation of current evolutionary search also implies that the EA has reached the fine search stage. The use of the LS will make the exploitation much more efficient than the EA itself. Since we do not need the EA to carry out exploitation, $T$ should be relatively small. A small $T$ can also avoid the EA expending computational resources in cases where a large attraction basin is encountered.

In the algorithmic framework, at the end of each cycle, the current best solution (or cycle best, i.e., $\mathbf{x}_{c}$ ) is used as the initial solution for the LS. During the search, we may think of not applying the LS to improve $\mathbf{x}_{c}$ in cases where its fitness is worse than previous ones (i.e., $\mathbf{x}_{j}, 0 \leq j \leq c-1$ ). However, it is still worth expending computational cost on improving $\mathbf{x}_{c}$ since we do not have any criteria to tell its location in the fitness landscape. Alternately, some criteria to decide intelligently whether to apply the local search could be developed. For example, if the minimal distance between $\mathbf{x}_{c}$ and $\mathbf{x}_{j}, 0 \leq j \leq c-1$ is less than a threshold, then it may not be wise to apply local search to improve $\mathbf{x}_{c}$ since it may lead to the same local optimum. We do not include this consideration in our implementation, since there are no theoretical rules to decide the threshold: the threshold will depend on the optimisation problem.

If the stop criterion has not been met, we either maintain the current search, or restart a new search. To restart the search in the $(c+1)$ th cycle, a new population of solutions can be randomly or heuristically generated. Note that as we already have some knowledge from previous search history, this may be useful for further searches in two ways. First, the new population can be generated intelligently by taking this knowledge into consideration. For example, we may want the generated population to be far away from the local optima identified so far, so that further searches can escape from them. Second, this knowledge may be used to guide the creation of offspring in the future searches. We will address these issues in the following sections.

To summarise, we see that developing an efficient MA based on the developed framework mostly depends on three factors, that is, an EA with effective exploration capability, a proper LS, and an intelligent diversification scheme. Among these factors, the diversification scheme is expected to help the search escape from local optima through the use of the learned knowledge if the EA fails to provide a solution that locates in the attraction basin of the global optimum. This implies that the developed MA may not perform well on optimisation problems if the learned knowledge has no prospective guidance on the global optimum, for example, problems with very unstructured fitness landscapes.

```
Algorithm 2 The EDA framework
1. Initialization. Randomly generate a set of solutions as the initial population \(\mathcal{P}(0)\); Set
    \(t:=0 ;\)
2. repeat
    Selection. Select promising solutions from \(\mathcal{P}(t)\) to constitute the parent set \(\mathcal{P}^{s}(t)\);
    Modeling. Build a probability model \(p(\mathbf{x}, t)\) from \(\mathcal{P}^{s}(t)\);
    Sampling. Sample offspring from \(p(\mathbf{x}, t)\) to constitute a set \(S\);
    Replacement. Replace all or partially \(\mathcal{P}(t)\) with \(S\) to form \(\mathcal{P}(t+1)\); set \(t:=t+1\);
3. until stop criterion has been met.
```

```
Algorithm 3 The adaptive univariate probability model
Input: The parent set \(\mathcal{P}^{s}(t)\).
Output: The probability \(p\left(x_{i}, t\right)\) for the \(i\)-th component \(x_{i}\).
    1. Find \(\ell_{i}^{\min }=\min \left\{x_{i}^{k}(t), 1 \leq k \leq K\right\}\), and \(\ell_{i}^{\max }=\max \left\{x_{i}^{k}(t), 1 \leq k \leq K\right\} ;\)
2. Assign a small probability value to the intervals \(\left[\ell_{i}^{\min }-\varepsilon_{i}, \ell_{i}^{\min }\right]\) and \(\left[\ell_{i}^{\max }, \ell_{i}^{\max }+\varepsilon_{i}\right]\), and a big probability value to \(\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]\), where \(\varepsilon_{i}\) is a predefined small positive real number.
```


# 3 Exemplar Algorithmic Implementation 

The previous section describes a generic algorithmic framework. In this section, we describe one specific implementation of the framework in which our implementation is based on an estimation of distribution algorithm (EDA). In this section, we describe the various components that form our implementation, including an adaptive multivariate model and an offspring generation scheme, and the embedding of these components. To begin, we briefly describe the EDA.

### 3.1 Estimation of Distribution Algorithm

The EDA was initially proposed by Mühlenbein and Paaß (1996). It maintains and evolves a set of individuals as in other EAs. But EDAs do not use crossover or mutation operators to produce new offspring. Instead, EDAs produce offspring by sampling from a probabilistic model. The statistical information extracted from promising solutions is used to construct the probabilistic model. The sampling of new offspring from the probability model is expected to guide the search to promising search areas. EDAs can be summarised as shown in Algorithm 2.

Existing EDAs for continuous optimisation can be classified with respect to the statistical model $p(\mathbf{x}, t)$ assumed. The probability models assumed include a Gaussian distribution (Larrañaga and Lozano, 2002), a Gaussian mixture (Bosman and Thierens, 2000), and a histogram (Tsutsui et al., 2001; Zhang et al., 2003). Readers are referred to Larrañaga and Lozano (2002) for a detailed description of EDAs.

### 3.2 Adaptive Multivariate Model

In our exemplar algorithm, an adaptive multivariate probability model $p(\mathbf{x}, t)=\prod_{i=1}^{n}$ $p\left(x_{i}, t\right)$ with $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ is assumed to represent the statistical information extracted from the parent set. Suppose that at generation $t$, the parent set consists of $\mathcal{P}^{s}(t)=$ $\left\{\mathbf{x}^{1}(t), \mathbf{x}^{2}(t), \ldots, \mathbf{x}^{K}(t)\right\}$ where $K$ is the size of the parent set. For the $i$ th dimension, $p\left(x_{i}, t\right)$ is computed as described in Algorithm 3.

![img-1.jpeg](img-1.jpeg)

Figure 2: (a) The adaptive multivariate probability model and (b) the univariate marginal histogram model at early and later stages.

The distributions of the $i$ th variable, $x_{i}$, in the early and later stages of the search could be the profile as shown in Figure 2(a). In comparison, the marginal histogram model developed in Zhang et al. (2003) could be the profile as shown in Figure 2(b). In the marginal histogram model, the range of each variable is divided into a fixed number of subintervals with the same length. The histogram of the selected solutions at each variable is used to represent the probability model. The difference between the developed model and the histogram model is that the range of the decision variable in the developed model will adapt to the search environment.

From Figure 2, we see that the flat distribution in the adaptive multivariate probability model could promote exploration of the search space. On the other hand, the developed model will inevitably shrink the search space, and so accelerate the speed of evolutionary search. However, the shrinkage will weaken the exploration capability, since there is no chance to explore the search space outside $\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$ whenever the shrinkage has happened. To moderate this problem, we adopt two strategies. First, we expand the present search space to $\left[\ell_{i}^{\min }-\varepsilon_{i}, \ell_{i}^{\max }+\varepsilon_{i}\right]$, where $\varepsilon_{i}$ is a small number which is proportional to $b_{i}-a_{i}$. Second, the uniform distribution is applied to the inter$\operatorname{val}\left[\ell_{i}^{\min }, \ell_{i}^{\max }\right]$ (step 2). This is to make the generated solutions as diversified as possible in the search space, so that a good exploration can be expected. The time complexity to compute $p(\mathbf{x}, t)$ is $\mathcal{O}(n K)$, which is linear to the dimension and the selected population size.

# 3.3 Guided Mutation and Multiple Sampling Strategy 

The proximate optimality principle (POP), first stated by Glover and Laguna (1998), has been applied widely (explicitly or implicitly) in meta-heuristics proposed for combinatorial optimisation problems, such as in Zhang et al. (2005) for the maximum clique problem, in Stützle (1999) and Zhang et al. (2004) for the quadratic assignment problem, and many others. It has been found in Glover (1998) that optimal solutions of the traveling salesman problem have $80 \%$ similarities. The POP states that good solutions

```
Algorithm 4 The guided mutation operator (note that \([A]\) rounds the elements of
\(A\) to the nearest integers greater than or equal to \(A\), and \(n\) is the dimension of the
solution vector).
Algorithm \(\left(\mathbf{x}^{*}, \alpha, p(\mathbf{x})\right)\)
Input: A template solution \(\mathbf{x}^{*}=\left(x_{1}^{*}, \cdots, x_{n}^{*}\right)\), a real number \(0 \leq \alpha \leq 1\) and a probability
    model \(p(\mathbf{x}, t)=\prod p\left(x_{i}, t\right)\).
Output: An offspring \(\mathbf{x}=\left(x_{1}, \cdots, x_{n}\right)\).
```

1. Set $U=\{1,2, \cdots, n\}$ and $d:=\lceil\alpha n\rceil$; Randomly select a set of indices $V \subset U$ with $|V|=d$
2. For all $i \in V$, set $x_{i}:=x_{i}^{*}$; For all $j \in U \backslash V$, sample a value $y$ from the probability model $p\left(x_{j}, t\right)$, set $x_{j}:=y$
3. Return $\mathbf{x}$;
have similar structures (components). The POP has also been successfully applied to continuous optimisation (Sun et al., 2005), which indicates that the POP can be very helpful in real-parameter optimisation. Actually, the POP has been widely but implicitly applied in EAs, such as in the mutation operators.

The explicit forms of the application of the POP are guided mutation (Zhang et al., 2005, 2004) and iterated local search (Stützle, 1999). Guided mutation has the advantage of generating offspring based on the guidance of statistical information. It has been particularly and most successfully applied to combinatorial optimisation problems. However, it can be easily applied to continuous optimisation problems in cases in which a fully factorised multivariate probability model is used. The offspring generation scheme can be summarised in Algorithm 4 with a template solution $\mathbf{x}^{*}$ and a probability model $p(\mathbf{x}, t)$.

To create offspring with Algorithm GMSampling, the best solution $\mathbf{x}^{*}$, that is, the solution with the least objective function value among all the visited solutions, is taken as the template solution. The fixing of some components (subset $V$ ) of $\mathbf{x}^{*}$ takes advantage of the legacy of the best solution. The creation of the rest of the components (subset $U \backslash V$ ) is guided by the probability model $p(\mathbf{x}, t)$. The random selection of $V$ makes it possible for the search to find components in $\mathbf{x}^{*}$ that are the same as the global or near-global optimum. The time complexity of sampling one individual is $\mathcal{O}(n)$.

Parameter $\alpha$, taking values from 0 to 1 , controls the intensity of the fixing of the decision variables. It reflects to what extent POP holds for a certain optimisation problem. It can be expected that a large $\alpha$ value implies a quick evolutionary search, but a weak exploration capability, since a large number of variables will be copied from the best solution found so far. Moreover, the optimal $\alpha$ setting for efficient exploration varies with optimisation problems, and there is no a priori guidance on how to choose the best value in advance. Therefore, we propose to learn the parameter adaptively during the search in our implementation.

Recalling the weakness of the adaptive multivariate model described in Section 3.2, here we moderate this weakness through a multiple sampling strategy. Note that in almost all probability model based evolutionary algorithms, the number of individuals sampled from the probability model is usually less than, or equal to, the population size. As known in statistics (e.g., Markov Chain Monte Carlo theory, Robert and Casella, 2004), to truly represent the distribution of $p(\mathbf{x}, t)$, a large set of data points needs to be sampled from $p(\mathbf{x}, t)$. Therefore, statistically speaking, the small sample size applied in most EDAs will result in high sampling noise, leading to the false guidance problem in

the search procedure. That is, the sampling noise may mislead the search to possibly wrong areas, even though $p(\mathbf{x}, t)$ is accurate. Once this has happened, it is then hard to change back to the right track and, importantly, computational effort will be wasted. One straightforward way to reduce the sampling noise is to sample many more individuals to carry out replacement for the construction of the follow-up generation. This is the so-called multiple sampling strategy.

It should be pointed out that if optimisation problems do not obey the POP assumption (e.g., optimisation problems with discontinuous search domains), that is, if the commonality among the local optima and the global optimum does not exist, the later search cannot obtain any benefit from the best solution found so far. Consequently, the search may be inefficient, since it will rely on EA and LS entirely.

# 3.4 The Specific Algorithm 

In this section, we embed the developed components described in Sections 3.2-3.3 to build the algorithm used in this paper.

### 3.4.1 The EDA

To construct an EDA, as seen in Algorithm 2, we first need to choose a selection method. Here, we apply the well-known truncation selection. In truncation selection, the fitness values of individuals in the population are sorted, and the individuals with the best fitness values are selected. We use the adaptive multivariate probability model described in Algorithm 3 to carry out modeling. The sampling method described in Algorithm 4 is applied to create new offspring. Note that there is a control parameter $\alpha \in[0,1]$ in the sampling method. We fix it in each cycle and adjust it adaptively at the end of each cycle as follows:
if the current cycle found a better solution $\mathbf{x}_{c}^{*}$ than the previous ones $\mathbf{x}_{j}^{*}, 1 \leq j \leq c-1$
then $\quad$ set $\alpha:=\alpha+\frac{1}{n} ;$
else $\quad$ set $\alpha:=\max \left\{\alpha-\frac{1}{n}, 0\right\}$;
end if

That is, when the current cycle has found a better solution $\left(f\left(\mathbf{x}_{c}^{*}\right)<f\left(\mathbf{x}_{j}^{*}\right), 0 \leq j \leq\right.$ $c-1$ ), we will set a bigger $\alpha$ value for the following cycle. The reasoning behind this is that we have more confidence that there are more similar components between the best solution $\mathbf{x}^{*}=\arg \min _{0 \leq t \leq c}\left\{f\left(\mathbf{x}_{t}^{*}\right), \ldots, f\left(\mathbf{x}_{c}^{*}\right)\right\}$ and the global optimum under the POP assumption. If the current cycle cannot find a better solution, then it means our choice of $\alpha$ is not proper. In this case, $\alpha$ decreases by $\frac{1}{n}$ (ensuring $\alpha$ is greater than zero). If no better solution is found in the new cycle of search, $\alpha$ will be decreased again. Obviously, $\alpha$ cannot be negative. In the first cycle, $\alpha$ is set to zero. This is to make the algorithm explore the search space as much as possible. Moreover, if in some consecutive cycles, there are no better solutions $\mathbf{x}_{c}^{*}$ found, $\alpha$ could decrease to zero, which means that new search areas are to be explored.

As discussed in Section 3.3, it is appropriate to sample a large number of offspring to reduce the sampling noise. In our implementation, we first introduce an indicator vector $I=\left\{i_{1}, \ldots, i_{M}\right\}$ in Selection. That is, if a solution $j$ is selected, $i_{j}:=1$, otherwise $i_{j}:=0$. We combine the sampling and replacement together as show in Algorithm 5.

```
Algorithm 5 Sampling and replacement
    for \(j=1\) to \(M\)
        if \(i_{j}=0\), then
            Sample \(L\) solutions from \(p(\mathbf{x}, t)\) using Algorithm GMSampling \(\left(\mathbf{x}^{*}, \alpha, p(\mathbf{x}, t)\right)\);
            Evaluate the sampled individuals, and pick the best one to replace \(\mathbf{x}_{j}\);
        else
            Keep the current solution \(\mathbf{x}_{j}\).
            end if
    end for
```


# 3.4.2 The Restart Mechanism 

In our implementation, we apply a simple diversification scheme. That is, we randomly generate a set of individuals with size $N=\max \{1000,2 n\} \gg M$. The $M$ individuals that have the largest distances to $\mathcal{X}=\left\{\mathbf{x}_{0}^{*}, \ldots, \mathbf{x}_{c}^{*}\right\}$ are selected to form the initial population of the $(c+1)$ th cycle. The distance between a randomly generated individual $\mathbf{x}$ and the set of visited local optima $\mathcal{X}$ is defined as:

$$
d_{\mathbf{x}}=\min _{0 \leq i \leq c}\left\|\mathbf{x}-\mathbf{x}_{i}^{*}\right\|
$$

where $\|\cdot\|$ is the Euclidean distance (but other distance measures may be used).

### 3.4.3 The Local Search

To carry out local search, we use an iterative derivative-free unconstrained optimisation algorithm developed by Powell (2006, 2008), called NEWUOA. Of course, we do not rule out the application of other local search algorithms.

Essentially, NEWUOA is an iterative trust-region method. At the $k$ th step, it constructs a local quadratic model $\mathcal{Q}_{k}$ by interpolating a set of $m$ solutions (initially sampled in the radius $\rho_{k}\left(\rho_{0}=\rho_{\text {beg }}\right)$ of the initial solution $\mathbf{x}_{\text {ini }}$ ). The local model within the trust region, which is a disc of radius $\Delta_{k}=\rho_{k}$, is optimized. Based on the quality of the obtained optimal solution $\mathbf{x}^{*}$, the trust region radius $\Delta_{k}$ is either expanded or contracted. The local model is updated by minimizing the Frobenius norm of the change to the second derivative of $\mathcal{Q}_{k}$. The local improvement continues until the step size $\delta=\left\|\mathbf{x}_{k}-\mathbf{x}^{*}\right\|<\rho_{k}$, in which case we decrease $\rho_{k}$. The algorithm terminates if $\rho_{\text {end }}$ is reached.

From this brief description of NEWUOA, we can see that the parameters of NEWUOA are $\rho_{\text {beg }}, \rho_{\text {end }}$, and an integer $m \in\left[n+2, \frac{1}{2}(n+1)(n+2)\right]$, apart from the initial solution $\mathbf{x}_{\text {ini }} \cdot m=2 n+1$ is used in our application (as recommended in Powell, 2008), $\rho_{\text {beg }}$ is set as $0.2 \max \left\{\left|\mathbf{x}_{\text {ini }}\right|\right\}$, and $\rho_{\text {end }}$ (which can be used to control the final accuracy of the local optima) is set as $10^{-10}$. NEWUOA does not need any gradient information and hence is applicable to a large set of continuous optimisation problems. Readers are referred to Powell (2008) for a detailed description of NEWUOA.

## 4 Experimental Studies

In this section, we experimentally study the performance of IMMA. The experimental studies are divided into three parts. First, we carry out experiments to study the effects of the algorithmic components and parameters on the performance of IMMA. The algorithmic parameters include the population size $M$, the selected population size $K$, the sampling multiplication number $L$, the restart criterion number $T$, and the

expansion parameter $\varepsilon_{i}$. The expansion in each dimension of the search space is set to be $\frac{b_{i}-\varepsilon_{i}}{M}, 1 \leq i \leq n$. This is set to eliminate the influence of the variable scales in different coordinates. Among these parameters, we found that the most important ones are $M$ and $L$, while $K$ and $T$ can simply be set as $K=M / 2$ and $T=5$, respectively.

Second, we compared the developed algorithm with a diverse set of evolutionary algorithms in literature. Finally, scalability analysis was carried out to study the effect of the dimensionality of the problem on the performance of the algorithm.

# 4.1 Test Suite and Performance Evaluation Criteria 

We test our algorithm on a set of 40 commonly used test functions in the literature. Appendix A lists the descriptions of the functions and their respective characteristics including the global optimum $f^{*}$, dimensionality, and the characteristics, such as epistasis, modality, and discontinuity. The test functions $f_{1}$ through $f_{10}, f_{26}$ through $f_{34}$, and $f_{37}$, which are the same as used in Noman and Iba (2008), are applied to carry out the component analysis. In component analysis, to evaluate the performance of the algorithms, the performance criteria applied in Noman and Iba (2008) and Suganthan et al. (2005) are adopted. The analysis is based on the statistics of the criteria within 25 trials. In all cases, the maximal number of fitness evaluations (NFE) to carry out the trials is $10,000 \times n$ where $n$ is the dimension of the problem. The criteria can be summarised as follows:

- Error Criterion. The function error value (FEV) is defined as $f(\mathbf{x})-f\left(\mathbf{x}^{*}\right)$, the difference between the objective values (fitness) of the global optimum of the function and a solution $\mathbf{x}$. We record the minimal FEV that the algorithm can find within the maximal NFE, and calculate the mean $\left(\mathrm{AVG}_{E}\right)$ and standard deviation (SD) of these FEVs. The notation $\mathrm{AVG}_{E} \pm S D_{E}$ is used to summarise the criterion.
- NFE Criterion. If the minimal FEV is less than an accuracy level $\epsilon$ within NFE, the trial is considered to be successful. We count the number of successful trials, and denote the number as SUC. The number of fitness evaluations required for the algorithm to be successful is recorded, and the mean and standard deviation are calculated, and denoted by $\mathrm{AVG}_{N}$ and $S D_{N}$. The accuracy level $\epsilon$ is fixed to $10^{-6}$ for $f_{1}$ through $f_{5}$ and $f_{26}$ through $f_{40}$, to $10^{-2}$ for $f_{6}$ through $f_{16}$ and to $10^{-1}$ for $f_{17}$ through $f_{25}$ as used in Suganthan et al. (2005). The notation used here is $\mathrm{AVG}_{N} \pm S D_{N}$.
- Convergence Graphs. The graphs show the evolution process of the algorithms, that is, the average error performance against the generations and/or NFEs.
- Hypothesis Test. Hypothesis test (either the rank sum test or the Z test) is applied in the following experiments at the $5 \%$ significance level. A $p$ value less than .05 suggests a significant difference.

NFEs used by IMMA include the NFEs consumed by NEWUOA and the developed EDA. The performance comparisons of the various EAs used varying performance criteria which will be described specifically in each context.

### 4.2 Component Analysis

### 4.2.1 Sensitivity to Population Size

The population size is an important factor to the performance of EAs. Large population sizes tend to encourage the preservation of diversity and hence improve the exploration

ability of EAs. However, a large population size will make EAs exhaust the fitness evaluations too quickly. Therefore, there should be a trade-off between the exploration capability and the computational cost used for the exploration. To investigate the effect of the population size on the IMMA performance, we apply the IMMA with varied population size on the test functions with $n=30$. The adaptive multivariate model and the multiple sampling strategy with $L=3$ are applied. The population size is set as $M=k n$, where $k \in\{1,2,5,10\}$. The experimental results are listed in Table 1, where best results are shown in bold type. The upper part of the table lists the NFE criterion obtained for those functions in which all runs reach the accuracy levels, while the lower part of the table shows the error criterion obtained for those functions that IMMA cannot reach the accuracy level in all 25 trials. Table 2 lists the average number of cycles in which IMMA reaches the accuracy level, the number of success trials, and the $p$ values obtained from the rank sum test between the results for $M=60$ and other population sizes.

The upper part of Table 1 indicates that the larger the population size, the more NFEs are required to reach the accuracy level. Moreover, the lower part of the table shows that (1) an IMMA with a small population size $(M=30,60)$ can find better solutions than an IMMA with a large population size except for $f_{8,32}$ where the IMMAs with different $M$ obtain similar results; (2) for $f_{30,34}$, the IMMA with a small population size achieves a higher success rate than the IMMA with a large population size $(M=150,300)$. These observations show that a small population size is preferred over a large population size.

Moreover, comparing the IMMAs with population sizes $M=30$ and 60 (i.e., $k=$ 1,2 ), we see that the IMMA with $k=1$ requires less computational cost to reach the accuracy level except for $f_{10.29,33}$. However, the computational cost of the IMMA with $k=2$ is still very competitive. Table 1 also indicates that the IMMA with $k=2$ obtains better optimal solutions than the IMMA with $k=1$ on the functions that cannot be solved successfully. Note that most of the functions in the upper part of Table 1 have no epistasis except for $f_{6,7,10,37}$, while most of these functions in the lower part have high epistasis (see Table A1 in the appendix). This shows that the IMMA with $k=2$ can deal with high-epistasis functions better than the IMMA with $k=1$. Hence, $k=2$ should be preferred in case we do not have any prior knowledge about the characteristics of the optimisation problems.

It can be seen from the upper part of Table 2 that the number of cycles has a tendency to decrease along with an increase of population size. This indicates that, with a large population, a large number of iterations and thereafter a large number of fitness evaluations are required to complete a cycle. Consequently, only a small number of cycles (equivalently, local searches) can be carried out within a fixed number of fitness evaluations. The superior performance of the IMMA with a small population size implies that more local searches are required in order to achieve better performance.

Figure 3 displays the convergence graphs of IMMA on some selected functions. On the $x$ axis is the number of fitness evaluations, and on the $y$ axis is the FEVs. From Figure 3, we can see that usually small population sizes $(M=30,60)$ require less NFEs to reach the accuracy level (e.g., Figure 3[a,b,c]) than with large population sizes ( $M=150,300$ ), while Figure 3(d) shows that small population sizes usually obtain better FEV.

# 4.2.2 Effects of Selection 

Another important factor affecting the performance of EAs is the selection operator. Note that under the IMMA framework, we need to speed up the exploration of EA. The selection method plays an important role in the convergence performance of EA. In

![img-2.jpeg](img-2.jpeg)

Table 2: The number of cycles and success trials to reach the accuracy level and the $p$ values obtained from the rank sum test between the results obtained by the IMMA with $M=60$ and the other population sizes.
![img-3.jpeg](img-3.jpeg)

Figure 3: Convergence curve of IMMA with variations of population size for selected functions $(n=30)$. The $x$ axis shows the number of fitness evaluations. The $y$ axis shows the error values.

this section, we experimentally compare two algorithms, IMMA-P (with proportional selection) and IMMA-T (with truncation selection) on the functions with $n=30$ to carry out analysis of different selection operators. In our implementation for fitness proportional selection, the probability that an individual with fitness $f$ is selected is proportional to $\exp (-f)$ (in case of minimization).

To apply the two algorithms, the parameters are set as $M=60$ and $L=3$. Table 3 lists the best error criterion and the NFE criterion, respectively, where best results are shown in bold type. In the table, columns $p_{v}$ and $p_{n}$ list the $p$ values of the rank sum test on the best error criterion and the NFE criterion, respectively. From the table, it can be seen that at a $5 \%$ significance level, IMMA-P reaches better performances than IMMA-T on only one test function, $f_{37}$, while on three functions, $f_{2.8 .29}$, the two algorithms perform similarly. Thus, we can conclude that IMMA-T outperforms IMMA-P on average in terms of solution quality and computational cost. The experimental result justifies that truncation selection is significantly better than proportional selection under the IMMA framework. Figure 4 shows the convergence curve comparing IMMA-P and IMMA-T on some selected functions. The plots show that IMMA-T has improved convergence characteristics over IMMA-P.

# 4.2.3 Study on the Multiple Sampling Strategy 

In this section, we experimentally analyze the effect of the multiple sampling strategy on the performance of IMMA. To carry out this study, we apply the IMMA with different sampling number $L$ on the functions. We are interested in whether the multiple sampling strategy is beneficial to the exploration capability of IMMA. The algorithmic parameter settings in the experiments are $M=60 . L$ is varied from 1 to 5 . Table 4 lists the experimental results obtained by the IMMA with different $L$ settings in terms of the best error values and NFEs. In the table, the best results are shown in bold type. The $p$ values of the rank sum test on the results of $L=2$ and $L=3$ against the other $L$ values are listed in Table 5. From Table 5 we see that:

1. On the functions that cannot be solved successfully, the IMMA with sampling size $L=1$ has the best performance in terms of error value on only one function $\left(f_{27}\right)$, but this performance difference is not significant. Moreover, it can be seen that the IMMA with a large sampling size $(L=4,5)$ does not necessarily result in better FEVs.
2. In terms of efficiency (NFEs), the IMMAs with $L=2,3$ require fewer fitness evaluations to reach the accuracy level on all the multimodal functions except $f_{6.31}$ (functions $f_{1}$ through $f_{3}$ and $f_{28}$ are unimodal).

From these observations, we see that relatively more individuals (e.g., $L=2,3$ ) sampled from the probability model can indeed improve exploration capability on average. However, a large $L$ (e.g., 5) usually needs more fitness evaluations to reach the accuracy level. Therefore, we may conclude that the multiple sampling strategy with a moderate $L$ can favour evolutionary search. Since it is difficult to develop a mathematical model to determine an optimal $L$ for the balance between the exploration capability and the computational cost, we have to rely on experimental study. As seen from the results, the IMMA with $L=2,3$ achieves better results on almost all the functions. Hence, in practice, we can simply start our search for optimal $L$ from 2.

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

Figure 4: Convergence curves of the IMMA with different selection operations for selected functions $f_{5,10,30,31}(n=30)$. The $x$ axis shows the number of fitness evaluations. The $y$ axis shows the best error values.

# 4.2.4 The Superiority of the Adaptive Model 

In this section, we investigate the effect of the adaptive multivariate model on the performance of IMMA. We compare two algorithms, IMMA-H and IMMA, to carry out the investigation. Both algorithms have the same algorithmic framework as described in Section 3.4. The difference is that in IMMA-H, the histogram model (Zhang et al., 2003) is embedded. The other parameters are set as $M=60$ and $L=3$. The comparison results are listed in Table 6, in which the best results are shown in bold type. In cases for which both algorithms reached the accuracy level in 25 trials, the rank test is performed on the NFE results and summarised in the $p_{n h}$ column. On the other hand, if both algorithms failed to reach the accuracy level in all 25 trials, the rank test is performed on the best error values and summarised in the $p_{v h}$ column.

From Table 6, we see that at the $5 \%$ significance level, in terms of the best error values, IMMA performs significantly better than IMMA-H on 10 functions that cannot be solved successfully, except for $f_{h}$, where the two algorithms perform similarly. In the other 10 functions that can be successfully solved, IMMA-H performs significantly better than IMMA on five functions ( $f_{6}, f_{28}$ through $f_{30}$, and $f_{37}$ ) in terms of NFEs, and IMMA is significantly better than IMMA-H on the other five functions. This shows the superiority of the adaptive multivariate model against the histogram model, on average. The graphs in Figure 5 show that the IMMA with the adaptive model exhibits a higher convergence speed than that of IMMA-H, except for function $f_{29}$. This also confirms that the developed adaptive multivariate model is better than the histogram model in generating promising solutions.

![img-6.jpeg](img-6.jpeg)

Table 5: The $p$ values obtained through the rank sum test on the experimental results obtained by $L=2$ and $L=3$ with the other $L$ values.
# 4.3 The Superiority of the Decoupled Strategy 

In this section, we aim to study the proposed decoupled hybridisation strategy against the intertwined hybridisation scheme. To carry out the study, we compared IMMA with intertwined MA, called WMMA. WMMA is basically the same as IMMA, except that NEWUOA is applied to the best solution found at every 10 generations. The modeling, reproduction, and multiple sampling strategy are the same as in IMMA.

Table 7 summarises the obtained results. The rank sum test was performed to compare the results. The $p$ values (shown in columns $p_{v w}$ and $p_{n w}$ ) are obtained for the comparison of the best error values and NFEs, respectively. In the table, - in the $p_{v w}$ column denotes that the rank sum test is not performed because both algorithms reach the termination criterion and hence it is not necessary to carry out the test in terms of the best error values. In the $p_{n w}$ column, if both algorithms cannot reach the termination criterion within the maximal NFEs, the test is also not necessary to carry out in terms of NFEs.

From the table, it can be observed that IMMA performs significantly better than the WMMA on eight functions for which both algorithms cannot reach the termination criterion, except for $f_{8}$, where the algorithms perform the same. Moreover, IMMA needs less NFEs than the WMMA on the functions that can be solved within maximal NFEs, except on five test functions ( $f_{1.2 .28 .30 .37}$ ). This shows that, on average, the proposed hybridisation strategy is superior to the intertwined hybridisation scheme.

### 4.4 Comparison with Known EAs

In this section, IMMA is compared with the following algorithms.

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

Figure 5: Convergence curve of the IMMA with different probability model for selected functions $f_{5,7,27.29}(n=30)$. The $x$ axis shows the number of fitness evaluations. The $y$ axis shows the best error values.

1 OGA/Q. The orthogonal genetic algorithm with quantisation (OGA/Q; Leung and Wang, 2001), in which an orthogonal design is used to construct a crossover operator.

2 HTGA. The hybrid Taguchi genetic algorithm (HTGA; Tsai et al., 2004), in which a robust experimental design method, Taguchi, is applied to generate new offspring.

3 EDA/L. The hybridisation of estimation of distribution algorithm with local search algorithms (EDA/L; Zhang et al., 2003), in which a cheap local search algorithm is applied to all newly generated individuals, and an expensive local search algorithm is applied only to the best individuals at each generation.

4 LEA. The evolutionary algorithm based on level-set evolution and Latin squares (LEA; Wang and Dang, 2007), in which the Latin squares technique is applied to design a new and effective crossover operator, and the level set is gradually evolved to approach the global optimum.

5 MEDA. The multiple restart EDA (MEDA), where the described EDA in Section 3.4 is restarted multiple times.

6 MNEW. The multiple restart NEWUOA (MNEW), where NEWUOA is restarted multiple times.

7 DNEW. The multiple restart NEWUOA with the diversification scheme (DNEW) as described in Section 3.4.2.

![img-9.jpeg](img-9.jpeg)

8 DEahcSPX. The differential evolution (DE) with adaptive hill-climbing XLS (AHCXLS), called DEahcSPX (Noman and Iba, 2008).

9 IPOP-CMA-ES. The restart covariance matrix adaptive evolution strategy (CMA-ES) with increasing population size (IPOP-CMA-ES; Auger and Hansen, 2005).

10 APrMF. The adaptive probabilistic memetic framework (APrMF; Nguyen et al., 2009).

The comparisons among the well-known EAs are divided into two parts. The first part involves the comparison between IMMA and the first seven algorithms on $f_{28}$ through $f_{40}$. The second part involves IMMA and the last three algorithms on $f_{1}$ through $f_{35}$. The division is due to the fact that we do not have the experimental results of Algorithms OGA/Q, HTGA, EDA/L, and LEA on the CEC 2005 test functions.

# 4.4.1 Comparison Between IMMA and the First Seven Algorithms 

In the comparison between the first seven algorithms and IMMA, the test functions are grouped into two categories w.r.t. the number of dimensions. The dimension of functions in Category I ( $f_{28}$ through $f_{36}$ ) is 30 , while that of Category II ( $f_{37}$ through $f_{40}$ ) is 100 .

In the experiments, the algorithmic parameters of IMMA are set as follows: $M=$ $2 n, T=5$ and $L=3$. In the comparison study, the evaluation criteria are different from those used in Section 4.1. Each of the compared algorithms uses the termination criteria as originally proposed by their authors. Since IMMA is essentially a multirestart algorithm, the algorithm can be terminated after any cycle for which the global best solution is satisfactory. To carry out a fair comparison, in our implementation, for Category I functions, IMMA will terminate if the best solution found is no worse than OGA/Q (this criterion was also used in Tsai et al., 2004). For the Category II test problems, we terminate IMMA when the best solution found is no worse than the average best solution found by the other compared algorithms. Moreover, we terminate the algorithm when the NFE exceeds $n \times 10^{5}$.

Table 8 summarises the experimental results of IMMA and the results of other algorithms on the test suite. We have taken the experimental results of the compared algorithms on these problems from corresponding papers. Note that there are many other algorithms, such as the hybrid cooperative particle swarm optimisation (Bergh and Engelbrecht, 2004), the self-organizing hierarchical particle swarm optimisation with time-varying acceleration coefficients (Ratnaweera et al., 2004), the fast evolutionary programming with Cauchy mutation (Yao and Liu, 1999), and so on. We do not include the results of these algorithms since they are not as competitive as LEA (as claimed in Wang and Dang, 2007).

In the tables, NFE is the average number of fitness evaluations within 25 runs. In column $p_{z}$, the $p$ values between the best function values obtained by IMMA and the other algorithms are shown. Here the Z-test is applied between IMMA and the first four algorithms, while the rank sum test is applied between IMMA and algorithms MEDA, MNEW, and DNEW.

From Table 8, it can be seen that IMMA performs significantly better than algorithms MEDA, MNEW, and DNEW on all functions except for $f_{28}$ and $f_{30}$, which are unimodal functions. This observation shows that IMMA successfully takes advantage of EDA and NEWUOA. Moreover, it can be seen that DNEW performs at least better than

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

Figure 6: Typical evolution procedures of the proposed algorithm on $f_{30,31,34,40}$. Particularly in (b), we see that in six cycles, IMMA reaches the global optimum.

MNEW. Recall that DNEW and MNEW are the same except that the restart scheme in Section 3.4.2 is adopted in DNEW. This observation justifies the usefulness of the applied restart scheme.

Comparing IMMA with LEA, we see that IMMA performs significantly better than LEA on almost all the functions in terms of best error values except $f_{29}$. In terms of NFE, IMMA requires less than LEA except $f_{38}$. Comparing the results of IMMA with EDA/L, we see that EDA/L needs more NFEs on all functions to obtain similar accuracy, except for functions $f_{33,34}$ where EDA/L obtains better accuracies.

In the comparison between IMMA and HTGA, it can be seen that on average, HTGA needs fewer NFEs to reach the global optimum than IMMA on four functions, that is, $f_{29,31,35,38}$, while IMMA needs fewer NFEs on the rest of the nine functions. Notice that except for functions $f_{29,31,35,38}$, the remaining functions have high epistasis properties. This implies that IMMA has a better capability in dealing with epistasis than that of HTGA. The observation that IMMA obtains significantly better solutions than those of HGTA when solving $f_{37,39,40}$, which are of high dimensions and high epitasis, also confirms the implication. Comparing IMMA with OGA/Q, we see that IMMA requires much fewer NFEs on all the selected functions except $f_{38}$, but the obtained objective function values are no worse than OGA/Q.

Figure 6 shows typical evolution procedures of the proposed algorithm on $f_{30,31,34}$ and $f_{40}$. In the figures, global best (the dotted line) shows the evolution of the best solution found so far, while cycle best (the dashed line) displays the evolution of the best solutions in the cycles. In Figure 6(a), we see that the developed algorithm needs four cycles to reach the global optimum. The figure demonstrates that in some problem instances (e.g., $f_{40}$ ), IMMA can find the global optimum in one cycle, while in most optimisation problems, several cycles are required to reach the attraction basin of the global optimum. Figure 6 shows that IMMA can approach the attraction basin

gradually through learning from previous search. For example, in Figures 6(b) and 6(c), the searches in later cycles find better solutions gradually until the attraction of the global optimum has been reached. While in Figure 6(a), the later cycles cannot always find better solutions than previous cycles, but the algorithm finally adapts to reach the global attraction basin. More interestingly, in Figure 6(a), the global optimum is obtained by applying the local search algorithm from a worse initial point.

In summary, we can claim that the novel hybrid strategy can form the basis of efficient memetic algorithms. Moreover, the empirical study indicates that on average, IMMA is comparable with HTGA if not better, and is significantly better than the other compared algorithms on these functions. Note that while these results are valid for 30-dimensional functions, they may not generalise to other dimensions.

# 4.4.2 The Comparison Among IMMA, DEahcSPX and IPOP-CMA-ES 

Only two algorithms, that is, DEahcSPX (Noman and Iba, 2008) and IPOP-CMA-ES (Auger and Hansen, 2005), have been applied to the test functions used in CEC 2005. The dimensions of the test functions adopted in the CEC 2005 competition, that is, the first 25 test functions as listed in Appendix A, are restricted to 10, 30, and 50. The algorithmic parameters of IMMA are set the same as in Section 4.4.1.

DEahcSPX (Noman and Iba, 2008) applies an adaptive crossover local search, called AHCXLS, to improve the best found solution at each generation. This hybrid strategy is similar to that developed in Zhang et al. (2003) except that the crossover LS rather than the classical LS is applied. IPOP-CMA-ES can be considered as a multi-restart version of CMA-ES in Hansen and Kern (2004). Several stop criteria have been designed to restart CMA-ES. In each restart, the population size is increased by a factor of two over the previous population size.

We summarise the experimental results in Figure 7, where the bar charts show the average values of 25 runs. In the plots, the average NFEs $\left(\mathrm{AVG}_{N}\right)$ are shown if the functions can be solved in all 25 trials, while the average best error values $\left(\mathrm{AVG}_{E}\right)$ are shown if the functions cannot be solved in all 25 trials. The $p$ values shown are the rank sum test over the corresponding experimental results. Detailed experimental results can be found in the online appendix. ${ }^{1}$

In the comparison between IMMA and DEahcSPX in terms of NFEs, we see that IMMA uses significantly fewer NFEs than DEahcSPX on $f_{1}$ through $f_{3}$ and $f_{6}$. Also, it can be seen that IMMA performs better than DEahcSPX on $f_{7}$ through $f_{10}$ but worse on $f_{4}$ and $f_{5}$ in terms of the best error values. From Table A1 in the appendix, we can see that $f_{4}$ is noisy and $f_{5}$ is discontinuous. Thus, they may break the POP assumptions of the developed algorithm. Also, these properties may make NEWUOA employed in IMMA less effective. In summary, we may conclude that IMMA works better than DEahcSPX for test problems that are continuous and without noise.

In the comparison between IMMA and IPOP-CMA-ES on these functions that can be successfully solved in terms of NFEs, we observe that IMMA performs worse than IPOP-CMA-ES only on $f_{1}(n=30,50)$ and $f_{3}(n=50)$. In the comparison between IMMA and IPOP-CMA-ES on the remaining functions (in total, 21 functions) in terms of the best error values, in the case where $n=10$, we see that IMMA performs better than IPOP-CMA-ES in 10 functions, worse in eight, and comparable in three. In the case where $n=30$, IMMA is better than IPOP-CMA-ES in 11 functions, worse in seven, and

[^0]
[^0]:    ${ }^{1}$ http://www.cpib.ac.uk/downloads/onlinesupplementary.pdf

![img-13.jpeg](img-13.jpeg)

Figure 7: Comparative results of IMMA on the CEC 2005 test problems with DEahcSPX and IPOP-CMA-ES. The $x$ axis shows the dimension, and the $y$ axis is either the average function error value $\left(\mathrm{AVG}_{E}\right)$ or the average number of fitness evaluations $\left(\mathrm{AVG}_{N}\right)$. The $p$ values shown in the plots are the $p$ values obtained through the rank-sum test between IMMA and IPOP-CMA-ES.
no different in three, while in the case where $n=50$, IMMA achieves better results in 11 functions, worse in six, and no different in four.

Note that the worst performance of IMMA occurs when solving the functions $f_{4,5,11,14,18,22,25}$. From Table A1 in the appendix, we see that most of these functions are with high-epistasis, very high-multimodal, and medium discontinuity and noise. This

Table 9: The comparison between IMMA and APrMF on the functions that can be solved successfully in terms of NFEs.

confirms our observation that IMMA cannot perform well on functions with noise and discontinuity. Moreover, it can be seen that in the case where $n=10$, IMMA does not perform as well as IPOP-CMA-ES on $f_{18.20 .22 .24}$, which are hybrid composition functions, while along the increase of the function dimensions, we see that the performance of IMMA becomes better. These observations indicate that IMMA may perform better for high-dimensional functions.

Tables 9 and 10 show the results in comparison with APrMF (Nguyen et al., 2009). Table 9 lists the results for those functions that can be solved successfully. The results show that IMMA needs fewer NFEs than APrMF on $f_{2,6,7}$ which have high epistasis, while APrMF is good on $f_{1,3,9}$ which have no epistasis. On the other hand, for these functions that are not easy to be solved as seen in Table 10, IMMA performs significantly better than APrMF on almost all the functions except for $f_{14,16,19}$ according to the Z-test between the algorithms.

In summary, we can conclude that on average IMMA can perform significantly better than DEahcSPX and APrMF on almost all functions. This justifies the following two conclusions: (1) the developed novel hybridisation strategy works better than the coupled hybridisation strategy as used in APrMF; (2) the incorporation of classical LS improves the algorithmic efficiency. On the other hand, we see that IPOP-CMA-ES performs better than IMMA on those functions with noise and discontinuous properties when $n=10$. However, IMMA performance improves along with the dimension increase of these functions. On average, we can conclude that IMMA is comparable with IPOP-CMA-ES on the CEC2005 test functions.

# 4.5 Scalability 

In this section, we carry out experiments to investigate the effect of dimensionality on the performance of IMMA. We use the same test functions as in Noman and Iba (2008), including $f_{26}$ through $f_{34}$ and $f_{37}$ to carry out the analysis. We carry out the study on these functions with dimensions at $n=10,50,100$, and 200. The criteria described in Section 4.1 are applied. The algorithmic parameters are set as $M=2 n$, and $L=3$.

Table 11 lists the results, including the best error values and the number of fitness evaluations, obtained by IMMA and DEahcSPX which are copied from Noman and Iba (2008). The global optimal values of these functions with different dimensions are all zero. From the table, it is clear that IMMA performs significantly better than DEahcSPX on all functions except for $f_{26}(n=10,50,200)$ in terms of the best error values and NFEs except for $f_{29}(n=10)$. Moreover, we can see that IMMA reaches the attraction basin of

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

![img-17.jpeg](img-17.jpeg)

Figure 8: The number of fitness evaluations versus the number of dimensions on $f_{29,31,33,35}$.
the global optimum linearly with respect to the dimensionality, in cases for which the accuracy level is achieved.

Figure 8 shows the average number of fitness evaluations against the dimensionality on $f_{29,31,33,35}$. The dimensionality is on the $x$ axis, and the $y$ axis shows the average number of fitness evaluations used to reach the predefined precision in 25 runs. Error bars indicate the standard deviation of the number of fitness evaluations. The solid line is the straight line fit between the average number of fitness evaluations and the dimensionality. From Figure 8, the number of fitness evaluations exhibits an approximately linear relationship w.r.t. the number of dimensions. We can also see that the standard deviations increase along with the dimensionality.

# 4.6 Additional Materials 

Following the release of the benchmark problems in the Genetic and Evolutionary Computation Conference (GECCO) workshop for real-parameter optimisation in 2009 (Hansen et al., 2009), we applied the developed algorithm to these problems. The experimental results including the details of the execution procedure and the comparison with the winner of the competition, called BIPOP (Hansen et al., 2010) are available elsewhere. ${ }^{2}$

To give a brief impression of the results, we include Figure 9, which summarises the comparison of IMMA and BIPOP on the 24 benchmark problems with various dimensions, using the format specified in the GECCO 2009 competition. In Figure 9, ERT stands for the expected run time to surpass $f_{\text {opt }}+\Delta f$, where $\Delta f$ is a given target

[^0]
[^0]:    ${ }^{2}$ http://www.cpib.ac.uk/downloads/onlinesupplementary.pdf

![img-18.jpeg](img-18.jpeg)

Figure 9: Ratio of ERT for IMMA over BIPOP versus $\log _{10}(\Delta f)$ in 2:+, 3: $\bigcirc, 5: \bullet, 10: \circ$ and 20: $\square$ dimensions. Ratios $<10^{\circ}$ indicate an advantage of IMMA, as smaller values are always better. For a complete description of the figures, see text.
difference to the optimal function value $f_{\text {opt }}$. The figure shows the log ratio of ERT for IMMA over ERT for BIPOP versus $\log _{10}(\Delta f)$ in 2, 3, 5, 10, and 20 dimensions. In Figure 9, log-ratios $<0$ indicate an advantage of IMMA, as smaller values are always better. The line becomes dashed when the ERT of the compared algorithms exceeds three times the median of the trial-wise overall number of $f$ evaluations. The best achieved $\Delta f$ value for each algorithm is indicated by a filled symbol. The dashed line continues as the fraction of successful trials of the other algorithms, where 0 means $0 \%$, and the $y$ axis limits mean $100 \%$, values below zero for IMMA. The line ends when no further algorithm reaches $\Delta f$. The number of successful trials is given only if it was in $\{1 \ldots 9\}$ for IMMA (1st number) and nonzero for BIPOP (2nd number). The results are significant with $p=.05$ for one star and $p=10^{-8 \bullet}$ otherwise, with Bonferroni

correction within each figure. From the figure, we see that for two test problems, $f_{21,22}$, there are no significant differences for all the dimensions. For the 2D functions, it can be seen that BIPOP performs significantly better than IMMA in three cases ( $f_{3,4,12}$ ), IMMA significantly better in sixteen ( $f_{1,2}, f_{5}$ through $f_{7}, f_{10,11}, f_{13}$ throuh $f_{19}$, and $f_{23,24}$ ), with no significant difference in the remaining five ( $f_{8,9}$, and $f_{20}$ through $f_{22}$ ). Similar patterns of results can be seen for the other dimensionalities of functions, with IMMA outperforming BIPOP more frequently than the reverse. From this observation, we state that overall, IMMA performs better than BIPOP on the GECCO 2009 competition functions in terms of ERT.

# 5 Discussion 

One of the main contributions in the developed memetic algorithm framework is to isolate the EA and the local search. Under this framework, traditional principles for efficient EA design will be profoundly changed. That is, we no longer need to focus on balancing exploration and exploitation, but instead focus on improving the capabilities of effective exploration and intelligent restart. The aim of effective exploration is to find a very promising solution using the least computational cost, while the aim of intelligent restart is to develop good strategies to take advantage of the search history to improve search efficiency. Moreover, the multiple-cycle structure provides a possibility to escape from local optima, once trapped. From the component studies, we found that an IMMA with high selection pressure does not necessarily worsen the performance of the resultant algorithm. This observation implies that the traditional EA design criteria, such as the selection pressure and the transformation from exploration to exploitation (Yao and Liu, 1999), are not appropriate to guide the EA design under the proposed framework. In this case, future research should concentrate on developing EAs with strong exploration capability and on proposing intelligent restart criteria.

Apart from the guided mutation operator which can incorporate previous history information, it is desirable to develop more intelligent strategies which can take advantage of the previous search history and reduce the randomness of the evolutionary search in order to improve robustness.

Another important issue in the framework is the choice of proper local optimisers. There are a diverse and large set of local optimisers for unconstrained and constrained continuous optimisation problems. Some local optimisers are developed particularly for some kind of problems, for example, N2FB (Dennis et al., 1981), which is particularly developed for least square problems. When applying the developed algorithm to a practical problem, specialised local optimisers would be more useful than NEWUOA in some situations. Moreover, in the case that local optimisers have their own control parameters, we may need to develop some strategies to search for the optimal control parameters during the optimisation process, and also develop multi-meme strategies (Krasnogor et al., 2006) such as those successfully deployed for combinatorial optimisation problems.

## 6 Conclusion

In this paper, we have studied the application of a memetic algorithm to continuous optimisation problems, and proposed an intelligent multi-restart memetic framework. We developed an EDA-like algorithm based on the proposed framework. In the implementation, an adaptive multivariate model is constructed and used to sample offspring. To replace a solution, we sample more than one solution from the probability model,

and pick the best of these to replace the current one. A derivative-free optimisation algorithm, NEWUOA, is applied to improve the current best solution when the current search cannot find a better solution in some consecutive generations. When the stop criterion has not been met, we restart the search. Hence, the new search will be carried out intelligently by incorporating the history information of previous searches. Experiments on some commonly used benchmark global optimisation problems showed that the proposed algorithm is very competitive with the best known EAs, including the winner of the CEC 2005 competition, and significantly better than other EAs.

In summary, we believe that the developed algorithm, based on our new framework, achieves highly competitive results (in terms of the solution quality) across a wide range of functions of various dimensions. Often it does this by using fewer fitness evaluations than other competitive algorithms. We also believe that the framework is relatively simple and flexible. Hence, we believe that this framework is a significant contribution, worthy of future study.

Moreover, we intend to explore four interesting avenues of research. The first avenue will be to examine the use of the niching technique (De Jong, 1975) to help the search escape from local optima and hence make the diversification more intelligent. The second avenue will be to apply the developed framework to a range of problems in combinatorial optimisation. The third avenue will be to modify the framework to accommodate the search for multiple optimum solutions in multi-modal optimisation problems. The fourth avenue will be to investigate a completely adaptive intelligent multi-restart algorithm, based on the proposed framework, to save manpower in practice.

# Acknowledgment 

This work was supported by BBSRC and EPSRC through grants BB/D019613/1 (The Centre for Plant Integrative Biology), EP/H010432/1 and EP/J004111/1.

# Appendix A 

Table A1 lists the benchmark functions used in our study. Functions $f_{1}$ through $f_{25}$ are the same functions as $F_{1}$ through $F_{25}$ defined in Suganthan et al. (2005), respectively.

Table A1: The basic characteristics of the test functions used in Noman and Iba (2008) and Suganthan et al. (2005). $f$ is the global optimum. In the table, properties such as epistasis (Epi), multi-modal (Mul), and discontinuous (Disc), are also shown.

