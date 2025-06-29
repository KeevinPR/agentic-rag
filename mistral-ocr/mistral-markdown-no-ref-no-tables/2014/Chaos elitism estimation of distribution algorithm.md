# Chaos Elitism Estimation of Distribution Algorithm 

Qingyang Xu


#### Abstract

Estimation of distribution algorithm (EDA) is a kind of EAs, which is based on the technique of probabilistic model and sampling. This paper presents a chaos elitism EDA to improve the performance of traditional EDA to solve high dimensional optimization problems. The famous elitism strategy is introduced to maintain a good convergent performance. The chaos perturbation strategy is used to improve the local search ability. Some simulation experiments conducted to verify the performance of CEEDA. The results of CEEDA are promising, and it is comparable with other EDA.


## I. InTRODUCTION

IN recent years, the Estimation of Distribution Algorithm(EDA) has attracted a lot of attention. It was proposed by Miuhlenbein and Paaß [1], and emerged as a generalization of EAs, for overcoming intrinsic disadvantages of EAs, like building blocks broken and poor performance in high dimensional problems and the difficulty of modeling the solution distribution. Compared with blocks building in EAs, EDA has some attractive characteristics. It does not use the recombination or mutation operators. Instead, they extract the global statistical information from the superiority individual and build the probability model of solution distribution[2]. It is the main advantages of EDA over EAs that the explanatory and transparency of the probabilistic model guides the search process [3]. The new solutions come from the sampling of established probability model which approximates the distribution of promising solutions [4]. Such reproduction procedure allows EDA to search for the global optimal solutions effectively. Additionally, the priori information about the problem structure can be captured by the probability model estimated during the search [5].

For large-scale problem, the optimization results of EDAs become unreliable [6], especially for the increases of number of variables and the number of mixture components. Additionally, the computational cost is huge considering all the possible (in) dependencies among the variables [7]. Therefore, in this paper we adopt a univariate Gaussian model to approximate the solution distribution. In the Gaussian model, some parameters are learnable. In this paper, we propose an chaos elitism EDA for large scale optimization problem. The learning rate of Gaussian parameter is adaptive in the optimization process. The elitism strategy is used to enhance the convergent performance, which is a popular strategy in EAs. In order to improve the local search ability, a

[^0]chaos perturbation operator is designed. The local search operator enhances the diversity of population in the iteration.

## II. CHAOS ELITISM ESTIMATION OF DISTRIBUTION ALGORITHM

Estimation of distribution algorithm is a series of EAs based on probability theory, which makes use of estimation and sampling technology to approximate solutions distribution and generate new solutions. The figure 1 is the flowchart of EDA.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of EDA

## A. The probability model build and updating mechanism

The most important and crucial step of EDAs is how to build the probabilitic model $\mathrm{P}(\mathrm{x})$ to express the promising solutions. In EDAs for global continuous optimization problem, the Gaussian distribution is a common one. Some other complex models, like Gaussian mixture, histogram etc., are also used [8]. In order to construct a Gaussian pdf model of the promising solutions, we should obtain the statistical information of promising solutions. Hence, statistical techniques have been extensively applied to the optimization problems. Fortunately, these parameters can be efficiently computed by the maximum-likelihood estimations [6]. In the algorithm assume full independence, every variable is assumed independent of any variable. That is, the probability distribution $P\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ of the vector $\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ of m variables is assumed to consist of a product of the distributions of individual variables:

$$
P^{k}\left(x_{1}, x_{2}, \cdots x_{D}\right)=\prod_{i=1}^{D} N\left(x_{i} \mid \mu_{i}^{k}, \sigma_{i}^{k}\right)
$$


[^0]:    Manuscript received May 12, 2014. This work was supported in part by the National Natural Science Foundation of China under Grant 61174044.

    Qingyang Xu is with the Shandong University, Weihai, 264209 China (86-0631-5688338; fax: 86-0631-5688338; e-mail: xuqy1981@163.com).

where $\mu_{i}^{k}$ is the mean and $\sigma_{i}^{k}$ is the standard deviation of k -th generation and i-th variable. D is the dimension size. This is very suitable for calculation. Different from the discrete EDAs, the number of parameters to be estimated does not grow exponentially with D .

The pdf $N\left(x_{i} \mid \mu_{i}^{k}, \sigma_{i}^{k}\right)$ for variables xi is parameterized by the mean $\mu_{i}^{k}$ and the standard deviation $\sigma_{i}^{k}$, which is defined by

$$
N\left(x_{i}^{k} \mid \mu_{i}^{k}, \sigma_{i}^{k}\right)=\frac{1}{\sigma_{i}^{k} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}^{k}\right)^{2}}{2 \sigma_{i}^{k^{2}}}}
$$

Therefore, the probability distribution $\mathrm{P}(\mathrm{x} 1, \mathrm{x} 2, \ldots, \mathrm{xD})$ of the vector $(\mathrm{x} 1, \mathrm{x} 2, \ldots, \mathrm{xD})$ of m variables is

$$
P\left(x_{1}, x_{2}, \cdots x_{D}\right)=\prod_{i=1}^{n} \frac{1}{\sigma_{i}^{k} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}^{k}\right)^{2}}{2 \sigma_{i}^{k^{2}}}}
$$

The parameters $\left(\mu_{i}^{k}, \sigma_{i}^{k}\right)$ can be estimated according to the selected best individuals. The parameters $(\mu i, \sigma i)$ can be updated every iteration.

The mean and standard deviation parameters of promising population can be computed adaptively by maximum likelihood technique according to the selected promising solutions.

$$
\begin{gathered}
\mu_{i}(k)=\frac{1}{N B} \sum_{n=1}^{N B} x_{i}^{n}(k) \\
\sigma_{i}^{2}(k)=\frac{1}{N B} \sum_{n=1}^{N B}\left(x_{i}^{n}(k)-\mu_{i}(k)\right)\left(x_{i}^{n}(k)-\mu_{i}(k)\right)^{T}
\end{gathered}
$$

$\mu_{i}(k)$ is the mean of i-th variable in k -th iteration, NB is the selected individuals size. $\sigma_{i}^{2}(k)$ is the covariance of i-th variable in k -th iteration.

## B. Probabilistic sampling

The probability sampling is used to generate new individuals using the learned probabilistic models instead of crossover or mutation operators. The sampling method depends on the type of probabilistic model and the characteristics of the problem. For normal pdf problem, a conversion can be used in order to convert the normal pdf to a standard normal pdf.

Supposing,

$$
y=\frac{x-\mu}{\sigma}
$$

The normal pdf about x is converted to a standard normal pdf about $y$.

$$
N(x \mid \mu, \sigma) \rightarrow N(y \mid 0,1)
$$

The variable x can be calculated by

$$
x=\sigma y+\mu
$$

In the probability models, every variable ( $\mathrm{x} 1, \mathrm{x} 2, \ldots, \mathrm{xm}$ ) is assumed independent of any variable. The mean and standard deviation of variable xi is $\mu i$ and $\sigma i$, when $\mathrm{n} \rightarrow \infty$,

$$
y=\left(\sum_{i=1}^{n} x_{i}-\sum_{i=1}^{n} \mu_{i}\right) / \sqrt{\sum_{i=1}^{n} \sigma_{i}^{2}} \rightarrow N(y, 0,1)
$$

when $\mathrm{n} \rightarrow \infty, \mathrm{y} \rightarrow \mathrm{N}(0,1)$. We can select an appropriate n to generate a normal pdf for probability sampling.

## C. Elitism strategy

Elitism strategy is an effective strategy to ensure the best individual(s) is selected as the next generation in EAs, because the best individual(s) maybe include the information of optimal solution[9]. Therefore, elitism can improves the convergence performance of EAs in many cases[10], and elitism has long been considered an effective method for improving the efficiency of EAs. This is achieved by simply copying the best individual(s) directly to the new generation[11]. However, the number of best individuals selected as the next generation must be handled properly and carefully otherwise may lead to premature convergence or can not improve the efficiency of algorithm.

$$
\operatorname{Pop}(k+1)=\operatorname{Elitism}(k)_{N B} \cup \operatorname{Sample}(k)_{N P-N B}
$$

where Elitism() is the operator to copy the best solution to $\operatorname{Pop}(k+1)$, and $\operatorname{Sample}()$ is the sampling function. $N$ is the population size, $N B$ is the number of best individuals selected to build probability model.

## D. Local search strategy

It is widely accepted that a local search procedure is efficient in improving the solutions generated by the EDA. Kinds of strategies are proposed to enhance the performance of EDA. In this paper, we use a chaos perturbation as the local search strategy[12]. The principle of perturbation is shown as figure 2.

The running of chaos operator is conditional. In this paper, the chaos perturbation is running under the condition of slower convergence.

$$
\left\{\begin{array}{l}
\operatorname{Pop}_{i}^{j}(k)=\operatorname{Pop}_{i}^{j}(k)+\eta z_{i} \text { if }<\text { meet criteria }> \\
\operatorname{Pop}_{i}^{j}(k)=\operatorname{Pop}_{i}^{j}(k) \text { else }<\text { does not meet criteria}>
\end{array}\right.
$$

where $\operatorname{Pop}_{i}^{j}(k)$ is the i-th variable of j -th individual of k -th iteration. $\eta$ is a perturbation coefficient. $z_{i}$ is the chaotic variable, which can be generated by chaotic models. Many chaotic models can be used to generate chaotic variables [13], such as Logistic mapping, Cube mapping or infinite folding mapping. Logistic chaotic model is the most commonly used one, which folded within a limited number under a limited range. The logistic model is shown as follows.

$$
z_{k+1}=\mu z_{k}\left(1-z_{k}\right), n=0,1,2,3 \ldots
$$

It is a typical chaotic system. $\mu$ is the control variable, and a definite time series $z_{1}, z_{2}, z_{3} \mathrm{~L}$ can be generated by iteration for any $z_{0} \in[0,1]$.
![img-2.jpeg](img-2.jpeg)

Fig. 2. The principle of perturbation
The model of infinite folding mapping is shown as equation (13):

$$
z_{k+1}= \begin{cases}\sin \frac{2}{z_{k}} & k=0,1,2 \cdots \\ -1<z_{0}<1 & \end{cases}
$$

The Cube mapping is shown as equation (14)

$$
z_{k+1}= \begin{cases}4 z_{k}^{3}-3 z_{k} & k=0,1,2 \cdots \\ -1<z_{0}<1 & \end{cases}
$$

The Cube and infinite folding mapping do not need control variable $u$. The chaotic sequence distribution of logistic mapping is asymmetric. The probability density follows the distribution property of Chebyshev. The three mappings iterate 10000 times, and we have a statistics of the results. The distribution properties of the three mappings are shown in figure 3. The distribution property of infinite folding mapping is better other two mappings. Therefore, this paper adopts the infinite folding mapping from the common chaotic models to generate the chaotic variables. Moreover, the infinite folding mapping has little sensitivity to the initial value. Therefore, the infinite folding mapping is selected as chaotic variables generator.

The above way to generate new solutions does not take into account the feasibility of the solutions. The individuals could be out of the domain due to the perturbation. Therefore, a repair procedure is needed if illegal individuals are constructed.

$$
\left\{\begin{array}{c}
\text { Pop }_{i}^{j}(k)=\text { Pop }_{i}^{j}(k) \text { if } \text { Pop }_{i}^{j}(k) \in\left[l b_{i} u b_{i}\right] \\
\text { Pop }_{i}^{j}(k)=u b_{i} \text { or } \text { Pop }_{i}^{j}(k)=l b_{i} \\
\text { else } \text { Pop }_{i}^{j}(k)>u b_{i} \text { or } \text { Pop }_{i}^{j}(k)<l b_{i}
\end{array}\right.
$$

$\left[l b_{i} \quad u b_{i}\right]$ is the domain of $i$-th variable.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Distribution property of Logistic, Cube and infinite folding mapping

## E. Procedure of CEEDA

With the design above, the procedure of the ALREEDA is illustrated as following.

## Begin

Initialization: Set parameters: Max_FEs, $N P, N B$,
$w_{-} \max , w_{-} \min , \sigma_{i}^{0},\left[l b_{i} \quad u b_{i}\right]$, and generate population Pop(0).
While(stop criteria ?)
Evaluation: Calculate the fitness of all individuals, and store the elitism.
Statistical information obtaining: Select NB individuals to estimate the parameter of the probabilistic model, and update the parameter.

$$
\begin{gathered}
\mu_{i}(k)=\frac{1}{N} \sum_{m=1}^{N} x_{i}^{n}(k) \\
\sigma_{i}^{2}(k)=\frac{1}{N} \sum_{m=1}^{N}\left(x_{i}^{n}(k)-\mu_{i}(k)\right)\left(x_{i}^{n}(k)-\mu_{i}(k)\right)^{2} \\
\sigma_{i}(k)=w \sigma_{i}(k)+(1-w) \sigma_{i}(k-1)
\end{gathered}
$$

Probabilistic model building: According to estimated parameters, build the probabilistic model of each variable $x_{i}$

$$
P\left(x_{1}, x_{2}, \cdots x_{m}\right)=\prod_{i=1}^{m} \frac{1}{\sigma_{i}^{2} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}^{2}\right)^{2}}{2 \sigma_{i}^{2}}}
$$

Probabilistic sampling: Make use of the sampling technology sampling ( $N P-N B$ ) individuals.
Elitism strategy: Combine the sampling individuals with elitism and generate new $\operatorname{Pop}(k)$.

$$
\operatorname{Pop}(k)=\operatorname{Elitism}(N B)_{k} \cup \operatorname{Sample}(N-N B)_{k}
$$

Chaos perturbation (perturbation criteria ?):
$\operatorname{Pop}_{i}^{j}(k)=\operatorname{Pop}_{i}^{j}(k)+t p_{i}$
$k=k+1$
End While
End Begin

## III. SIMULATION EXPERIMENTS

To testify the performance and scalability of the proposed algorithm, we use a special function f 7 with complex structure of CEC08. The concrete formulas of functions are shown as follows, and we also give a graphical exposition to express the complexity of the functions.
$f_{c}(\mathbf{x})=\sum_{i=1}^{D} \operatorname{fractal1D}\left(x_{i}+\operatorname{twist}\left(x_{i+\operatorname{twist} D \mid c i}\right)\right)$
$\operatorname{twist}(y)=4\left(y^{4}-2 y^{3}+y^{2}\right)$
Fractal1D $(x) \approx$
$\sum_{k=1}^{4} \sum_{1}^{D-1} \sum_{1}^{2} \sum_{1}^{2} \operatorname{doubledip}(x, \operatorname{ranl}(o), \frac{1}{2^{k-1}(2-\operatorname{ranl}(o))})$
$\operatorname{doubledip}(x, c, s)= \begin{cases}(-6144(x-c)^{8}+3088(x-c)^{4} \\ -392(x-c)^{2}+1) s, x \in(-0.5,0.5) \\ 0, \text { otherwise }\end{cases}$
$\mathbf{x}=\left(x_{1}, x_{2}, \cdots, x_{D}\right), \mathrm{D}$ is the dimensions, $x_{i} \in[-1,1]$. $\operatorname{ran} 1(\mathrm{o})$ is a pseudorandomly chosen funciton, with seed o and equal probability from the interval $[0,1]$, and having the precision of double. ran2(o) is also pseudorandomly chosen fucntion, with seed o and equal probability from the set $\{0,1,2\}$. fractal1D(x) is an approximation to a recursive algorithm; it does not take account of wrapping at the boundaries, or local re-seeding of the random generators. $f_{7}$ is a multimodal non-separable function. The global minimal is unknown.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The graph of $f 7$
We can see from the figure $4, f 7$ is a very complex function. It looks like mountain range profile. There are many bigger maintains and also many narrow and dense peaks. The global optimum of $f 7$ is unknown so far.

In the iteration optimization algorithm, such as EAs, the maximal iteration number (Max_FEs) is an essential parameter [14], while it is maybe varied. The Max_FEs is set to $3 \mathrm{E}+6$ in this paper. For EDAs, the population size NP and the promising solution number NB are important except for

Max_FEs. It is obvious that for an easy problem, a small value of NP is sufficient, but for difficult problems, a large value of NP is recommended in order to avoid trapping to a local optimum. The large NP may provide better optimization with larger calculation [15]. However, it is maybe vary from problem to problem. We pay attention to the performance of EDA instead of the population size. We provide some choices $(100,200,300,500)$ to obtain better performance for the CEEDA. We have a comparisons of different population size, and select the best population size as the final decision of the algorithm on the problem with the given problem size. The NB is also an important parameter for the probabilistic model learning of EDA, and we also have a comparison to determine a proper NB. In the comparisons, the error recorded finally is the absolute margin between the fitness of the best solution found and the fitness of the global optimum.

In figure 5, it is the testing result when the dimension D is 100 and has different NP and NB.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Convergence graph for $f_{7}(\mathrm{D}=100$, different NP)
We also do some tests when the dimension D is 500 in figure 6. Firstly, we test the algorithm under different population size 100,200 and 500 . According to the performance of the algorithm, the population size is selected as 500.50 is a suitable value for NB according to the performance of the algorithm on the benchmarks.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence graph for $f_{7}(\mathrm{D}=500$, different NP)

We also do a small test to testify the effect of the elitism strategy. The optimization process partial enlarge graph of $f_{5}$ are shown in figure 7. $f_{5}$ is the most obvious one. The optimization process is concussive without elitism strategy due to the complex $\mathrm{f7}$ function, though the optimization is convergent finally. The convergence is smooth and steady when the elitism strategy is added to the algorithm.
![img-6.jpeg](img-6.jpeg)

Fig. 7. The optimization process partial enlarge graph of $f_{5}$
We also compare CEEDA with other EDA. LSEDA-gl is a robust univariate EDA, which is proposed for large scale optimization and has good performance. In LSEDA-gl, an effective sampling under mixed Gaussian and Levy probability distribution is introduced to balance optimization and learning. And a restart mechanism is used to stop some variables shrinking dramatically to zero solely.

The convergent graph on 1000-D of the two algorithms is shown in figure 8. From the figure we can see the convergent process of CEEDA is gentle than LSEDA-gl. In comparison, CEEDA outperforms LSEDA-gl even though the convergence is kindly.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Convergence graph for $f_{7}(\mathrm{D}=1000)$

## ACKNOWLEDGMENT

This work is supported by the National Natural Science Foundation of China (under Grant 61174044). The authors want to thank Ke Tang for providing the source code of the benchmarks and competition result of CEC'08 large scale optimization at website (http://nical.ustc.edu.cn/cec08ss.php).
