# Benchmarking RM-MEDA on the Bi-objective BBOB-2016 Test Suite 

Anne Auger*<br>Dejan Tušar<br>*Inria Saclay-Ile-de-France TACI team, France LRI, Univ. Paris-Sud firstname.lastname@inria.fr

Dimo Brockhoff*<br>Tea Tušar*<br>*Inria Lille Nord-Europe<br>DOLPHIN team, France<br>Univ. Lille, CNRS, UMR 9189 - CRISIAL<br>firstname.lastname@inria.fr<br>Nikolaus Hansen*<br>Tobias Wagner*<br>*TU Dortmund University Institute of Machining Technology (ISF), Germany wagner@isf.de


#### Abstract

In this paper, we benchmark the Regularity Model-Based Multiobjective Estimation of Distribution Algorithm (RMMEDA) of Zhang et al. on the bi-objective bbob-biobj test suite of the Comparing Continuous Optimizers (COCO) platform. It turns out that, starting from about 200 times dimension many function evaluations, RM-MEDA shows a linear increase in the solved hypervolume-based target values with time until a stagnation of the performance occurs rather quickly on all problems. The final percentage of solved hypervolume targets seems to decrease with the problem dimension.


## Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—global optimization, unconstrained optimization; F.2.1 [Analysis of Algorithms and Problem Complexity]: Numerical Algorithms and Problems

## Keywords

Benchmarking, Black-box optimization, Bi-objective optimization

## 1. INTRODUCTION

Multi-objective optimization differs from single-objective optimization most importantly in the type of the desired approximation. In the single-objective case, a single solution with a function value as small as possible is sought. In the multi-objective case, one is interested in finding an approximation of the set of Pareto-optimal solutions. The quality of this approximation is given explicitly or implicitly by an indicator function, such as the hypervolume indicator [1].

Despite this difference of aiming to converge either to a set or to a single solution, only few efforts have been pursued to specifically develop variation or solution generation

[^0]approaches for the multi-objective case. In most cases, still the established variation operators from single-objective optimization are used. One proposal of such a specific variation method is the Regularity Model-Based Multiobjective Estimation of Distribution Algorithm (RM-MEDA) by Zhang et al. We will benchmark this approach on the bi-objective bbobbiobj test suite [6] of the Comparing Continuous Optimizers platform COCO [4].

Throughout the paper, $n$ will denote the problem dimension.

## 2. ALGORITHM

The main idea behind RM-MEDA is to approximate the Pareto set of a multi-objective problem by an $(n-1)$-dimensional manifold represented by a piecewise linear model. This model is used to sample candidate solutions in the vicinity of the current approximation, where the selected solutions are in turn used to improve the sampling model. The number of segments or clusters is a parameter of the algorithm and the respective submodels are learned through the application of a linear principle component analysis (LPCA). The sampling of the piecewise linear model is performed by randomly picking a segment of the model. The probability of picking a segment is relative to the segments ${ }^{1}$ volume ${ }^{1}$. On the segment, a point is chosen uniformly at random and a random perturbation in terms of an isotropic $n$-dimensional normal distribution is added. The variance or step size of the perturbation depends on the variation of the solutions of the current population assigned to the chosen segment.

For a more detailed algorithm description of RM-MEDA, we refer the interested reader to the original publication [7].

### 2.1 Parameter Settings

The MATLAB implementation of RM-MEDA ${ }^{2}$ was run with the default parameters [7]. The code was slightly adjusted to cope with the assumptions regarding the vector and variable representation mady by the COCO platform. A population size $N=100$ was set. The generator of the distribution for sampling new solutions was based on a linear principal component analysis (LPCA) with 5 clusters, 50 training steps, and an extension rate of 0.25 . The budget of $10^{5} n$ was used

[^1]
[^0]:    ${ }^{1}$ In the bi-objective case, the lengths of the segments are
    2. ${ }^{2}$ http://cwwww.essex.ac.uk/staff/qzhang/code/ RM-MEDA-Matlab v0.1.zip

[^1]:    ${ }^{1}$ In the bi-objective case, the lengths of the segments are

to determine the number of generations. No restarts were performed.

## 3. CPU TIMING

In order to evaluate the CPU timing of the algorithm, we have run the RM-MEDA with restarts on the entire bbob-biobj test suite for $100 n$ function evaluations. The COCO Matlab/Octave code was run with Octave 4.0.0 on a Windows 7 machine with Intel(R) Core(TM) i7-5600U CPU 2.60 GHz with 1 processor and 2 cores. The time per function evaluation for dimensions $2,3,5,10,20$, and 40 equaled $4.7 \cdot 10^{-4}$, $5.0 \cdot 10^{-4}, 5.2 \cdot 10^{-4}, 5.8 \cdot 10^{-4}, 7.0 \cdot 10^{-4}$, and $8.7 \cdot 10^{-4}$ seconds respectively.

## 4. RESULTS

Results of RM-MEDA from experiments according to [5], [3] and [2] and on the benchmark functions given in [6] are presented in Figures 1, 2, 3, and 4, and in Table 1. The experiments were performed with COCO [4], version 1.0.1 and the plots were produced with version 1.1.

On almost all problems, three phases can be distinguished in the ECDF plots of Figures 1, 2, and 3. The first phase of initialization and learning of the piecewise representation takes about $100 . .200 n$ function evaluations. In this phase, none or almost none of the target precisions are reached. It coincides with the performance of a pure random search within the region of interest $[-100,100]^{n}$ (comparison results with pure random search not shown here). The second phase shows a linear convergence in which the performance displayed in the ECDFs does not differ much for changing dimension (ECDFs for different dimensions are almost parallel). In this phase, the algorithm successfully exploits the sampling model. The last phase is characterized by a stagnation of the approximation quality. The sampling model cannot further be refined and the number of targets achieved remains constant. The actual percentages of solved problems at the end of the runs depend on the dimension of the problems.

For the linear convergence phase, on some functions, the algorithm seems to be quicker for smaller problem dimensions (on the four functions $11,12,16$, and 23 ) while on most, the algorithm shows an increased performance with higher dimension (on the 35 functions $1-10,17,21,26,28-$ $30,32-40,44-50,52,54,55$, and on almost all function groups). This observation, however, depends on the relative quality of the reference sets and the corresponding hypervolume reference values underlying the performance assessment of COCO. This limitation must be taken into account before making more general statements.

This also holds for the performance of RM-MEDA in the last phase, but to a smaller degree: it is expected that algorithm performance is decreasing when the problem dimension increases as this is the case also for RM-MEDA on all function groups and most functions. Exceptions are f26 (Attractive sector/Schwefel), and functions for which pairs of dimensions show similar performance. Here, it is most likely that the reference sets have a larger impact on the display than the actual effect of the dimension.

## 5. CONCLUSION

After a short initialization phase, the Regularity ModelBased Multiobjective Estimation of Distribution Algorithm
(RM-MEDA) of Zhang et al. showed a linear increase in the solved hypervolume-based target values on the bi-objective bbob-biobj test suite of the Comparing Continuous Optimizers (COCO) platform. However, after some time, a stagnation of the performance occurred. The final percentage of solved hypervolume targets seems to decrease with the problem dimension.

## 6. ACKNOWLEDGMENTS

This work was supported by the grant ANR-12-MONU0009 (NumBBO) of the French National Research Agency.
