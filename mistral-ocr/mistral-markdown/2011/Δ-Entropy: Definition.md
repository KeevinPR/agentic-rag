# $\Delta$-Entropy: Definition, properties and applications in system identification with quantized data 

Badong Chen ${ }^{\mathrm{a}, *}$, Yu Zhu ${ }^{\text {b }}$, Jinchun $\mathrm{Hu}^{\mathrm{b}}$, José C. Príncipe ${ }^{\mathrm{a}}$<br>${ }^{a}$ Department of Electrical and Computer Engineering, University of Florida, Gainesville, FL 32611, USA<br>${ }^{\mathrm{b}}$ Department of Precision Instruments and Mechanology, Tsinghua University, Beijing 100084, PR China

## A R T I C L E I N F O

## Article history:

Received 23 January 2010
Received in revised form 21 November 2010
Accepted 29 November 2010
Available online 7 December 2010

## Keywords:

$\Delta$-Entropy
Minimum error entropy criterion
System identification
Estimation of distribution algorithm

A B S T R A C T

Recently, the minimum error entropy criterion, an information theoretic alternative to the traditional mean square error criterion, has been successfully used in the contexts of machine learning and signal processing. For system identification, however, the MEE criterion will be no longer suitable if the training data are discrete-valued, since minimizing error's discrete entropy cannot constrain error's dispersion. In this paper, to make the MEE criterion suitable for the discrete-valued data cases, we give a new entropy definition for the discrete random variables, i.e. the $\Delta$-entropy, based on Riemann sums for finite size partitions. A probability weighted formula is established to calculate the average partition.This new entropy retains some important properties of the differential entropy and reduces to discrete entropy under certain conditions. Unlike discrete entropy, the $\Delta$-entropy is sensitive to the dynamic range of the data, and can be used as a superior optimality criterion in system identification problems. Also, we present a plug-in estimate of $\Delta$-entropy, analyze its asymptotic behavior and explore the links to the kernel based and $m$-spacing based estimates for differential entropy. Finally, the $\Delta$-entropy criterion is applied in system identification with coarsely quantized input-output data to search for the optimum parameter set. Monte Carlo simulations demonstrate the performance improvement that may be achieved with the $\Delta$-entropy criterion.

Published by Elsevier Inc.

## 1. Introduction

For the univariate discrete random variable $X$ with $M$ discrete values $\boldsymbol{S}=\left(s_{1}, s_{2}, \ldots, s_{M}\right)$, and corresponding probability distribution $\boldsymbol{P}=\left(p_{1}, p_{2}, \ldots, p_{M}\right)$, the discrete entropy, denoted by $H(X)$ or $H(\boldsymbol{P})$, is defined by [4]

$$
H(X)=-\sum_{i=1}^{M} p_{i} \log p_{i}
$$

which is a non-negative concave function of $\boldsymbol{P}$. This definition can be extended to the case where the discrete variable takes a countable infinite set of values.

The discrete entropy measures the average uncertainty (information) contained in the probability distribution, ${ }^{1}$ and can be used to measure many other concepts such as equality, disorder, diversity, similarity, unbiasedness, randomness, and so

[^0]
[^0]:    * Corresponding author.

    E-mail address: chenbd04@mails.tsinghua.edu.cn (B. Chen).
    ${ }^{1}$ This entropy is called probabilistic entropy. In order to measure non-probabilistic uncertainty contained in a fuzzy set, a variety of fuzzy entropies are also defined (see e.g. [45-48]).

on [15]. However, as the discrete entropy depends only on the distribution $\mathbf{P}$, and takes no account of the discrete values, it is independent of the dynamic range of the random variable. Therefore, we conclude that discrete entropy is unable to differentiate between two random variables that have different dynamic ranges and the same distribution. In fact, the discrete random variables with the same entropy may have arbitrarily small or large variance, a typical measure for dispersion of the random variable, where dispersion here is defined loosely as the concentration spread around the mean value.

If $X$ is a continuous random variable with probability density function (PDF) $f(x)$, the differential entropy, denoted by $h(X)$ or $h(f)$, is defined as [4]

$$
h(X)=-\int_{-\infty}^{\infty} f(x) \log f(x) d x
$$

Different from the discrete entropy, the differential entropy can be negative and even minus infinite. So strictly speaking, the differential entropy cannot represent a measure of uncertainty since uncertainty should in general be positive, although it can be used as such if we take into consideration the dimension of the distribution [49]. However, differential entropy can be used to measure the dispersion of a continuous random variable. For example, if $X$ is of Gaussian distribution with variance $\operatorname{Var}(X)$, the differential entropy will be

$$
h(X)=\frac{1}{2} \log (2 \pi e \operatorname{Var}(X))
$$

It is clear that smaller differential entropy implies smaller variance (dispersion).
As the differential entropy measures both the probabilistic uncertainty and dispersion, it can be used as an optimality criterion in the estimation and identification problems, which leads to the so called minimum error entropy (MEE) criterion [2,6-8,13,20,23,27,37]. The MEE criterion is concerned with the use of differential entropy as a cost function for system identification and parameter estimation. Traditionally, the minimum mean square error (MMSE) criterion has been the workhorse of estimation and identification because of simplicity and solid statistical foundation. However, recent studies suggest that, as an optimality criterion, MEE is superior to MMSE, since minimizing the error entropy constrains all moments of the error's PDF, whereas MMSE constrains only the first and second moments of the PDF [2,6-8,23,27]. The previous studies have demonstrated that the MEE criterion offers potentially significant performance improvement in system identification, particularly in nonlinear and non-Gaussian settings.

In many practical system identification scenarios, the unknown system's inputs and outputs may be discrete-valued for a variety of reasons:
(1) For many systems, especially in the field of digital communication, the input signals take values only in finite alphabetical sets $[10,17,18,25]$.
(2) Coarsely quantized plant's inputs and outputs are commonly used, when the data are obtained from an A/D converter or from a communication channel $[1,21,26,33,38]$. Typical contexts involving quantized data include digital control systems (DCS), networked control systems (NCS), wireless sensor networks (WSN), etc.
(3) Binary-valued sensors occur frequently in practical systems [35,36,40]. Some typical examples of binary-valued sensors can be found in [36].
(4) Discrete-valued time-series are common in practice. In recent years, the count or integer-valued data time-series have gained increasing attention for point processes [41-44].

Sometimes, due to computational consideration, even if the observed input and output signals are continuous-valued, one may classify the data into groups and obtain the discrete-valued data [24, Chapter 5]. In all these situations one normally applies differential entropy to implement the MEE criterion, in spite of the fact that the random variable is indeed discrete. When the discretization is coarse (i.e. few levels) the use of differential entropy may carry a penalty in performance that is normally not quantified. Alternatively, the MEE implemented with discrete entropy will become ill-suited since the minimization fails to constrain the error's dispersion which should be pursued because the error dynamic range decreases over iterations.

The present paper augments the MEE criterion choices by providing a new entropy definition for discrete random variables, called $\Delta$-entropy, which comprises two terms: one is the discrete entropy, and the other is the logarithm of the average interval between two successive discrete values. This new entropy retains important properties of the differential entropy and reduces to the traditional discrete entropy for a special case. More importantly, the proposed entropy definition can still be used to measure the dispersion of a discrete random variable, and hence can be used as an MEE optimality criterion in system identification with discrete-valued data.

The paper is organized as follows. In Section 2 we give the definition of $\Delta$-entropy. In Section 3 we investigate the properties of $\Delta$-entropy. In Section 4 we analyze the plug-in estimate of $\Delta$-entropy. In Section 4.2, we apply the $\Delta$-entropy criterion in system identification with quantized I/O data. The estimation of distribution algorithm (EDA) is used as the parameter search algorithm, and Monte Carlo simulations are performed to demonstrate the satisfactory performance. Finally, in Section 5, we draw some conclusions and discuss future work.

# 2. Definition of $\Delta$-entropy 

In this section, we propose an alternative entropy definition for discrete random variables. Before proceeding, let's review the relationship between the differential and the discrete entropy (see also [4] for details). Consider a continuous random variable $X$ with PDF $f(x)$. We can produce a quantized random variable $X^{\Delta}$ (see Fig. 1), given by

$$
X^{\Delta}=s_{i}, \quad \text { if } i \Delta \leqslant X<(i+1) \Delta
$$

where $s_{i}$ is one of countable values, which satisfies

$$
i \Delta \leqslant s_{i}<(i+1) \Delta, \quad \text { and } \quad f\left(s_{i}\right) \Delta=\int_{i \Delta}^{(i+1) \Delta} f(x) d x
$$

The probability that $X^{\Delta}=s_{i}$ is

$$
p_{i}=\operatorname{Pr}\left(X^{\Delta}=s_{i}\right)=f\left(s_{i}\right) \Delta
$$

And the discrete entropy $H\left(X^{\Delta}\right)$ can be calculated as

$$
H\left(X^{\Delta}\right)=-\sum_{i=-\infty}^{\infty} p_{i} \log p_{i}=-\sum_{i=-\infty}^{\infty} \Delta f\left(s_{i}\right) \log f\left(s_{i}\right)-\log \Delta
$$

If the density function $f(x)$ is Riemann integrable, the following limit holds

$$
\lim _{\Delta \rightarrow 0}\left(H\left(X^{\Delta}\right)+\log \Delta\right)=-\int_{-\infty}^{\infty} f(x) \log f(x) d x=h(X)
$$

This suggests that, if the quantization interval $\Delta$ is small enough, we have

$$
h(X) \approx H\left(X^{\Delta}\right)+\log \Delta
$$

Thus the differential entropy of a continuous random variable $X$ is approximately equal to the discrete entropy of the quantized variable $X^{\Delta}$ plus the logarithm of the quantization interval $\Delta$. This important relationship explains why differential entropy is sensitive to dispersion. That is, compared with the discrete entropy, the differential entropy "contains" the term $\log \Delta$, which measures the average interval between two successive quantized values since

$$
\Delta=\lim _{N \rightarrow \infty} \frac{1}{2 N+1} \sum_{i=-N}^{N}\left|s_{i+1}-s_{i}\right|
$$

The above analysis inspired us to seek a new entropy definition for discrete random variables that will measure uncertainty as well as dispersion and is defined as follows:

Definition 1. For a discrete random variable $X$ with values $\boldsymbol{S}=\left(s_{1}, s_{2}, \ldots, s_{M}\right)$, and the corresponding distribution $\boldsymbol{P}=\left(p_{1}\right.$, $\left.p_{2}, \ldots, p_{M}\right)$, the $\Delta$-entropy, denoted by $H_{\Delta}(X)$ or $H_{\Delta}(\boldsymbol{S}, \boldsymbol{P})$, is defined as

$$
H_{\Delta}(X)=-\sum_{i=1}^{M} p_{i} \log p_{i}+\log \Delta(X)
$$

where $\Delta(X)$ (or $\Delta(\boldsymbol{S}, \boldsymbol{P})$ ) stands for the average interval (distance) between two successive values.

Remark 1. The $\Delta$-entropy contains two terms, where the first term is identical to the classical discrete entropy and the second term equals the logarithm of the average interval between two successive values. Obviously, this new entropy can be used as an optimality criterion in the estimation and identification problems, because minimizing error's $\Delta$-entropy will decrease the average interval and automatically force the error samples to concentrate without renormalization of the error variable through training.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Quantization of a continuous random variable.

Now we discuss how to calculate the average interval $\Delta(X)$ to preserve the known properties of entropy. In the rest of the paper, we assume, without loss of generality, that the discrete values satisfy $s_{1}<s_{2}<\cdots<s_{M}$. Naturally, we immediately think of the arithmetic and geometric means, that is

$$
\left\{\begin{array}{l}
\Delta(X)=\sum_{M-1}^{1} \sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| \text { for arithmetic mean } \\
\Delta(X)=\left(\prod_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right|\right)^{1 /(M-1)} \text { for geometric mean }
\end{array}\right.
$$

Both arithmetic and geometric means take no account of the distribution $\boldsymbol{P}$. A more reasonable approach is to calculate the average interval $\Delta(X)$ by a probability-weighted method. For example, we can use the following formula:

$$
\Delta(X)=\sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| \frac{p_{i}+p_{i+1}}{2}
$$

However, if $\left(p_{1}+p_{M}\right)>0$, the sum of weights will be less than one, because

$$
\sum_{i=1}^{M-1} \frac{p_{i}+p_{i+1}}{2}=1-\frac{p_{1}+p_{M}}{2}<1
$$

To address this issue, we propose the formula:

$$
\Delta(X)=\sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| \frac{p_{i}+p_{i+1}}{2}+\frac{\left|s_{M}-s_{1}\right|}{M-1} \frac{p_{1}+p_{M}}{2}
$$

The second term of (15) equals the arithmetic mean multiplied by $\left(p_{1}+p_{M}\right) / 2$, which normalizes the weight sum to one. Substituting (15) into (11), we obtain

$$
H_{\Delta}(X)=-\sum_{i=1}^{M} p_{i} \log p_{i}+\log \left(\sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| \frac{p_{i}+p_{i+1}}{2}+\frac{\left|s_{M}-s_{1}\right|}{M-1} \frac{p_{1}+p_{M}}{2}\right)
$$

The above $\Delta$-entropy can be immediately extended to the infinite value-set case, that is

$$
H_{\Delta}(X)=-\sum_{i=-\infty}^{\infty} p_{i} \log p_{i}+\log \left(\sum_{i=-\infty}^{\infty}\left|s_{i+1}-s_{i}\right| \frac{p_{i}+p_{i+1}}{2}+\lim _{\| \rightarrow \infty} \frac{\left|s_{N}-s_{-N}\right|}{2 N} \frac{p_{-N}+p_{N}}{2}\right)
$$

In the rest of the paper, we use (16) and (17) as the $\Delta$-entropy expression, which has strong links with the differential entropy, and reduces to the traditional discrete entropy under an obvious condition. In the next section, we explore some important properties of the $\Delta$-entropy.

# 3. Some important properties 

As discussed in the previous section, the definition of $\Delta$-entropy is enlightened by the connection between the differential entropy and its quantized discrete entropy, so $\Delta$-entropy should maintain a close connection to the differential entropy. We first show that the $\Delta$-entropy and the differential entropy have the following relationship in the limit:

Theorem 1. For any continuous random variable $X$ with Riemann integrable PDF $f(x)$, we have $\lim _{\Delta \rightarrow 0} H_{\Delta}\left(X^{\Delta}\right)=h(X)$, where the quantized discrete variable $X^{\Delta}$ is given by (4).

Proof. See Appendix A.

Remark 1. By Theorem 1, the differential entropy of $X$ is the limit of the $\Delta$-entropy of $X^{\Delta}$ as $\Delta \rightarrow 0$. To some extent, we can regard the $\Delta$-entropy as a "quantized version" of the differential entropy.

## Theorem 2

$$
\log \left(\max _{j=1,2, \ldots M-1}\left|s_{j+1}-s_{j}\right|\right) \geqslant H_{\Delta}(X)-H(X) \geqslant \log \left(\min _{j=1,2, \ldots M-1}\left|s_{j+1}-s_{j}\right|\right)
$$

Proof. Omitted due to simplicity.

Remark 2. An appealing feature of Theorem 2 is that, if the minimum interval between two successive discrete values is larger than one, we have $H_{\Delta}(X)>H(X)$, whereas if the maximum interval between two successive discrete values is smaller than one, we have $H_{\Delta}(X)<H(X)$.

Theorem 3. If $X$ is a discrete random variable with equally spaced values, i.e. $\forall i, 1 \leqslant i \leqslant M-1,\left|s_{i+1}-s_{i}\right| \equiv \Delta$, and $\Delta=1$, then $H_{\Delta}(X)=H(X)$.

Proof. For equally spaced intervals, the difference between the $\Delta$-entropy and the discrete entropy equals $\log \Delta$. Hence, the statement follows directly.

Now we can understand why we chose the name $\Delta$-entropy for the new measure: when the scale goes to zero we end up with differential entropy and when the scale defaults to the natural numbers the measure is indistinguishable from discrete entropy. Classification is a typical example of the error variable distributed on equally spaced values $(0,1,2,3, \ldots)$. Therefore, in classification, the error's discrete entropy is equivalent to the $\Delta$-entropy. This fact also gives an interpretation for why the discrete entropy can be successfully used in the test and classification problems [1431].

We can use Theorem 2 and the bound of the discrete entropy to obtain a bound on the $\Delta$-entropy.

# Corollary 1 

$$
\log \left(\min _{j=1,2, \ldots, M-1}\left|s_{j+1}-s_{j}\right|\right) \leqslant H_{\Delta}(X) \leqslant \frac{1}{2} \log \left(2 \pi e\left(\sum_{i=1}^{M} p_{i}\right)^{2}-\left(\sum_{i=1}^{M} i p_{i}\right)+\frac{1}{12}\right)\left(\max _{j=1,2, \ldots, M-1}\left|s_{j+1}-s_{j}\right|\right)^{2}\right)
$$

Proof. In information theory, it has been proved that (see [4, p. 489])

$$
0 \leqslant H(X) \leqslant \frac{1}{2} \log \left(2 \pi e\left(\sum_{i=1}^{M} p_{i}\right)^{2}-\left(\sum_{i=1}^{M} i p_{i}\right)+\frac{1}{12}\right)\right)
$$

Combining the above result and Theorem 2, the corollary is proved.
The lower bound of the $\Delta$-entropy can also be expressed in term of the variance $\operatorname{Var}(X)$, as given in the following theorem.
Theorem 4. If $p_{\min }=\min \left\{p_{i}\right\}>0$, then $H_{\Delta}(X) \geqslant \log \left(\frac{2 \mathrm{~N} p_{\min }}{M}\right)+\frac{1}{2} \log (\operatorname{Var}(X))$.
Proof. See Appendix B.
The above lower bound confirms the fact that minimizing the $\Delta$-entropy will constrain the variance. This is a key difference between the $\Delta$-entropy and the classical discrete entropy.

Theorem 5. For any discrete random variable $X, \forall c \in \mathbb{R}, H_{\Delta}(X+c)=H_{\Delta}(X)$.
Proof. Since $H(X+c)=H(X)$, and $\Delta(X+c)=\Delta(X)$, we have $H_{\Delta}(X+c)=H_{\Delta}(X)$.

## Theorem 6

$$
\forall \alpha \in \mathbb{R}, \quad \alpha \neq 0, \quad H_{\Delta}(\alpha X)=H_{\Delta}(X)+\log |\alpha|
$$

Proof. Since $H(\alpha X)=H(X)$, and $\Delta(\alpha X)=|\alpha| \Delta(X)$, we have $H_{\Delta}(\alpha X)=H_{\Delta}(X)+\log |\alpha|$.

Remark 3. Theorems 5 and 6 indicate that the $\Delta$-entropy has the same shifting and scaling properties of differential entropy.

Theorem 7. The $\Delta$-entropy is a concave function of $\boldsymbol{P}=\left(p_{1}, p_{2}, \ldots, p_{M}\right)$.

Proof. See Appendix C.

Remark 4. The concavity of the $\Delta$-entropy is a desirable property for the entropy optimization problem. Specifically, this property ensures that when a stationary value of the $\Delta$-entropy subject to linear constraints is found, it gives the global maximum value [15].

Now we solve the maximum $\Delta$-entropy distribution. Consider the constrained optimization problem:

$$
\left\{\begin{array}{l}
\max _{i=1}^{M} H_{\Delta}(X) \\
\text { s.t. }\left\{\begin{array}{l}
\sum_{i=1}^{M} p_{i}=1 \\
\sum_{i=1}^{M} p_{i} g_{k}\left(s_{i}\right)=a_{k}, \quad k=1,2, \ldots, K
\end{array}\right.
$$

in which $a_{k}$ is the expected value of function $g_{k}(X)$. The Lagrangian is given by

$$
L=H_{\Delta}(X)-\left(\lambda_{0}-1\right)\left(\sum_{i=1}^{M} p_{i}-1\right)-\sum_{k=1}^{K} \lambda_{k}\left(\sum_{i=1}^{M} p_{i} g_{k}\left(s_{i}\right)-a_{k}\right)
$$

where $\lambda_{0}, \lambda_{1}, \ldots, \lambda_{K}$ are the $(K+1)$ Lagrange multipliers corresponding to the $(K+1)$ constraints. Here $\lambda_{0}-1$ is used as the first Lagrange multiplier instead of $\lambda_{0}$ as a matter of convenience. Let $\partial L / \partial p_{i}=0$, we have

$$
\Delta(X)\left(-\lambda_{0}-\sum_{k=1}^{K} \lambda_{k} g_{k}\left(s_{i}\right)-\log p_{i}\right)+c_{i}=0, \quad i=1,2, \ldots, M
$$

where

$$
c_{i}= \begin{cases}\frac{\left\|_{M}-s_{1}\right\|}{2\|M-1\|}+\frac{\left\|s_{1}-s_{2}\right\|}{2}, & i=1 \\ \frac{\left\|s_{i-1}-s_{i-1}\right\|}{2}, & i=2, \ldots, M-1 \\ \frac{\left\|_{M}-s_{2}\right\|}{2\|M-1\|}+\frac{\left\|s_{M}-s_{M-1}\right\|}{2}, & i=M\end{cases}
$$

Solving Eq. (21), we have the theorem:
Theorem 8. The distribution $\boldsymbol{P}$ that maximizes the $\Delta$-entropy subject to the constraints of (19) is given by

$$
p_{i}=\exp \left(-\lambda_{0}-\sum_{k=1}^{K} \lambda_{k} g_{k}\left(s_{i}\right)+\frac{c_{i}}{\Delta(X)}\right), \quad i=1,2, \ldots, M
$$

where $\lambda_{0}, \lambda_{1}, \ldots, \lambda_{K}$ are determined by substituting for $p_{i}$ from (23) into the constraints of (19).

Remark 5. For the case in which the discrete values are equally spaced, we have $c_{1}=c_{2}=\cdots=c_{M}=\Delta$, and (23) becomes

$$
p_{i}=\exp \left(\left(1-\lambda_{0}-\sum_{k=1}^{K} \lambda_{k} g_{k}\left(s_{i}\right)\right)\right)
$$

In this case, the maximum $\Delta$-entropy distribution is identical to the maximum discrete entropy distribution [15].

# 4. Estimation of $\Delta$-entropy 

In practical applications, the discrete values $\left\{s_{i}\right\}$ and probabilities $\left\{p_{i}\right\}$ are usually unknown, so we have to estimate them from sample data $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, which is straight forward for the new measure. An immediate approach is to group the sample data into different values $\left\{\hat{s}_{i}\right\}$ and calculate the corresponding relative frequencies $\left\{\hat{p}_{i}\right\}$, given by

$$
\hat{p}_{i}=n_{i} / n, \quad i=1,2, \ldots, M
$$

in which $n_{i}$ denotes the number of these outcomes belonging to the value $\hat{s}_{i}$, with $\sum_{i=1}^{M} n_{i}=n$.
Based on the estimated values $\left\{\hat{s}_{i}\right\}$ and probabilities $\left\{p_{i}\right\}$, a "plug-in" estimate of $\Delta$-entropy can be obtained as follows:

$$
H_{\Delta}(\tilde{\boldsymbol{S}}, \tilde{\boldsymbol{P}})=-\sum_{i=1}^{M} \hat{p}_{i} \log \hat{p}_{i}+\log \left(\sum_{i=1}^{M-1}\left|\hat{s}_{i+1}-\hat{s}_{i}\right| \frac{\hat{p}_{i}+\hat{p}_{i+1}}{2}+\frac{\left|\hat{s}_{M}-\hat{s}_{1}\right|}{M-1} \frac{\hat{p}_{1}+\hat{p}_{M}}{2}\right)
$$

where $\tilde{\boldsymbol{S}}=\left\{\hat{s}_{1}, \hat{s}_{2}, \ldots, \hat{s}_{M}\right\}$, and $\tilde{\boldsymbol{P}}=\left\{\hat{p}_{1}, \hat{p}_{2}, \ldots, \hat{p}_{M}\right\}$.
For the large sample case, the estimated value set $\tilde{\boldsymbol{S}}$ will match the true value set $\boldsymbol{S}$ with probability one, i.e. $\operatorname{Pr}(\tilde{\boldsymbol{S}}=\boldsymbol{S})=1$, as $n \rightarrow \infty$. In fact, assume $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ is an i.i.d. sample from the distribution $\boldsymbol{P}$, and $p_{i}>0, i=1, \ldots, M$, we have

$$
\operatorname{Pr}(\tilde{\boldsymbol{S}} \neq \boldsymbol{S})=\sum_{i=1}^{M} \operatorname{Pr}\left(s_{i} \notin\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}\right)=\sum_{i=1}^{M}\left(\prod_{j=1}^{n} \operatorname{Pr}\left(X_{j} \neq s_{i}\right)\right)=\sum_{i=1}^{M}\left(1-p_{i}\right)^{n} \rightarrow 0 \text { as } n \rightarrow \infty
$$

In the following, we investigate the asymptotic behavior of the $\Delta$-entropy in random sampling. For tractability, we assume the value set $\boldsymbol{S}$ is known (or has been exactly estimated). Following the similar derivation of the asymptotic distribution for the $\phi$-entropy (see [24, Chapter 2]), we denote the parameter vector $\theta=\left(\theta_{1}, \theta_{2}, \ldots, \theta_{M-1}\right)^{T}=\left(p_{1}, p_{2}, \ldots, p_{M-1}\right)^{T}$, and rewrite (26) as

$$
\begin{aligned}
H_{\Delta}(\tilde{\theta})= & -\sum_{i=1}^{M-1} \hat{v}_{i} \log \hat{v}_{i}-\left(1-\sum_{j=1}^{M-1} \hat{v}_{j}\right) \log \left(1-\sum_{j=1}^{M-1} \hat{v}_{j}\right) \\
& +\log \left(\sum_{i=1}^{M-2}\left|s_{i+1}-s_{i}\right| \frac{\hat{v}_{i}+\hat{v}_{i+1}}{2}+\left|s_{M}-s_{M-1}\right| \frac{\hat{v}_{M-1}+\left(1-\sum_{j=1}^{M-1} \hat{v}_{j}\right)}{2}+\frac{\left|s_{M}-s_{1}\right|}{M-1} \frac{\hat{v}_{1}+\left(1-\sum_{j=1}^{M-1} \hat{v}_{j}\right)}{2}\right)
\end{aligned}
$$

The first order Taylor expansion of $H_{\Delta}(\widetilde{\theta})$ around $\theta$ gives

$$
H_{\Delta}(\widetilde{\theta})=H_{\Delta}(\theta)+\sum_{i=1}^{M-1} \frac{\partial H_{\Delta}(\theta)}{\partial \theta_{i}}\left(\hat{\theta}_{i}-\theta_{i}\right)+o\left(\|\widetilde{\theta}-\theta\|\right)
$$

where $\|\widetilde{\theta}-\theta\|=\sqrt{(\widetilde{\theta}-\theta)^{T}(\widetilde{\theta}-\theta)}$, and $\partial H_{\Delta}(\theta) / \partial \theta_{i}$ is calculated as

$$
\frac{\partial H_{\Delta}(\theta)}{\partial \theta_{i}}=\left\{\begin{array}{l}
-\log \theta_{i}+\log \left(1-\sum_{j=1}^{M-1} \theta_{j}\right)+\frac{s_{i-1}-s_{i-1}-\left(s_{M}-s_{M-1}\right)}{2 \Delta}-\frac{\left|s_{M}-s_{1}\right|}{2(M-1) \Delta}, \quad i \neq 1, M-1 \\
-\log \theta_{1}+\log \left(1-\sum_{j=1}^{M-1} \theta_{j}\right)+\frac{s_{2}-s_{1}-\left(s_{M}-s_{M-1}\right)}{2 \Delta}, \quad i=1 \\
-\log \theta_{M-1}+\log \left(1-\sum_{j=1}^{M-1} \theta_{j}\right)+\frac{s_{M-1}-s_{M-2}}{2 \Delta}-\frac{\left|s_{M}-s_{1}\right|}{2(M-1) \Delta}, \quad i=M-1
\end{array}\right.
$$

in which

$$
\Delta=\left(\sum_{i=1}^{M-2}\left|s_{i-1}-s_{i}\right| \frac{\hat{\theta}_{i}+\hat{\theta}_{i-1}}{2}+\left|s_{M}-s_{M-1}\right| \frac{\hat{\theta}_{M-1}+\left(1-\sum_{j=1}^{M-1} \theta_{j}\right)}{2}+\frac{\left|s_{M}-s_{1}\right|}{M-1} \frac{\hat{\theta}_{1}+\left(1-\sum_{j=1}^{M-1} \theta_{j}\right)}{2}\right)
$$

According to [24, Chapter 2], we have

$$
\sqrt{n}(\widetilde{\theta}-\theta) \frac{i}{n-\infty} N\left(0, I_{F}(\theta)^{-1}\right)
$$

where the inverse of the Fisher information matrix of $\theta$ is given by $I_{F}(\theta)^{-1}=\operatorname{diag}(\theta)-\theta \theta^{T}$. It follows that $\sqrt{n}\|\widetilde{\theta}-\theta\|$ is bounded in probability, and

$$
\sqrt{n}(o(\|\widetilde{\theta}-\theta\|))) \frac{P}{n-\infty} 0
$$

Therefore, the random variable $\sqrt{n}\left(H_{\Delta}(\widetilde{\theta})-H_{\Delta}(\theta)\right)$ and $\sqrt{n} \sum_{i=1}^{M-1} \frac{\partial H_{\Delta}(\theta)}{\partial \theta_{i}}\left(\hat{\theta}_{i}-\theta_{i}\right)$ have the same asymptotic distribution. Then the following theorem holds.

Theorem 9. The estimate $H_{\Delta}(\boldsymbol{S}, \widetilde{\boldsymbol{P}})$, obtained by replacing the $\left\{p_{i}\right\}$ by their relative frequencies $\left\{\tilde{p}_{i}\right\}$, in a random sample of size $n$, satisfies

$$
\sqrt{n}\left(H_{\Delta}(\boldsymbol{S}, \widetilde{\boldsymbol{P}})-H_{\Delta}(\boldsymbol{S}, \boldsymbol{P})\right) \frac{1}{n-\infty} N\left(0, \boldsymbol{U}^{\boldsymbol{T}} I_{F}(\boldsymbol{\theta})^{-1} \boldsymbol{U}\right)
$$

provided $\boldsymbol{U}^{\boldsymbol{T}} I_{F}(\boldsymbol{\theta})^{-1} \boldsymbol{U}>0$, where $\boldsymbol{\theta}=\left(p_{1}, p_{2}, \ldots, p_{M-1}\right)^{T}, I_{F}(\boldsymbol{\theta})^{-1}=\operatorname{diag}(\theta)-\theta \theta^{T}$, and

$$
\boldsymbol{U}=\left(\partial H_{\Delta}(\boldsymbol{\theta}) / \partial \theta_{1}, \partial H_{\Delta}(\boldsymbol{\theta}) / \partial \theta_{2}, \ldots, \partial H_{\Delta}(\boldsymbol{\theta}) / \partial \theta_{M-1}\right)^{T}
$$

where $\partial H_{\Delta}(\theta) / \partial \theta_{i}$ is calculated as (30).
Theorem 9 suggests that the $\Delta$-entropy can be effectively estimated from random samples by replacing the probabilities $\left\{p_{i}\right\}$ by their relative frequencies $\left\{\tilde{p}_{i}\right\}$.

It can also be shown that the plug-in estimate of the $\Delta$-entropy has close relationships with certain estimates of the differential entropy.

# 4.1. Relation to differential entropy estimate based on kernel density estimation 

Assume $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ are samples from a discrete random variable $X$, we rewrite the plug-in estimate (26) as

$$
H_{\Delta}(\widetilde{\boldsymbol{S}}, \widetilde{\boldsymbol{P}})=-\sum_{i=1}^{M} \tilde{p}_{i} \log \tilde{p}_{i}+\log \tilde{\Delta}
$$

where $\tilde{\Delta}=\sum_{i=1}^{M-1}\left|\tilde{s}_{i-1}-\tilde{s}_{i}\right| \frac{\tilde{p}_{i}+\tilde{p}_{i-1}}{2}+\frac{\left\|s_{M}-\tilde{s}_{1}\right\|}{M-1} \frac{\tilde{p}_{1}+\tilde{p}_{M}}{2}$.
Denote $\Delta_{\min }=\min _{i=1, \ldots, M-1}\left|\tilde{s}_{i-1}-\tilde{s}_{i}\right|$, and let $\tau=\tilde{\Delta} / \Delta_{\min }$, we construct another set of samples:

$$
\left\{x_{1}^{\prime}, x_{2}^{\prime}, \ldots, x_{n}^{\prime}\right\}=\left\{\tau x_{1}, \tau x_{2}, \ldots, \tau x_{n}\right\}
$$

which can be regarded as the samples from discrete random variable $\tau X$. It follows easily that

$$
\nabla x_{i}^{\prime} \neq x_{j}^{\prime}, \quad\left|x_{i}^{\prime}-x_{j}^{\prime}\right| \geqslant \tilde{\Delta}
$$

We now consider $\left\{x_{1}^{\prime}, x_{2}^{\prime}, \ldots, x_{n}^{\prime}\right\}$ as samples from a "continuous" random variable $X^{\prime}$. The PDF of $X^{\prime}$ can be estimated by the kernel approach [5]

$$
\hat{p}\left(x^{\prime}\right)=\frac{1}{n} \sum_{i=1}^{n} K\left(x^{\prime}-x_{i}^{\prime}\right)
$$

The kernel function $K: \mathbb{R} \rightarrow[0, \infty)$ satisfies $K \geqslant 0$ and $\int_{-\infty}^{\infty} K(x) d x=1$. Here we use the following uniform kernel:

$$
K_{\hat{A}}(x)= \begin{cases}1 / \hat{A}, & x \in[-\hat{A} / 2, \hat{A} / 2] \\ 0 & \text { otherwise }\end{cases}
$$

Then the kernel density estimation (KDE) of (39) becomes

$$
\hat{p}\left(x^{\prime}\right)=\frac{1}{n} \sum_{j=1}^{n} K_{\hat{A}}\left(x^{\prime}-x_{j}^{\prime}\right)=\frac{1}{n} \sum_{i=1}^{M} n_{i} K_{\hat{A}}\left(x^{\prime}-x_{i}^{\prime}\right) \stackrel{( \circ ) { ( } { ) } { \pm } \stackrel{p_{i}}{\rightarrow}, x^{\prime} \in\left[x_{i}^{\prime}-\hat{A} / 2, x_{i}^{\prime}+\hat{A} / 2\right]$
where (a) follows from $\hat{p}_{i}=n_{i} / n$, and $\forall x_{i}^{\prime} \neq x_{j}^{\prime},\left|x_{i}^{\prime}-x_{j}^{\prime}\right| \geqslant \hat{A}$. The differential entropy of $X^{\prime}$ can be estimated by the plug-in approach:

$$
\begin{aligned}
\hat{h}\left(X^{\prime}\right) & =-\int_{-\infty}^{\infty} \hat{p}\left(x^{\prime}\right) \log \hat{p}\left(x^{\prime}\right) d x^{\prime}=-\sum_{i=1}^{M} \int_{x_{i}^{\prime}-\hat{A} / 2}^{x_{i}^{\prime}+\hat{A} / 2} \hat{p}\left(x^{\prime}\right) \log \hat{p}\left(x^{\prime}\right) d x^{\prime}=-\sum_{i=1}^{M} \int_{x_{i}^{\prime}-\hat{A} / 2}^{x_{i}^{\prime}+\hat{A} / 2} \frac{p_{i}}{\hat{A}} \log \frac{p_{i}}{\hat{A}} d x^{\prime} \\
& =-\sum_{i=1}^{M} p_{i} \log p_{i}+\log \hat{A}=H_{\hat{A}}(\widehat{\mathbf{S}}, \widehat{\boldsymbol{P}})
\end{aligned}
$$

As a result, the plug-in estimate of the $\Delta$-entropy equals a uniform kernel based estimate for the differential entropy from the scaled samples (37).

# 4.2. Relation to differential entropy estimate based on sample-spacing 

It is also interesting to note that the plug-in estimate of the $\Delta$-entropy has a close connection with the sample-spacing estimate $[23,34]$ of differential entropy. Suppose the sample data are different from each other, and have been rearranged in an increasing order: $\left\{x_{1}<x_{2}<\cdots<x_{n}\right\}$, the $m$-spacing estimate is given by [23]

$$
\hat{h}_{m}(X)=\frac{1}{n} \sum_{i=1}^{n-m} \log \left(\frac{n}{m}\left(x_{i+m}-x_{i}\right)\right)
$$

where $m \in \mathbb{N}$, and $m<n$. Let $m=1$, we obtain the 1 -spacing estimate:

$$
\hat{h}_{1}(X)=\frac{1}{n} \sum_{i=1}^{n-1} \log \left(n\left(x_{i+1}-x_{i}\right)\right)
$$

In general, regarding $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ as samples from a discrete distribution, we estimate the value set and probabilities as

$$
\left\{\begin{array}{l}
\widehat{\mathbf{S}}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \\
\widehat{\boldsymbol{P}}=(1 / n, 1 / n, \ldots, 1 / n)
\end{array}\right.
$$

Then the plug-in estimate of $\Delta$-entropy can be calculated as

$$
H_{\hat{A}}(\widehat{\mathbf{S}}, \widehat{\boldsymbol{P}})=-\sum_{i=1}^{n} \frac{1}{n} \log \frac{1}{n}+\log \left(\sum_{i=1}^{n-1}\left(x_{i+1}-x_{i}\right) \frac{1}{n}+\frac{\left(x_{n}-x_{1}\right)}{n-1} \frac{1}{n}\right)
$$

It follows that

$$
\begin{aligned}
H_{\hat{A}}(\widehat{\mathbf{S}}, \widehat{\boldsymbol{P}}) & =-\underset{i=1}{m} \frac{1}{n} \log \frac{1}{n}+\log \left(\sum_{i=1}^{n-1}\left(x_{i+1}-x_{i}\right) \frac{1}{n}+\frac{\left(x_{n}-x_{1}\right)}{n-1} \frac{1}{n}\right) \stackrel{( \circ ) { ( } { ( ) ) } { \geq } \frac { ( 1 ) } { n } \sum_{i=1}^{n} \log n \\
& +\frac{1}{n}\left(\sum_{i=1}^{n-1} \log \left(x_{i+1}-x_{i}\right)+\log \frac{\left(x_{n}-x_{1}\right)}{n-1}\right) \\
& =\frac{1}{n} \sum_{i=1}^{n-1} \log \left(n\left(x_{i+1}-x_{i}\right)\right)+\frac{1}{n} \log \frac{n\left(x_{n}-x_{1}\right)}{n-1}=\hat{h}_{1}(X)+\frac{1}{n} \log \frac{n\left(x_{n}-x_{1}\right)}{n-1}
\end{aligned}
$$

where (a) follows from the concavity of the logarithm function. If $\left\{x_{i}\right\}$ is bounded, we have

![img-1.jpeg](img-1.jpeg)

Fig. 2. System identification with quantized I/O data.

$$
\lim _{n \rightarrow \infty} H_{\Delta}(\tilde{\boldsymbol{S}}, \tilde{\boldsymbol{P}}) \geqslant \lim _{n \rightarrow \infty}\left(\tilde{h}_{1}(X)+\frac{1}{n} \log \frac{n\left(x_{0}-x_{1}\right)}{n-1}\right)=\lim _{n \rightarrow \infty} \tilde{h}_{1}(X)
$$

In this case, the plug-in estimate of $\Delta$-entropy provides an asymptotic upper bound to the 1 -spacing entropy estimate.

# 5. Application to system identification with quantized data 

As $\Delta$-entropy measures both the probabilistic uncertainty and the dispersion of a discrete random variable, it can be used as an optimality criterion in system identification where the error signal is distributed on an unknown (and varying with iterations) countable value set.

Consider the system identification scheme with quantized I/O data, as shown in Fig. 2, in which $f(\cdot)$ and $h(\cdot, W)$ denote the unknown system and the parametric model respectively, $W=\left\{w_{1}, \ldots, w_{d}\right\}^{\mathrm{T}}$ is the $d$-dimensional parameter vector (weight vector) of the model. $x(k)$ and $z(k)$ are the actual input and output signals (usually continuous-valued) of the unknown system at $k$ time; $n(k)$ is the additive noise and $d(k)$ the noisy output. $\bar{x}(k)$ and $\bar{d}(k)$ represent the quantized I/O observations, which are obtained via quantizers $Q_{i}$ and $Q_{o}$. With uniform quantization box-sizes $q_{i}$ and $q_{o}, \bar{x}(k)$ and $\bar{d}(k)$ are given by

$$
\left\{\begin{array}{l}
\bar{x}(k)=\left\lceil x(k) / q_{i}+1 / 2\right\rceil \times q_{i} \\
\bar{d}(k)=\left\lceil d(k) / q_{o}+1 / 2\right\rceil \times q_{o}
\end{array}\right.
$$

where $|x|$ gives the largest integer that is less than or equal to $x$.
The error signal $e(k)$ is calculated as

$$
e(k)=\bar{d}(k)-y(k)
$$

where $y(k)$ is the output of the model driven by quantized data $\bar{x}(k)$. Now the problem is to identify the unknown system using the quantized I/O data $\{(\bar{x}(k), \bar{d}(k)), k=1,2, \ldots, L\}$.

In the above identification setting, the error $e(k)$ will be discrete-valued, and hence the $\Delta$-entropy can be used as the training cost. The optimum parameters of the model would be

$$
W_{\text {opt }}=\underset{W \in \boldsymbol{W}}{\arg \min } H_{\Delta}(e)
$$

where $\boldsymbol{W} \subset \mathbb{R}^{d}$ denotes the parameter space. That is, we propose to determine the model parameters by minimizing the $\Delta$-entropy of the discrete-valued error residuals. ${ }^{2}$

In a practical application, $\Delta$-entropy cannot be in general analytically computed, since the error's values and corresponding probabilities are unknown. We need to estimate the $\Delta$-entropy by the plug-in method as discussed in the previous section. Therefore, the optimization of (51) becomes

$$
W_{\text {opt }}=\underset{W \in \boldsymbol{W}}{\arg \min } H_{\Delta}\left(\tilde{\boldsymbol{S}}^{(e)}, \tilde{\boldsymbol{P}}^{(e)}\right)
$$

where $\tilde{\boldsymbol{S}}^{(e)}=\left(\bar{s}_{1}^{(e)}, \bar{s}_{2}^{(e)}, \ldots, \bar{s}_{M}^{(e)}\right)$ and $\tilde{\boldsymbol{P}}^{(e)}=\left(\bar{p}_{1}^{(e)}, \bar{p}_{2}^{(e)}, \ldots, \bar{p}_{M}^{(e)}\right)$ denote the estimated value-set of the error and the corresponding relative frequencies.

The classical gradient based methods cannot be used to solve the optimization problem of (52), since the objective function $H_{\Delta}\left(\tilde{\boldsymbol{S}}^{(e)}, \tilde{\boldsymbol{P}}^{(e)}\right)$ is usually not differentiable. So we have to resort to other methods such as evolutionary algorithms (EAs), although they are usually more computationally complex. Here we adopt the estimation of distribution algorithms (EDAs)

[^0]
[^0]:    ${ }^{2}$ For the case in which the underlying distribution of the error residual is continuous, we can still use the $\Delta$-entropy as the optimization criterion if we classify the errors into groups and obtain the quantized error data.

[16], which is a new class of EAs. The EDAs use the probability model built from the objective function to generate the promising search points instead of crossover and mutation as done in traditional genetic algorithms (GAs). Compared with other EAs, the EDAs may achieve better evolutionary performances [12,19,30]. Some theoretical results related to the convergence and time complexity of the EDAs can be found in [3,11,29,39].

Based on Delta-entropy and EDAs, we propose the parameter search algorithm as summarized in Table 1.
Usually, we use a Gaussian model with diagonal covariance matrix (GM/DCM) [16] to estimate the density function $f_{g}(W)$ of the $g$ th generation. With GM/DCM model, we have

$$
f_{g}(W)=\prod_{j=1}^{d} \frac{1}{\sqrt{2 \pi} \sigma_{j}^{(g)}} \exp \left(-\left(w_{j}-\mu_{j}^{(g)}\right)^{2} /\left(2\left(\sigma_{j}^{(g)}\right)^{2}\right)\right)
$$

where the means $\mu_{j}^{(g)}$ and the deviations $\sigma_{j}^{(g)}$ can be estimated as

$$
\left\{\begin{array}{l}
\mu_{j}^{(g)}=\frac{1}{N} \sum_{l=1}^{N} W_{R(l)}^{(g-1)}(j) \\
\sigma_{j}^{(g)}=\sqrt{\frac{1}{N} \sum_{l=1}^{N}\left(W_{R(l)}^{(g-1)}(j)-\mu_{j}^{(g)}\right)^{2}}
\end{array}\right.
$$

We now perform a series of Monte-Carlo simulations of system identification based on quantized I/O data to demonstrate the performance of EDAs with $\Delta$-entropy criterion. In all of the experiments below, we set the quantization box-sizes $q_{i}=$ $q_{o}=q$. For the EDAs, we set $R=100$ and $N=30$.

# 5.1. Comparison with other optimality criteria 

We will contrast the performances of $\Delta$-entropy criterion and several other optimality criteria by using EDAs as parameter search algorithm. Consider the linear system identification case, in which we assume the unknown system and the parametric model are both two-tap FIR filters, that is

$$
\left\{\begin{array}{l}
z(k)=w_{1}^{\prime} x(k)+w_{2}^{\prime} x(k-1) \\
y(k)=w_{1} \bar{x}(k)+w_{2} \bar{x}(k-1)
\end{array}\right.
$$

Here we set the true weight vector of the unknown system $W^{\prime}=[1.0,0.5]^{T}$, and the initial weight vector of FIR model $W_{( }^{( } 0)=[0,0]^{T}$. In addition, we assume the input signal $\{x(k)\}$ and the additive noise $\{n(k)\}$ are both white Gaussian processes with variances 1.0 and 0.04 , respectively. The length of training data is $L=500$.

First, we compare the performances of three entropy criteria: $\Delta$-entropy, differential entropy ${ }^{3}$ and discrete entropy, using the same adaptation method. For different entropy criteria and different quantization box-sizes, the average evolution curves of weight error norm ( $\left.\|W^{\prime \prime}-W\right\|$ ) over 100 Monte Carlo runs are shown in Fig. 3. Evidently, the $\Delta$-entropy criterion achieves the best performance with the fastest convergence speed and the smallest error (weight error norm) at the final stage of learning. Further, we have two observations: (1) the discrete entropy criterion fails to converge as seen from the evolution of the learning curves, which agrees with the fact that the discrete entropy cannot constrain the error's dispersion; (2) the performance (especially final bias) of the differential entropy approaches that of the $\Delta$-entropy when the quantization box-size $q$ becomes smaller. This result agrees with the limiting relationship between the $\Delta$-entropy and differential entropy.

In order to compare the error dispersions, we plot in Fig. 4 the probability mass functions of the error samples for different entropy criteria ( $q=1.0$ ). Here the error samples are obtained using 500 test data after training the model. From Fig. 4, it is clear that the $\Delta$-entropy produces the most concentrated error samples, while the discrete entropy yields errors with the largest dispersion. The average intervals (calculated as (15)) of error samples for the $\Delta$-entropy, differential entropy and discrete entropy are $0.0068,0.0097$ and 0.0622 , respectively.

The performance of $\Delta$-entropy criterion is also compared with that of the MSE criterion, with the same experimental setup. As one can see in Fig. 5, the $\Delta$-entropy achieves again significantly smaller bias at the final stage of evolution, although its convergence speed is slightly slower than that of the MSE criterion.

### 5.2. Comparison with LMS and SIG algorithms

In the following we will contrast the performances of the $\Delta$-entropy based EDA, LMS, and SIG (stochastic information gradient) algorithm [9] in a 4-tap FIR identification problem. The LMS and SIG are stochastic gradient based algorithms under MSE and MEE criterion respectively, so they both display a performance penalty called the misadjustment that is proportional to the stepsize utilized, while EDA is immune to this phenomenon. So the difference in algorithm performance cannot be only allotted to the difference in cost functions. The true weight vector of the unknown system is set as $W^{\prime \prime}=[-0.2,0.9$, $0.7,-0.5]^{T}$. The input signal $\{x(k)\}$ is white and uniformly distributed on the interval $[-2,2]$ with data length $L=2000$. The

[^0]
[^0]:    ${ }^{3}$ Strictly speaking, the differential entropy criterion is invalid in this example, because the observed error is a discrete random variable. However, in the simulation, we can still use the $m$-spacing estimator of differential entropy.

Table 1
EDAs based parameter search algorithm with $\Lambda$-entropy criterion.

1. BEGIN
2. Generate $R$ individuals $A_{0}=\left\{W_{1}^{(0)}, W_{2}^{(0)}, \ldots, W_{R}^{(0)}\right\}$ randomly from parameter space $\boldsymbol{W}, g \leftarrow 0$
3. WHILE the final stopping criterion is not met DO
4. $g \leftarrow g * 1$
5. For each parameter vector in $A_{g-1}$, estimate the error's $\Lambda$-entropy using a training data set $\{(\bar{x}(k), \hat{d}(k))\}$
6. Select $N(N \leqslant R)$ promising individuals $B_{g}=\left\{W_{R(1)}^{(g-1)}, W_{R(2)}^{(g-1)}, \ldots, W_{R(m)}^{(g-1)}\right\}$ from $A_{g-1}$ according to the truncation selection method (using $\Lambda$-entropy as the fitness function) ${ }^{a}$
7. Estimate the probability density function $f_{g}(W)$ based on the statistical information extracted from the selected $N$ individuals $B_{g}$
8. Sample $R$ individuals $A_{g}=\left\{W_{1}^{(g)}, W_{2}^{(g)}, \ldots, W_{R}^{(g)}\right\}$ from $f_{g}(W)$
9. END WHILE
10. Calculate the estimated parameter: $W(g)=(1 / N) \sum_{n=1}^{R} W_{R(n)}^{(g-1)}$
11. END
[^0]additive noise $\{n(k)\}$ is a white Gaussian process with variance $\sigma_{n}^{2}=0.01$ or 0.25 . In the simulations, the step-sizes (and the kernel size for SIG) of the two gradient algorithms are adjusted so as to produce the least weight error norm. Fig. 6 shows the histograms of error norm at the final stage of system training based on 100 Monte Carlo experiments. The inset plots in Fig. 6 give the summary of the mean and the spread of the histograms for each algorithm. Clearly, the EDA (with $\Lambda$-entropy criterion) outperforms both the LMS and SIG algorithms in terms of final bias, especially for the case of coarser quantization ${ }^{a}$ $(q=1.0)$. It should be noted that although the EDA (with $\Lambda$-entropy criterion) can achieve significant improvements in the weight bias, it is much more computationally intensive than LMS and SIG algorithms. A runtime comparison shows that, for $q=1.0$ case, the proposed method took on average 39 s to complete a single Monte Carlo run (with 15 generations), while the LMS and SIG only took 0.02 and 0.18 s , respectively (with 2000 iterations).

### 5.3. Comparison with TLS, EWC and IV methods

Considering the quantization noises, the system identification scheme of Fig. 2 is actually an errors-in-variables (EIV) identification problem where both input and output are corrupted by noises [32]. In this example, we will compare the proposed method with the total least squares (TLS), error whitening criterion (EWC) [28] and the instrumental variables (IV) method, which under certain conditions give an unbiased estimate in identification of the EIV model. Assume the unknown system is a 6 -tap FIR system with $W^{*}=[-0.6,0.4,0.8,0.6,0.3,-0.5]^{T}$. The input signal is a first-order AR process given by

$$
x(k)=0.2 x(k-1)+\varepsilon(k)
$$

where $\varepsilon(k)$ is a white Gaussian noise with unit variance. The additive noise $\{n(k)\}$ is a white Gaussian process with variance $\sigma_{n}^{2}=0.04$. Further, the quantization box-size is $q=1.0$ and the length of training data $L=2000$. For the TLS, we use the recursive algorithm derived in [9] to obtain the solution. For the EWC, we adopt the stochastic gradient based algorithm, i.e. EWCLMS [28]. For the IV method, we choose the delayed input vector as the instrument. The histograms of weight error norm for 100 Monte Carlo simulations are shown in Fig. 7, from which we see that the new approach outperforms the EWC and IV methods and achieves estimation accuracy comparable to that of TLS which, however, requires some a priori information on the noise statistics.

### 5.4. Nonlinear system identification case

Consider a nonlinear system identification case, in which we assume the unknown system and parametric model are both second-order polynomial basis function networks (second-order Volterra systems with 2-sample memory), that is

$$
\left\{\begin{array}{l}
z(k)=w_{1}^{\prime}+w_{2}^{\prime} x(k)+w_{3}^{\prime} x(k-1)+w_{4}^{\prime} x^{2}(k)+w_{5}^{\prime} x(k) x(k-1)+w_{6}^{\prime} x^{2}(k-1) \\
y(k)=w_{1}+w_{2} \bar{x}(k)+w_{3} \bar{x}(k-1)+w_{4} \bar{x}^{2}(k)+w_{5} \bar{x}(k) \bar{x}(k-1)+w_{6} \bar{x}^{2}(k-1)
\end{array}\right.
$$

Let the weight vector of unknown system be $W^{*}=[0.5,0.8,-0.6,0.2,-0.7,0.1]^{T}$, and assume that the input signal, additive noise and training data length are the same as the previous example. As $\Lambda$-entropy is shift invariant (see Theorem 5), during simulation the bias weight $w_{1}$ is adjusted so as to yield zero-mean error.

First we set $q=0.5$ and compare again the performance of the EDA (with $\Lambda$-entropy criterion), LMS and SIG algorithms. The histogram shown in Fig. 8 indicates that the new method still performs best in terms of bias (measured by the weight

[^1]
[^0]:    ${ }^{a}$ The truncation selection is a widely-used selection method in EDAs. In the truncation selection, individuals are sorted according to their objective function (or fitness function) values and only the best individuals are selected.
[^1]:    ${ }^{a}$ The coarse quantization frequently occurs in many practical systems. For example, in the wireless sensor networks (WSN), the cheap sensors might produce very roughly quantized measurements (less than 8 bit) due to energy consumption constraint or very limited data communication rate.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Evolution curves of weight error norm for different entropy criteria and different quantization box-sizes.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Probability mass functions of errors for three entropy criteria: (a) $\Delta$-entropy, (b) differential entropy, and (c) discrete entropy.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Evolution curves of weight error norm for $\Delta$-entropy and MSE criterion.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Histogram plots of the weight error norm for LMS, SIG and the EDA with $\Delta$-entropy criterion.
error norm). This result can also be confirmed by Fig. 9, in which the probability density functions of the intrinsic errors are plotted. Here the intrinsic error is defined as

![img-6.jpeg](img-6.jpeg)

Fig. 7. Histogram plots of the weight error norm for TLS, EWC, IV method and the EDA with $\Delta$-entropy criterion.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Histogram plots of the weight error norm for LMS, SIG and the EDA with $\Delta$-entropy criterion (nonlinear system case).

$$
\hat{e}(k)=z(k)-\bar{y}(k)
$$

where $\bar{y}(k)$ denotes the output of the model (after training) driven by the unquantized input signal $\{x(k)\}$, that is

$$
\bar{y}(k)=w_{1}+w_{2} x(k)+w_{3} x(k-1)+w_{4} x^{2}(k)+w_{5} x(k) x(k-1)+w_{6} x^{2}(k-1)
$$

As shown in Fig. 9, the EDA ( $\Delta$-entropy) produces the largest and most concentrated peak centered at the zero intrinsic error.
In order to further evaluate the performance of the new approach, we also compare it with a recently proposed method by Ozertem and Erdogmus [22] which under certain conditions provides an unbiased estimate of the true parameters of an or-der-2 Volterra model with noisy input-output measurements. Similar to [22], we use the angle between the estimated and the actual weight vector (coefficient vector) as the performance metric. Fig. 10 shows the angles averaged over 100 Monte Carlo simulations for the two approaches for different quantization box-sizes. One can see clearly that our approach achieves much smaller angles.

Remark 6. Our previous simulations show that the proposed $\Delta$-entropy criterion performs better than the existing criteria like MSE and MEE. One intuitive reason for this is that, minimizing the $\Delta$-entropy will decrease both the probabilistic uncertainty and the average interval, which enforces the residual errors to concentrate. A more rational explanation for this performance improvement is given in Appendix D, wherein we also report some supplementary simulation results.

# 6. Conclusion remarks 

The minimum error entropy (MEE) criterion applied to discrete data minimizes statistical uncertainty in the error PDF but fails to constrain the error's dispersion, which penalizes performance. To address this problem, we develop a new definition

![img-8.jpeg](img-8.jpeg)

Fig. 9. Probability density functions of the intrinsic errors produced by three algorithms.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Angles (degrees) between the estimated and the actual weight vector.
of entropy for discrete random variables, called $\Lambda$-entropy. Inspired by the connection between differential and discrete entropies, we define the $\Lambda$-entropy as the sum of the discrete entropy and the logarithm of average interval between two successive values, in which the first term measures the probabilistic uncertainty, and the second term measures the dispersion in the error variable.

The $\Lambda$-entropy has strong links both with differential entropy and discrete entropy, acting as a bridge between the differential and the discrete entropy, but when evaluated for a given analytic distribution its value will differ from them. However, when entropy is estimated directly from data, it is interesting that the plug-in estimate of the $\Lambda$-entropy ties in closely with the kernel based and $m$-spacing based estimates of the differential entropy. Specifically, the plug-in estimate of the $\Lambda$-entropy equals a uniform kernel based entropy estimate from the scaled samples, and establishes an asymptotic upper bound to the 1 -spacing entropy estimate. Further work is necessary to establish the role of $\Lambda$-entropy as an estimator for differential entropy.

As the $\Lambda$-entropy measures both the probabilistic uncertainty and dispersion of the random variable, its role as a cost function in adaptation of linear or nonlinear systems with discretized inputs and desired responses is much clearer and has been validated in this study. At present, however, the gradient based algorithms have not been derived since the objective function is not differentiable. In this work, the estimation of distribution algorithm (EDA) is used as the parameter search algorithm, despite the increase in computational cost. Monte Carlo simulations are performed for the system identification with quantized input-output data. Simulation results confirm that the $\Lambda$-entropy criterion may achieve a significant improvement in estimation accuracy.

As a new entropy definition, the $\Lambda$-entropy will find applications in many other fields. Potential applications lie particularly in machine learning and signal processing with discrete-valued data. Typical examples are: (1) count data time-series modeling and prediction; (2) channel equalization in digital transmission and (3) blind separation of discrete-valued sources. Exploring these applications will be the goal of future research.

# Acknowledgements 

This work was partially supported by NSF Grant ECCS 0856441, NSF IIS 0964197 and ONR N00014-10-1-0375, and National Natural Science Foundation of China (No. 60904054), National Key Basic Research and Development Program (973) of China (No. 2009CB724205).

## Appendix A

Proof of theorem 1. Combining (6) and (17), we have

$$
\begin{aligned}
H_{\Delta}\left(X^{\Delta}\right) & =-\sum_{i=-\infty}^{\infty} f\left(s_{i}\right) \Delta \log \left(f\left(s_{i}\right) \Delta\right)+\log \left(\sum_{i=-\infty}^{\infty}\left|s_{i+1}-s_{i}\right| \frac{f\left(s_{i}\right) \Delta+f\left(s_{i+1}\right) \Delta}{2}+\lim _{N \rightarrow \infty} \frac{\left|s_{N}-s_{-N}\right| \frac{f\left(s_{-N}\right) \Delta+f\left(s_{N}\right) \Delta}{2}}{2}\right) \\
& =-\sum_{i=-\infty}^{\infty} \Delta f\left(s_{i}\right) \log f\left(s_{i}\right)+\log \left(\sum_{i=-\infty}^{\infty}\left|s_{i+1}-s_{i}\right| \frac{f\left(s_{i}\right)+f\left(s_{i+1}\right)}{2}\right)
\end{aligned}
$$

As $f(x)$ is Riemann integrable, it follows that

$$
\lim _{\Delta \rightarrow 0} H_{\Delta}\left(X^{\Delta}\right)=-\int_{-\infty}^{\infty} f(x) \log f(x) d x+\log \left(\int_{-\infty}^{\infty} f(x) d x\right)=-\int_{-\infty}^{\infty} f(x) \log f(x) d x=\hbar(X)
$$

which completes the proof.

## Appendix B

Proof of theorem 4. It is easy to derive

$$
\operatorname{Var}(X)=\sum_{i=1}^{M}\left(s_{i}-\bar{s}\right)^{2} p_{i} \leqslant \sum_{i=1}^{M}\left(s_{i}-\frac{s_{M}+s_{1}}{2}\right)^{2} p_{i} \leqslant \sum_{i=1}^{M}\left(s_{M}-\frac{s_{M}+s_{1}}{2}\right)^{2} p_{i}=\frac{1}{4}\left(s_{M}-s_{1}\right)^{2}
$$

It follows that $\left|s_{M}-s_{1}\right| \geqslant 2 \sqrt{\operatorname{Var}(X)}$, and hence

$$
\begin{aligned}
H_{\Delta}(X) & \geqslant \log \left(\sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| \frac{p_{i}+p_{i+1}}{2}+\frac{\left|s_{M}-s_{1}\right|}{M-1} \frac{p_{1}+p_{M}}{2}\right) \geqslant \log \left(\sum_{i=1}^{M-1}\left|s_{i+1}-s_{i}\right| p_{\min }+\frac{\left|s_{M}-s_{1}\right|}{M-1} p_{\min }\right) \\
& =\log \left(\frac{M\left|s_{M}-s_{1}\right|}{M-1} p_{\min }\right) \geqslant \log \left(\frac{2 M \sqrt{\operatorname{Var}(X)}}{M-1} p_{\min }\right)=\log \left(\frac{2 M p_{\min }}{M-1}\right)+\frac{1}{2} \log (\operatorname{Var}(X))
\end{aligned}
$$

## Appendix C

Proof of theorem 7. $\forall \boldsymbol{P}_{1}=\left(p_{1}^{(1)}, p_{2}^{(1)}, \ldots, p_{M}^{(1)}\right), \boldsymbol{P}_{2}=\left(p_{1}^{(2)}, p_{2}^{(2)}, \ldots, p_{M}^{(2)}\right)$, and $\forall 0 \leqslant \lambda \leqslant 1$, we have

$$
\Delta\left(\boldsymbol{S}, \lambda \boldsymbol{P}_{1}+(1-\lambda) \boldsymbol{P}_{2}\right)=\lambda \Delta\left(\boldsymbol{S}, \boldsymbol{P}_{1}\right)+(1-\lambda) \Delta\left(\boldsymbol{S}, \boldsymbol{P}_{2}\right)
$$

By the concavity of the logarithm function, we get

$$
\log \left(\Delta\left(\boldsymbol{S}, \lambda \boldsymbol{P}_{1}+(1-\lambda) \boldsymbol{P}_{2}\right)\right) \geqslant \lambda \log \left(\Delta\left(\boldsymbol{S}, \boldsymbol{P}_{1}\right)\right)+(1-\lambda) \log \left(\Delta\left(\boldsymbol{S}, \boldsymbol{P}_{2}\right)\right)
$$

Further, it is well-known the discrete entropy $H(\boldsymbol{P})$ is a concave function of the distribution $\boldsymbol{P}$, that is

$$
H\left(\lambda \boldsymbol{P}_{1}+(1-\lambda) \boldsymbol{P}_{2}\right) \geqslant \lambda H\left(\boldsymbol{P}_{1}\right)+(1-\lambda) H\left(\boldsymbol{P}_{2}\right), \quad \forall 0 \leqslant \lambda \leqslant 1
$$

Combining (B.2) and (B.3), we have

$$
H_{\Delta}\left(\boldsymbol{S}, \lambda \boldsymbol{P}_{1}+(1-\lambda) \boldsymbol{P}_{2}\right) \geqslant \lambda H_{\Delta}\left(\boldsymbol{S}, \boldsymbol{P}_{1}\right)+(1-\lambda) H_{\Delta}\left(\boldsymbol{S}, \boldsymbol{P}_{2}\right)
$$

which implies $\Delta$-entropy is a concave function of $\boldsymbol{P}$.

## Appendix D

## D.1. An explanation for the satisfactory performance of the $\Delta$-entropy criterion

Here we give an explanation on why $\Delta$-entropy criterion performs well in system identification. To clarify the analysis, we consider the errors-in-variables (EIV) case in which the input signal $\{x(k)\}$, input noise $\left\{n_{1}(k)\right\}$, and the output noise

$\left\{n_{2}(k)\right\}$ are all discrete-valued data with finite value-sets. Further, we assume the unknown system and the parametric model are both $m$-tap FIR filters, that is

$$
\left\{\begin{array}{l}
G^{*}(z)=\sum_{i=1}^{m} w_{i}^{z} z^{-i+1} \\
G(z)=\sum_{i=1}^{m} w_{i} z^{-i+1}
\end{array}\right.
$$

where $G_{*}(z)$ and $G(z)$ denote the transfer functions of the unknown system and the model, respectively. In this case, the error signal $e(k)$ is

$$
e(k)=\sum_{i=1}^{m}\left(w_{i}^{z}-w_{i}\right) x(k-i+1)-\sum_{i=1}^{m} w_{i} n_{1}(k-i+1)+n_{2}(k)=\bar{e}(k)+\bar{e}(k)
$$

where $\bar{e}(k)$ and $\bar{n}(k)$ stand for the intrinsic error and the "equivalent output noise", i.e.

$$
\left\{\begin{array}{l}
\bar{e}(k)=\sum_{i=1}^{m}\left(w_{i}^{z}-w_{i}\right) x(k-i+1) \\
\bar{n}(k)=-\sum_{i=1}^{m} w_{i} n_{1}(k-i+1)+n_{2}(k)
\end{array}\right.
$$

Let the value-sets and the probability distributions of $\bar{e}(k)$ and $\bar{n}(k)$ be

$$
\left\{\begin{array}{l}
\boldsymbol{S}^{(\bar{e})}=\left(s_{1}^{(\bar{e})}, s_{2}^{(\bar{e})}, \ldots, s_{M_{1}}^{(\bar{e})}\right) \\
\boldsymbol{S}^{(\bar{n})}=\left(s_{1}^{(\bar{n})}, s_{2}^{(\bar{n})}, \ldots, s_{M_{2}}^{(\bar{n})}\right)
\end{array}\right.
$$

and

$$
\left\{\begin{array}{l}
\boldsymbol{P}^{(\bar{e})}=\left(p_{1}^{(\bar{e})}, p_{2}^{(\bar{e})}, \ldots, p_{M_{1}}^{(\bar{e})}\right) \\
\boldsymbol{P}^{(\bar{n})}=\left(p_{1}^{(\bar{n})}, p_{2}^{(\bar{n})}, \ldots, p_{M_{2}}^{(\bar{n})}\right)
\end{array}\right.
$$

Then we have $\Delta(e(k)) \approx \Delta(\bar{e}(k))$, provided the following assumptions hold:

# Assumption 1 

$\bar{e}(k)$ is independent of $\bar{n}(k)$.
Assumption 2. $\bar{e}(k)$ is small enough such that $|\bar{e}(k)|<\frac{1}{2}\left(\min _{j=1,2, \ldots, M_{2}-1}\left|s_{j-1}^{(\bar{e})}-s_{j}^{(\bar{e})}\right|\right)$.

Assumption 3. The probabilities of the extreme values of $\bar{e}(k)$ are nearly zero, that is, $p_{1}^{(\bar{e})} \approx 0, p_{M_{1}}^{(\bar{e})} \approx 0$.
Assumption 1 will be valid if the input signal $\{x(k)\}$ is independent of the noises $\left\{n_{1}(k)\right\}$ and $\left\{n_{2}(k)\right\}$. Assumption 2 will hold if the model weight vector $W$ is close enough to the true weight vector $W^{*}$. Assumption 3 is reasonable for most practical distributions.

Under Assumptions 1 and 2, the value-set and probability distribution of $e(k)$ will be

Table 2
Mean $\pm$ deviation results of $w_{1}$ and $w_{2}$ at the 10th EDA generation for different $\sigma_{n_{1}}\left(\sigma_{n_{2}}=0.1\right)$.

| $\sigma_{n_{1}}$ | $\Delta$-entropy |  | MSE |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $w_{1}$ | $w_{2}$ | $w_{1}$ | $w_{2}$ |
| 0.1 | $1.0000 \pm 0.0008$ | $0.4999 \pm 0.0007$ | $0.9896 \pm 0.0071$ | $0.4952 \pm 0.0067$ |
| 0.2 | $0.9997 \pm 0.0015$ | $0.4995 \pm 0.0015$ | $0.9609 \pm 0.0098$ | $0.4800 \pm 0.0097$ |
| 0.3 | $0.9994 \pm 0.0016$ | $0.4993 \pm 0.0017$ | $0.9192 \pm 0.0118$ | $0.4617 \pm 0.0140$ |
| 0.4 | $0.9991 \pm 0.0019$ | $0.4991 \pm 0.0019$ | $0.8629 \pm 0.0129$ | $0.4316 \pm 0.0163$ |
| 0.5 | $0.9980 \pm 0.0039$ | $0.4972 \pm 0.0077$ | $0.8015 \pm 0.0146$ | $0.4016 \pm 0.0200$ |

Table 3
Mean $\pm$ deviation results of $w_{1}$ and $w_{2}$ at the 10th EDA generation for different $\sigma_{n_{1}}\left(\sigma_{n_{1}}=0.1\right)$.

| $\sigma_{n_{1}}$ | $\Delta$-entropy |  | MSE |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $w_{1}$ | $w_{2}$ | $w_{1}$ | $w_{2}$ |
| 0.1 | $1.0000 \pm 0.0008$ | $0.4999 \pm 0.0007$ | 0.9896 $\pm 0.0071$ | $0.4952 \pm 0.0067$ |
| 0.2 | $0.9999 \pm 0.0009$ | $0.4999 \pm 0.0008$ | $0.9887 \pm 0.0096$ | $0.4949 \pm 0.0089$ |
| 0.3 | $0.9999 \pm 0.0012$ | $0.4998 \pm 0.0011$ | $0.9908 \pm 0.0139$ | $0.4943 \pm 0.0142$ |
| 0.4 | $0.9999 \pm 0.0020$ | $0.4998 \pm 0.0017$ | $0.9880 \pm 0.0192$ | $0.4948 \pm 0.0208$ |
| 0.5 | $1.0001 \pm 0.0039$ | $0.4998 \pm 0.0024$ | $0.9926 \pm 0.0231$ | $0.4946 \pm 0.0235$ |

$$
\left\{\begin{array}{l}
\boldsymbol{S}^{(e)}=\left(s_{1}^{(e)}, s_{2}^{(e)}, \ldots, s_{M_{1} M_{2}}^{(e)}\right) \\
\boldsymbol{p}^{(e)}=\left(p_{1}^{(e)}, p_{2}^{(e)}, \ldots, p_{M_{1} M_{2}}^{(e)}\right)
\end{array}\right.
$$

where $s_{j}^{(e)}=s_{j}^{(\bar{n})}+s_{i}^{(\bar{e})}, p_{i}^{(e)}=p_{j}^{(\bar{n})} p_{i}^{(\bar{e})}$, in which $j=\left[(l-1) / M_{1}\right]+1, i=l-(j-1) M_{1}$.
Thus we have

$$
\begin{aligned}
\Delta(\mathrm{e}(k))= & \sum_{l=1}^{M_{1} M_{2}-1}\left|s_{l+1}^{(e)}-s_{l}^{(e)}\right| \frac{p_{l}^{(n)}+p_{l+1}^{(e)}}{2}+\frac{\left|s_{M_{1} M_{2}}^{(e)}-s_{1}^{(e)}\right|}{M_{1} M_{2}-1} \frac{p_{1}^{(e)}+p_{M_{1} M_{2}}^{(e)}}{2} \\
= & \sum_{j=1}^{M_{2}} \sum_{i=1}^{M_{1}-1}\left|\left(s_{j}^{(\bar{n})}+s_{i+1}^{(\bar{e})}\right)-\left(s_{j}^{(\bar{n})}+s_{i}^{(\bar{e})}\right)\right| \frac{p_{j}^{(\bar{n})} p_{i}^{(\bar{e})}+p_{j}^{(\bar{n})} p_{i+1}^{(\bar{e})}}{2} \\
& +\sum_{j=1}^{M_{2}-1}\left|\left(s_{j}^{(\bar{n})}+s_{M_{1}}^{(e)}\right)-\left(s_{j+1}^{(\bar{n})}+s_{1}^{(\bar{e})}\right)\right| \frac{p_{j}^{(\bar{n})} p_{M_{1}}^{(\bar{e})}+p_{j+1}^{(\bar{n})} p_{1}^{(\bar{e})}}{2} \\
& +\frac{\left|\left(s_{M_{2}}^{(e)}+s_{M_{1}}^{(e)}\right)-\left(s_{1}^{(e)}+s_{1}^{(\bar{e})}\right)\right|}{M_{1} M_{2}-1} \frac{p_{1}^{(e)} p_{1}^{(e)}+p_{M_{2}}^{(e)} p_{M_{1}}^{(e)}}{2} \\
& \stackrel{(b)}{\approx} \sum_{j=1}^{M_{2}} \sum_{i=1}^{M_{1}-1}\left|\left(s_{j}^{(\bar{n})}+s_{i+1}^{(\bar{e})}\right)-\left(s_{j}^{(\bar{n})}+s_{i}^{(\bar{e})}\right)\right| \frac{p_{j}^{(\bar{n})} p_{i}^{(\bar{e})}+p_{j}^{(\bar{n})} p_{i+1}^{(\bar{e})}}{2} \\
& =\sum_{j=1}^{M_{2}} p_{j}^{(\bar{n})}\left\{\sum_{i=1}^{M_{1}-1}\left|s_{i+1}^{(\bar{e})}-s_{i}^{(\bar{e})}\right| \frac{p_{i}^{(\bar{e})}+p_{i+1}^{(\bar{e})}}{2}\right\} \stackrel{(b)}{\approx} \sum_{j=1}^{M_{2}} p_{j}^{(\bar{n})} \Delta(\bar{e}(k))
\end{aligned}
$$

where (a) and (b) follows from Assumption 3 (i.e. $p_{i}^{(\bar{e})} \approx 0, p_{M_{1}}^{(\bar{e})} \approx 0$ ). The above result is promising, since it implies minimizing the $\Delta$-entropy of the noise-corrupted error $e(k)$ will be approximately equivalent to minimizing the $\Delta$-entropy of the intrinsic error, which is the ultimate objective function that needs to be minimized. Therefore, the $\Delta$-entropy criterion may yield approximately an unbiased solution even if the input and output data are both corrupted by noises. To verify the "unbiasness" of the $\Delta$-entropy criterion, we present herein a supplementary example. Consider again the identification of a two-tap FIR filter in which $G^{\prime}(z)=w_{1}^{\prime}+w_{2}^{\prime} z^{-1}=1.0 \div 0.5 z^{-1}$. This time we assume the input signal $x(k)$, input noise $n_{1}(k)$, and output noise $n_{2}(k)$ are all zero-mean white Bernoulli processes with distributions below

$$
\left\{\begin{array}{l}
\operatorname{Pr}\left\{x(k)=\sigma_{n}\right\}=0.5, \quad \operatorname{Pr}\left\{x(k)=-\sigma_{n}\right\}=0.5 \\
\operatorname{Pr}\left\{n_{1}(k)=\sigma_{n_{1}}\right\}=0.5, \quad \operatorname{Pr}\left\{n_{1}(k)=-\sigma_{n_{1}}\right\}=0.5 \\
\operatorname{Pr}\left\{n_{2}(k)=\sigma_{n_{2}}\right\}=0.5, \quad \operatorname{Pr}\left\{n_{2}(k)=-\sigma_{n_{2}}\right\}=0.5
\end{array}\right.
$$

where $\sigma_{n}, \sigma_{n_{1}}$ and $\sigma_{n_{2}}$ denote respectively, the standard deviations of $x(k), n_{1}(k)$ and $n_{2}(k)$. In the simulation we set $\sigma_{n}=1.0$, and the training data length $L=500$.

Tables 2 and 3 list the "mean $\pm$ deviation" results (over 100 Monte Carlo runs) of the estimated parameters ( $w_{1}$ and $w_{2}$ ) at the 10th EDA generation for different values of $\sigma_{n_{1}}$ and $\sigma_{n_{2}}$. For comparison purpose we also include the results obtained using MSE criterion. From the tables, we observe that the $\Delta$-entropy criterion produces nearly mean-unbiased estimates under various SNR conditions, whereas the MSE criterion yields mean-biased solution especially when the input noise power $\left(\sigma_{n_{1}}^{2}\right)$ increasing.

## References

[1] J.C. Aguero, G.C. Goodwin, J.I. Yuz, System identification using quantized data, in: Proceedings of the 46th IEEE Conference on Decision and Control, New Orleans, LA, USA, December 2007, pp. 4263-4268.
[2] B. Chen, J. Hu, L. Pu, Z. Sun, Stochastic gradient algorithm under (h.-p)-entropy criterion, Circuits Systems Signal Processing 26 (2007) 941-960.
[3] T. Chen, K. Tang, G. Chen, X. Yao, On the analysis of average time complexity of estimation of distribution algorithms, in: Proceedings of 2007 IEEE Congress on Evolutionary Computation (CEC2007), 2007, pp. 453-460.
[4] T.M. Cover, J.A. Thomas, Element of Information Theory, Wiley \& Son, Inc., Chichester, 1991.
[5] L. Devroye, G. Lugosi, Combinatorial Methods in Density Estimation, Springer-Verlag, 2000.
[6] D. Erdogmus, E.H. Kenneth, J.C. Principe, Online entropy manipulation: stochastic information gradient, IEEE Signal Processing Letters 10 (2003) 242245.
[7] D. Erdogmus, J.C. Principe, Generalized information potential criterion for adaptive system training, IEEE Transactions on Neural Networks 13 (2002) $1035-1044$.
[8] D. Erdogmus, J.C. Principe, Convergence properties and data efficiency of the minimum error entropy criterion in Adaline training, IEEE Transactions on Signal Processing 51 (2003) 1966-1978.
[9] D.Z. Feng, X.D. Zhang, D.X. Chang, W.X. Zheng, A fast recursive total least squares algorithm for adaptive FIR filtering, IEEE Transactions on Signal Processing 52 (2004) 2729-2737.
[10] E. Gassiat, E. Gautherat, Identification of noisy linear systems with discrete random input, IEEE Transactions on Information Theory 44 (1998) 19411952.
[11] C. Gonzalez, A. Ramirez, J.A. Lozano, P. Larranaga, Average time complexity of estimation of distribution algorithms, in: The 18th International WorkConference on Artificial Neural Networks (IWANN2005), Lecture Notes in Computer Science, vol. 3512, 2005, pp. 42-49.
[12] L. Hu, C. Zhou, Z. Sun, Estimating biped gait using spline-based probability distribution function with Q-learning, IEEE Transactions on Industrial Electronics 55 (2008) 1444-1452.
[13] M. Janzura, T. Koski, A. Otahal, Minimum entropy of error principle in estimation, Information Sciences 79 (1994) 123-144.
[14] M. Janzura, T. Koski, A. Otahal, Minimum entropy of error estimation for discrete random variables, IEEE Transactions on Information Theory 42 (4) (1996) 1193-1201.
[15] J.N. Kapur, H.K. Kesavan, Entropy Optimization Principles with Applications, Academic Press Inc., 1992.
[16] P. Larranaga, J.A. Lozano, Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation, Kluwer Academic Publishers, Boston, 2002.
[17] T.H. Li, Blind identification and deconvolution of linear systems driven by binary random sequences, IEEE Transactions on Information Theory 38 (1992) 26-38.
[18] T.H. Li, Finite-alphabet information and multivariate blind deconvolution and identification of linear systems, IEEE Transactions on Information Theory 49 (2003) 330-337.
[19] T. Ling, T. David, Adaptive estimated maximum-entropy distribution model, Information Science 177 (2007) 3110-3128.
[20] N. Minamide, An extension of the entropy theorem for parameter estimation, Information and Control 53 (1982) 81-90.
[21] A. Okao, M. Ikeda, R. Takahashi, System identification for nano control: a finite wordlength problem, in: Proceedings of Conference on Control Applications, Istanbul, Turkey, June 2003, pp. 49-53.
[22] U. Ozettem, D. Erdogmus, Second-order volterra system identification with noisy input-output measurements, IEEE Signal Processing Letters 16 (2009) 18-21.
[23] U. Ozettem, I. Uysal, D. Erdogmus, Continuously differentiable sample-spacing entropy estimation, IEEE Transactions on Neural Networks 19 (2008) 1978-1984.
[24] L. Pardo, Statistical Inference Based on Divergence Measures, Chapman \& Hall/CRC, 2006.
[25] J.C. Patra, R.N. Pal, R. Baliarsingh, G. Panda, Nonlinear channel equalization for QAM signal constellation using artificial neural networks, IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics 29 (2) (1999) 262-271.
[26] C.L. Phillips, H.T. Nagle, Digital Control System Analysis and Design, fourth ed., Prentice Hall Press, 2007.
[27] J.C. Principe, D. Xu, Q. Zhao, et al, Learning from examples with information theoretic criteria, Journal of VLSI Signal Processing Systems 26 (2000) 6177.
[28] Y.N. Rao, D. Erdogmus, J.C. Principe, Error whitening criterion for adaptive filtering: theory and algorithms, IEEE Transactions on Signal Processing 53 (2005) 1057-1069.
[29] R. Rastegar, M.R. Meybodi, A study on global convergence time complexity of estimation of distribution algorithms, in: Rough Sets, Fuzzy Sets, Data Mining and Granular Computing (RSFDGrC2005), Lecture Notes in Artificial Intelligence, vol. 3641, 2005, pp. 441-450.
[30] R. Santana, P. Larranaga, J.A. Lozano, Side chain placement using estimation of distribution algorithms, Artificial Intelligence in Medicine 39 (2007) 4963.
[31] L.M. Silva, C.S. Felgueiras, L.A. Alexandre, J. Marques, Error entropy in classification problems: a univariate data analysis, Neural Computation 18 (2006) 2036-2061.
[32] T. Soerstrom, Errors-in-variables methods in system identification, Automatica 43 (2007) 939-958.
[33] H. Suzuki, T. Sugie, System identification based on quantized I/O data corrupted with noise and its performance improvement, in: Proceedings of the 45th IEEE Conference on Decision and Control, San Diego, CA, USA, December 2006, pp. 3684-3689.
[34] O. Vasicek, A test for normality based on sample entropy, Journal of the Royal Statistical Society Series A 38 (1976) 54-59.
[35] L.Y. Wang, G.G. Yin, Y. Zhao, J.F. Zhang, Identification input design for consistent parameter estimation of linear systems with binary-valued output observations, IEEE Transactions on Automatic Control 53 (2008) 867-880.
[36] L.Y. Wang, J.F. Zhang, G.G. Yin, System identification using binary sensors, IEEE Transactions on Automatic Control 48 (11) (2003) 1892-1907.
[37] H.L. Weidemann, E.B. Stear, Entropy analysis of estimating systems, IEEE Transactions on Information Theory 16 (1970) 264-270.
[38] T.C. Yang, Networked control system: a brief survey, Control Theory and Applications, IEE Proceedings 153 (4) (2006) 403-412.
[39] Q. Zhang, H. Muhlenbein, On the convergence of a class of estimation of distribution algorithms, IEEE Transactions on Evolutionary Computation 8 (2) (2004) 127-136.
[40] Y. Zhao, L.Y. Wang, G.G. Yin, J.F. Zhang, Identification of Wiener systems with binary-valued output observations, Automatica 43 (2007) 1752-1765.
[41] A.C. Harvey, C. Fernandez, Time series for count data or qualitative observations, Journal of Business and Economic Statistics 7 (1989) 407-417.
[42] M. Al-Osh, A. Alzaid, First order integer-valued autoregressive (NAR 1) process, Journal of Time Series Analysis 8 (3) (1987) 261-275.
[43] K. Brannas, A. Hall, Estimation in integer-valued moving average models, Applied Stochastic Models in Business and Industry 17 (3) (2001) 277-291.
[44] C.H. Weiß, Thinning operations for modeling time series of counts-a survey, ASIA Advances in Statistical Analysis 92 (3) (2008) 319-341.
[45] M. Sato-Ilic, Fuzzy regression models on entropy based blocking structures, International Journal of Innovative Computing, Information and Control 5 (6) (2009) 1475-1484.
[46] W. Zeng, F. Yu, X. Yu, H. Chen, S. Wu, Entropy of intuitionistic fuzzy set based on similarity measure, International Journal of Innovative Computing, Information and Control 5 (12A) (2009) 4737-4744.
[47] X. Gao, C. You, Maximum entropy membership functions for discrete fuzzy variables, Information Sciences 179 (14) (2009) 2353-2361.
[48] Q.S. Zhang, S.Y. Jiang, A note on information entropy measures for vague sets and its applications, Information Sciences 178 (21) (2008) 4184-4191.
[49] J. Balatoni, A. Renyi, On the notion of entropy (Hungarian), vol. 1, Publ. Math. Inst. Hungarian Acad. Sci., 1956, pp. 9-40 (English Translation: Selected Papers of Alfred Renyi, vol. 1, Akademiat Kiado, Budapest, 1976, pp. 558-584).