# Hybrid estimation of distribution algorithms for solving a keyboard layout problem 

T.G. Pradeepmon (1) Vinay V. Panicker (2) and R. Sridharan (3)

Department of Mechanical Engineering, National Institute of Technology, Calicut, India


#### Abstract

The use of smartphones and handheld devices in our daily activities has sharply increased. The added features of wireless technology and related applications on these devices make it possible to write emails, notes, and long text. Even though the most commonly used electronic input device is a keyboard, very little work has been dedicated for finding an optimal layout for this device. In this research, the aim is to propose a better layout for the single-finger keyboard in terms of rapid typing. The keyboard layout problem can be formulated as a quadratic assignment problem, which is one of the hardest combinatorial optimization problems. Some well-known literary works in English are chosen for estimating the keying-in-time. A variant of genetic algorithm, namely, the estimation of distribution algorithms is used to find a better layout. The new layout is found to be efficient compared with some of the existing prominent keyboard layouts.


## ARTICLE HISTORY

Received 9 December 2016 Accepted 11 June 2018

## KEYWORDS

Single-finger keyboard; estimation of distribution algorithm; quadratic assignment problem; keyboard layout problem; population based incremental learning; univariate marginal distribution algorithm

## 1. Introduction

The most commonly used input device for computers and other text processing electronic devices is the keyboard. However, a novice computer user will get surprised by the seemingly arbitrary arrangement of keys in the standard keyboard. The most widely used keyboard is the "QWERTY" keyboard - named after the first six characters in the top row of letters - or the Sholes keyboard - named after its inventor, Christopher Latham Sholes. This keyboard layout was designed in 1868 by Sholes, for use in a mechanical typewriter in which the typing is done with both the hands. In this keyboard, the letters are arranged in a special, non-alphabetical order to improve the speed of typing by minimizing the jamming of keys in the typewriter. Since then, the QWERTY layout had become popular and is still the most accepted device used to input data into personal computers. However, the recent spread of smartphones, Portable Data Assistants (PDA), Tablet PCs, etc., has necessitated the redesign of the keyboard layout. Since the digital keys do not jam, it is possible to place any combination of keys nearby. Many of these devices are held in one hand and only a single finger of the other hand is used for pressing the keys to input data (hence, the name "single-finger (s-finger) keyboard"), which makes the s-finger keyboard a necessity.

The QWERTY keyboard was developed by Christopher Latham Sholes and he obtained patent for the same in 1968. He continued to develop on his typing machine and one of the problems faced by him was the jamming of the type bars when certain
combinations of keys were struck in a very close succession. In order to solve this problem, Sholes arranged the keys in such a way that the keys most likely to be struck in close succession approached the type point from opposite sides of the machine. Thus, the layout was not actually designed for increasing the speed of typing, but to decrease the jamming of the keys during typing. In 1873, the patent was sold to E. Remington and Sons who added further mechanical improvements and began the commercial production of the typewriters using this keyboard [1]. The QWERTY keyboard was accepted as a standard and people using it outperformed others in typing competitions held in those years. Thus, the QWERTY keyboard became popular among people using typewriters.

In the year 1936, August Dvorak designed a new layout for the keyboard and obtained patent for the same. This keyboard layout is known as Dvorak Simplified Keyboard. It claimed to reduce the finger movements necessary for typing by equally dividing the load between the hands and loading the stronger fingers more heavily. After the introduction of Dvorak keyboard, there were many debates on the efficiency of the two layouts. Some authors even claimed that the QWERTY keyboard actually reduced the typing speed and, by doing so, avoided the jamming of keys. The Dvorak keyboard claimed the advantages of greater speed, reduced fatigue, and easier learning. Even with all the claims, the Dvorak keyboard failed to find much acceptance.

The competition between the two keyboards was of interest to economists also, and they used this example to demonstrate how the standards are being set and how it is difficult to replace an already set standard with a new one even if the new one is better. Paul A. David started this discussion in 1985 through a paper in which he claimed that the Dvorak keyboard is better than QWERTY keyboard [2]. But Liebowitz and Margolis rejected the claim through their paper "The fable of Keys" [1]. The battle on the superiority of the keyboards continued through a series of papers [3]. During this period, some researches tried to find out a better layout for the keyboard than the QWERTY and Dvorak. Many of such works focused on developing customized keyboards for special purposes.

Eggers et al. [4] introduced an abstract representation of a keyboard and an evaluation function taking account of ergonomic criteria is proposed. The resulted optimization problem was named the keyboard arrangement problem and based on the generic framework of Ant Colony optimization; an algorithm is developed and applied to this problem.

Kwon et al. [5] compared the performance and the subjective ratings of the conventional finger touch text-entry method and the regional error-correction method, for a touch-screen QWERTY keyboard. The regional error correction reduced both the time and the number of touches required to complete text entry when keys were small, but no difference was observed when keys were large.

Cardinal and Langerman [6] investigated the problem of placing symbols of an alphabet onto the minimum number of keys of a small keyboard so that any word of a given dictionary could be recognized unambiguously only by looking at the corresponding sequence of keys. The paper also provides optimized incomplete keyboards with 6, 8, and 12 keys. Curran et al. [7] conducted a survey to establish which mobile phone text input method best suits the requirements of a select group of target users. The survey used a diverse range of users to compare devices that are in everyday use by most of the adult population. The targeted group preferred larger keypad/keyboard devices to their smaller equivalents and the standard keypad layout to the non-standard layout on mobile phones.

Yin and Su [8] proposed a Cyber Swarm method considering multiple objectives and it accommodates ergonomic criteria and disambiguation/prediction effectiveness simultaneously. Experimental results proved that the proposed keyboard outperforms several benchmark keyboards and other competing algorithms. The work also gives an illustrative example for preliminary keyboard shape design, which could be very useful in customized keyboard production for
motor-impaired users whose physical capacity has been evaluated a priori.

Alswaidan et al. [9] proposed a genetic algorithm to find an optimal layout for the s-finger Arabic keyboard. To adapt the problem to the requirements of optimizing the s-finger Arabic keyboard, two measures, namely, the keyboard row weight and the hit direction of the finger were added to the objective function of the Quadratic Assignment Problem (QAP). The resulting keyboard was compared with the Arabic keyboard layouts developed for m-fingers in Khorshid et al. [10], Malas et al. [11], and the iPhone Operating System (iOS) Arabic keyboard and was proved to be better in terms of improving in the objective function value. Govind and Panicker [12] proposed a Genetic Algorithm for the optimization of the sfinger keyboard problem. In the paper, the problem was considered a multiple attribute decision-making problem and Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is applied to find out the best layout. The attributes selected were to minimize the flow distance, learning percentage, and maximize the typing speed.

Although many works related to text entry on mobile devices had been conducted in the human-computer interface zone, it seems that not many of them treat the problem of redefining the actual keyboard layout. Amico et al. [13] consider a s-finger keyboard layout to be a generalization of the well-known QAP. In this paper, a s-finger keyboard layout is considered as a QAP and an optimal layout is determined for the keys in terms of typing time. Since the QAP is proved to be an NP-hard problem [14], there is a need to develop heuristic algorithm to solve it to nearoptimality. McKendall and Li [15] proposed a generalization of QAP and proposed a tabu search for solving it. Other heuristic and metaheuristic methods for solving QAPs were proposed by Tosun et al. [16], Hafiz and Abdennour [17], Zhu et al. [18,19], etc. In this work, the Estimation of Distribution Algorithms (EDAs), which are relatively new evolutionary algorithms, are employed for solving QAPs. In order to improve the effectiveness of the algorithms, two local search methods are also employed. Similarly, in this work, a keyboard layout problem is formulated as a QAP. The size of the QAP is 27, as the language considered is English and the punctuations are omitted for simplicity. A summary of literature survey is provided in Table 1.

In the proposed research, the experiments are carried out in three stages. In the first stage, four algorithms are developed combining two EDAs and two local search methods. The effectiveness of the algorithms in solving QAPs is verified by solving 57 benchmark problems taken from QAP Library. In the second stage, a test instance is generated using seven literary works in English and word frequency list of English language. Using this test instance, optimized layouts for least typing time and

least finger movement are found out. These layouts are employed for validation experiments in the third stage.

The rapid increase in the usage of handheld electronic data entry devices demands the relaying out of the on-screen keyboards. For faster data input using only a single finger, the best layout for the keyboard may not be the one which is optimized for all the 10 fingers. This is the motivation behind this research. The proposed layouts are promising in terms of typing time and this direction of relaying out the keyboard is a significant contribution of this work. The algorithms derived from EDAs and local searches are employed for solving QAPs, which are one of the hardest of combinatorial optimization problems. The possibility of employing EDAs for solving QAPs has not been much explored in the past. Thus, the objectives of this work are as follows:

- Develop algorithms combining EDAs and local searches for solving QAPs.
- Establish the effectiveness of the algorithms using benchmark instances taken from QAP Library.
- Generate new layouts for keyboard, optimized for typing time and finger movement.
- Validate the layouts by conducting physical experiments on the optimized layouts.

The rest of the paper is composed as follows: Section 2 presents a brief review of currently existing keyboards. The general description of the s-finger keyboard problem is described in Section 3. Section 4 explains the concepts of algorithms used in this study, namely, EDAs and 2-opt local search. Section 5 provides the details of the computational experiments carried out and the results obtained. The modified keyboard layout is also presented in Section 5. Section 6 concludes the paper.

## 2. Keyboards

A keyboard is a typewriter-like device, which is used to enter data to an electronic device using an arrangement of buttons or keys. A keyboard has characters inscribed or printed on the keys and each key press corresponds to a single written symbol. However,
some symbols require pressing or holding of several keys all together or in specific sequence. Most of the keys on the keyboard produce characters, but other keys or simultaneous key presses may produce actions or execute computer commands. Even though there are a number of other input devices, such as mouse, touch screen, pen devices, character recognition and voice recognition, the keyboard remains the most commonly used device for the direct input of alphanumeric data into computers.

### 2.1. n-finger keyboards

These keyboards use more than one finger for typing. Most of the n-finger keyboards are designed for typing with all the fingers on both hands.

### 2.1.1. QWERTY keyboard

This keyboard layout was designed by Christopher Latham Sholes in 1878 for use in a typewriter with both the hands. The letters were arranged in a special, non-alphabetical order so as to improve the speed of typing by minimizing the jamming of the typewriter. Figure 1 shows the layout of QWERTY keyboard. The QWERTY layout is the most popular alpha-numeric data input device for personal computers. However, this layout suffers from the following drawbacks [20]:

- Many common letter combinations require awkward finger motions or a finger to jump over the home row or need to be typed with one hand.
- In this keyboard, most of the typing is done with left hand, but most people are dominant on their right hand.
- Moreover, about $16 \%$ of typing is done on the lower row, $52 \%$ on the top row, and only $32 \%$ on the home row.


### 2.1.2. Dvorak keyboard

The Dvorak layout was patented in 1936 by Dvorak and Dealey. Figure 2 shows the keyboard layout proposed by Dvorak and Dealey. This layout claims to provide lesser finger motions, increased typing rate, and reduced errors compared to the standard QWERTY keyboard. This leads to faster rates of typing while reducing repetitive strain
![img-0.jpeg](img-0.jpeg)

Figure 1. QWERTY keyboard.

![img-2.jpeg](img-2.jpeg)

Figure 2. The Dvorak keyboard.
injuries. Nevertheless, these advantages have been questioned by Liebowitz and Margolis [1]. Over the years, several slight variations were designed by the team led by Dvorak or by American National Standards Institute (ANSI); however, it failed to replace the QWERTY keyboard.

Many researchers have tried to compare the behavior of various keyboard layouts [21]. Recently, researchers have started applying quantitative methods to design optimal layouts for keyboards. Egger et al. [4] has considered the problem of assigning characters to keys arranged in a pre-specified layout structure.

### 2.2. s-finger keyboards

All the aforementioned layouts are used for the purpose of data entry to personal computers. With the recent spread of mobile phones and PDAs, the necessity for small keyboard layouts has been identified by researchers in this field. Users of such devices normally use just one finger to type in the data to be entered while holding the device in the other hand. This situation gave way to the concept of s-finger keyboard layouts. The size has to be reduced so as to include all the characters in a limited space. Many different layouts are proposed by various researchers, which can be classified into two main categories: complete and incomplete keyboards.

### 2.2.1 Complete keyboards

These are the keyboard layouts similar to QWERTY or Dvorak layouts, but the size is reduced and the keys are arranged in such an order that only one finger is being used for the purpose of text entry. An example of such a keyboard is the FITALY keyboard patented by Textware solutions. It has been designed for English on the basis of the corresponding words frequency. The ABC layout, OPTI, Metropolis, Hooke, Lewis, and many more layouts are available. MacKenzie and Soukoreff [22] provides a complete review of such layouts.

### 2.2.2. Incomplete keyboards

In an incomplete keyboard, many characters are incorporated into the same key and repetitive pressing gives these characters in order. An example of this type of keyboard layout is the 12-key keyboards commonly used in mobile phones. The problem of finding an optimal layout for an incomplete keyboard (called KEYBOARD) by Cardinal and Langerman [6] is a combinatorial optimization problem with an aim of finding the minimum size partition of an alphabet, allowing the users to type any word of a given dictionary so that each word is recognized without ambiguity. Cardinal and Langerman [6] report that the optimal layout determination problem is NP-hard even if it is decided that two keys are sufficient.

## 3. Problem description

This paper considers the s-finger complete keyboard layout problem with the following assumptions:

- All keys or locations except one in the position of spacebar in QWERTY keyboard are unit squares and arranged and numbered as shown in Figure 3. The unit squares represent a "key" or a possible "location."
- Each key or location must contain exactly one of the different symbols or characters used in the given language, say English in this case.
![img-2.jpeg](img-2.jpeg)

Figure 3. Dimensions and positions keys in the keyboard.

The first assumption is that the keyboard considered for the experiments is a normal keyboard with QWERTY layout, which can be transformed into other layouts by rearranging the positions of the keys. The second assumption implies that the keyboard cannot contain duplicate symbols. Now, the problem is to assign the symbols or characters to the locations while minimizing the average time required to type a statement in the given language.

The average time to type a statement using an s-finger keyboard can be computed by considering the frequency in which each ordered pair of symbols appears in the language and the time needed to move the s-finger between the keys accommodating these symbols. The average time can be obtained by summing up the product of the frequency with the corresponding time over all the ordered pairs of symbols.

Fitts's law experiment is often applied when studying the performance of typing devices like keyboards. The Fitts's experiment proved that movement time is related to movement distance and target size [23]. The effort or time taken for typing ( $T_{i k}$ ) two symbols $i$ and $k$, consecutively is given by the Fitts's law [24]

$$
T_{i k}=\theta+\phi \log _{2}\left(\frac{D_{i k}}{W_{k}}+1\right)
$$

where $\theta$ and $\phi$ are constants having pre-fixed values, $D_{i k}$ is the distance between the keys assigned with symbols $i$ and $k$, and $W_{k}$ is the width of the key assigned with symbol $k$. The contribution to the overall writing time due to the repetition of a symbol can be omitted, as it is independent of the assignment of the symbol to a location. Moreover, the equal sized key assumption in our problem enforces that the objective function only depends on the distance between the centers of two locations. In this work, $\theta=0$ and $\phi=10 / 49$ in accordance with Soukoreff [24].

The s-finger keyboard layout problem can be stated as to find the permutation $\varphi$ from the set of all permutations of the number of symbols $P$, which minimizes

$$
Z=\min _{\varphi \in P} \sum_{i=1}^{N} \sum_{k=1}^{N} a_{i k} b_{\varphi(i) \varphi(k)}
$$

where $N$ is the number of symbols or characters to be assigned to $N$ locations or keys, $a_{i k}$ is the number of occurrences of the symbol $k$ immediately after symbol $i$ in the text, $b_{\varphi(i) \varphi(k)}$ is the value of Fitts's function, computed with respect to the Euclidean distance from the center of key assigned with symbol $\varphi(i)$ to the center of key assigned with symbol $\varphi(k)$. The value of $Z$ provides the total time in seconds to type the text with the given ordered symbol pair frequencies. This formulation invariably represents a QAP of size $N$. In addition to the Fitts's time taken for keying in the text, the total distance covered by the finger is minimized. This is achieved by replacing the $b_{j l}$ values with the Euclidean distance from the center of location $j$ to the center of location $l$.

QAP is a well-known NP-hard problem and hence the s-finger keyboard problem, stated earlier, is also an NPhard problem. QAP is one of the most challenging optimization problems and benchmark instances proposed by Nugent et al. [25] in the late sixties have been solved exactly only recently.

## 4. Solution methodology - algorithms

This work aims to develop four algorithms combining two EDAs namely Univariate Marginal Distribution Algorithm (UMDA) and Population-Based Incremental Learning Algorithm (PBILA) with the recursive versions of 2-opt local search denoted by S2opt and R2opt. The following four algorithms are developed combining two EDAs and two local search methods as follows:
(1) UMDA with S2opt,
(2) UMDA with R2opt,
(3) PBILA with S2opt and
(4) PBILA with R2opt.

The details of the algorithms employed in this work are explained in the following sections.

### 4.1. Estimation of distribution algorithms (EDAs)

EDAs, also known as Probabilistic Model Building Genetic Algorithms (PMBGAs), incorporate probability into heuristic search procedures. EDAs are new development in genetic and evolutionary computation research. The algorithms exploit a feasible probabilistic model built around superior solutions so far found within the problem domain. There are three basic steps in EDAs as follows:
(1) Select superior candidate solutions from an initially randomly generated population.
(2) Estimate the probability distribution from the selected solutions.
(3) Generate new candidate solutions or offspring from the estimated probability distribution.

It may be noted that the second and third steps differentiate the EDAs from Genetic Algorithms by replacing the crossover and mutation operators. EDAs create a probabilistic model of the sample population and the new generation is based on this model. The main challenge faced by the EDAs

involves estimating an accurate distribution and thus creating a probabilistic model that can represent the structure of the given problem effectively. This has led to the development of various categories of EDAs, like UMDA, PBILA, Compact Genetic Algorithm, Bivariate Marginal Distribution Algorithm, Mutual Information Maximization for Input Clustering Algorithm, Bayesian Optimization Algorithm, etc. [26]. EDAs were used for solving a variety of problems such as scheduling [27-29], control design, [30] etc.

While solving QAP, EDA maintains during each generation $t$, a population of $m$ solutions $\Phi_{(t)}=\left\{\varphi^{1}{ }_{(t)}\right.$, $\varphi^{2}{ }_{(t)}, \varphi^{3}{ }_{(t)}, \ldots, \varphi^{m}{ }_{(t)}\}$ and a probability matrix $\Pi_{(t)}=\left(\begin{array}{ccc}n_{11(t)} & \cdots & n_{1 N(t)} \\ \vdots & & \vdots \\ n_{N 1(t)} & \cdots & n_{N N(t)}\end{array}\right)$ which models the distribution of solutions in $\Phi_{(t)}$. Figure 4 gives the pseudocode of general EDA.

In this work, two EDAs namely, UMDA and PBILA are used for developing algorithms.

### 4.1.1. Univariate marginal distribution algorithm

UMDA was proposed by Muehlenbein and Paaß [31], and it is one of the early works in the field of EDAs. This algorithm assumes that all the variables are independent, i.e. the value of variable $X i$ does not depend on the state of any other variable. It does not carry forward the probability of model in the previous generations. During each generation, a new population is produced based upon the model generated from the current population [32]. Figure 5 gives the pseudo-code of general UMDA.

### 4.1.2. Population-based incremental learning algorithm

PBILA is another simple EDA, and this also assumes no dependence among the variables. The statistical model in use is a real-valued vector with each element independently representing the probability of assigning value 1 to

1. $\Phi_{0} \leftarrow$ Generate the initial population ( $m$ individuals)
2. Evaluate the population $\Phi_{0}$
3. $t=l$
4. Repeat
a. $\Theta_{r . l} \leftarrow$ Select $n \leq m$ individuals from $\Phi_{r-1}$
b. Estimate / learn a new model $\Pi$ from $\Theta_{r . l}$
c. $\Phi_{\text {new }} \leftarrow$ Sample $m$ individuals from $\Pi$
d. Evaluate $\Phi_{\text {new }}$
e. $\Phi_{t} \leftarrow$ Select $m$ individuals from $\Phi_{t-1} \cup \Phi_{\text {new }}$
f. $t=t+1$

Until stop condition

Figure 4. Pseudo-code of General EDA.

1. Generate a population $\Phi$ of $m$ number of solutions
2. Select set $\Theta$ from $\Phi$ consisting of $n$ promising solutions, where $n<=m$
3. Estimate univariate marginal probabilities $\Pi\left(x_{i}\right)$ from $\Theta$ for each $x_{i}$
4. Sample $\Pi\left(x_{i}\right)$ to generate $m$ new individuals and replace $\Phi$
5. Go to step 2 until termination criteria are met

Figure 5. Pseudo-code of UMDA.
each corresponding bit in a binary string (candidate solution). PBILA starts with a probability vector with all elements set to 0.5 , which means that each bit in a generated individual is set to 0 or 1 with equal probability. During evolution, the value of each element is updated using the best individual in the population and drifts away from 0.5 , modifying its estimation of the structure of good individuals. Typically, PBILA will converge to a vector with each element close to 0 or 1 . During each generation, the probability vector is updated as per the equation $\Pi_{(t+1)}=(1-\boldsymbol{a}) \cdot \Pi_{(t)}+\boldsymbol{a} \cdot \boldsymbol{n}_{(t)}^{\text {Best }}$. But, instead of using best solution, the proposed algorithm uses all solutions in the current generation to update the probability vector. This is continued till the probability vector when rounded, becomes a valid solution [33]. Figure 6 gives the pseudo-code of general PBILA.

There are two decision parameters to be made, namely, (i) the value of the learning rate parameter, alpha (a) and (ii) the number of elite individuals ( $n$ ) used to update the vector. In the current study, alpha is set to 0.1 and $n$ is set to 10 .

### 4.2. 2-opt local search

In simple 2-opt local search method [34], the algorithm searches the set of all possible solutions resulting from swapping two distinct elements of the current solution and the best solution among all the resulting solutions replaces the current solution.

1. Initialize a probability vector $\Pi=\left\{\pi_{1}, \pi_{2}, \ldots, \pi_{N}\right\}$ with 0.5 at each position. Here, each $\pi_{i}$ represents the probability of 1 for the $i^{\text {th }}$ position in the solution.
2. Generate population $\Phi$ of $m$ solutions by sampling probabilities in $\Pi$
3. Select set $\Theta$ from $\Phi$ consisting of $n$ promising solutions, where $n<=m$
4. Estimate univariate marginal probabilities $\Pi\left(\pi_{i}\right)$ for each $\pi_{i}$
5. For each $i$, update $\pi_{i}$ using $\pi_{i}=\pi_{i}+\alpha\left(\Pi\left(\pi_{i}\right)-\pi_{i}\right)$
6. Go to step 2 until termination criteria are met.

Figure 6. The PBIL pseudo code.

However, in the recursive version of the 2-opt local search, if a better solution is found, it replaces the original solution and the search is restarted with the replaced solution as the central solution. This is continued till a solution with no better solution in its 2opt neighborhood is found. In this paper, a simple as well as recursive versions of 2-opt local search denoted by S2opt and R2opt are applied.

### 4.3. The proposed algorithm for the optimal layout of keyboard

The proposed algorithms start with $m$ random solutions. Each of the $m$ solutions then undergoes 2-opt local search (S2-opt or R2-opt) and the resulting population is the initial population, $\Phi_{0}=\left(n^{1}{ }_{00}, n^{n}{ }_{00}, n^{2}{ }_{00}, \ldots, n^{n}{ }_{00}\right)$. From $\Phi_{0}, n$ solutions are selected and the probability matrix $\Pi_{0}$ is calculated. For the next generation, the population, $\Phi_{1}$ is modeled using $\Pi_{0}$. This process is repeated until a termination criterion is reached. There are two algorithms and two local searches, which result in four different algorithms, namely, UMDA-S2opt, UMDA-R2opt, PBILAS2opt, and PBILA-R2opt. The four algorithms are coded in MATLAB and first tested for efficiency by solving benchmark problems taken from QAP Library [35]. The algorithms are then used to solve a test instance generated using the frequency list of English alphabets obtained from http://www.wiktionary.org [36] and seven famous books in English literature.

### 4.4. Parameter tuning

In order to find the best parameter combinations for the algorithms, a parametric optimization study has been conducted using Taguchi's robust design methodology. The parameters for the algorithms are number of maximum generations, population size, and elite population size for UMDA and maximum generations, population size, elite population size and learning rate (alpha) for PBILA. Since the local search does not have any parameter, only the base algorithm has to be optimized. For consistency, the parametric optimization is done for PBILA and the same values are applied for UMDA. The list of parameters with corresponding levels is given in Table 2.
alpha - learning rate, MG - maximum generation, PS - Population Size, EPS - Elite Population Size and Av - Average Solution

The orthogonal array for the DOE is L18 in which there is one parameter with six levels and all other three parameters with three levels each. In order to conduct the Taguchi's experiments an average-sized problem namely, esc16a from QAP Library is selected. Each experiment in the L18 array is done 10 times and the average is reported. Table 3 gives the result of the experiments.

Table 1. Summary of literature survey.

Table 2. List of Parameters and levels.

Table 3. Result of Taguchi's experiments.

From Figures 7 and 8, we can find out the optimal combination of parameters as alpha $=$ level $5=0.4$, maximum generation $=$ level $2=\mathrm{N}^{*} 10$, Population Size $=$ level $2=\mathrm{N}$ and Elite Population Size $=$ level $2=\mathrm{N} / 2$.

Table 4: Data for illustrations

![img-3.jpeg](img-3.jpeg)

Figure 7. Main effects plot for means from Taguchi's experiments.
![img-4.jpeg](img-4.jpeg)

Figure 8. Main effects plot for SN ratios from Taguchi's experiments.

Table 4. Distance Matrix. Flow Matrix.

## 5. Illustrative example

For a step-by-step illustration of the proposed algorithms, we consider a QAP with six facilities. This problem is derived from the benchmark problems on Dynamic Facility Layout problems provided by Balakrishnan and Cheng [37]. Table 4 gives the distance matrix of the departments and the material handling costs between departments.
5.1. Working of the proposed UMDA with S2opt
(1) Generate population $\Phi_{0}=\left(\begin{array}{cccccc}5 & 2 & 1 & 4 & 6 & 3 \\ 2 & 3 & 5 & 6 & 1 & 4 \\ & \vdots & & & \\ 3 & 5 & 6 & 2 & 1 & 4\end{array}\right)$ of $m$ random solutions.
(2) Run S2opt local search on each of the $m$ solutions.

$$
\Phi_{0}=\left(\begin{array}{cccccc}
3 & 1 & 2 & 4 & 6 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& \vdots & & & \\
6 & 5 & 2 & 4 & 1 & 3
\end{array}\right)
$$

(3) Calculate the objective function value as the material handling cost or transportation cost.

$$
\Phi_{T C}=\left(\begin{array}{c}
20253 \\
20253 \\
\vdots \\
20361
\end{array}\right)
$$

(4) Select set $\Theta$ from $\Phi$ consisting of $n$ promising solutions, where $n \leq m$.

$$
\Theta=\left(\begin{array}{cccccc}
1 & 3 & 2 & 6 & 4 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& \vdots & & & \\
6 & 4 & 5 & 1 & 3 & 2
\end{array}\right)
$$

(5) Estimate univariate marginal probabilities $\pi_{i j, j i}$ for each $(i, j)$ using $\Theta$

For calculating univariate marginal probabilities, convert each solution in $\Theta$ to the corresponding permuta-
tion matrix. For example, [1 32645$]=\left[\begin{array}{llllll}1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0\end{array}\right]$
Add the permutation matrices and divide it by $n$ to get $\Pi^{r} \quad\left[\begin{array}{llllll}2 & 0 & 5 & 2 & 0 & 3 \\ 5 & 0 & 2 & 3 & 0 & 2 \\ 0 & 7 & 0 & 0 & 5 & 0 \\ 3 & 0 & 2 & 5 & 0 & 2 \\ 2 & 0 & 3 & 2 & 0 & 5 \\ 0 & 5 & 0 & 0 & 7 & 0\end{array}\right]$
(6) Replace $\Pi$ with $\Pi^{r}$ and generate new population based on $\Pi$.
(7) Repeat steps 2 to 6 until termination criteria are satisfied. The termination criteria selected is the number of iterations and its value is $10 \times$ number of facilities.
(8) Save the solution with the lowest cost. The solution for the aforementioned problem is (1 3256 4) with a total cost of 20,253.

### 5.2. Working of the proposed PBILA with S2opt

(1) Initialize a probability matrix $\Pi$ as $N \times N$ matrix with all values set to $1 / N$. Here, each $(i, j)$ element in the matrix represents the probability that $j^{\text {th }}$ department is located in $j^{\text {th }}$ location.

$$
\Pi=\left[\begin{array}{lllll}
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 \\
1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6 & 1 / 6
\end{array}\right]
$$

(2) Generate population $\Phi=\left\{\begin{array}{lllll}5 & 2 & 1 & 4 & 6 & 3 \\ 2 & 3 & 5 & 6 & 1 & 4 \\ & & \vdots \\ 3 & 5 & 6 & 2 & 1 & 4\end{array}\right\}$ of $m$
solutions by sampling probabilities in $\Pi$.
(3) Run S2opt local search on each of the $m$ solutions.

$$
\Phi=\left\{\begin{array}{llll}
3 & 1 & 2 & 4 & 6 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& & \vdots \\
6 & 5 & 2 & 4 & 1 & 3
\end{array}\right\}
$$

(4) Calculate the objective function value.

$$
\Phi=\left\{\begin{array}{c}
20253 \\
20253 \\
\vdots \\
20361
\end{array}\right\}
$$

(5) Select set $\Theta$ from $\Phi$ consisting of $n$ promising solutions, where $n \leq p$.

$$
\Theta=\left\{\begin{array}{llll}
1 & 3 & 2 & 6 & 4 & 5 \\
4 & 6 & 5 & 3 & 1 & 2 \\
& & \vdots \\
6 & 4 & 5 & 1 & 3 & 2
\end{array}\right\}
$$

(6) Estimate univariate marginal probabilities $\pi_{i j, j)}^{\prime}$ for each $(i, j)$ using $\Theta$
For calculating univariate marginal probabilities, convert each solution in $\Theta$ to the corresponding permuta-
tion matrix. For example, [1 32645$]=\left[\begin{array}{lllll}1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0\end{array}\right]$
Add the permutation matrices and divide it by $n$ to get $\Pi^{\prime}$
i.e.

$$
\Pi=\frac{1}{12}\left[\begin{array}{lllll}
2 & 0 & 5 & 2 & 0 & 3 \\
5 & 0 & 2 & 3 & 0 & 2 \\
0 & 7 & 0 & 0 & 5 & 0 \\
3 & 0 & 2 & 5 & 0 & 2 \\
2 & 0 & 3 & 2 & 0 & 5 \\
0 & 5 & 0 & 0 & 7 & 0
\end{array}\right]
$$

(7) For each ( $i, j$ ), update $\Pi$ using $n_{(i, j)}=n_{(i, j)}+\alpha$ $\left(n_{i j, j)}^{\prime}-n_{(i, j)}\right)$

$$
\Pi=\left[\begin{array}{l}
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1
\end{array}\right]+\mathrm{0.4}\left[\left[\begin{array}{lllll}
0 & 5 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 15 & 00 & 12
\end{array}\right]-\left[\begin{array}{l}
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1
\end{array}\right]+\mathrm{0.4}
$$

(8) Repeat steps 2 to 7 until termination criteria are satisfied. Repeat steps 2 to 6 until termination criteria are satisfied. The termination criteria selected is the number of iterations and its value is $10 \times$ number of facilities.
(9) Save the solution with the lowest cost. The solution for the aforementioned problem is (1 32564 ) with a total cost of 20,253.

The logic of UMDA R2opt and PBILA R2opt can be derived from the aforementioned illustrations by replacing the S2opt local search with R2opt local search method.

## 6. Computational study

The computational experiments are carried out in three stages. First of all, the efficiency of the proposed algorithms is demonstrated by solving benchmark instances taken from QAP Library. In the second stage, the algorithms are applied to determine new layouts for the s-finger keyboard by solving a test instance generated from frequency list of letter pairs for English language. Finally, from the stage two, a keyboard with optimal layouts is obtained and experiments are conducted to validate the results obtained. The detailed description of each of these stages is given below.

### 6.1. Results and analysis - stage 1 experiments

To demonstrate the efficiency of the proposed algorithms, we consider 57 problems of size varying from 12 to 32 from QAP Library. All the problems were solved using the four proposed algorithms. Each problem was solved by each algorithm 10 times and the best, worst, and average solutions are reported. Table 5 gives the results of the efficiency tests along with the problem name and known best solution.

Table 6 gives the percentage variation of the best, worst, and average solutions from the known best solution. From the results presented in Tables

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

5 and 6 , it is evident that the proposed algorithms perform well while solving QAP. Out of the 57 problems solved using UMDA-S2opt, for 21 problems, the solution obtained is the same as that of the best-known solution. The corresponding number for UMDA-R2opt is 49. For PBILA-S2opt and PBILA-R2opt, the corresponding numbers are 24 and 47, respectively. For most problems which resulted in inferior solutions, the variation from known optimal solution is less than two percentage, which shows the efficiency of the proposed algorithms. Out of the four algorithms proposed, those with the R2opt local search perform better compared to those with S2opt local search.

### 6.2. Results and analysis - stage 2 experiments

We generated a test instance for determining a better layout for the s-finger keyboards. The test instance used in this study is the frequency lists of letter pairs taken from seven well-known books in English literature and the 10,000 most frequently used words in English language obtained from http://www.wiktionary.org. We have merged the frequency lists of all the seven books and the frequently used words to form a single list, which invariably represents the frequency list for English language. The books considered are as follows.

- The Alchemist by Paulo Coelho
- Alice's Adventures in Wonderland by Lewis Carroll
- Animal Farm by George Orwell
- Anna Karenina by Leo Tolstoy
- Othello by William Shakespeare
- The Odyssey by Homer
- Time Machine by H. G. Wells

These books are available to download in text format from https://www.gutenberg.org/[38]. The frequency list of letter pairs are calculated for each book separately and then all are added together to get the final list. While finding out the frequencies, punctuations and new paragraph characters are removed for simplicity. A script was coded in MATLAB to find out the frequency list of letter pairs of the selected books and words. Table 7 gives the frequency table for letter pairs.

The Fitts's times for the test instances in QWERTY keyboard and the ABC keyboard are given as 2,070,670.2 and 2,097,922.2, respectively. The corresponding Euclidean distances are 27,272,066.6 and 28,950,018.9, respectively. The results obtained for the different algorithms for the objective of minimizing the Fitts's time and the Euclidean distance are given in Table 8.

Table 6. Percentage deviation of best, worst, and average solutions from the known optimal solutions for the benchmark problems.

The layout corresponding to minimum value for Fitts's time is represented as $\boldsymbol{L 1}$ and the layout corresponding to the minimum value for Euclidean distance is represented as $\mathbf{L 2}$ in Table 8. The corresponding layouts are shown in Figures 9 and 10, respectively.

Table 9 shows the comparison of keyboard layouts L1 and L2 with QWERTY and ABC layouts in terms of Fitts's time and total Euclidean distance moved by the finger.

For both these cases, the Fitts's time as well as the Euclidean distance is very much lesser than that of QWERTY keyboard and ABC keyboard. This means that theoretically there is a chance of improvement in typing speed for single finger used text entry, if we change the layout of the keyboard. In order to validate this finding, we conducted physical experiments also, the details of which are presented in the following sub-section.

Table 7. The combined frequency list for letter pairs.
Table 8. Results of running algorithms for minimizing Fitts's time and Euclidean distance.
### 6.3. Results and analysis - stage 3 validation experiments

In order to validate the effectiveness of the new layouts, we conducted experiments by rearranging physical keyboards conforming to the obtained new layouts using Keytweak 2.3 software, which is free for use. The text
used for the experiments is a small poem "Stopping by Woods on a Snowy Evening" by Robert Frost. The punctuation marks and newline characters were removed from the poem and only the alphabets and spaces were keyed in during the experiment. The experiments were done in two steps, one with a person who is

Figure 9. Layout giving the best Fitts's time ( $L 1$ ).

Figure 10. Layout giving the best Euclidean distance ( $L 2$ ).

Table 9. Comparison of selected layouts with QWERTY and ABC layouts.

familiar with computers and is using the QWERTY keyboard for quite a long time, and other with a child who is not using computers and hence has no idea about the layout of the keyboards. The first person was given the new layouts and allowed to practice on the new keyboards for some time to make the layout somewhat familiar. After this familiarization period, the time for typing is noted and these values are shown in Table 10.

The time for typing using the QWERTY keyboard, in this case, is much lower than that for other layouts due to the fact that the person who did the experiments has been using the keyboard for a long time and is familiar with it.

In order to negate the effect of familiarity with QWERTY keyboard, we repeated the experiments with a 10-year-old child who is not familiar with

Table 10. Typing time of the selected text in seconds (QWERTY is familiar).
Table 11. Typing time of the selected text in seconds (QWERTY is not familiar).
computers. In this case also, the child was given time to practice in a layout for some time. The typing times obtained are shown in Table 11.

It is evident that the layouts $\mathbf{L 1}$ and $\mathbf{L 2}$ involve lesser time when compared with QWERTY and ABC layouts.

## 7. Conclusions

The popular electronic text entry devices, such as QWERTY and Dvorak keyboards, are optimized for 10 finger usages. Handheld electronic devices such as PDAs, smartphones, and Tablet PCs require revised layouts for the on-screen keyboard. In this work, new layouts for s-finger typing are introduced. Optimization algorithms combining EDAs and local search methods are developed for solving the QAPs. The effectiveness of the algorithms is verified using 57 benchmark instances of QAP taken from QAP Library. A test instance is developed using seven popular literary works in English and the word frequency list for English language. Based results of optimization of the test instances, two layouts are selected. The proposed layouts are validated by keying in a popular poem, "Stopping by Woods on a Snowy Evening" by Robert Frost.

From the results obtained, it is evident that the QWERTY and ABC layouts for the keyboards are not suitable for applications where s-finger typing is involved. These layouts are suitable for applications where all the 10 fingers are employed for pressing the keys. In devices such as mobile phones, PDAs, and Tablet PCs, it is better to use an improved layout to reduce the typing time using only a single finger. The proposed layouts $\mathbf{L 1}$ and $\mathbf{L 2}$ are promising layouts for the aforementioned devices. Moreover, the rearranging of keys does not require any effort on these devices and for each language used, the layout can be different also.

The research reported in this paper is limited to solve the single keyboard layout problem using only 27 keys, i.e. all the 26 alphabets and the space key. The present research can be extended for solving keyboard layout problem including other keys, such as numerals and symbols. Another research area could be incorporating multiple fingers of the same

hand while holding the device in the other hand, which require more ergonomic aspects also to be considered.

## Acknowledgments

The authors are thankful to the referees and the editor for their constructive suggestions and comments which have immensely helped to bring this paper to the present form.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Notes on contributors

T.G. Pradeepmon is a research scholar in the Department of Mechanical Engineering. He is pursuing research on the development of heuristics for solving QAPs. His areas of interest include supply chain management, combinatorial optimization, metaheuristics, and simulation.
Vinay V. Panicker is an Assistant Professor from the National Institute of Technology Calicut (NITC), Kerala, India, where he teaches courses on Supply Chain Management, Work System Design, and Statistics for Management. He has done research in the area of supply chain management for his doctoral degree from the NITC. His research interests focus in the areas of supply chain management, logistics management, and ergonomics. He has published technical papers in the referred international journals and proceedings of international and national conferences.
R. Sridharan is a Professor of Industrial Engineering in the Department of Mechanical Engineering at NITC, India. He received his PhD in 1995 from the Department of Mechanical Engineering from the Indian Institute of Technology, Bombay, India. His research interests include modeling and analysis of decision problems in supply chain management, job shop production systems, and flexible manufacturing systems. He has published papers in the referred international journals and proceedings of international and national conferences. He has been conferred with the Fellowship award by the National Council of Indian Institution of Industrial Engineering in 2017 for the outstanding contribution to the field of Industrial Engineering and the Institution.

## ORCID

T.G. Pradeepmon (s) http://orcid.org/0000-0002-1524-5831 Vinay V. Panicker (2) http://orcid.org/0000-0003-2167-3653 R. Sridharan (2) http://orcid.org/0000-0002-0186-6442
