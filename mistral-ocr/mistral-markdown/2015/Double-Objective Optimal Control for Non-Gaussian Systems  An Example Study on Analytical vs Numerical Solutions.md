# Double-Objective Optimal Control for Non-Gaussian Systems: An Example Study on Analytical vs Numerical Solutions 

Mifeng Ren*, Jianhua Zhang**,<br>Hong Wang ${ }^{* * *}$, Min Huang ${ }^{* * * *}$<br>* College of Information Engineering, Taiyuan University of Technology, Taiyuan, 030024<br>China (e-mail: renmifeng@ 126.com).<br>** State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power<br>University, Beijing, 102206 China (e-mail: zjh@ncepu.edu.cn).<br>*** Control System Centre, School of Electrical and Electronics Engineering, The University of Manchester, M60 1QD, UK , China (e-mail: hong.wang@machester.ac.uk).<br>**** the State Key Laboratory of Synthetical Automation for Process Industry, Northeastern University, Shenyang 110819, China (e-mail: mhuang@mail.neu.edu.cn).


#### Abstract

Minimum entropy control has been proven to be an effective method in control of nonGaussian stochastic systems. In this case, the entropy is proposed as a generalization of the variance measure to characterize the randomness of the process. Minimum entropy corresponds to small uncertainty (or derivation), but it cannot guarantee the tracking error approaching to zero. Therefore, mean square error also should be added in the criterion. In this paper, by using a simple example, the method of generating a representative approximation of the Pareto optimal control set is investigated in both analytical and numerical ways. And simulation results show the feasibility of the proposed doubleobjective optimal control method.


(C) 2015, IFAC (International Federation of Automatic Control) Hosting by Elsevier Ltd. All rights reserved.

Keywords: Double-objective optimal control, non-Gaussian stochastic systems, Renyi's entropy, $\varepsilon$ - constrained method, estimation of distribution algorithm.

## 1. INTRODUCTION

With the increasing quality requirements for industrial dynamic processes, more than one design objective should be satisfied and consequently multi-objective optimal control problems has received considerable attention for a long time (Scherer et al., 1997; Heo et al., 2006; Kumar et al., 2010). Generally, we can distinguish two main approaches to solve multi-objective optimal control problems: 1) dynamical programming techniques (Scherer et al., 1997); and 2) evolutionary algorithms (Heo et al., 2006; Kumar et al., 2010). On the other hand, practical processes are inevitably subject to non-Gaussian random disturbances and nonlinearities, which make the multi-objective optimal control even more complicated (Yue and Wang 2003; Zhang et al., 2009, 2012).

Traditionally, based upon the generalized minimum entropy criterion, the multi-objective stochastic control problem could be transformed into a single-objective dynamic optimization, where the weights denote the different relative importance of different objectives (Yue and Wang 2003; Zhang et al., 2009, 2012). This method is easy to understand, but the value of the weights usually could be only decided by try-and-error method, based on engineering experiences, repeating simulations and other information. And another important disadvantage is that only one optimal control signal can be obtained by using this method, which cannot meet the
requirements of decision maker from different angles. Although we could get different Pareto solution by parametrically varying the weights in the combined single objective function (Jaimes et al., 2011), the non-convexity and previous required information make it difficult to solve or even cannot be solvable. These complexities call for alternative approaches, evolutionary algorithms, to deal with certain types of multi-objective optimal problems (Jaimes et al., 2011). In Afshar et al., 2010, 2011a, differential evolution method was adopted to investigate the multi-objective minimum entropy control problems for nonlinear and nonGaussian stochastic systems. A data-based local multiobjective steepest descent algorithm was used to deal with the energy efficiency problem in papermaking (Afshar et al., 2011b).

In this paper, two-objective optimal controller is designed for a simple nonlinear stochastic system with non-Gaussian disturbances. By using $\varepsilon$ - constrained method (Eichfelder, 2009) and estimation of distribution algorithm (Hauschild and Pelikan, 2011; Zhang et al., 2008), analytical and numerical Pareto optimal control set are obtained, respectively. Another important purpose of this paper is to illustrate that establishing analytical expression of optimal control set is much more difficult than generating numerical ones.

[^0]
[^0]:    2405-8963 (C) 2015, IFAC (International Federation of Automatic Control) Hosting by Elsevier Ltd. All rights reserved.

## 2. A GENERAL PROBLEM FORMULATION

Consider the following SISO nonlinear stochastic system:
$y_{k}=f\left(y_{k-1}, \cdots, y_{k-m}, u_{k}, \cdots, u_{k-m}, \omega_{k}\right)$
where $y_{k} \in \mathfrak{R}^{1}$ is the measured output from the system, $u_{k} \in \mathfrak{R}^{1}\left(\left|u_{k}\right| \leq U_{\max }\right)$ is the control input to the system, $f(\cdot)$ is the nonlinear functional dynamics of the system, $\omega_{k} \in \mathfrak{R}^{1}$ is the bounded random input which has an assumed known PDF denoted by $\gamma_{n t}(x)$.

Denote the set point as $r_{k}$. The objective is to determine $u_{k}$ such that the system output approaches the set point as closely as possible with a small randomness. The mean squarer error is expressed as
$J_{1}\left(u_{k}\right)=\left(r_{k}-E\left(y_{k}\right)\right)^{2}=\left(r_{k}-\int_{a_{1}}^{b_{1}} x \gamma_{y_{k}}\left(u_{k}, x\right) d x\right)^{2}$
where $\gamma_{y_{k}}\left(u_{k}, x\right)$ is the probability density function (PDF) of output $y_{k} \cdot a_{y}$ and $b_{y}$ are the lower and upper bounds of $y_{k}$ respectively.

Since the system output is non-Gaussian, Renyi's entropy is used to characterize the randomness of the output, and it can be formulated as
$J_{2}\left(u_{k}\right)=-\log \int_{a_{2}}^{b_{2}} \gamma_{y_{k}}^{2}\left(u_{k}, x\right) d x$
Therefore, the task of controller design is to find optimal control input $u_{k}^{*}$ to minimize the above two objectives simultaneously, i.e.
$\underset{u_{k}}{\arg \min } J\left(u_{k}\right)=\left(J_{1}\left(u_{k}\right), J_{2}\left(u_{k}\right)\right)$
This is a multi-objective optimal control problem. In general, a weighted expression between these two performance indexes is formulated and minimized in an analytical way in order to obtain the control sequences (Zhang et al., 2012; Yue et al., 2003). This would involve the formulation of output probability density function of the system (1) using the system structure function $f(\cdot)$ and the knowledge on the probability density function of the noise. However, true optimization is still a problem.

In this paper we will consider a simple example and use both analytical and numerical approaches to compare the features of the optimization procedure. The example is given as
$y_{k}=\frac{0.8 y_{k-1}+0.2 u_{k}+\omega_{k}}{\left(1+y_{k-1}\right)^{2}}$
The set point is $r_{k}=1$. The probability density function of the noise is expressed as

$$
\gamma_{n t}(x)=\left\{\begin{array}{cc}
\frac{3}{4 \sqrt{5}}\left(1-0.2 x^{2}\right), & |x| \leq \sqrt{5} \\
0, & \text { otherwise }
\end{array}\right.
$$

## 3. OPTIMAL CONTROL ALGORITHM

## $3.1 \varepsilon$-constrained method

In order to calculate the performance index $J\left(u_{k}\right)$, we will firstly give the PDF of output $\gamma_{y_{k}}\left(u_{k}, \tau\right)$.

From (5a), we have
$\tau=\left(1+y_{k-1}\right)^{2} x-0.8 y_{k-1}-0.2 u_{k}$
where $\tau$ and $x$ are any possible values of $\omega_{k}$ and $y_{k}$, respectively. Combined with Eq. (5b), the PDF of output can be obtained as
$\gamma_{y_{k}}(x)=\left\{\begin{array}{c}\frac{3\left(1+y_{k-1}\right)^{2}}{4 \sqrt{5}}(1-0.2 \\ *\left(\left(1+y_{k-1}\right)^{2} x-0.8 y_{k-1}-0.2 u_{k}\right)^{2},|x| \leq y_{\max } \\ 0, \quad \text { otherwise }\end{array}\right.$
where $y_{\max }=\frac{\sqrt{5}+0.2 U_{\max }+0.8\left|y_{k-1}\right|}{\left(1+y_{k-1}\right)^{2}}$.
Then, according to Eq. (2), we have

$$
\begin{aligned}
J_{1}\left(u_{k}\right) & =\left(r_{k}-E\left(y_{k}\right)\right)^{2} \\
& =a_{2} u_{k}^{2}+a_{1} u_{k}+a_{0}
\end{aligned}
$$

where it has been denoted that

$$
\begin{aligned}
a_{2} & =\frac{\left(1+y_{k-1}\right)^{8} y_{\max }^{6}}{3125} \\
a_{1} & =\frac{8}{3125}\left(1+y_{k-1}\right)^{8} y_{k-1} y_{\max }^{6}-\frac{2}{25 \sqrt{5}} r_{k} y_{\max }^{3} \\
a_{0} & =r_{k}^{2}-\frac{8}{25 \sqrt{5}}\left(1+y_{k-1}\right)^{8} y_{k-1} r_{k} y_{\max }^{3}+\frac{16}{3125}\left(1+y_{k-1}\right)^{8} y_{k-1}^{2} y_{\max }^{6}
\end{aligned}
$$

Similarly, the second performance index presented in Eq. (3) can be formulated as
$J_{2}\left(u_{k}\right)=-\log \int_{x-y_{\max }}^{y_{\max }} \gamma_{y_{k}}^{2}\left(u_{k}, x\right) d x$
$=-\log \left(b_{4} u_{k}^{4}+b_{1} u_{k}^{3}+b_{2} u_{k}^{2}+b_{1} u_{k}+b_{0}\right)$
where it has been formulated that

$$
\begin{aligned}
b_{4}= & 1.44 \times 10^{-5}\left(1+y_{k-1}\right)^{4} y_{\max } \\
b_{3}= & 2.304 \times 10^{-4}\left(1+y_{k-1}\right)^{4} y_{k-1} y_{\max } \\
b_{2}= & -3.6 \times 10^{-3}\left(1+y_{k-1}\right)^{4} y_{\max }+7.2 \times 10^{-4}\left(1+y_{k-1}\right)^{8} y_{\max }^{3} \\
& +1.3824 \times 10^{-3}\left(1+y_{k-1}\right)^{4} y_{k-1}^{2} y_{\max } \\
b_{1}= & -2.88 \times 10^{-2}\left(1+y_{k-1}\right)^{4} y_{k-1} y_{\max } \\
& +5.76 \times 10^{-3}\left(1+y_{k-1}\right)^{4} y_{k-1} y_{\max }^{3} \\
& +3.6864 \times 10^{-3}\left(1+y_{k-1}\right)^{4} y_{k-1}^{3} y_{\max } \\
b_{0}= & 0.225\left(1+y_{k-1}\right)^{4} y_{\max }-0.03\left(1+y_{k-1}\right)^{8} y_{\max }^{3} \\
& -5.76 \times 10^{-2}\left(1+y_{k-1}\right)^{4} y_{k-1}^{3} y_{\max } \\
& +1.8 \times 10^{-3}\left(1+y_{k-1}\right)^{12} y_{\max }^{3} \\
& +1.152 \times 10^{-2}\left(1+y_{k-1}\right)^{4} y_{k-1}^{2} y_{\max }^{3} \\
& +3.6864 \times 10^{-3}\left(1+y_{k-1}\right)^{4} y_{k-1}^{4} y_{\max }
\end{aligned}
$$

Using the $\varepsilon$-constrained method, the optimal problem (4) can be rewritten as

$$
\begin{aligned}
& \text { minimize } J_{2}\left(u_{k}\right) \\
& \text { subject to } J_{1}\left(u_{k}\right) \leq \varepsilon,\left|u_{k}\right| \leq U_{\max }
\end{aligned}
$$

Here, it is assumed that the constrained optimal problem (10) is the convex programming. Then, the $\mathrm{K}-\mathrm{T}$ conditions can be used to solve this problem.

From (8) and (9), the first and second derivatives of $J_{2}\left(u_{k}\right)$ and $g\left(u_{k}\right)=J_{1}\left(u_{k}\right)-\varepsilon$ are formulated as follows:

$$
\begin{aligned}
& \nabla g\left(u_{k}\right)=2 a_{2} u_{k}+a_{1}, \nabla^{2} g\left(u_{k}\right)=2 a_{1}>0 \\
& \nabla J_{2}\left(u_{k}\right)=-\frac{4 b_{4} u_{k}^{3}+3 b_{3} u_{k}^{2}+2 b_{2} u_{k}+b_{1}}{b_{4} u_{k}^{4}+b_{3} u_{k}^{3}+b_{2} u_{k}^{2}+b_{1} u_{k}+b_{0}} \\
& \nabla^{2} J_{2}\left(u_{k}\right) \\
& =\frac{4 b_{4}^{2} u_{k}^{4}+6 b_{3} b_{4} u_{k}^{3}+\left(2 b_{2} b_{4}+9 b_{3}^{2}\right) u_{k}^{2}+\left(4 b_{2} b_{4}-4 b_{1} b_{4}\right) u_{k}^{3}}{\left(b_{4} u_{k}^{4}+b_{3} u_{k}^{3}+b_{2} u_{k}^{2}+b_{1} u_{k}+b_{0}\right)^{2}} \\
& +\frac{\left(2 b_{2}^{2}-12 b_{0} b_{4}\right) u_{k}^{2}+\left(6 b_{0} b_{2}+2 b_{1} b_{2}\right) u_{k}+\left(b_{1}^{2}-2 b_{0} b_{2}\right)}{\left(b_{4} u_{k}^{4}+b_{3} u_{k}^{3}+b_{2} u_{k}^{2}+b_{1} u_{k}+b_{0}\right)^{2}}
\end{aligned}
$$

Then, the $\mathrm{K}-\mathrm{T}$ conditions formula can be given as

$$
\left\{\begin{array}{l}
\nabla J_{2}\left(u_{k}\right)-\lambda \nabla g\left(u_{k}\right)=0 \\
\lambda g\left(u_{k}\right)=0 \\
\lambda \geq 0 \\
\left|u_{k}\right| \leq U_{\text {max }}
\end{array}\right.
$$

1) When $\lambda=0$, we have

$$
\nabla J_{2}\left(u_{k}\right)=-\frac{4 b_{4} u_{k}^{3}+3 b_{3} u_{k}^{2}+2 b_{2} u_{k}+b_{1}}{b_{4} u_{k}^{4}+b_{3} u_{k}^{3}+b_{2} u_{k}^{2}+b_{1} u_{k}+b_{0}}=0
$$

i.c. $4 b_{4} u_{k}^{3}+3 b_{3} u_{k}^{2}+2 b_{2} u_{k}+b_{1}=0$.

According to the intermediate value theorem, The above cubic equation (13) with real coefficients has at least one solution $u_{k}$ among the real numbers, which can be formulated as:

$$
u_{k}^{(n)}=-\frac{1}{12 b_{k}}\left(3 b_{3}+x^{(n)} C+\frac{\Delta_{0}}{x^{(n)} C}\right), \quad n=\{1,2,3\}
$$

where $x^{(1)}=1, x^{(2)}=\frac{-1+i \sqrt{3}}{2}, x^{(3)}=\frac{-1-i \sqrt{3}}{2}$ and

$$
C=\sqrt{\frac{\Delta_{1}+\sqrt{\Delta_{1}^{2}-4 \Delta_{0}^{2}}}{2}} \quad \text { with } \quad \Delta_{0}=9 b_{3}^{2}-24 b_{2} b_{4}
$$

$\Delta_{1}=54 b_{3}^{3}-216 b_{2} b_{3} b_{4}+432 b_{3} b_{4}^{3}$ and $\Delta_{1}^{2}-4 \Delta_{0}^{3}=-432 b_{4}^{2} \Delta$.
If $u_{k}^{n} \in \Re^{1}$ and $\left|u_{k}^{(n)}\right| \leq U_{\text {max }}$, then, it is the optimal solution. Otherwise, there is no solution for equation (11).
2) When $\lambda \neq 0$, we have

$$
g\left(u_{k}\right)=a_{2} u_{k}^{2}+a_{1} u_{k}+a_{0}-\varepsilon=0
$$

Then, we have

$$
u_{k}=\frac{-a_{1} \pm \sqrt{a_{1}^{2}-4 a_{2}\left(a_{0}-\varepsilon\right)}}{2 a_{2}}
$$

For given $\varepsilon$, we will get the solutions. Substitute (16) into (12), and if $u_{k}^{n} \in \Re^{1},\left|u_{k}\right| \leq U_{\text {max }}$ and $\lambda>0$, the obtained solution is the optimal one.

According to Eichfelder, 2009, we choose the parameter $\varepsilon$ as follows:

$$
\varepsilon^{(+)}:=\varepsilon^{l}-\frac{\alpha}{\sqrt{1+\left(\frac{\partial J_{2}\left(u_{k}\left(\varepsilon^{l}\right)\right)}{\partial \varepsilon^{l}}\right)^{2}}}
$$

where $\alpha>0$ is a desired distance between approximation points and satisfies

$$
\left\|J_{2}\left(u_{k}\left(\varepsilon^{(+)}\right)\right)-J_{2}\left(u_{k}\left(\varepsilon^{l}\right)\right)\right\|=\alpha
$$

For different $\varepsilon$, we can obtain different Pareto optimal control inputs.

Remark 1. Analytical method proposed in subsection 3.1 has two main contributions:

1) It provides a general formula of Pareto optimal control inputs solutions for a certain class of control problem.

Anyone can obtain their own wanted result according to the general solution formula without consider other factors.
2)The PDF of tracking error obtained from Eq. (7) forms the relationship among the PDF of system output, randomness and control input, it clearly reveals the PDF evolution of the output. It is the basis to analyze the stability of the closed loop stochastic systems.

Remark 2. The above analytical solution is dependent on the convexity of the problem, and when the problem is complex, it is difficult to have the exact analytical solution. Therefore, in the next subsection, the numerical method will be used to solve the problem proposed in Section 2.

### 3.2 Estimation of distribution algorithm (EDA)

Estimation of distribution algorithms (EDAs) are stochastic optimization methods that search for the space of potential solutions. Different from GA(Genetic Algorithm), there is no crossover or mutation in EDAs. Instead, they build and sample explicit probability distribution model of promising solutions. In the following, details of how to use EDA optimization techniques to solve the multi-objective optimal control problem (4) will be presented.

Denote $u_{k}=u_{k-1}+\Delta u_{k}$, the EDA method is used to find the optimal $\Delta u_{k}$ by minimizing $J_{1}$ and $J_{2}$ simultaneously. The algorithm consists of four main stages: initialization, modelling, reproduction, and selection, which are briefly presented as follows.

Generate initial population randomly in the decision space $\left(-\left(U_{\max }+u_{k-1}\right) \leq \Delta u_{k} \leq U_{\max }-u_{k-1}\right)$ according to the uniform distribution:
$P_{G=0}=\left\{\Delta u_{k, G=0}^{1}, \cdots, \Delta u_{k, G=0}^{M}\right\}$
where $M$ is the total number of populations. Generate $N$ random noises based on PDF (2): $\omega_{k}=\left\{\omega_{k, G=0}^{1}, \cdots, \omega_{k, G=0}^{N}\right\}$. For every $\Delta u_{k, G=0}^{1}(i=1,2, \cdots, M)$ in $P_{G=0}$, we can obtain $N$ output $y_{k}=\left\{y_{k, G=0}^{1}, \cdots, y_{k, G=0}^{N}\right\}$ according to (1). Then, use the following equations to obtain the mean value and entropy of output:
$E\left(y_{k}\right)=\frac{1}{N} \sum_{i=1}^{N} y_{k, G=0}^{i}$
Entropy $\left\{y_{k}\right\}=-\log \frac{1}{N^{2}} \sum_{i=1}^{N} \sum_{j=1}^{N} \kappa\left(y_{k, G=0}^{i}-y_{k, G=0}^{j}, 2 \sigma^{2}\right)$
where $\kappa\left(s, \sigma^{2}\right)=\frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{s^{2}}{2 \sigma^{2}}\right)$ is the Gaussian kernel function, $\sigma^{2}$ represents typical symmetric variance. Eventually, the objectives can be obtained according to equation (3) and (4):

$$
\begin{aligned}
J\left(u_{k, G=0}\right)= & {\left[\left(J_{1}\left(u_{k, G=0}^{1}\right), J_{2}\left(u_{k, G=0}^{1}\right)\right) \cdots\right.} \\
& \left.\left(J_{1}\left(u_{k, G=0}^{M}\right), J_{2}\left(u_{k, G=0}^{M}\right)\right)\right]^{T}
\end{aligned}
$$

By using the non-domination sorting selection method, the Pareto optimal solutions can be obtained. Choose the PDF of these solutions as the probability model of the EDA. Generate a new set $Q=\left\{\Delta u_{k, G=\sigma}^{1}, \Delta u_{k, G=\sigma}^{2}, \cdots, \Delta u_{k, G=\sigma}^{M}\right\}$ with $M$ random members according to the established model. Select $M$ optimal individuals from $Q \cup P_{G=\sigma}$ to create $P_{G=1+1}$ based on the following principle:

1) Use the fast non-dominated sorting approach to establish the partial ordering relation of population $Q \bigcup \operatorname{Pop}(t): J^{1} \succ J^{2} \succ \cdots \succ J^{1}$. Denote $\operatorname{Pop}(t+1)=\varnothing$, and $\operatorname{Pop}(t+1)=\operatorname{Pop}(t+1) \bigcup J^{n}, \quad n=1,2, \cdots, l \quad$ until $|(P o p(t+1))|>M$
2) If $|(P o p(t+1))|>M$, for all members in $\operatorname{Pop}(t+1) \cap J^{n}$, compute their crowding distances using the following equation:

$$
\begin{aligned}
d\left[\Delta u_{k, G=1+1}^{i}\right] & =\left|J_{1}\left[\Delta u_{k, G=1+1}^{i+1}\right]-J_{1}\left[\Delta u_{k, G=1+1}^{i-1}\right]\right| \\
& +\left|J_{2}\left[\Delta u_{k, G=1+1}^{i+1}\right]-J_{2}\left[\Delta u_{k, G=1+1}^{i-1}\right]\right|
\end{aligned}
$$

Remove the element in $\operatorname{Pop}(t+1) \cap J^{n}$ with the smallest crowding distance from $\operatorname{Pop}(t+1)$. In the case when there are more than one member with the smallest crowding distance, randomly choose one and remove it.

The EDA for problem (5) at $k$ instant can be summarized as follows:

Step 1 Initialization: Set $t:=0$. Generate an initial population $P_{G=0}=\left\{\Delta u_{k, G=0}^{1}, \cdots, \Delta u_{k, G=0}^{M}\right\}$ and compute the $J-$ value of each individual solution in $P_{G=0}$.

Step 2 Modelling: Build the probability model of the Pareto optimal solutions in generation $P_{G=\sigma}$.

Step 3 Reproduction: Generate a new solution set $P_{G=\sigma}$ from the model established in Step 2. Evaluate the $J$-value of each solution in $Q$.

Step 4 Selection: Select $M$ individuals from $Q \cup P_{G=\sigma}$ to create $P_{G=1+1}$.

Step 5 Set $t=t+1$ and go to Step 1.

### 3.3 Comparison of the two approaches

Analytical and numerical Pareto control sets for the simple example (1) have been obtained in the previous subsections.

Both approaches have advantages and disadvantages, which can be presented as follows.

The analytical expression of Pareto optimal control law, obtained by $\varepsilon$-constrained method, gives a general formula of two-objective optimal control problem for example (1). However, it can be seen that it is so troublesome to solve nonlinear equations for such a simple example. When the considered system is more complex, the corresponding nonlinear programming may not be solvable. Moreover, the feasibility of this method depends on the convexity of the two objectives. Even those problems are conquered, the following limitations still exist:

1) We need to run many times the analytical control algorithm to find several elements of the Pareto optimal control set.
2) It requires domain knowledge about the problems to be solved, such as the initial value of upper bound $\varepsilon$ in (10).

For the evolution method, estimation of distribution algorithm presented in subsection 3.2, the problems exist in the analytical approach can be ignored. It can generate the whole Pareto control set at one time. Nevertheless, the biggest problem, but a crucial step, for this method is that it is difficult to establish an adequate probabilistic model and in some cases it is possible to create problems that render some model building algorithms ineffective.

## 4. SIMULATION RESULTS

Based on the method in Section 3, MOEDA finds members of the new generation belonging to the Pareto front at each instant (considered time horizon in this simulation is [0s, 30s]). The best member (the point where both objectives are minimized) is found at the end of 20 generations. The simulation results are shown in Figs. 1-6.

The variation of the control input is shown in Fig.1, which is composed by the most preferred solution choosing from the Pareto front at each instant. The selection criterion is that find a compromise between two performance indexes. The corresponding response of the closed loop system under the proposed multi-objective control strategy is presented in Fig.2. It can be seen that the system output can track the set point well. In Fig. 3 and Fig.4, the Pareto optimal control set and Pareto front found by MODEA in the last generation at instant $k=30$ are presented, respectively. The empty zone between $J_{s}=0.007$ to 0.018 in Fig. 4 shows that the Pareto front is uneven distributed, which may be caused by the improper probability model or the small size of population. We will focus this problem in the future research. In Figure 5, both the range and PDF of tracking error at instant $k=30$ are given, it can be seen that the shape of PDF of the tracking error becomes narrower and sharper along with the increasing generation, which illustrates the dispersions of tracking error can be reduced. In order to clarify the improvements, the PDFs in initial and final generations are shown in Figure 6. It can be shown from Figures 5 and 6 that the proposed

MOEDA can decrease the uncertainties of the tracking error and drive the tracking error approaching to zero.

## 5. CONCLUSIONS

In this paper, the double-objective optimal control problem is investigated for a given simple nonlinear and non-Gaussian stochastic system. Different from the previous minimum entropy control strategy, two criteria, entropy and mean square error, are minimized simultaneously instead of combining them into a single objective connected by weights. In order to solve this problem, both analytical and numerical approaches are adopted in this paper. The paper has completed the following two tasks: 1) establish the multiobjective stochastic control algorithm in analytical and numerical ways in the entropy framework; 2) illustrate the difficulty of formulating the analytical Pareto optimal control set. In the future work, the same problem for multivariable stochastic systems will be investigated.

## ACKNOWLEDGEMENTS

This work was supported by the National Basic Research Program of China under Grant 973 Program 2011 CB710706 and China National Science Foundation under Grant 6137405261290323 and 61333007, and the Key Laboratory Open project with Anhui University, these are gratefully acknowledged.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Control input.
![img-1.jpeg](img-1.jpeg)

Fig. 2. System response.

![img-4.jpeg](img-4.jpeg)

Fig. 3. Pareto optimal control inputs at instant $k=30$.
![img-5.jpeg](img-5.jpeg)

Fig. 4. Pareto front at instant $k=30$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. PDF of tracking error at instant $k=30$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. PDFs of initial and final generations at instant $k=30$.

## REFERENCES

Afshar, P., Nobakhti, A., Wang, H. and Chai, T. (2010). Multi-objective Minimum Entropy Controller Design for Stochastic Processes. 2010 American Control Conference, Marriott Waterfront, Baltimore, MD, USA, June 30-July 02, 355-360.
Afshar, P. and Wang, H. (2011a) Multiobjective MetaHeuristic Product Scheduling for Multi-Machine Manufacturing Systems. 2011 50thIEEE Conference on Decision and Control and European Control Conference (CDC-ECC), Orlando, FL, USA, December 12-15, 14051410.

Afshar, P., Brown, M., Maciejowski, J. and Wang, H. (2011b). Data-Based Robust Multiobjective Optimization of Interconnected Processes: Energy Efficiency Case Study in Papermaking. IEEE Transactions on Neural Networks, 22 (12), 2324-2338.
Eichfelder, G. (2009). A constraint method in nonlinear multi-objective optimization. Lecture Notes in Economics and Mathematical Systems, 618, 3-12.
Heo, J.S., Lee, K.Y. and Garduno-Ramirez, R. (2006). Multiobjective Control of Power Plants Using Particle Swarm Optimization Techniques. IEEE Transactions on Energy Conversion, 21 (2), 552-561.
Hauschild, M. and Pelikan, M. (2011). An introduction and survey of estimation of distribution algorithms. Swarm and Evolutionary Computation, 1 (3), 111-128.
Jaimes, A.L., Martinez, S.Z. and Coello, C.A. (2011). An Introduction to Multiobjective Optimization Techniques. In Antonio Gaspar-Cunha and Jose Antonio Covas, editors, Optimization in Polymer Processing, chapter 3, 29-57. Nova Science Publishers, New York, USA.
Kumar, C.A. and Nair, N.K. (2010). Multi-objective PID Controller Based on Adaptive Weighted PSO With Application to Steam Temperature Control in Boilers. International Journal of Engineering Science and Technology, 2 (7), 3179-3184.
Scherer, C., Gahinet, P. and Chilali M. (1997). Multiobjective Output-Feedback Control via LMI Optimization. IEEE Transactions on Automatic Control, 42 (7), 896-911.
Yue, H. and Wang, H. (2003). Minimum entropy control of closed loop tracking errors for dynamic stochastic systems. IEEE Transactions on automatic control, 48 (1), 118-122.
Zhang, J., Chu, C., Munoz, J. and Chen, J. (2009). Minimum entropy based run-to-ran control for semiconductor processes with uncertain metrology delay. Journal of Process Control, 19 (10), 1688-1697.
Zhang, J., Ren, M. and Wang, H. (2012). Minimum entropy control for non-linear andnon-Gaussian two-input and two-output dynamicstochastic systems. IET Control Theory Appl., 6 (15), 2434-2441.
Zhang, Q., Zhou, A. and Jin Y. (2008). RM-MEDA: A Regularity Model Based Multiobjective Estimation of Distribution Algorithm. IEEE Transactions on Evolutionary Computation, 12 (1), 41-63.