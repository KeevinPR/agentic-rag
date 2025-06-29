# Motif Discovery Using Evolutionary Algorithms 

Linlin Shao<br>School of Information Science and Engineering<br>University of Jinan<br>Jinan 250022, Shandong, P.R. China<br>Email: shao-lin-lin@hotmail.com

Ajith Abraham<br>Machine Intelligence Research Labs (MIR Labs)<br>Scientific Network for Innovation and Research Excellence<br>P.O. Box 2259, Auburn, Washington 98071-2259, USA<br>Email: ajith.abraham@ieee.org


#### Abstract

The bacterial foraging optimization (BFO) algorithm is a nature and biologically inspired computing method. We propose an alternative solution integrating bacterial foraging optimization algorithm and tabu search (TS) algorithm namely TS-BFO. We modify the original BFO via established a self-control multi-length chemotactic step mechanism, and introduce rao metric. We utilize it to solve motif discovery problem and compare the experimental result with existing famous DE/EDA algorithm which combines global information extracted by estimation of distribution algorithm (EDA) with differential information obtained by Differential evolution (DE) to search promising solutions. The experiments on real data set selected from TRANSFAC and SCPD database have predicted meaningful motif which demonstrated that TS-BFO and DE/EDA are promising approaches for finding motif and enrich the technique of motif discovery.


Keywords-motif discovery; bacterial foraging optimization; tabu search; DE/EDA;

## I. InTRODUCTION

With the increasing volume of biologic sequences available in public databases. Identification the transcription factor binding sites (TFBSs), which are relative short, recurring, conservative patterns in the regulatory regions of deoxyribonucleic acid (DNA) and are regard as having a specified biological meaning to regulate the transcriptional activity of genes (gene expression) [1], by computational methods is a major challenge in bioinformatics.

In all the existing algorithms for motif discovery, they employed different search techniques to explore different fitness landscape based on the corresponding fitness function. The majority of these algorithms could be assort two categories: stochastic searching algorithms based on position specific weight matrix (PSWM) such as MEME [3], AlignACE [4], and BioProspector [5]. The second category is combinatorial search algorithms based on consensus sequence such as Weeder [6], YMF [7], and Projection [8]. Regarded no one approach is outstanding as the only best, and experiments have shown that the overall performance of motif finding

Yuehui Chen<br>School of Information Science and Engineering<br>University of Jinan<br>Jinan 250022, Shandong, P.R. China<br>Email: yhchen@ujn.edu.cn

algorithms is still quite low. Nevertheless, there seems to be a slight advantage by combinatorial approaches [9].

In this paper, we propose an alternative solution integrating bacterial foraging optimization algorithm [10], which is a natural foraging strategy technique, and tabu search algorithm [11] [12] for motif discovery. We also compare the experimental result with the DE/EDA algorithm and other well-known methods.

## II. ObJective Function

For the given $H$ sequences, each length is $Q$. For the purpose of explore motifs we use a total fitness score function, our approaching which part of it as the sequence alignment FMGA [13] did, we also did some modification to adapt to our TS-BFO algorithm and describe it below. Therefore, we consider the fitness score of one single sequence, defined as follows:

$$
\begin{aligned}
& F S\left(S_{m}, P_{n}\right) \\
& \quad=\max \left\{\sum_{i=1}^{w} \operatorname{match}\left(S_{m j i}, P_{n i}\right)+L / w\right\} / w
\end{aligned}
$$

Where

$$
\operatorname{match}\left(S_{m j i}, P_{n i}\right)=\left\{\begin{array}{ll}
1 & \text { if } S_{m j i}=P_{n i} \\
0 & \text { if } S_{m j i} \neq P_{n i}
\end{array}\right.
$$

$m$ is the index of sequences, $i$ is the position within the motif, $n$ is the index of motif patterns, $w$ is the length of motif pattern, $j$ is number of matched regions in the sequence. And $L$ is the value of the number of all the continuous mismatched segments minus one, it reflect the multiple sequence alignment phenomena biologically [14]. To find the maximum mentioned above, we resort to a slide window which moves from the beginning of the sequence to the end of it.

The total fitness score function of an individual is the summation of fitness score function for all sequences. We

establish the total fitness score function as follows.

$$
J=T F S\left(S, P_{n}\right)=\sum_{m=1}^{H} F S\left(S_{m}, P_{n}\right)
$$

## III. The TS-BFO Algorithm For Motif Discovery

## A. The Original BFO Algorithm

Bacterial Foraging Optimization (BFO) algorithm has been applied to model the E. coli bacteria foraging behavior for solving optimization problems [10]. It has some remarkable accomplishment in applied to some Control Systems (such as PID controller, harmonic estimation, etc) [15] [16] [17]. In our method one candidate motif regard as one bacteria to undergo the evolution. The foraging action of E. coli experience four series of steps namely, chemotaxis, swarming, reproduction, and elimination and dispersal.

## B. The Tabu search

Tabu search (TS) method [11] [12] is a modern metaheuristic optimization technology. The crucial part of this algorithm is to make use of a "memory" to creating one (or more) tabu list, which contain the historical information of solutions that have been obtained lately. The list reserve a set of solutions as tabu to avoid visited repeatedly and guide the search orientation. The use of tabu search on the largescale non-linear problem has proved it can find the global solution very effectively.

To the motif discovery problem, the tabu list in our method is composed of three items:

1. All the candidate motifs themselves.
2. Each candidate motif's fitness value.
3. The un-update iteration time that each motif has been suffered.
In the search procedure, check and update the tabu list is a pivotal step, in view of finding motif based on the BFO algorithm, we summarize our visit tabu list mechanism as follow:
step1: When the new individual generates in swarming step, if there is no duplicate in list, then insert it to the list (update tabu list successfully), else, update tabu list unsuccessful.
step2: When the new individual generates in reproduction or in elimination and dispersal step, if it can satisfy the aspiration criterion (better than the average fitness value of all the individuals), and there is no duplicate in list, then insert it to the list(successful), else, failed.
step3: When some individuals have not updated for K consecutive iterations and its fitness below the average (its fitness rank at the posterior part of the population),
delete it and create a new one, then go to step 1. If its fitness above the average, shorten its Chemotactic step length.
step4: Sort the individuals by fitness in increasing order, keep the population constant, and update each individual's K value.

## C. The Detailed TS-BFO Algorithm

We summarize the general principles of TS-BFO algorithm in detail as follows:

1) Initialize: $j=k=l=0$
2) Elimination-dispersal loop: $l=l+1$
3) Reproduction loop: $k=k+1$
4) Chemotaxis loop: $j=j+1$
a) For $i=1,2, \ldots, S$, take a chemotactic step for bacterium as follows.
b) Compute $J(i, j, k, l)$. Let

$$
\begin{gathered}
J(i, j, k, l)=J(i, j, k, l) \\
+J_{c c}\left(\theta^{i}(j, k, l), P(j, k, l)\right)
\end{gathered}
$$

c) Let $J_{\text {last }}=J(i, j, k, l)$ to save this value since we may find a better cost via a run.
d) Tumble: Generate a random vector $\Delta(i) \in \Re^{p}$ with each element $\Delta_{m}(i), m=1,2, \ldots, p$, a random number on $[1,1]$.
e) Move: Let

$$
\begin{gathered}
\theta^{i}(j+1, k, l)=\theta^{i}(j, k, l) \\
+C(i) \frac{\Delta(i)}{\sqrt{\Delta^{T}(i) \Delta(i)}}
\end{gathered}
$$

This results in a step of size $C(i)$ in the direction of the tumble for bacterium $i$.
f) Compute $J(i, j+1, k, l)$, and then let

$$
\begin{gathered}
J(i, j+1, k, l)=J(i, j+1, k, l) \\
+J_{c c}\left(\theta^{i}(j+1, k, l), P(j+1, k, l)\right)
\end{gathered}
$$

g) Swim:
i.) Let $m=0$ (counter for swim length);
ii.) While $m<N_{s}$ (if have not swam enough distance)

- Let $m=m+1$
- If $J(i, j+1, k, l)>J_{\text {last }}$ (if doing better) and update tabu list successfully, let $J_{\text {last }}=$ $J(i, j+1, k, l)$ and let

$$
\begin{gathered}
\theta^{i}(j+1, k, l)=\theta^{i}(j+1, k, l) \\
+C(i) \frac{\Delta(i)}{\sqrt{\Delta^{T}(i) \Delta(i)}}
\end{gathered}
$$

and use this $\theta^{i}(j+1, k, l)$ to compute the new $J(i, j+1, k, l)$ as we did in f ).

- If update tabu list unsuccessfully, go to d).

- If $J(i, j+1, k, l)<J_{\text {last }}$ and haven't update for consecutive $K(i)$ times, let $K(i)=$ $K(i)+1$.
h) Go to next bacterium $(i+1)$ if $i \neq S$ (i.e., go to b) to process the next bacterium).

5) If $j<N_{c}$, go to step 4. In this case, continue chemotaxis, since the life of the bacteria is not over.
6) Reproduction:

- Let $t=0$ (counter for Reproduce time);
- while $\left(t<R_{s}\right)$ (if have not Reproduce enough children)
(1) Choose 2 individuals whose fitness above the average as parents, executing the random one point crossover based on elitist selection for reproduction.
(2) Update the tabu list. If failed, go to (1). Else, let $t=t+1$.

7) If $k<N_{r e}$, go to step 3. In this case, we have not reached the number of specified reproduction steps, so we start the next generation in the chemotactic loop.
8) Elimination-dispersal: For $i=1,2, \ldots, S$, with probability $P_{e d}$, eliminate and disperse each bacterium. To do this, if you eliminate a bacterium, simply disperse one to a random location on the optimization domain, and Update the tabu list.
9) If $l<N_{e d}$, then go to step 2 ; otherwise end.

In formula (4), where

$$
\begin{aligned}
& J_{c c}(\theta, P(j, k, l))=\sum_{i=1}^{S} J_{c c}^{i}\left(\theta, \theta^{i}(j, k, l)\right) \\
& =\sum_{i=1}^{S}\left[-d_{a t t} \exp \left(-w_{a t t} \sum_{m=1}^{p}\left(\theta_{m}-\theta_{m}^{i}\right)^{2}\right)\right] \\
& =\sum_{i=1}^{S}\left[-h_{r e p} \exp \left(-w_{r e p} \sum_{m=1}^{p}\left(\theta_{m}-\theta_{m}^{i}\right)^{2}\right)\right]
\end{aligned}
$$

Denote the combined cell-to-cell attraction and repelling effects, dynamically deforms the search landscape as the cells move to represent the desire to swarm, where $\theta=$ $\left[\theta_{1}, \ldots, \theta_{p}\right]^{T}$ is a point on the optimization space and $\theta_{m}^{i}$ is the $m$ th component of the $i$ th bacterium position.

In this paper we introduced the Rao metric to state the combined cell-to-cell attraction and repelling effects $\left(J_{c c}\right)$. The Rao metric has a statistical meaning, it is, one of the similarity measure, the distance metric for comparing parameter vectors [18][19], we just use the simple form substituted for $\sum_{m=1}^{p}\left(\theta_{m}-\theta_{m}^{i}\right)^{2}$ which refer to $J_{c c}$, in the interest of understand the relationship between one single motif and the whole population. The Rao metric defined as follows.

$$
R a o=\frac{x}{w}
$$

Where $w$ still represent the length of a motif, $x$ is the amount of all the matched positions at a alignment time. We Then modify $J_{c c}$ to $F_{c c}$ as follow.

$$
\begin{aligned}
F_{c c}(\theta, & P(j, k, l))=\sum_{i=1}^{S} F_{c c}^{i}\left(\theta, \theta^{i}(j, k, l)\right) \\
& =\sum_{i=1}^{S}\left[-d_{a t t} \exp \left(-w_{a t t} R a o^{i}(j, k, l)\right)\right] \\
& =\sum_{i=1}^{S}\left[-h_{r e p} \exp \left(-w_{r e p} R a o^{i}(j, k, l)\right)\right]
\end{aligned}
$$

where $F_{c c}$ function is time varying in that if many bacteria come close together there will be a high amount of attractant and hence an increasing likelihood that other bacteria will move toward the group.

Apart from that $d_{a t t}, w_{a t t}, h_{r e p}$ and $w_{r e p}$ indicate that the depth of the attractant released, the width of the attractant signal, the height of the repellant effect, and the width of the repellant by the cell respectively.

## D. The Self-control Multi-length Chemotactic Steps

In the original BFO (as in other search techniques), we have to face the problem that keep balance between the exploration and the exploitation, that's where the shoe pinches. Our study will focus on the concernful chemotactic step. There have many achievements reached by other scientists. Das [20] have proved that at some point of time the constant step-size violates the conditions of asymptotic stability and the bacterium starts oscillating around the optimum, instead of converging to it. Datta and Misra [21] made the chemotaxis adaptive using principle of adaptive delta modulation. Chen [22] established an"individual run-length unit"with 2 Criterions, and so on.

We present our self-control multi-length chemotactic step mechanism as follow:

1. Initialize large run-length for each bacteria at the very beginning.
2. If the bacteria's current fitness is un-update for K consecutive iterations, then abate its run-length (avoid reaching zero).
3. With the run-length minish gradually, trying relative large run-length at least one time in each iterations.
We brought about this self-control multi-length chemotactic step mechanism for the sake of increase the diversity of the population and avoid being in the local extremum trouble.

## IV. THE DE/EDA ALGORITHM

The DE/DEA algorithm [23] is an improved DE algorithm based on the estimation of distribution algorithm. In DE/EDA, new promising solution is created by DE/EDA offspring generation scheme, in which local information obtained by the DE mutation and global information extracted

from a population of solutions by the EDA modeling are incorporated together. We list the major steps of DE/DEA below and the detailed information about it you can see [23].

```
Step 1: Select the best M solutions from the current
    population, construct probability modelp \((x)\)
Step 2: Generate a trial solution \(u=\left(u_{1}, u_{2}, \ldots, u_{n}\right)\);
        if \((r a n d()<\delta)\)
            \(u_{j}\) generate by DE operator;
            else
                \(u_{j}\) generate by EDA operator;
Step 3: If \(f(u)<f\left(x_{i}^{k}\right)\)
                \(x_{i}^{k+1}=u\);
            else
                \(x_{i}^{k+1}=x_{i}^{k}\)
```


## V. EXPERIMENTAL RESULT

We carried out some experiments demonstrate the feasibility of TS-BFO and DE/DEA, and compare them with known motifs those found by these two methods and by other famous approaches, the data sets for the discovery of transcription factor binding sites were selected from public database.

The $\overparen{\%}$ denotes the motif that TS-BFO can predict but DE/EDA can't, whereas The denotes the motif that DE/EDA can predict but TS-BFO can't. N/A means there is no other method we can find which discover the same motif. Besides, we don't list all the output we had gotten, and only present some of them to illuminate our algorithm.

The first set contains 7 promoter sequences of saccharomyces cerevisiae (yeast), which were collected from SCPD database. We give the results of our TS-BFO algorithm predicted and their rank in output in Table 1 and the result get from DE/DEA algorithm in Table 2. we also Compare the results with known binding sites. In TS-BFO, $N_{c}=4$, $N_{r e}=4, N_{e d}=4$, and $N_{s}=5$ respectively.

The performance of TS-BFO and DE/EDA from Table 1 and Table 2 illuminated that they can predict meaningful motif, therefore they are promising methods for motif discovery. With the length of the motif become longer the difficulty to discover also augment, so the fitness is descending as the motif length largen. Next, we exhibit their discrimination by test on different dataset.

The secondary $h m 03 r$ sequence data set contains 10 sequences of 1500 bps each which is a larger set comparatively and was collected from TRANSFAC database. Table 3 and 4 shows the result, the lengths of the conservative motif set with $6,7,10$ and 13 , and compare the results with AlignACE, MEME, and other known methods [9], Other key parameter Choose $N_{c}=10, N_{r e}=5, N_{e d}=5$, and $N_{s}=20$ for our TS-BFO.

Thirdly, the $y s t 04 r$ sequence data set which from TRANSFAC database contains 7 sequences of 1000 bps each.

Table I
COMPARISON OF THE KNOWN BINDING SITES OF S. CEREVISIAE AND THE PREDICTION RESULTS GIVEN BY TS-BFO.
The predicted motif patterns are shown in Table 3. we choose $N_{c}=5, N_{r e}=4, N_{e d}=4$, and $N_{s}=5$ for our TS-BFO.

From table $3,45,6$ we observed that there some motifs only one of the algorithm can predict. It means that different search strategy explore different search space. In fact, most of the results from these two methods are the same, because they based on the same objective function. Hence, we can choose different approach to deal with different datasets, and the technique of motif discovery enriched by the TS-BFO and the DE/EDA.

## VI. CONCLUSION

The results presented shows that TS-BFO and DE/EDA are promising approach for motif discovery. The performance of them illuminated that they can predict meaningful motif.

Thus, we sum up TS-BFO's 4 advantages. First, we established a self-control multi-length chemotactic step mechanism which could extend the search space, avoid local extremum and speed up the constringency. Second, we introduced The Rao metric to exhibit swarm together effect in order to achieve the finding motif aim which based on BFO algorithm, and it works. Third, using the one point crossover based on elitist selection to conquer the trouble of local extremum which arises in the original BFO with higher probability. Finally and the one of the most important point, integrating Tabu Search algorithm could abstain the duplicate individuals generates in each step, guide the search orientation, and find the global solution.

Table II
COMPARISON OF THE KNOWN BINDING SITES OF S.cerevisiae AND THE PREDICTION RESULTS GIVEN BY DE/EDA.
Table III
COMPARISONS OF TS-BFO PREDICTED MOTIFS WITH DIFFERENT METHODS FOR hml03r.

Table IV
COMPARISONS OF DE/EDA PREDICTED MOTIFS WITH DIFFERENT
METHODS FOR hml03r.


## ACKNOWLEDGMENT

This research was supported by the NSFC (60573065), the the Natural Science Foundation of Shandong Province (Y2007G33), and the Key Subject Research Foundation of Shandong Province.
