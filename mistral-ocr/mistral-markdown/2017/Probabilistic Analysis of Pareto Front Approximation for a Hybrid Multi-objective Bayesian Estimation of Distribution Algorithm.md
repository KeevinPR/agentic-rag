# Probabilistic Analysis of Pareto Front Approximation for a Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm 

Marcella S. R. Martins,<br>Myriam Delgado and Ricardo Lüders<br>Federal University of Technology - Paraná<br>Email: \{marcella,myriamdelg,luders\}@utfpr.edu.br<br>Roberto Santana<br>University of the Basque Country<br>Email: roberto.santana@ehu.es<br>Richard A. Gonçalves<br>and Carolina P. de Almeida<br>Midwest State University of Paraná<br>Email: \{richard,carol\}@unicentro.br


#### Abstract

Metaheuristics that explore the decision variables space to construct probabilistic modeling from promising solutions, like estimation of distribution algorithms (EDAs), are becoming very popular in the context of Multi-objective Evolutionary Algorithms (MOEAs). The probabilistic model used in EDAs captures certain statistics of problem variables and their interdependencies. Moreover, the incorporation of local search methods tends to achieve synergy of MOEAs' operators and local heuristics aiming to improve the performance. In this work, we aim to scrutinize the probabilistic graphic model (PGM) presented in Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA), which is based on a Bayesian network. Different from traditional EDA-based approaches, the PGM of HMOBEDA provides the joint probability of decision variables, objectives, and configuration parameters of an embedded local search. HMOBEDA has shown to be very competitive on instances of Multi-Objective Knapsack Problem (MOKP), outperforming state-of-the-art approaches. Two variants of HMOBEDA are proposed in this paper using different sample methods. We aim to compare the learnt structure in terms of the probabilistic Pareto Front approximation produced at the end of evolution. Results on instances of MOKP with 2 to 8 objectives show that both proposed variants outperform the original approach, providing not only the best values for hypervolume and inverted generational distance indicators, but also a higher diversity in the solution set.


Keywords-Multi-objective optimization; estimation of distribution algorithms; automatic algorithm configuration;

## I. INTRODUCTION

A large number of metaheuristics have been developed for efficiently solving multi-objective optimization problems (MOPs). These problems contain two or more, usually conflicting, objectives. This means, optimizing one objective does not necessarily optimize the others. Because of the objectives trade-off, a set called Pareto-optimal is formed by compromise solutions. Different approaches have been proposed to approximate the Pareto-optimal front (its corresponding objectives) in various scenarios [1].

Multi-objective evolutionary algorithms (MOEAs) are classical examples of these approaches. They have achieved good results in MOPs as they search multiple solutions in parallel with some advantages when compared with math programming-based approaches. Estimation of distribution algorithms (EDAs) are a class of EAs that explore the search
space by building a probabilistic model from a set with the current best candidate solutions [2]. Since new solutions are sampled from the probabilistic model, the evolution is guided toward more promising areas of the search space.

Probabilistic Graphical Models (PGM) [3] combining graph and the probability theory have been adopted to improve EDAs performance [2]. EDAs developed to solve multi-objective problems [4] are usually called Multi-objective Estimation of Distribution Algorithm (MOEDA) and most of those developed to deal with combinatorial MOPs adopt Bayesian Networks as their PGM. However, recently the role of the probabilistic model has been extended to model the dependencies between variables and objectives [4]. In addition, MOEDAs can be notably enhanced by adding a local optimizer that can refine the solutions found by sampling from the PGM [5], [6].

Therefore, in this paper we investigate the approach presented in [7], called Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA), which is based on a joint probabilistic modeling of decision variables, objectives, and parameters of the local optimizers. Some recent MOEDA-based approaches model a joint distribution of variables and objectives in order to explore their relationship, which means investigating how objectives influence variables and vice versa. However, HMOBEDA also includes a Local Search (LS) parameter tuning in the same model, which, according to the authors, turns possible to the PGM sampling appropriate LS parameters for different configurations of decision variables and objective values. Since providing relationships among solution variables is one of the advantages of using EDA, differently from [7], this work aims to scrutinize information present in the final PGM. The main objective here is to explore, from a probabilistic point of view, the approximated Pareto-front using the final PGM structure. Two variants of HMOBEDA that use different sampling techniques are then proposed in this paper based on the weaknesses detected in this probabilistic analysis.

In [7], the embedded PGM is evaluated on the Multiobjective Knapsack Problem (MOKP) - the multi-objective version of the well known knapsack problem, which has been recently explored in other works in the literature [8], [9]. In

particular, MOEDAs that use different types of probabilistic models have already been applied to MOKP [5], [6], especially those based on Bayesian Networks (BN) [10]. However, these works do not consider the objectives and parameters structured all together in the same BN, as was proposed in HMOBEDA . Therefore, HMOBEDA was chosen to be investigated in this work using the same instances of MOKP addressed in [7].

## II. BACKGROUND

One of the most general probabilistic models for discrete variables used in EDAs and MOEDAs is the Bayesian Network [3], and we briefly describe it in the next section.

A Bayesian Network (BN) is a probabilistic model which topology structure is a directed acyclic graph (DAG) whose nodes represent variables and edges express the probabilistic dependency relationship between them [11]. Let us assume $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{M}\right)$ as a vector of random variables, where $y_{m}$ is a value of the $m$-th component $\left(Y_{m}\right)$ of the vector $\mathbf{Y}$. The set of conditional dependencies of all variables in $\mathbf{Y}$ is described by the DAG structure $B . \mathbf{P a}_{m}^{B}$ represents the set of parents of the variable $Y_{m}$ given by $B$, and the set of local parameters $\Theta$ contains, for each variable, the conditional probability distribution of its values given different value settings for its parents, according to structure $B$.

Therefore, a Bayesian network encodes a factorization for the probability mass function (pmf) as follows:

$$
p(\mathbf{y})=p\left(y_{1}, y_{2}, \ldots, y_{M}\right)=\prod_{m=1}^{M} p\left(y_{m} \mid \mathbf{p a}_{m}^{B}\right)
$$

In discrete domains, we can assume that $Y_{m}$ has $s_{m}$ possible values, $y_{m}^{i}, \ldots, y_{m}^{s_{m}}$, therefore the particular conditional probability, $p\left(y_{m}^{i} \mid \mathbf{p a}_{m}^{i, B}\right)$ can be defined as:

$$
p\left(y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}\right)=\theta_{y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}}=\theta_{m j k}
$$

where $\mathbf{p a}_{m}^{j, B} \in\left\{\mathbf{p a}_{m}^{1, B}, \ldots, \mathbf{p a}_{m}^{t_{m}, B}\right\}$ denotes a particular combination of values for $\mathbf{P a}_{m}^{B}$ and $t_{m}$ is the total number of different possible instantiations of the parent variables of $Y_{m}$ given by $t_{m}=\prod_{Y_{v} \in \mathbf{P a}_{m}^{B}} s_{v}$, where $s_{v}$ is the total of possible values (states) that $Y_{v}$ can assume. The parameter $\theta_{m j k}$ represents the conditional probability that variable $Y_{m}$ takes its $k$-th value $\left(y_{m}^{k}\right)$, knowing that its parent variables have taken their $j$-th combination of values $\left(\mathbf{p a}_{m}^{j, B}\right)$. This way, the parameter set is given by $\Theta=\left\{\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{m}, \ldots \boldsymbol{\theta}_{M}\right\}$, where $\boldsymbol{\theta}_{m}=\left(\theta_{m 11}, \ldots, \theta_{m j k}, \ldots, \theta_{m, t_{m}, s_{m}}\right)$.

BN's are often used for modeling multinomial data with discrete variables [11] generating new solutions using the particular conditional probability described in Equation (2) (direct sampling method).

Generally, the parameters in the whole set $\Theta$ are unknown, and their estimation process is based on the current data Pop with $N$ observations (instantiations) of $\mathbf{Y}$.

There are two approaches to estimate each $\theta_{m j k}$ parameter: Maximum Likelihood Estimate (MLE) and Bayesian Estimate.

With MLE, we expect to find a vector in $\Theta$ that maximizes the likelihood. We can denote this vector as $\hat{\boldsymbol{\theta}}$. In MLE, each
$\hat{\boldsymbol{\theta}} \in \Theta$ is a point estimation, not a random variable. Therefore, MLE does not consider any priori information, and the estimation is is calculated according to $\hat{\theta}_{m j k}=N_{m j k} / N_{m j}$, where $\hat{\theta}_{m j k}$ is the MLE estimated parameter for $\theta_{m j k}, N_{m j k}$ is the number of observations in Pop for which $Y_{m}$ assumes the $k$-th value given the $j$-th combination of values from its parents and $\mathbf{N}_{m j}=\left\{N_{m j 1}, \ldots, N_{m j s_{m}}\right\}$.

Regarding to Bayesian estimation, it calculates the posteriori distribution $p(\Theta \mid$ Pop, $B)$ considering a priori information $p(\Theta \mid B)$. In practice, it is useful to require that the prior for each factor is a conjugate prior. For example, Dirichlet priors are conjugate priors for multinomial factors.

The expected value $E\left(\theta_{m j k} \mid \mathbf{N}_{m j}, B\right)$ of $\theta_{m j k}$ is an estimate of $\theta_{m j k}$, shown in Equation (3), considering the Dirichlet distribution with hyperparameters $\alpha_{m j k}$ values as 1 :

$$
\hat{\theta}_{m j k}=\left(1+N_{m j k}\right) /\left(s_{m}+N_{m j}\right)
$$

There are three main approaches to learn BN structures: score-based learning, constraint-based learning, and hybrid methods. Score-based learning methods evaluate the quality of BN structures using a scoring function, like Bayesian Dirichlet (BD)-metric [12], and selects the best one.

Most of the developed structure learning algorithms fall into the score-based approaches. Combining the statistical data from a given data set with prior knowledge about the problem, Equation (4) defines the BD-metric considered in [12].

$$
p(B \mid P o p)=p(B) \prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\Gamma\left(\alpha_{m j}\right)}{\Gamma\left(\alpha_{m j}+N_{m j}\right)} \prod_{k=1}^{s_{m}} \frac{\Gamma\left(\alpha_{m j k}+N_{m j k}\right)}{\Gamma\left(\alpha_{m j k}\right)}
$$

where $p(B)$ is the prior factor of quality information of the network $B$ and the parameter $\alpha_{m j k}$ stands for prior information about the number of instances that have $Y_{m}$ set to its $k$-th value and the set of parents of $Y_{m}$ is instantiated to its $j$-th combination. The product on $j \in\left\{1, \ldots, t_{m}\right\}$ runs over all combinations of the parents of $Y_{m}$ and the product on $k \in\left\{1, \ldots, s_{m}\right\}$ runs over all possible values of $Y_{m}$.

If there is no prior information for $B, p(B)$ is considered a uniform probability distribution and generally its value is set to 1 , such as parameters $\alpha_{m j k}$, providing the so-called K2 metric [13] as shown in Equation (5).

$$
p(B \mid P o p)=p(B) \prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\left(s_{m}-1\right)!}{\left(N_{m j}+s_{m}-1\right)!} \prod_{k=1}^{s_{m}}\left(N_{m j k}\right)!
$$

Using the logarithm of the scoring metric prevents factorials in Equation (5) to grow up in an uncontrolled way. The logarithmic version of Equation (5) is the one considered in this paper.

To find the network structure that maximizes the scoring metric, we use the K2 algorithm. It is a greedy local search technique that applies the K2 metric. Initially it assumes that a node, in a (pre-defined) ordered list, does not have any parent, then at each step it gradually adds the edges that increase the scoring metric the most, until no edge increases the metric anymore.

## III. HMOBEDA VERSIONS

HMOBEDA is a hybrid EDA approach introduced in [7]. The term hybrid concerns a local search (LS) mechanism included into the EDA framework to improve its performance. This way, LS can be combined with sorting and selection techniques usually adopted in MOEAs and also be configured with suitable parameters during the search. The general scheme of the HMOBEDA is presented in Figure 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1: The HMOBEDA Framework
As can be noticed, HMOBEDA uses a probabilistic model (based on BN) of objectives, variables and local search parameters to sample new individuals. Every solution is thus represented by a joint vector with $Q+R+L$ elements, $\mathbf{y}=(\mathbf{x}, \mathbf{z}, \mathbf{p})=\left(X_{1}, \ldots, X_{Q}, Z_{1}, \ldots, Z_{R}, P_{1}, \ldots, P_{L}\right)$, denoting the decision variables $\left(X_{1}, \ldots, X_{Q}\right)$, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ and LS parameters $\left(P_{1}, \ldots, P_{L}\right)$.

The main characteristic of the original HMOBEDA introduced in [7] is that it uses an estimation of the ideal point $Z^{*}$ to guide the search. This is achieved by fixing discretized values of $Z^{*}$ achieved so far, as evidences in the root nodes of the BN structure (i.e., in nodes $Z_{1}, \ldots, Z_{R}$ of Figure 1) during probabilistic logic sampling. In this paper, we are proposing two variants of HMOBEDA named $\mathrm{HMOBEDA}_{E X T}$ and $\mathrm{HMOBEDA}_{C P T}$ which represent different possibilities to guide the search. Roughly speaking, $\mathrm{HMOBEDA}_{C P T}$ uses the priori probabilities of $Z_{1}, \ldots, Z_{R}$ described in the Conditional Probability Table (CPT) to draw and further fix their evidences; and $\mathrm{HMOBEDA}_{E X T}$, besides also considering $Z^{*}$ like the original version, it includes the extremes points of the approximated Pareto-front as candidates for the evidences in the root nodes.

In what follows, we describe the main steps performed by the three versions of the HMOBEDA considered in this paper. At the first iteration, solutions are randomly generated in the Initialization process and the corresponding objectives are calculated based on the objective functions of the addressed problem. A Local Search based on Hill Climbing procedure [14]) generates a neighbor for each solution, calculates its fitness and updates the solution in case the neighbor has a better fitness.

In order to select a total of $N_{P G M}$ individuals from the current population, the Non-dominated Sorting [15] technique is applied. The Selection procedure randomly selects two solutions and the one positioned in the best front is chosen. If they lie in the same front, it chooses that solution with the greatest Crowding Distance [16].

Aiming to encode the joint probabilistic distribution of decision variables, objectives and LS parameters, the $P G M$ Learning procedure estimates the BN structure and parameters based on the pre-selected population. In other words, they are estimated based on the K2 algorithm running over a set of $N_{P G M}$ best individuals each one composed of $Q$ decision variables, $R$ objectives and $L$ local search parameters, (i.e. $\mathbf{Y}=\left(Y_{1}, \ldots Y_{M}\right)=\left(Z_{1}, \ldots Z_{R}, X_{1}, \ldots X_{Q}, P_{1}, \ldots P_{L}\right)$ ). This way the BN structure encodes a factorization of the joint probability distributions or the probability mass function (pmf) given by:

$$
p(\mathbf{y})=\prod_{r=1}^{R} p\left(z_{r} \mid \mathbf{p a}_{r}^{B}\right) \cdot \prod_{q=1}^{Q} p\left(x_{q} \mid \mathbf{p a}_{q}^{B}\right) \cdot \prod_{l=1}^{L} p\left(p_{l} \mid \mathbf{p a}_{l}^{B}\right)
$$

where $\mathbf{p a}_{r}^{B}, \mathbf{p a}_{q}^{B}$ and $\mathbf{p a}_{l}^{B}$ represent combinations of values for the parents of objective, decision variable and LS parameter nodes respectively, with $\mathbf{P a}_{r}^{B}=\emptyset, \mathbf{P a}_{q}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}$ and $\mathbf{P a}_{l}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}$.

New $N_{\text {smp }}$ individuals are generated from this joint probability distribution using probabilistic logic sampling, in the Sampling block. As previously discussed, the main difference between the two proposed approaches and the original version of HMOBEDA described in [7] concerns the Sampling block. HMOBEDA considers evidences fixed as maximum values for all objectives (i.e. the ideal point $Z^{*}$ ). $\mathrm{HMOBEDA}_{C P T}$ considers evidences fixed according to the parameters and probabilities estimated to compose the CPT. And finally, $\mathrm{HMOBEDA}_{E X T}$ considers evidences fixed as combinations (all of them with the same probability of occurrence) of maximum and minimum values for the objectives, i.e., the ideal point $Z^{*}$ plus the estimated extreme points of the current approximation of the Pareto Front. These values are uniformly distributed according the number of objectives in each generation (excluding the combination with minimum values for all objectives).

The main advantage of using the HMOBEDA framework, is that not only decision variables, but also LS parameters can be obtained through the Sampling block. Therefore, after sampling decision variables $\left(X_{1}, \ldots, X_{Q}\right)$, the LS parameters $\left(P_{1}, \ldots, P_{L}\right)$ more related to the objectives fixed as evidences can be drawn for each new individual. Finally, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ are calculated based on the fitness function (in the case of surrogate assisted approaches, PGM can also be used to sample the objective values) or least squares method can provide objective value approximations.

After the union of the sampled population and the current population, a truncation selection using the Non-dominated Sorting [15] is applied to select the best solutions, creating the new population for the next generation. The main loop continues until the stop condition is achieved.

## IV. EXPERIMENTS AND RESULTS

We compare the original version of HMOBEDA with the two proposed variants through the hypervolume and inverted generational distance (IGD) indicators, which are usually adopted for measuring the quality of the optimal solution

set for multi-objective optimization [17]. The Hypervolume (HV-) considered here measures the difference between the hypervolume achieved by the solution set of an algorithm and that of the reference set [18]. The IGD measures the average distance from each solution in the reference set to the nearest solution in the solution set [19]. Therefore, smaller values of $\mathrm{HV}^{-}$and IGD correspond to higher quality solutions in nondominated sets indicating both better convergence and good coverage of the reference set. We use PISA framework [20] to compute $\mathrm{HV}^{-}$and Matlab to compute IGD.

All the comparisons are made considering the multiobjective knapsack problem that can be formulated as follows:

$$
\begin{aligned}
& \max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right) \\
& \text { subject to } \sum_{q=1}^{Q} b_{r q} x_{q} \leq c_{r}, r=1, \ldots, R \\
& \text { with } z_{r}(\mathbf{x})=\sum_{q=1}^{Q} a_{r q} x_{q}, \mathbf{x} \in\{0,1\}^{Q}
\end{aligned}
$$

where, $a_{r q}$ is the profit of item $q$, according to knapsack $r$, $b_{r q}$ denotes the weight of item $q$ according to knapsack $r$, and $c_{r}$ is the constraint capacity of knapsack $r$, given a total of $R$ objective functions (knapsacks) and $Q$ items. The decision variables are represented by $\mathbf{x}$, a $Q$-dimension binary vector, such that if $q$ is selected to be in $r$-th knapsack then $x_{q}=1$.

In the conducted experiments, $a_{q}^{r}$ and $b_{q}^{r}$ are specified as integers in the interval $[10,100]$. The capacity $c_{r}$ is defined as $50 \%$ of the sum of all weights related to each knapsack $r$ as in [18]. The set of instances (characterized as $R-Q$ ) is the union of those considered in [8], [9], [18]. We use thus instances for 100 and 250 items, with 2 to 5 and 8 objectives.

If an infeasible solution is generated, we apply the same greedy repair method used in [18], [7]. This method repairs a solution by removing items in an ascending order of the relation profit/weight until the constraints are satisfied.

As in [7], we estimate the parameters through Bayesian Estimate, using the Dirichlet prior, and we adopt K2 metric as score-based technique, although any other method could be used as well. The K2 algorithm is used here by setting parent nodes as objectives in the network.

Aiming to facilitate the sampling process, in the experiments, learned structures do not consider any relation between variables, between parameters and between variables and parameters. Therefore, fixing objective values as target evidences enables the estimation of their associated decision variables and LS parameters.

In this section, we compare the original HMOBEDA with two modified versions: HMOBEDA ${ }_{C P T}$ and $\mathrm{HMOBEDA}_{E X T}$. As discussed in Section III, the differences among them are mainly in the sampling step. Based on the assumptions of each variant, we aim to investigated how the evidences may influence the distribution of non-dominated solutions along the approximated Pareto front. In addition to $\mathrm{HV}^{-}$and IGD indicators, this paper aims to evaluate the quality of the final approximation of the Pareto front through the analysis of the final achieved PGM. This way, we want to explore one of the main advantages of using EDA:
the possibility of scrutinizing its probabilistic model which encompasses relationship among variables.

The parameters for all the HMOBEDA versions considered in this section are: population size $(N=100)$, number of selected individuals for PGM building $N_{P G M}=N / 2$, Number of sampled individuals $N_{\text {snap }}=10 N$. The stop condition is based on the maximum number of fitness evaluations ( $M a x_{\text {veal }}=100,000$ ), which includes repair procedures and LS-iterations.

The optimal Pareto front for each instance of the addressed problem is not known. Therefore, we use a reference set which is constructed by gathering all non-dominated solutions from all the approaches addressed in [7] plus the ones obtained by the three HMOBEDA versions over all executions.

## A. Results and discussions

In order to analyze the final Approximated Pareto Front achieved by each HMOBEDA version taking into account the information available in the final PGM, we calculate the pmf $P(\mathbf{y})$, defined by Equation (6), for each solution from the final set (dominated and non-dominated solutions) achieved at the end of each execution. After that, the mean of pmf values along all executions is obtained for further calculating the marginal distribution $P\left(Z_{1}=z_{1}, \ldots, Z_{R}=z_{R}\right)$. The probabilistic view of the Pareto set is defined by gathering all non-dominated solutions obtained over all 20 executions. Each non-dominated solution is represented by a circle, which is proportional to the corresponding marginal probability $P\left(Z_{1}=z_{1}, \ldots, Z_{R}=z_{R}\right)$.

Figure 2 presents the analysis of the approximated Pareto front for 2-100 instance considering the probabilistic information available through the PGM. We can observe that for HMOBEDA the solutions with high probabilities are concentrated on a special region of Pareto front (around the ideal point). However, in $\mathrm{HMOBEDA}_{E X T}$ some solutions are well distributed along the entire front, with extreme points presenting higher probabilities values than HMOBEDA and $\mathrm{HMOBEDA}_{C P T}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2: A probabilistic view of the approximated Pareto front for 2 objectives.

Figure 3a illustrates the Euclidean distance between each solution and the ideal point, calculated for 2-100 instance, gathering all non-dominated solutions obtained over all 20 executions. We note that HMOBEDA presents the smoother distance fluctuation. This observation, associated with the analysis of Figure 2 and IGD values in Table I, shows that HMOBEDA provides an approximation of the Pareto Front with a slightly higher concentration around the ideal point.

Besides, Figure 3a shows that $\mathrm{HMOBEDA}_{E X T}$ provides more non-dominated solutions (points) along the curve. Finally, we can conclude that solutions present different probabilities values along the Pareto front, concentrated around the ideal point, as also notable in Figure 2.
![img-2.jpeg](img-2.jpeg)

Fig. 3: The Euclidean distance between each solution and the ideal point for (a) 2 objectives and (b) 8 objectives.

Another example can be seen in Figure 3b for 8-100 instance, gathering all non-dominated solutions obtained over all 20 executions. In this case, since it is not possible to visualize the Pareto Front, the Euclidean distance between each solution and the ideal point is calculated.

We note, in Figure 3b, that the solutions present similar probabilities values since there is no larger points plotted in the Pareto front. This happens because, differently from the biobjective case, as the number of objectives increases, solutions with exactly the same discretized objective values are much less frequent, which results in small differences between the pmf and the marginal distribution $P\left(Z_{1}=z_{1}, \ldots, Z_{R}=z_{R}\right)$.

Now, similarly to the bi-objective case, $\mathrm{HMOBEDA}_{E X T}$ and $\mathrm{HMOBEDA}_{C P T}$ produce solutions with a higher diversity and smaller mean distances from ideal point. Some solutions might be closer to the ideal point (e.g. the knee of the approximated Pareto front) but other can be far away (the extremes of the curve). HMOBEDA, on the other hand, produces solutions at a narrower distance deviation of the ideal point.

With these experiments, we can conclude that, examining BN structures according to the marginal distribution of the corresponding objectives values taken over all the algorithm executions, enables the analysis of the influence of fixing evidences in the HMOBEDA approach. According to the results we could note that fixing evidences along the evolutionary process can guide the search through specific regions of the Pareto front, providing higher/lower convergence and diversity. HMOBEDA has fixed the highest values for objectives as evidences in the network, its solutions are not well distributed around the ideal point. On the other hand, when the evidences are uniformly distributed between ideal and extreme points (i.e. equally probable combinations with high and low objectives values), the solutions are more distributed along the front, as depicted in Figure 2 through the red points.

Table I shows the hypervolume difference $\left(\mathrm{HV}^{-}\right)$and IGD metric, both averaged over 20 executions of each HMOBEDAversion including the traditional approaches addressed in [7]: MBN-EDA [4], NSGA-II [16], S-MOGLS (NSGA-II
with local search) [21], MOEA/D [22], and NSGA-III [23]. The lowest values are highlighted in bold and results with no statistically significant differences in comparison with the best values are emphasized in light blue, using Kruskal-Wallis and Dunn-Sidaks post-hoc tests with a significance level of $\alpha=5 \%$.

Although Table I shows that there is no statistically significant differences between HMOBEDA, $\mathrm{HMOBEDA}_{C P T}$, $\mathrm{HMOBEDA}_{E X T}$, NSGA-III and MOEA/D regarding $\mathrm{HV}^{-}$ indicator for the 2-100, 3-100 and 3-250 instances, there are statistically significant differences regarding the IGD metric for the 5-100, 5-250, 8-100 and 8-250 instances. Besides, $\mathrm{HMOBEDA}_{E X T}$ and $\mathrm{HMOBEDA}_{C P T}$ present better results than HMOBEDA for 5-100, 5-250, 8-100 and 8-250 instances, with some advantage for $\mathrm{HMOBEDA}_{E X T}$, which also presents the lowest values in comparison with all other traditional approaches.

The run times range from approximately 3 minutes (instance 2-100) to 66 minutes (instance 8-250) for the three HMOBEDA versions.

## V. CONCLUSION

In this paper we have compared three different versions of a hybrid EDA named Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA) in the context multi-objective combinatorial optimization. The main issues investigated in this paper concern the analysis of the final PGM structure, how it can represent the interdependencies between variables, objectives and parameters, and how fixing evidences during the evolution can influence both convergence and diversity along the approximated Pareto front.

We have evaluated the quality of the final Pareto front approximations of HMOBEDA, $\mathrm{HMOBEDA}_{C P T}$ and $\mathrm{HMOBEDA}_{E X T}$ through the analysis of the final achieved PGM for instances of the multi-objective knapsack problem. We aimed to explore one of the main advantages of using EDA: the possibility of scrutinizing its probabilistic model which encompasses relationship among variables.

In addition to the analysis of the final achieved PGM, this paper evaluated the performance of HMOBEDA versions in comparison with traditional approaches considering two metrics: Hypervolume $\left(\mathrm{HV}^{-}\right)$and Inverted Generational Distance (IGD). Based on the experiments with the MOKP instances addressed in this paper, we can conclude that HMOBEDA versions present the best values for both $\mathrm{HV}^{-}$ and IGD indicators, specially when the number of objectives and variables increase, in comparison with all other traditional approaches. Besides, the final PGM is a powerful model providing useful information that can be explored at the end or during evolution. Moreover, we concluded that uniformly distributing the evidences among ideal and extreme points of the Pareto front (EXT version) in the sample process is beneficial for HMOBEDA .

In the future, other learning structure techniques should be examined, such as constraint-based and hybrid approaches for example. These new approaches will be investigated with more

TABLE I: Average HV ${ }^{-}$and IGD over 20 executions. The lowest values are in bold and results with no statistically significant differences (according Kruskal-Wallis and Dunn-Sidaks post-hoc tests) are emphasized in blue.

| Instance | 2.100 | 2.250 | 3.100 | 3.250 | 4.100 | 4.250 | 5.100 | 5.250 | 8.100 | 8.250 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Average hypervolume differences (HV ${ }^{-}$) |  |  |  |  |  |  |  |  |  |  |
|  | $\times 10^{3}$ | $\times 10^{8}$ | $\times 10^{10}$ | $\times 10^{11}$ | $\times 10^{14}$ | $\times 10^{15}$ | $\times 10^{17}$ | $\times 10^{19}$ | $\times 10^{2} 0$ | $\times 10^{30}$ |
| HMOBEDA | 1.5113 | 1.0589 | 2.4364 | 4.1725 | 1.7636 | 4.5313 | 5.4539 | 5.4936 | 8.0816 | 1.3433 |
| HMOBEDA ${ }_{C X T}$ | 1.5091 | 1.0550 | 2.4284 | 4.1649 | 1.7902 | 4.5208 | 5.2559 | 5.4919 | 8.0724 | 1.3427 |
| HMOBEDA ${ }_{C T T T}$ | 1.5046 | 1.0562 | 2.4380 | 4.2007 | 1.7604 | 4.5373 | 5.4657 | 5.5210 | 8.0819 | 1.3458 |
| MBNADA | 1.5801 | 1.0970 | 3.1139 | 4.9970 | 2.1104 | 5.7474 | 6.7614 | 6.4183 | 8.2010 | 1.4549 |
| NSGA-II | 1.5572 | 1.1096 | 2.9675 | 5.0176 | 2.0944 | 5.6352 | 6.4577 | 6.2135 | 8.1963 | 1.4601 |
| S-MOGLS | 1.6866 | 1.1006 | 2.9886 | 5.0135 | 1.9956 | 5.6412 | 6.3791 | 6.2463 | 8.1951 | 1.4537 |
| NSGA-III | 1.5121 | 1.0866 | 2.4461 | 4.2254 | 1.7815 | 5.4369 | 6.3693 | 6.0640 | 8.1820 | 1.4423 |
| MOEA/D | 1.5174 | 0.7219 | 2.4487 | 4.2432 | 1.8215 | 5.2503 | 6.4815 | 5.8908 | 8.1914 | 1.4467 |
| Average IGD metric |  |  |  |  |  |  |  |  |  |  |
|  | $\times 10^{3}$ | $\times 10^{3}$ | $\times 1$ | $\times 1$ | $\times 1$ | $\times 1$ | $\times 1$ | $\times 10^{3}$ | $\times 10^{4}$ |  |
| HMOBEDA | 2.4985 | 6.5341 | 22.5367 | 45.9726 | 19.9013 | 26.7674 | 10.7065 | 16.9647 | 8.1062 | 1.3548 |
| HMOBEDA ${ }_{C X T}$ | 2.4969 | 6.5290 | 21.7047 | 44.2044 | 18.2645 | 26.3493 | 10.2432 | 16.3464 | 8.0231 | 1.3235 |
| HMOBEDA ${ }_{C T T T}$ | 2.4012 | 6.5325 | 22.7251 | 44.9913 | 18.8076 | 26.9888 | 11.2089 | 16.4851 | 8.0274 | 1.3435 |
| MBNADA | 2.5449 | 6.7565 | 32.9048 | 53.4658 | 23.8543 | 30.2950 | 14.8650 | 21.9795 | 8.2153 | 1.6470 |
| NSGA-II | 2.5286 | 6.7907 | 32.1872 | 55.1838 | 23.8436 | 30.0147 | 15.1695 | 22.8114 | 8.4397 | 1.7084 |
| S-MOGLS | 2.7496 | 6.7745 | 32.4780 | 54.6336 | 23.6078 | 29.9242 | 15.2941 | 22.5989 | 8.3997 | 1.7059 |
| NSGA-III | 2.4931 | 6.7602 | 22.5150 | 45.8885 | 18.1235 | 29.5950 | 14.1986 | 20.9275 | 8.2402 | 1.5197 |
| MOEA/D | 2.4992 | 5.0465 | 23.9015 | 45.9216 | 20.3025 | 30.2128 | 14.6657 | 21.9553 | 8.1993 | 1.5268 |

than eight objectives and with other problems. Additionally, another interesting research direction is the application of other types of PGM that can learn and explore dependencies between variables, objectives and automatically control the application of local search operators.

## ACKNOWLEDGMENT

M.Delgado acknowledges CNPq grant 309197/2014-7. M.Martins acknowledges CAPES/Brazil. R. Santana acknowledges support from the IT-609-13 program (Basque Government), TIN2016-78365-R (Spanish Ministry of Economy, Industry and Competitiveness), and CNPq Program Science Without Borders Nos.: 400125/2014-5 (Brazil Government).

## REFERENCES

[1] K. Deb, Multi-objective optimization using evolutionary algorithms. New York: John Wiley and Sons, 2001.
[2] P. Larrañaga and J. A. Lozano, Estimation of distribution algorithms: A new tool for evolutionary computation. Netherlands: Springer, 2002, vol. 2 .
[3] D. Koller and N. Friedman, Probabilistic Graphical Models: Principles and Techniques. The MIT Press, 2009.
[4] H. Karshenas, R. Santana, C. Bielza, and P. Larrañaga, "Multiobjective Estimation of Distribution Algorithm Based on Joint Modeling of Objectives and Variables," IEEE Transactions on Evolutionary Computation, vol. 18, pp. 519-542, 2014.
[5] H. Li, Q. Zhang, E. Tsang, and J. A. Ford, "Hybrid Estimation of Distribution Algorithm for Multiobjective Knapsack Problem," Evolutionary Computation in Combinatorial Optimization, pp. 145-154, 2004.
[6] L. Wang, S. Wang, and Y. Xu, "An effective hybrid EDA-based algorithm for solving multidimensional knapsack problem," Expert Systems with Applications, vol. 39, pp. 5593-5599, 2012.
[7] M. S. Martins, M. R. Delgado, R. Santana, R. Lüders, R. A. Gonçalves, and C. P. d. Almeida, "HMOBEDA: Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm," in Proceedings of the 2016 on Genetic and Evolutionary Computation Conference, ser. GECCO '16. New York, NY, USA: ACM, 2016, pp. 357-364.
[8] H. Ishibuchi, N. Akedo, and Y. Nojima, "Behavior of Multiobjective Evolutionary Algorithms on Many-Objective Knapsack Problems," IEEE Transactions on Evolutionary Computation, vol. 19, no. 2, pp. 264-283, 2015.
[9] Y. Tanigaki, K. Narukawa, Y. Nojima, and H. Ishibuchi, "PreferenceBased NSGA-II for Many-Objective Knapsack Problems," in 7th International Conference on Soft Computing and Intelligent Systems (SCIS) and Advanced Intelligent Systems (ISIS), 2014, pp. 637-642.
[10] M. Laumanns and J. Ocenasek, "Bayesian Optimization Algorithms for Multi-Objective Optimization," in Parallel Problem Solving from NaturePPSN VII, ser. Lecture Notes in Computer Science, vol. 2439, 2002, pp. 298-307.
[11] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference. San Mateo CA: Morgan Kaufmann, 1988.
[12] D. Heckerman, D. Geiger, and D. Chickering, "Learning bayesian networks: the combination of knowledge and statistical data," Machine Learning, vol. 20, no. 3, pp. 197-243, 1995.
[13] G. Cooper and E. Herskovits, "A bayesian method for the induction of probabilistic networks from data," Machine Learning, vol. 9, no. 4, pp. 309-347, 1992.
[14] S. J. Russel and P. Norvig, Artificial Intelligence: A Modern Approach, Second ed. Upper Saddle River, New Jersey: Prentice Hall, 2003.
[15] N. Srinivas and K. Deb, "Multiobjective optimization using nondominated sorting in genetic algorithms," Evolutionary Computation, vol. 2, pp. 221-248, 1994.
[16] K. Deb, S. Agrawal, A. Pratab, and T. Meyarivan, "A Fast and Elitist Multi-Objective Genetic Algorithm: NSGA-II," IEEE Transactions on Evolutionary Computation, vol. 6, pp. 182-197, 2002.
[17] S. Jiang, Y. S. Ong, J. Zhang, and L. Feng, "Consistencies and Contradictions of Performance Metrics in Multiobjective Optimization," IEEE Transactions on Cybernetics, vol. 44, no. 12, pp. 2391-2404, 2014.
[18] E. Zitzler and L. Thiele, "Multiple objective evolutionary algorithms: A comparative case study and the strength Pareto approach," IEEE Transactions on Evolutionary Computation, vol. 3, pp. 257-271, 1999.
[19] D. A. D. A. van Veldhuizen and G. B. Lamont, "Multiobjective Evolutionary Algorithm Test Suites," in Proceedings of the 1999 ACM Symposium on Applied Computing, ser. SAC '99. New York, NY, USA: ACM, 1999, pp. 351-357.
[20] S. Bleuler, M. Laumanns, L.Thiele, and E.Zitzler, "PISA - A Platform and Programming Language Independent Interface for Search Algorithms," in Evolutionary multi-criterion optimization (EMO 2003), ser. Lecture notes in computer science, Berlin, 2003, pp. 494-508.
[21] H. Ishibuchi, Y. Hitotsuyanagi, and Y. Nojima, "Scalability of Multiobjective Genetic Local Search to Many-Objective Problems:Knapsack Problem Case Studies," in Evolutionary Computation, 2008. CEC 2008. IEEE World Congress on Computational Intelligence), June 2008, pp. 3586-3593.
[22] Q. Zhang and H. Li, "MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition," IEEE Transactions on Evolutionary Computation, vol. 11, no. 6, pp. 712-731, 2007.
[23] K. Deb and H. Jain, "An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point-Based Nondominated Sorting Approach, Part I: Solving Problems With Box Constraints," IEEE Transactions on Evolutionary Computation, vol. 18, no. 4, pp. 577-601, 2014.