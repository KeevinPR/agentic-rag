# Protein Folding in Simplified Models With Estimation of Distribution Algorithms 

Roberto Santana, Pedro Larrañaga, and Jose A. Lozano, Member, IEEE


#### Abstract

Simplified lattice models have played an important role in protein structure prediction and protein folding problems. These models can be useful for an initial approximation of the protein structure, and for the investigation of the dynamics that govern the protein folding process. Estimation of distribution algorithms (EDAs) are efficient evolutionary algorithms that can learn and exploit the search space regularities in the form of probabilistic dependencies. This paper introduces the application of different variants of EDAs to the solution of the protein structure prediction problem in simplified models, and proposes their use as a simulation tool for the analysis of the protein folding process. We develop new ideas for the application of EDAs to the bidimensional and tridimensional (2-d and 3-d) simplified protein folding problems. This paper analyzes the rationale behind the application of EDAs to these problems, and elucidates the relationship between our proposal and other population-based approaches proposed for the protein folding problem. We argue that EDAs are an efficient alternative for many instances of the protein structure prediction problem and are indeed appropriate for a theoretical analysis of search procedures in lattice models. All the algorithms introduced are tested on a set of difficult 2-d and 3-d instances from lattice models. Some of the results obtained with EDAs are superior to the ones obtained with other well-known population-based optimization algorithms.


Index Terms-Estimation of distribution algorithm (EDAs), hydrophobic-polar (HP) model, protein folding, protein structure prediction.

## I. INTRODUCTION

PROTEINS play a fundamental role in nature. These structures made of amino acids participate in many important tasks that guarantee the correct functioning of living cells. The protein structure is the result of the so-called protein folding process in which the initially unfolded chain of amino acids is transformed into its final structure. Under suitable conditions, this structure is uniquely determined by the sequence.

[^0]The complex and challenging nature of the protein folding process is highlighted by the Levinthal paradox [1]. If an unfolded protein were to attain its corrected folded configuration by sequentially sampling all possible configurations, then it would require a huge time exponential in the number of residues. This happens because each molecule could adopt an astronomical number of configurations. Nevertheless, proteins in nature can fold very quickly, often within a matter of seconds. Obviously, the protein folding does not proceed as an exhaustive search. Therefore, it is fundamental to understand how proteins attain their native configuration. However, the exact laws that govern the protein folding process are unknown, and the problem of finding the 3-d native structure of the protein given its sequence of amino acids is open.

Protein modeling and the computational simulation of protein mechanisms have proved to be valuable tools to answer the questions posed in the biological domain. Since it is difficult to scale modeling to a fine level of detail, some simplified models have been proposed in order to study, to different extents, the protein folding process. In this paper, we concentrate on a class of coarse-grained models that have been extensively used to study approximations of the protein folding problem. Using this model, we propose the use of estimation of distribution algorithms (EDAs) for two related problems: to find the native structure of the protein from its sequence, and to simulate the protein folding mechanism.

Most of the application results for EDAs on discrete problems have been achieved for problems with binary representation. Theoretical analysis of the EDA behavior for discrete problems is also mainly constrained to problems with binary representation. The use of protein coarse-grained models as a testbed for EDAs can help to advance the understanding of EDAs and to investigate their performance when applied to nonbinary problems. Coarse-grained models have also been 6 treated with a variety of optimization methods, allowing us to evaluate the performance of EDAs in comparison with these algorithms.

The protein model of choice is the hydrophobic-polar (HP) model [2], which is based on the fact that hydrophobic interactions are a dominant force in protein folding. The HP model has arisen as a suitable benchmark for cross-disciplinary studies involving domains such as computational biology, statistical and chemical physics, and optimization. This research has revealed different but related facets of the protein folding problem. In computational biology, the HP model has served to study sequence-structure mapping in proteins [3], to analyze the role of local structures in protein folding [4], and to study aspects related to protein design [5]. In statistical and chemical physics, the HP model has been used for exhaustive generation and analysis of protein conformations [6]. More recently, it has also


[^0]:    Manuscript received March 21, 2007; revised June 12, 2007. Published July 30, 2008 (projected). The work of J. A. Lozano was supported by Grant PR20060315, while at the University of California, San Diego. This work was supported in part by SAIOTEK-Autoimmune (II) 2006 Research Project from the Basque Government, and in part by the Etortek Research Project from the Basque Government, in part by the Spanish Ministerio de Ciencia y Tecnología under Grant TIN 2005-03824, and in part by the SGI/IZO-SGIker UPV/EHU (supported by the Spanish Program for the Promotion of Human Resources within the National Plan of Scientific Research, Development and Innovation-Fondo Social Europeo and MC y T), gratefully acknowledged for generous allocation of computational resources.
    R. Santana and J. A. Lozano are with the Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country, 20080 San Sebastian-Donostia, Guipuzcoa, Spain (e-mail: rsantana@si.ehu.es; ja.lozano@ehu.es).
    P. Larrañaga is with the Department of Artificial Intelligence, Technical University of Madrid, 28660 Boadilla del Monte, Madrid, Spain (e-mail: pedro. larranaga@fi.upm.es).

    Digital Object Identifier 10.1109/TEVC. 2007.906095

been used for doing folding and unfolding simulations [7] and to study density and ground states of the protein folding model [8], [9].

In the optimization domain, the search for the protein structure is transformed into the search for the optimal configuration given an energy function that takes into account the HP interactions that arise in the model. The problem of finding such a minimum energy configuration is NP-complete for the bidimensional (2-d)[10] and tridimensional (3-d) [11] lattices. Perfor-mance-guaranteed approximation algorithms of bounded complexity have been proposed to solve this problem [12], but the error bound guaranteed is not small enough for many applications.

The number of optimization heuristics applied to the HP model is extensive [13]-[19] with a significant number of the contributions made in recent years [20]-[30]. Work on evolutionary search applied to protein structure prediction and protein folding for lattice models and real proteins has been surveyed in [31]. A well documented review of current approaches to protein structure prediction is provided in [32].

In an early and very influential paper [19], Unger and Moult described a genetic algorithm (GA) application that used heuristic-based crossover and mutation operators to solve the HP model. The GA was able to outperform a number of variants of Monte Carlo methods at different sequences. Remarkably, the authors identified GAs as being particularly suited to reproducing some aspects of the protein folding process.

Although other GAs have been proposed to address the problem of structure prediction in the HP model, the difficulties of crossover operators to deal with this type of problem have been acknowledged [16], [33]. Particularly, it has been pointed out that one-point and uniform crossover do not perform well for this problem, and a number of explanations for this have been proposed [33]. Even if the GA results have been shown to improve by employing more sophisticated operators, another more general alternative is the conception of evolutionary algorithms able to learn and use the relevant interactions that may arise between the variables of the problem.

EDAs [34]-[37] are evolutionary algorithms that construct an explicit probability model of a set of selected solutions. This model can capture, by means of probabilistic dependencies, relevant interactions among the variables of the problem. The model can be conveniently used to generate new promising solutions. In [27], an EDA that uses a Markov probabilistic model outperformed other population-based methods when solving the 2-d protein folding problem. In the present paper, we further improve and generalize the results achieved in [27] by considering other types of probabilistic models, and by treating the more challenging class of 3-d simplified protein folding models. On the other hand, we investigate the use of EDAs as a simulating tool for the protein folding mechanism. Starting from current biological approaches to the protein folding process, and based on EDA capabilities to save and update probability models of the search, we provide evidence showing that EDAs can mimic the protein folding process to a certain extent, and more consistently than GAs.

This paper is arranged as follows. In Section II, we briefly review the biological concepts related to protein folding, and introduce the HP model and the functional model protein.

Section III reviews a number of previous approaches to the solution of simplified models using evolutionary and Monte Carlo-based algorithms. Section IV presents the class of EDAs. Section V introduces the problem representation and discusses how the probability model can capture the regularities that may arise in the HP problem. In Section VI, the probabilistic models and the EDAs used for the protein structure problem are introduced. This section also presents the EDA model of protein folding. In Section VII, the experimental benchmark is introduced and numerical results of our experiments are presented. Finally, in Section VIII, the conclusions of our research are given, and further work is discussed.

## II. Protein Folding

We will briefly recall some of the main biological concepts related to the protein folding problem that are relevant to our discussion.

Proteins are macromolecules made out of 20 different amino acids, also referred to as residues. An amino acid has a peptide backbone and a distinctive side chain group. The peptide bond is defined by an amino group and a carboxyl group connected to an alpha carbon to which a hydrogen and side chain group are attached.

Amino acids are combined to form sequences which are considered the primary structure of the peptides or proteins. The secondary structure is the locally ordered structure brought about via hydrogen bounding mainly within the peptide backbone. The most common secondary structure elements in proteins are the alpha helix and the beta sheet. The tertiary structure is the global folding of a single polypeptide chain.

Under specific conditions, the protein sequence folds into a unique native 3-d structure. Each possible protein fold has an associated energy. The thermodynamic hypothesis states that the native structure of a protein is the one for which the free energy achieves the global minimum. Based on this hypothesis, many methods that search for the protein native structure define an approximation of the protein energy and use optimization algorithms that look for the protein fold that minimizes this energy. These approaches mainly differ in the type of energy approximation employed and in the characteristics of the protein modeling.

The achievement of the protein native structure is the result of the so-called protein folding process. The laws that govern protein folding are unknown. Therefore a number of ideas have emerged that try to answer this question: how do amino acid sequences specify proteins 3-d structure?

There are two main approaches to protein folding, commonly referred as the "classical" and "new" views. The "classical" view considers folding as a defined sequence of states leading from the unfolded to the native state. This sequence is called the pathway [38]. In the "new" view approach, folding is seen as the progressive organization of an ensemble of partially folded structures through which the protein passes on its way to the folded structure [39]. This approach emphasizes the idea of each state being an ensemble of rapidly interconverting conformations. One of the main differences between both approaches is that the "new" view allows for a more heterogeneous transition

![img-0.jpeg](img-0.jpeg)

Fig. 1. Schematic representation of the "classical" (left) and "new" (right) views of protein folding.
state than the "classical" view, which concentrates on a single, well-defined folding pathway [40].

Fig. 1 shows one schematic representation of the "classical" (left) and "new" (right) views of protein folding. In the figure, each possible protein configuration is represented as a circle, and arrows represent possible transitions between configurations. In both approaches, the native state (filled circle) is achieved when the energy is minimized.

## A. The "New" View of Protein Folding

The EDA-based model of protein folding presented in this paper adopts the second view. Therefore, we must study in greater detail some of the aspects related to it.

In the "new" view approach, the energy landscape of a folding protein resembles a partially rough funnel. The local roughness of the funnel reflects transient trapping of the protein configurations in local free energy minima. Another important role is played by frustration.

There are two main sources of frustration in a protein [41]: energetical and topological. We will focus on energetical frustration which is associated with the amino acid sequence in the protein. It occurs when incorrect contacts are formed as the chain folds, when the sequence forces mismatched residues to be in contact in the native state or when there is competition between the protein interactions (i.e., not all of them can be simultaneously satisfied). The importance of frustration due to competing interactions and its influence in the emergence of highly multimodal search landscapes, which are difficult to optimize using GAs, have been studied in [42].

The emergence of frustration and other properties of proteins can be analyzed by using order parameters or progress coordinates which help to describe and quantify the protein ensembles during the protein folding process. They are used to explore the connection between the folding process and the topology of the protein native state. A parallel can be traced between the role of order parameters in protein folding and the role of parameters commonly used to describe the behavior of evolutionary algorithms (e.g., average fitness of the population at each generation, convergence and diversity measures, etc.) for functions of different difficulty.

Examples of order parameters are the contact order and the volume of the protein. Another quantifying measure is the
folding rate. The contact order of the protein is the average sequence separation between residues that make contact in the three-dimensional structure. The volume is a measure of the degree of folding of the protein, allowing distinction between compact and extended conformations. The folding rate is the amount of time the protein takes to fold.

In the case of small proteins, other measurements of the folding reactions can be made. Among them are the distribution of structures in the transition state ensemble, and the structure of the native state. The fraction of native contacts $Q$ that exist in the current conformation [43] can be used as a measure of frustration. For a given conformation, $Q$ varies between 0 and 1 , with the native conformation at $Q=1$. It is also possible to compute the total free energy $F_{\text {tot }}(Q)$ as a function of $Q$

$$
F_{\mathrm{tot}}(Q)=F_{\mathrm{int}}(Q)-T \cdot S_{\mathrm{conf}}(Q)
$$

where $F_{\text {int }}(Q)$ is the average internal energy of conformations with $Q$ native contacts, $T$ is the temperature of the system, and $S_{\text {conf }}(Q)$ is the corresponding conformational entropy (the logarithm of the number of accessible conformations with $Q$ native contacts) [40].

We enumerate a number of facts commonly accepted and explained in the "new" view of protein folding [39], [40], [43], [44]. Some of these issues will be investigated through simulation of the EDA-based model.

- The folding rates of small proteins correlate with their contact order. Proteins with a large fraction of their contacts between residues close in sequence tend to fold faster than proteins with more nonlocal interactions.
- Protein folding rates and mechanisms are largely determined by the protein native topology. Proteins with similar native states are expected to exhibit a similar protein folding behavior.
- Local interactions are more likely to form early in folding than nonlocal interactions.
- During the folding process, the energy of the structures will decrease on average as they become more and more similar to the native structure of a natural protein.
- Folding is not only determined by properties of the folded state but also by the energetic difference between the folded and unfolded ensembles of states.
- The geometrical accessibility of different native contacts is different, and therefore some are more easily formed than others.
- Some contacts may be topologically required (or at least be more likely) to be formed before others during folding.


## B. The HP and Functional Model Protein

This section briefly introduces the HP and functional model protein.

The HP model considers two types of residues: hydrophobic (H) residues and hydrophilic or polar (P) residues. A protein is considered a sequence of these two types of residues, which are located in regular lattice models forming self-avoided paths. Given a pair of residues, they are considered neighbors if they are adjacent either in the chain (connected neighbors) or in the lattice but not connected in the chain (topological neighbors).

![img-1.jpeg](img-1.jpeg)

Fig. 2. One possible configuration of sequence $H H H P H P P P P H$ in the HP model. There is one $H H$ (represented by a dotted line with wide spaces), one $H P$ (represented by a dashed line) and two $P P$ (represented by dotted lines) contacts.

The total number of topological neighboring positions in the lattice $\langle z\rangle$ is called the lattice coordination number.

For the HP model, an energy function that measures the interaction between topological neighbor residues is defined as $\epsilon_{H H}=-1$ and $\epsilon_{H P}=\epsilon_{P P}=0$. The HP problem consists of finding the solution that minimizes the total energy. In the linear representation of the sequence, hydrophobic residues are represented with the letter H and polar ones with P . In the graphical representation, hydrophobic proteins are represented by black beads and polar proteins, by white beads. Fig. 2 shows the graphical representation of a possible configuration for sequence $H H H P H P P P P H$. The energy that the HP model associates with this configuration is -1 because there is only one $H H$ contact, arisen between the second and fifth residues.

Although more complex models have been proposed [45]-[48], the HP model remains a focus of research in computational biology [3], [5], [6], [49] and chemical and statistical physics [7]-[9]. In evolutionary computation [17], [22], [26], [27], [29], [33], [50], the model is still employed given its simplicity and its usefulness as a testbed for new evolutionary optimization approaches.

The functional model protein is a "shifted" HP model. The name comes from the fact that the model supports a significant number of proteins that can be characterized as functional. This model has native states, some of which are not maximally compact. Thus, in some cases, they have cavities or potential binding sites, a key property that is required in order to investigate ligand binding using these models [51]. The energy values associated with the model contain both attractive $\epsilon_{H H}=-2$ and repulsive interactions ( $\epsilon_{P P}=1, \epsilon_{H P}=1$, and $\epsilon_{P H}=1$ ). Again, the objective is to minimize the total energy. For example, the energy that the functional model protein associates with the configuration shown in Fig. 2 is 1 because there is one $H H$ (represented by a wide dotted line), one $H P$ (represented by a dashed line) and two $P P$ (represented by dotted lines) contacts.

## III. REVIEW OF PREVIOUS EVOLUTIONARY METHODS

Previous population-based approaches to simplified protein folding include the use of nature-inspired and Monte Carlo methods [52]. Some versions of these methods are compared with EDAs in the experiments section.

Since the publication of the Unger and Moult paper [19] on the use of GAs for protein structure prediction, new issues have arisen along with new points of view on the protein folding problem. However, GA applications to the HP problem are many and varied. In [15], a search strategy called pioneer search was used together with a simple GA. Although the algorithm improved some of the results achieved in [19], it was unable to
find the optimal solutions for the longest instances considered. In [30], a GA with specialized genetic operators was used to solve HP sequences up to 50 residues. The algorithm found the best solutions for the six sequences tried, but increasing the GA efficiency was acknowledged to be a requirement for solving longer sequences.

In [21] and [53], evolutionary algorithms for the 3-d HP problem are proposed. While in [53] a simple GA showed no better results than those achieved in [19], a more sophisticated approach is presented in [21]. By using a backtracking-based repairing procedure, the latter algorithm guarantees that the search is constrained to the space of legal solutions. Since the number of self-avoided paths on square lattices is exponential in the length of the sequence [19], generating legal solutions with a backtracking algorithm is a feasible alternative.

The multimeme algorithm (MMA) for protein structure prediction [17] is a GA combined with a set of local searches. From this set, the algorithm self-adaptively selects which local search heuristic to use for different instances, states of the search, or individuals in the population. This algorithm was used to find solutions of the functional model protein. A relevant issue of this algorithm is the use of a contact map memory as a way to collect and use important problem information. Contact maps abstract the geometric details of the structures, keeping only the essential topological features of the configurations. In [26], MMA was extended by the incorporation of fuzzy-logic-based local searchers. The modifications led to obtain a more robust algorithm that improved previous MMA results in the protein structure prediction problem. Memetic algorithms were also combined with a population of rules [29] to solve the HP model in a two-dimensional triangular lattice. The algorithm proposed outperformed simple versions of GAs and memetic algorithms.

Different variants of immune algorithms (IAs) [22], [23], [50] have been proposed for the HP problem. These evolutionary algorithms inspired in the theory of clonal selection, use hypermacromutation and aging as important operators to proceed the search. In [50], the algorithm found the optimal configurations of the regular 2-d HP model for the smallest problems. The algorithm failed to find the optimum for the longest instances. In [22], the original IA is developed to include a memory mechanism that improves results for the 2-d regular lattice. Recently, IA has been used with very good results to solve HP problems on the 3-d lattice and instances from the functional protein model [23].

Traditional Monte Carlo methods that use Markov chains sample from the protein folding space one point at a time. Due to the rugged landscape, these methods tend to get trapped in local minima. New Monte Carlo methods have been proposed to cope with these problems [54]. Among the alternatives proposed, two main classes of the strategies used by the Monte Carlo methods can be distinguished: to use chain growth algorithms [13], or to sample the space with a population of Markov chains in which a different temperature is attached to each chain [55]. Chain growth algorithms [25], [56]-[58] such as the pruned-enriched Rosenbluth method (PERM) [25] are based on growing the sequence conformation by successively adding individual particles, guiding the growth towards configurations with lower energies, and using population control to eliminate bad configurations and increase good ones [58].

Although chain growth methods have achieved some of the best results for HP models in regular 2-d and 3-d lattices, it is important to emphasize that algorithms such as PERM combine the process of constructing the solutions with the evaluation step of the solutions. Even if this strategy allows one to use more information about the HP fitness function, it lacks generality because it cannot be applied to problems where subsolutions cannot be independently evaluated.

All the above-mentioned algorithms either use genetic operators or Markov chain transitions. They do not use any model of the search space. An algorithm that incorporates, to a certain scale, the modeling step is the ant colony optimization (ACO) method presented in [18] and [28]. In this approach, the simulated ants construct candidate conformations for a given HP protein sequence, apply a local search to achieve further improvement, and update a probability value based on the quality of the solutions found. In ACO terminology, this value is called the pheromone trail.

Additionally, we mention that there are several examples of the application of GAs and other evolutionary algorithms to protein structure prediction problems using more complex protein models. For a review on evolutionary algorithms and other optimization methods applications to protein problems, [59], [60] can be consulted. We briefly analyze some connections between the use of evolutionary algorithms for simple and more complex protein models.

While more complex protein folding models (e.g., rotamerbased protein models [45]) can provide more realistic results in some protein folding and protein design studies, they are of limited use for other tasks (e.g., the exhaustive generation and analysis of protein configurations for many instances). Similarly, there are successful applications of EDAs to rotamer-based protein models [61], [62], but the complexity of these models would not allow one to conduct the sort of detailed analysis that will be presented in Section V. To summarize, the decision of using the HP or more complex protein models will depend on the type of optimization or simulation tasks addressed.

However, the application of GAs to more complex models can provide clues for the simulations done with simpler models. In [63], an evolutionary algorithm is applied to de novo all-atom folding of a protein comprising 60 aminoacids. The authors use the concept of "native content" of the population of solutions to evaluate convergence of the algorithm. A related idea will be presented in Section VII-E1, where we use the number of native contacts to investigate the way in which our evolutionary algorithm samples the energy landscape of the function.

In [64], a GA is used for protein structure prediction of 28 fragments of protein structures up to 14 residues long. The search is done in the torsion space of the protein atoms. The GA protocol is successful in finding a lower energy than the corresponding minimized structure in 26 out of the 28 cases examined. The high computational cost of the algorithm is attributed by the authors to the difficulty of finding acceptable crossover conformations. We notice that one of the advantages of EDAs is their ability to avoid the disruption caused in the structure of the solutions by crossover operators.

Results achieved in [62]-[64] also show that in the case of protein structure prediction with complex models the addition
of local optimization techniques to GAs and EDAs may be a requirement for attaining realistic protein conformations.

Even though this short overview has focused on Monte Carlo and nature inspired methods, we emphasize that there are several applications of heuristic algorithms to the protein structure problem that are beyond the scope of this paper.

## IV. Estimation of Distribution Algorithms

The results of the GAs for the protein structure problem can be improved by designing heuristic-based genetic operators. However, the improvements are constrained by the narrow scope of application of these types of knowledge-based operators. A more robust solution is the use of evolutionary algorithms able to use probabilistic models of the search space.

EDAs replace the traditional crossover and mutation operators used in GAs by probabilistic models. These algorithms construct, in each generation, a probabilistic model that estimates the probability distribution of the selected solutions. The probabilistic model must be able to capture, in the form of statistical dependencies, a number of relevant relationships among the variables. Dependencies are then used to generate solutions during a simulation step. It is expected that the generated solutions share a number of characteristics with the selected ones. In this way, the search leads to promising areas of the search space.

EDAs can be seen as a development of GAs. By recombining a subset of selected solutions, GAs are able to process the information learned during the search, and to orient the exploration to promising areas of the search space. Nevertheless, it has been proved that GAs experience limitations in their capacity to deal with problems where there are complex interactions between different components of the solutions [65], [66]. In these scenarios, EDAs can exhibit a better performance. The success of EDAs in the solution of different practical problems has been documented in the literature [34].

The general scheme of the EDA approach is shown in Algorithm 1. The selection method employed can be any of those traditionally used by GAs. In the literature, truncation, Boltzmann, and tournament selection are commonly used with EDAs. A key characteristic and crucial step of EDAs is the construction of the probabilistic model. These models may differ in the order and number of the probabilistic dependencies that they represent.

## Algorithm 1: Main scheme of the EDA approach

1. $D_{0} \leftarrow$ Generate $M$ individuals randomly
2. $l=1$
3. do $\{$
4. $D_{l=1}^{s} \leftarrow$ Select $N \leq M$ individuals from $D_{l-1}$ according to a selection method
5. $p_{l}(\boldsymbol{x})=p\left(\boldsymbol{x} \mid D_{l=1}^{s}\right) \leftarrow$ Estimate the joint probability of selected individuals
6. $D_{l} \leftarrow$ Sample $M$ individuals (the new population) from $p_{l}(\boldsymbol{x})$
7. $\}$ until A stop criterion is met

TABLE I
The DENSITY of the Different ENERGY LEVELS $H P_{f}$ and $F P_{f}$ CORRESPONDING TO the HP and Functional Model Protein of Sequence HHH P P P P P H

Different classifications of EDAs can be used to analyze these algorithms. Relevant to our research is the classification according to the complexity of the models used to capture the interdependencies between the variables [67]. Considering methods of learning is done in the probability model, EDAs can be divided into two classes. One class groups the algorithms that do a parametric learning of the probabilities, and the other comprises those algorithms that also undertake structural learning. Parametric and structural learning are also known as model fitting and model selection. To the first class, belong population-based incremental learning (PBIL) [68], compact GA (cGA) [69], the univariate marginal distribution algorithm (UMDA) [36], and the factorized distribution algorithm that uses a fixed model of the interactions in all the generations (FDA) [66]. Among EDAs that do a structural learning of the model, are the mutual information maximization for input clustering algorithm (MIMIC) [70], the extended compact GA (EcGA) [71], and EDAs that use Bayesian networks [72]-[74].

## V. DEPENDENCIES IN THE SIMPLIFIED PROTEIN MODELS

In this section, we show evidence on the emergence of regularities in the search space of the HP model. In order to achieve this goal, we employ the Boltzmann probability distribution. We start by introducing the problem representation.

## A. Problem Representation

Let $n$ be the sequence length. We use $X_{i}$ to represent a discrete random variable. A possible value of $X_{i}$ is denoted $x_{i}$. Similarly, we use $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ to represent an $n$-dimensional random variable and $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ to represent one of its possible values. For a given sequence and lattice, $X_{i}$ will represent the relative move of residue $i$ in relation to the previous two residues.

Taking as a reference the location of the previous two residues in the lattice, $X_{i}$ takes values in $\{0,1, \ldots, z-2\}$, where $z-1$ is the number of movements allowed in the given lattice. These values, respectively, mean that the new residue will be located in one of the $z-1$ numbers of possible directions with respect to the previous two locations. Therefore, values for $X_{1}$ and $X_{2}$ are meaningless. The locations of these two residues are fixed. A solution $\mathbf{x}$ can be seen as a walk in the lattice, representing one possible folding of the protein. The codification used is called relative encoding, and has been experimentally compared with absolute encoding in [16], showing better results.

We use 2-d and 3-d regular lattices. For regular $d$-dimensional lattices, $z=2 d$, where $d$ is the lattice dimension.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Best solutions of the functional model protein (left) and HP model (right) for sequence HHH P H P P P P H. The optimal energy values are -4 and -2 for the functional and HP model, respectively. HH contacts are shown using dotted lines with wide spaces.

## B. Regularities and Dependencies in the HP Model

We illustrate the emergence of regularities in the search space of the HP model using the HHHPHPPPPH sequence, introduced in [51]. For this sequence, and using the representation previously introduced, we find all possible solutions and evaluate them according to the HP and functional protein energy functions. The number of solutions evaluated are $3^{9}=19683$. Of these configurations, 8658 are not self-avoiding and they are assigned a very high energy equal to 100 . In Table I, $H(\mathbf{x})$ denotes all the possible values that the two evaluated energy functions can reach for sequence HHHPHPPPPH. $H P_{f}$ and $F P_{f}$, respectively, indicate the number of solutions where the corresponding value of $H(\mathbf{x})$ has been achieved for the HP and functional protein energy functions.

It is important to highlight that there is not a one-to-one mapping between each solution and each state of the sequence. The reason is that one state can have more than one solution representation, i.e., the representation is redundant. For instance, while there exists only one optimal state for the functional model protein, in our representation, this optimal state has two possible representations corresponding to symmetrical configurations. In the case of the HP model, there are 16 optimal solutions. Fig. 3 shows optimal configurations for the functional model protein and the HP model.

To associate a probability value with every point of the search space, we will use a theoretical benchmark based on the Boltzmann distribution. In this benchmark, the probability of each solution is equal to the Boltzmann distribution calculated from the energy evaluation

$$
p(\mathbf{x})=\frac{e^{\frac{-H(\mathbf{x})}{\tau}}}{\sum_{\mathbf{x}^{\prime}} e^{\frac{-H(\mathbf{x}^{\prime})}{\tau}}}
$$

where $H(\mathbf{x})$ is the energy of $\mathbf{x}$ and $t$ is the temperature.

TABLE II
Marginal Probability Distributions for $\left(X_{3}, X_{4}, X_{5}\right)$ CALCULATED From the Boltzmann Distributions for HP and the Functional Model Protein for Sequence HHHPPPPPPH


Equation (2) shows the expression of the Boltzmann distribution. We set the temperature at 1 , but $t$ can be changed to simulate different experimental conditions. The Boltzmann distribution is a natural candidate for the fitness distribution. From a theoretical point-of-view, the Boltzmann distribution allows one to associate probabilistic independence properties between the variables of the problem with certain characteristics of the energy function [66]. It exhibits another convenient feature: higher probabilities are associated with points of the search space with better function evaluation. Therefore, these probabilities describe the desired performance of an ideal optimization algorithm: better points are visited with a higher probability. The Boltzmann distribution has also been used together with Monte Carlo-based methods for HP model optimization [55].

From the Boltzmann distribution, it is possible to compute the marginal probability distribution of any subset of variables by marginalization. This process is feasible in our case because the total number of configurations $\left(3^{3}\right)$ is relatively small. Therefore, we calculate the marginal probability distributions corresponding to variables $\left(X_{3}, X_{4}, X_{5}\right)$ for probability distributions $p_{H P}$ and $p_{F P}$, which are shown in Table II. The table shows the marginal probabilities of the $3^{3}$ configurations (from 000 to 222) of variables $\left(X_{3}, X_{4}, X_{5}\right)$.

In Table II, the lowest probability values are bold-faced, while the highest values are underlined. The two configurations with zero probability ${ }^{1}$ are shown in Fig. 4, where the direction of the sequence is represented as an arrow between the first and second residue of the sequence. Not surprisingly, these are the only two self-intersecting configurations that can be formed with three contiguous moves. Any solution that contains subchains 000 or 222 is not self-avoiding, and therefore receives a very low probability.

The two configurations with the highest probabilities are shown in Fig. 5. These are two symmetrical helices. In the

[^0]HP and functional model protein, these type of substructures can give an important contribution to the final energy. Helices are present in the optimal solutions for both models, shown in Fig. 3.

A remarkable difference between the marginal probabilities corresponding to the HP and functional model protein is related to the probabilities given to the helices. The difference between the probabilities of the best and second best configurations is 0.012 for the HP model, and 0.06 for the functional model protein. This gives an idea of the difference due to the energy function used.

One conclusion from this experiment is that if we assume that subsolutions with highest probabilities in the model are those that represent optimal problem substructures (i.e., those likely to be present in the optimal solutions), then we can identify optimal substructures by inspecting the marginal distributions from the search distribution. These substructures are likely to be present in those population-based optimization algorithms able to respect the relevant interactions between the variables. In EDAs, the mapping between the problem structure and the probabilistic dependencies represented in the structure and parameters of the probabilistic models allows the use of the models as a source of information about the problem.

We investigate the effect that disregarding the potential interactions between variables may have on the modeling of the problem. In the next experiment, a univariate probability approximation of $p\left(x_{3}, x_{4}, x_{5}\right)$ is calculated. First, univariate marginal distributions are calculated for the three variables, $p\left(x_{i}\right)=\sum_{X_{i}=x_{i}} p(\mathbf{x})$. Afterwards, the approximation $p_{a}\left(x_{3}, x_{4}, x_{5}\right)$ is computed as the product of the univariate marginals $p_{a}\left(x_{3}, x_{4}, x_{5}\right)=p\left(x_{3}\right) p\left(x_{4}\right) p\left(x_{5}\right)$. The approximation is shown in Table III.

As in Table II, the lowest probability values are bold-faced, while the highest values are underlined. Due to the effect of rounding, some other configurations appear in the table with equal (rounded) probabilities than the lowest (respectively, highest) ones.

In Table III, it can be observed that the best and worst configurations do not agree with the ones obtained using the whole three-variate marginal probability distribution. The univariate approximation is not able to capture the structural features of the problem represented in Table II. This experiment illustrates the convenience of using higher order interactions to capture relevant features of the problem structure. As it has been analyzed in previous sections, traditional crossover operators do not respect these interactions. Furthermore, as explicit modeling of the search space is missing in most of nature-inspired algorithms, it is impossible to detect, represent, and store these regularities efficiently. In the following sections, we show how different probability models can detect and exploit this information.

The experiments presented in this section have been conducted using a single HP instance. Obviously, there are other factors that influence the marginal probability distributions corresponding to the different energy models. We have focused on showing the way in which structural regularities are exposed by the probability models learned. The analysis of other factors is beyond the scope of this paper.


[^0]:    ${ }^{1}$ Strictly speaking, the probabilities are never zero but they approximate this value.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Self-intersecting short paths: configurations with zero probability.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Short helices: configurations with the highest probability.

TABLE III
Univariate APPROXIMATION OF THE Marginal Probability of $\left(X_{3}, X_{4}, X_{5}\right)$ Calculated From the Boltzmann Distributions for HP and Functional Model Protein for Sequence HHHPHPPPPPH


## VI. EDAs for Protein Structure Prediction

The existence of regularities in the search space, expressed in probabilistic dependencies between subsets of variables naturally leads to the convenience of using EDAs to take advantage of these regularities by capturing the dependencies. Probability models used by EDAs are built from the selected set of solutions. Therefore, the type of selection method used also influences the number and strength of the interactions learned by the model. Similarly to the Boltzmann distribution analyzed before, selection methods assign higher selection probabilities to solutions with higher fitness value.

In this section, we detail the main contributions of this paper: the introduction of EDAs to face the solution of the protein structure prediction problem, and the definition of the EDAbased model of protein folding. The section starts by introducing the probability models used by EDAs and explaining the rationale behind our choice. Finally, we define the EDA-based model of protein folding and describe the analogies between this model and some of the known behavioral characteristics of protein folding.

## A. Probabilistic Models and Algorithms

We propose three types of probabilistic models to be applied to the protein structure prediction problem. In every case, solutions are represented using the vector representation introduced in Section V-A. Probabilistic models are presented together with the EDA that uses the model. EDAs are named according to the probability model that they use.

The first model considered is a $k$-order Markov model in which the configuration of variable $X_{i}$ depends on the configuration of the previous $k$ variables, where $k \geq 0$ is a parameter of the model. The joint probability distribution can be factorized as follows:

$$
p_{M K}(\mathbf{x})=p\left(x_{1}, \ldots, x_{k+1}\right) \prod_{i=k+2}^{n} p\left(x_{i} \mid x_{i-1}, \ldots, x_{i-k}\right)
$$

The pseudocode of the Markov EDA $\left(\mathrm{MK}-\mathrm{EDA}_{k}\right)$ is shown in Algorithm 2. The main step is the parametric learning of the probabilistic model. Since the structure of the Markov model is given, this step comprises to calculate the frequencies from the set of selected individuals and to compute the marginal and conditional probabilities. To sample a solution, first variables in the factor $\left(x_{1}, \ldots, x_{k+1}\right)$ are generated and the rest of variables are sampled according to the order specified by the Markov factorization.

## Algorithm 2: Markov-EDA

1. $D_{0} \leftarrow$ Generate $M$ individuals randomly
2. $l=1$
3. do $\{$
4. $D_{l-1}^{s} \leftarrow$ Select $N \leq M$ individuals from $D_{l-1}$ according to a selection method
5. Compute the marginal and conditional probabilities corresponding to each factor of factorization (3)
6. $D_{l} \leftarrow$ Sample $M$ individuals (the new population) from the $k$-order Markov model
7. $\}$ until A stop criterion is met

The second probabilistic model is based on a tree where each variable may depend on no more than one variable that is called the parent. A probability distribution $p_{\text {Tree }}(\mathbf{x})$ that is conformal with a tree is defined as

$$
p_{\text {Tree }}(\mathbf{x})=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

where $P a\left(X_{i}\right)$ is the parent of variable $X_{i}$ in the tree, and $p\left(x_{i} \mid p a\left(x_{i}\right)\right)=p\left(x_{i}\right)$ when $P a\left(X_{i}\right)=\emptyset$, i.e., when $X_{i}$ is the root of the tree. The distribution $p_{\text {Tree }}(\mathbf{x})$ itself will be called

a tree model when no confusion is possible. Probabilistic trees are represented by acyclic connected graphs.

The pseudocode of the tree-based EDA (Tree-EDA) is shown in Algorithm 3.

## Algorithm 3: Tree-EDA

1. $D_{0} \leftarrow$ Generate $M$ individuals randomly
2. $l=1$
3. do $\{$
4. $\quad D_{l-1}^{s} \leftarrow$ Select $N \leq M$ individuals from $D_{l-1}$ according to a selection method
5. Compute the univariate and bivariate marginal frequencies $p_{i}^{s}\left(x_{i} \mid D_{l-1}^{s}\right)$ and $p_{i, j}^{s}\left(x_{i}, x_{j} \mid D_{l-1}^{s}\right)$ of $D_{l-1}^{s}$
6. Calculate the matrix of mutual information using the univariate and bivariate marginals
7. Calculate the maximum weight spanning tree from the matrix of mutual information
8. Compute the parameters of the model
9. $\quad D_{l} \leftarrow$ Sample $M$ individuals (the new population) from the tree
10. \} until A stop criterion is met

As presented in Algorithm 3, the bivariate probabilities are initially calculated for every pair of variables. From these bivariate probabilities, the mutual information between variables is found. To construct the tree structure, an algorithm introduced in [75], that calculates the maximum weight spanning tree from the matrix of mutual information between pairs of variables is used. To sample the solutions from the tree, we have used probabilistic logic sampling (PLS) [76], first the root variable is instantiated, and following the tree structure each variable is sampled conditioned on its parent.

The third model considered is a mixture of trees [77]. A mixture of trees is defined as a distribution of the form

$$
p_{\mathrm{MT}}(\mathbf{x})=\sum_{j=1}^{m} \lambda_{j} p_{\mathrm{Dee}}^{j}(\mathbf{x})
$$

with $\lambda_{j}>0, j=1, \ldots, m, \sum_{j=1}^{m} \lambda_{j}=1$.
In this case, the tree distributions are the mixture components. The $m$ trees may have different structures and different parameters.

MT $-\mathrm{EDA}_{m}$ is the name given to the EDA that uses a mixture of trees, $m$ being the number of components in the mixture. MT $-\mathrm{EDA}_{m}$ 's pseudocode is shown in Algorithm 4.

To learn a mixture of trees that gives a good approximation of the selected individuals we use an expectation-maximization (EM) mixtures of trees learning algorithm that was originally introduced in [77]. The idea underlying the EM algorithm is to compute and optimize the expected value of a likelihood function which is the log-likelihood of both, the observed and the
unobserved data, given the current model estimate. The EM algorithm alternates the expectation and maximization steps until one stop condition is satisfied. To learn the structure of each component, the tree learning method used by Algorithm 3 is employed. More details about the mixture of trees learning algorithm can be found in [77] and [78]. To sample the solutions from each component the PLS method is used.

## Algorithm 4: Mixtures of Trees EDA

1. $D_{0} \leftarrow$ Generate $M$ individuals randomly
2. $l=1$
3. do $\{$
4. $D_{l=1}^{s} \leftarrow$ Select $N \leq M$ individuals from $D_{l-1}$ according to a selection method
5. Compute a mixture of trees $Q$ using the EM algorithm.
6. Compute the parameters of the model
7. $D_{l} \leftarrow$ Sample $M$ individuals (the new population) from $Q$
8. \} until A stop criterion is met

The probability models used by the previous EDAs can be separated into two classes according to the part of the problem structure that they exploit. The first class of probability models is based on the existence of connected neighbors. The assumption behind the use of Markov models is that the most important source of problem interactions comes from the connected neighbors. Markov models have been used in computational biology to identify coding regions in proteins, to align sequences, and to predict the protein secondary structure.

The second class of models allows for the existence of arbitrary connections between the variables of the problem subject to the representation constraints determined by the probabilistic models. This choice of the models tries to capture interactions arising from both, connected and topological neighbors. Therefore, algorithms that learn the structure of the model from the data [75], [77] are incorporated. Models that belong to this class differ in the type of structural constraints they represent.

Initial results of an EDA based on the Markov model, for the solution of 2-d lattice problems, were presented in [27]. These EDAs make a parametric learning of the model. An EDA called combining optimizers with mutual information trees, which searches for probabilistic models that can be represented using tree-shaped networks was introduced in [65]. MT-EDA was originally presented in [78]. All these algorithms have mainly been applied to binary problems. Poor results for preliminary experiments conducted using EDAs based on unconstrained Bayesian networks [72] determined to discard these algorithms from our experimental benchmark.

## B. Implementation

In the chosen representation, there might be invalid vectors that correspond to self-intersecting sequences. To enforce the

validity of the solutions, we employ a variation of the backtracking method used in [21]. A solution is incrementally repaired in such a way that the self-avoidance constraint is fulfilled. At position $i$, the backtracking call is invoked only if self-avoidance cannot be fulfilled with any of the possible assignments to $X_{i}$. The order in which values are assigned to each variable is random. If all the possible values have been checked, and self-avoidance is not fulfilled yet, backtracking is invoked.

On the other hand, if the number of backtracking calls have reached a prespecified threshold, the repair procedure is abandoned. This is a compromise solution for situations in which the repair procedure can be too costly in terms of time. The threshold for the number of backtracking calls was set to 500 and this value was determined empirically. Further details about the original backtracking algorithm can be found in [21].

In our implementation of EDAs, ${ }^{2}$ the truncation selection of parameter $T=0.1$ is used. Let $M$ be the population size. In this type of selection, the best $N=T \cdot M$ individuals, according to their function evaluations, are selected. We use best elitism, a replacement strategy where the population selected at generation $t$ is incorporated into the population of generation $t+1$. Thus, only $M-N$ individuals are generated at each generation except the first one. All the EDAs have been implemented in C++ language. All the experiments have been executed in a Pentium III processor with 933 MHz .

## C. Computational Cost of the Algorithms

In this section, we analyze the computational cost of the different steps of the EDAs proposed for the protein structure prediction problem. The complexity of some of the steps are common to all the algorithms. Since the complexity of the algorithms depends on the cardinality of the variables, we use $r_{\mathrm{MAX}}=\max _{i \in 1, \ldots, n}\left|X_{i}\right|$ to represent the highest cardinality among the variables.

1) Initialization: The initialization step of all the algorithms consists in randomly initializing all the solutions in the first population. It has complexity $O(n M)$.
2) Evaluation: The computational cost of this step is problem dependent. It will depend on the function implementation. Let $\operatorname{cost}_{f}$ be the running time associated to the evaluation of function $f$, the running time complexity of this step is $O\left(M \cos t_{f}\right)$.
3) Selection: The complexity of the selection step depends on the selection method used. Truncation selection consists on selecting the $\tau M$ best individuals of the population. In the worst case, the complexity of this step is $O(M \log (M))$.
4) Probabilistic Model Learning Algorithms: The cost of the learning step changes for each algorithm.

- $\mathrm{MK}-\mathrm{EDA}_{k}$ : Computing the marginal probabilities used by $\mathrm{MK}-\mathrm{EDA}_{k}$ implies computing the $n-k$ marginal probability tables from the selected population, it has complexity $O((n-k) N)$.
- Tree-EDA: Computing the bivariate marginal probabilities used by Tree-EDA has complexity $O\left(n^{2} N\right)$. The
[^0]calculation of the mutual information has complexity $O\left(n^{2} r_{\mathrm{MAX}}^{2}\right)$. The step that returns the maximum weight spanning tree has complexity $O\left(n^{2}\right)$. The total complexity of Tree-EDA is $O\left(n^{2} N+n^{2} r_{\mathrm{MAX}}^{2}\right)$.
- MT - EDA $_{m}$ : The running time of EM for mixtures of trees was calculated in [77]. The total time complexity is $O\left(m n^{2} N+m n^{2} r_{\mathrm{MAX}}^{2}\right)$. Notice that, as expected, the complexity is equal to the complexity or learning a tree scaled by the number of components $m$.

5) Sampling: The cost of the sampling step changes for each algorithm. MK - EDA $_{k}$ : Sampling $M$ individuals from the Markov models has a complexity order $O\left((n-k) M r_{\mathrm{MAX}}^{k}\right)$.

Tree-EDA: Sampling $M$ individuals with a tree has a complexity order $O\left(n M r_{\mathrm{MAX}}^{2}\right)$.
MT - EDA $_{m}$ : Sampling $M$ individuals with a mixture of trees has a complexity order $O\left(m n M r_{\mathrm{MAX}}^{2}\right)$.
6) Total Computational Costs of the Algorithms: The total computational costs of algorithms $\mathrm{MK}-\mathrm{EDA}_{k}$, Tree-EDA, and MT - EDA $_{m}$ are, respectively, $O\left(G\left((n-k) M r_{\mathrm{MAX}}^{k}+\right.\right.$ $\left.\left.M \cos t_{f}\right)\right), O\left(G\left(n^{2} M+n^{2} r_{\mathrm{MAX}}^{2}+n M r_{\mathrm{MAX}}^{2}+M \cos t_{f}\right)\right)$, and $O\left(G\left(m n^{2} M+m n^{2} r_{\mathrm{MAX}}^{2}+m n M r_{\mathrm{MAX}}^{2}+M \cos t_{f}\right)\right)$, where the population size $M$ and the number of generations $G$ change according to the difficulty of the problem. While the cost of $\mathrm{MK}-\mathrm{EDA}_{k}$ scales linearly with the number of variables, the costs of Tree-EDA, and MT - EDA $_{m}$ have a quadratical scaling.

## D. EDAs as a Model of the Protein Folding Mechanism

The existence of a number of analogies between the "new" view of the protein folding mechanism and the way EDAs behave motivate us to analyze EDAs as a model of protein folding. Basically, we highlight these coincidences, drawing parallels between both entities, and investigating to what extent each of the entities can provide answers to questions arisen in the other domain.

To explain our model of the protein folding process, we will use the same representation introduced in Section V-A. We will assume that all solutions are feasible (i.e., self-intersecting paths are repaired). At first, during the real folding process, a protein can only be in one state at each time $t$. However, in EDAs, at each time more than one configuration can be part of the population. To cover this gap, we will assign the main role in modeling to the EDA probabilistic model. This resembles the "new" view of protein folding, where proteins are seen as an ensemble of rapidly interconverting conformations. At each time, a probability $p(\mathbf{x})$ can be associated with every possible configuration $\mathbf{x}$ of the sequence. This probability is related to the energy of the configuration, usually using the Boltzmann distribution defined in (2).

Consider that a given EDA shall model the protein folding process. Each generation of the EDA will be considered a time step of the folding process. We will assume that the probability of the sequence to fold to a given conformation is equal to the probability given to the same configuration by the probabilistic model of the EDA constructed at generation $t$.


[^0]:    ${ }^{2}$ The EDAs programs are available from the authors upon request.

Starting from this assumption, we advance the following statements.

- Both the "new" view and the EDA define a sampling of the space of configurations.
- The sampling processes pursue to sample the sequence configurations with a probability dependent of the quality of their respective energy function evaluations.
- The goal of the EDA and the protein folding process is achieved when $p(\mathbf{x})=1$, where $\mathbf{x}$ is the protein native state.
- Both entities tend to preserve local favorable conformational features through successive generations (time steps).
In principle, some of the features presented above are not exclusive attributes of EDAs. For instance, other population-based methods (e.g., GAs) can be used to sample the space of sequence configurations. The preservation of local favorable configurations, that may correspond to autonomous folding units in the real protein folding process, can also be accomplished to a certain extent by different evolutionary methods. However, the advantage of EDAs is that the probability model which they employ treats phenomena such as solution disruption and frustration, which may arise in the protein folding process, more effectively. Although in GAs a probability distribution of the solutions is implicitly used for the search, this probability distribution is explicitly learned and used in EDAs.

As explained in previous sections, traditional crossover operators tend to disrupt the construction of relevant subsolutions. The probabilistic model used by EDA matches to the statistical nature of the ensemble of conformations. This model is a condensed description of the selected population and, under suitable conditions, it also matches well with the EDA population at time $t+1$. The main advantage of an EDA model of protein folding is that it can provide not only global statistical information, but also information about the local conformations in the ensemble. This information can be appropriately combined to avoid the disruption of relevant subsolutions.

Let us exemplify this with the frustration problem. In frustrated systems, there are contacts that are locally unfavorable but that exist in the optimal solution, or there are favorable contacts that first must be broken to reach the optimal solution [43]. Analogous to a frustrated system would be a population-based method that tries to optimize a frustrated function.

Let $f(\mathbf{x})$ be a function that can be decomposed into the sum of local functions defined on (possibly overlapping) subsets of its variables. $f(\mathbf{x})$ is said to exhibit frustration when the point $\mathbf{x}$ where its global optimum is reached does not maximize one or more of the local functions.

These types of functions are difficult to optimize because finding the optima of the local subfunctions does not guarantee that the global optimum will be found by the combination of these optima. The role of frustration as a source of hardness for evolutionary algorithms has been discussed in [42]. In [66], it is shown that taking into account the interactions that arise between the variables of the problem, EDAs can optimize frustrated functions. Although the capacity of EDAs to deal with frustration also depends on the probability model employed, we
emphasize (in this respect) the suitability of using EDAs over GAs.

In the section of experiments, devoted to the simulation of the protein folding process using EDAs, we investigate some of the features exhibited by the EDA-model that mimic the behavior of the protein folding process. The issues considered are the following.

1) Whether there is a correlation between the successful rate of EDAs and the contact order of the protein models.
2) Whether there is a relationship between the generation convergence of EDAs for the HP model, and the contact order of the optimal solution.
3) Whether there are differences in the rate of formation of native contacts, and if these differences are associated with their contact separation.
In our simulations, we will employ some of the order parameters commonly used to investigate the protein folding process, but adapted to the simplified models. For the functional model protein, the contact order is calculated as the average sequence separation of the $H H$ contacts in the corresponding solution. For example, the contact order of the configurations shown in Figs. 2 and 3 (left) are, respectively, 3 and 6.

## VII. EXPERIMENTS

In this section, we present experiments on the use of the EDAs introduced in this paper. The section is divided into three main parts. First, the problem instances used for the HP model, and the benchmark used for the functional model protein are presented. In the second part, we present results on the protein structure prediction problem in the 2-d and 3-d regular lattices. Finally, this section presents the results of the study through EDA simulations of some factors related to the protein folding process.

## A. Problem Benchmark

The HP instances used in our experiments, and shown in Table IV, have previously been used in [13], [18], [19], [21], [27], [28], and [79]. The values shown in Table IV correspond to the best-known solutions $\left(H\left(x^{*}\right)\right)$ for the 2-d regular lattice. It is important to highlight that most randomly generated amino acid sequences do not behave like natural proteins, because the latter are products of natural selection. Likewise, most randomly generated sequences of H and P residues in the HP model do not fold to a single conformation [3].

We have used the functional model protein for the experiments with the EDA-based model and for evaluating EDAs as optimization algorithms. The existence of a unique native state for the instances of this model is a desired attribute, particularly for the experiments done using the EDA-based model. For this type of experiment, we employed a set of 15545 functional model proteins ${ }^{3}$ that were optimally embedded on a 2-d square lattice [51]. For each instance, the benchmark provides the energy of the unique native state, together with the energy value and number of structures that are in the first excited state (best suboptimum). The length for each sequence is 23.
${ }^{3}$ http://www.cs.nott.ac.uk/ nxk/HP-PDB/2dfmp.html.

TABLE IV
HP Instances Used in the Experiments. The Search Space of Each InSTANCE is $2^{n}$, WHERE $n$ IS THE SIZE OF THE INSTANCE


For the optimization experiments using the functional model protein, we have selected a subset of 11 instances from the benchmark. The selected instances have been previously used as testbed of optimization algorithms in [17] and [23]. The set of instances selected and their minimal energy values are shown in Table V.

## B. Results for the HP Model in the Two-Dimensional Lattice

The first experiment consists of finding the optimum of sequences shown in Table IV using EDAs with different probability models. The EDAs described in Section VI $\left(\mathrm{MK}-\mathrm{EDA}_{2}\right.$, Tree-EDA, and $\mathrm{MT}-\mathrm{EDA}_{4}$ ) are used in our experiments. All the algorithms use a population size of 5000 individuals and a maximum of 5000 generations. The results of the experiments are shown in Table VI, where $S$ is the percentage of times the best solution has been found in 50 experiments, and $\bar{g}$ is the average number of generations needed to find the optimum. Since we use best elitism (the whole selected population is passed to the next population), the average number of function evaluations needed to reach the optimum can be calculated as $M+(M-N)(\bar{g}-1)$. Using truncation selection $(T=0.1)$, the average number of function evaluations is $5000+4000(\bar{g}-1)$.

The first remarkable result is that all EDAs are able to find the optimum solution for sequences $s 1-s 6$. All the algorithms

TABLE V
Functional Model Protein Instances

TABLE VI
Results of EDAs for HP Instances in the $2-d$ Lattice. $S$ : PERCENTAGE of Times the Best Solution Has Brps Found, $\bar{g}$ : Average Number of Generations Needed to Find the Optimum


find the second best solution for sequence $s 7$, the best or second best for sequence $s 8$, and very good solutions for the rest of the longer sequences. There are two facts that help to put these results in perspective: EDAs do not use local optimizers that could improve the results, and the parameters of the algorithms have not been tuned for every instance.

1) Deceptive Instances for EDAs: Instance $s 7$ is deceptive for EDAs. We investigate in detail the performance of the EDAs for this instance. Detailed research on the dynamics of EDAs for deceptive problems throws light on the limitations of these methods and could contribute to their improvement.

The optimum of sequence $s 7$ is -36 . There are many suboptimal solutions with value -35 . Fig. 6, lower left, shows the optimum solution that cannot be found by the EDAs. The rest of the solutions are the suboptimal ones $(H(\mathbf{x})=-35)$ found by

![img-5.jpeg](img-5.jpeg)

Fig. 6. Optimal solution (bottom left) and three suboptimal solutions for the $s 7$ sequence.
the EDAs. A clear difference between the optimal and the rest of the solutions shown in the figure is the number of short helices. The optimum has fewer short helices than the other solutions. Most of the energy contributions come from interactions between a central cross-shaped structure and the neighboring residues. As the optimal solution cannot be constructed from the combination of the good substructures present in the other solutions, the EDA cannot reach it. As a hypothesis for the reason of this deceptive behavior, we advance the existence of isolated optimal solutions with components that are not present in the suboptimal solutions.

To validate this empirical conclusion, we calculate different Markov probabilistic models $(k=0, \ldots, 3)$ from the 5375 solutions with energy between -33 and -35 . Using these models, the probabilities corresponding to each of the data base solutions and to the optimal solution shown in Fig. 6 are calculated. The models indicate the probability for the solutions to be present at the new EDA generation.

Results can be appreciated in Table VII. In this table, $p\left(\mathbf{x}_{\text {opt }}\right)$, $\max (p(\mathbf{x}))$, mean $(p(\mathbf{x}))$, and $\min (p(\mathbf{x}))$, respectively, correspond to the probabilities given by the models with different $k$ values (from 0 to 3 ) to the optimum of the problem, the maximum, mean, and minimum probabilities given by the models to the 5375 solutions. Similarly, $N\left(p(\mathbf{x})>p\left(\mathbf{x}_{\text {opt }}\right)\right)$ is the number of solutions with a probability higher than the probability of the optimum.

The most revealing fact is that the probability given to the optimal solution by probability models with $k=2$ and $k=3$ is zero. This fact means that the optimal structure does not share some of its substructures with any of the other 5375 suboptimal solutions. The analysis of the model revealed that in the case of $k=2$, only one of the substructures was absent in the other solutions, while when $k=3$, four substructures were absent.

TABLE VII
Statistical Information Extracted From $k$-Order Markov
Probabilistic Models $(0 \leq k \leq 3)$ of the 5375 Solutions
of the $s 7$ Sequence With Energy Lower Than -32


TABLE VIII
Results Achieved by Different Search Heuristics FOR THE HP InSTANCES


This experiment shows that deception also arises in the case of the HP model, and that deceptive instances for the EDAs can be found and described as those which do not share a number of good substructures with most of the closest suboptimal solutions. These substructures cannot be captured by the probability models used.
2) Comparison With Other Algorithms: The performance of EDAs is compared now with the best results achieved with other evolutionary and Monte Carlo optimization algorithms. The results are shown in Table VIII. The results of GA [19] and MMA [17] correspond to the best solution found in five runs. The results of ACO and NewACO [28] are based on 20-700 tries for the former algorithm and 300-500 for the latter [28]. PERM [25] reports 20-200 tries for sequences $s 9$ and $s 11$; the other instances have been faced in [28]. Results for other optimization methods [15], [22], [50] were not displayed because either they were unable to find the best results achieved by EDAs or the number of functions evaluations required to find them was

![img-6.jpeg](img-6.jpeg)

Fig. 7. Average of the best solution at each generation for different EDAs in sequence $s 6$.
much higher. All the results shown for EDAs are obtained from 50 runs.

A first conclusion is that none of the algorithms are able to outperform the rest of algorithms for all the instances. PERM is one of the best contenders in all cases except $s 8$ in which its results are consistently very poor. In comparison with the NewACO, EDA reaches equal or better results in all instances except one. It should be noted that NewACO applies local optimization techniques. In this sense, a fairer comparison would be between EDAs and ACO. In such a comparison, EDA is the clear winner. Analysis shows that none of the other algorithms achieves similar results.
3) Dynamics of the Algorithms: Another relevant issue related to EDAs concerns their particular dynamics for the HP models. The existence of a model of the search space enables a compact representation of characteristic features of the best solutions but also determines the particular way in which the optimal solutions are constructed.

In the next experiment, we analyze the convergence dynamic of the three types of EDAs employed in our experiments, in the optimization of sequence $s 6$. The average of the best solutions at each generation is calculated by running each algorithm 50 times. The population size and the rest of the parameters were the same as in previous experiments. The results are shown in Fig. 7. It can be appreciated from the figure that, for all EDAs, a small number of generations are enough to find the optimal solutions. Nevertheless, there are differences in the dynamics of the algorithms. MK - EDA $_{2}$ reaches better solutions earlier than the other algorithms, but in the experiments conducted, $\mathrm{MT}-\mathrm{EDA}_{4}$ reached the optimum more often. Tree-EDA is the slowest algorithm.

## C. Results of the HP Model in the Three-Dimensional Lattice

In the following experiments, we investigate the behavior of EDAs in the solution of the HP model in the regular 3-d lattice. EDAs are compared with the hybrid GA that uses a fea-sible-space approach with relative encoding [21] and with results achieved using the IA [23]. A maximum number of $10^{5}$
evaluations was set in the experiments presented in [21] and [23]. Therefore, we imposed the same restriction and in our comparison EDAs with two possible instantiations of the parameters were used: A population size $N=2500$ with $g=40$ generations, and a population size $N=5000$ with $g=20$ generations. Since we use elitism with parameter $E=1$ (i.e., the best individual is passed to the next generation), the maximum number of evaluations is slightly smaller than $10^{5}$. The results of the experiments are shown in Table IX, where average and fitness values are computed from 50 runs for each algorithm. For each instance, the first row shows the results of EDAs with $N=2500$ and the second those for $N=5000$. Best and average results of the EDAs are in bold whenever they are equal or better than those achieved by the hybrid GA and the IA.

It can be seen in Table IX that in terms of the average fitness of the solutions, the results reached by all EDAs are strictly better than those achieved with the other two algorithms for instances s1, s2, s3, and s6. For instances s5, s7, and s8, the IA clearly outperforms all the EDAs in terms of the average fitness. For instance s4, the Tree-EDA and the MT - EDA $_{4}$ that use a population size of 2500 outperform the IA. For instances s6 and s8, EDAs are able to achieve best new solutions.

We hypothesized that the best solutions found by the algorithms for some of the instances may be far from optimal. EDAs that use a constrained population size cannot reach these optimal solutions. To validate this hypothesis, and in order to evaluate the capacity of EDAs to reach better solutions when more evaluations are allowed, we used a population size of 5000 individuals and a maximum of 1000 generations. In this case, we employ the best elitism strategy. We also run experiments for the hybrid GA allowing a maximum of $5 \cdot 10^{6}$ evaluations. The IA program was not available for conducting new experiments. The results are shown in Table X.

Since in this case we could collect the best result achieved in each run for all the algorithms, we could determine whether differences between the algorithms are statistically significant. We have used the Kruskal-Wallis test to accept or reject the null hypothesis that the samples have been taken from equal populations. The test significance level was 0.01 . For all the instances considered, significant statistical differences have been found between the hybrid GA results and those achieved by the Markov (MK - EDA $\mathrm{DA}_{2}$ ) and mixture (MT - EDA $\mathrm{A}_{4}$ ) EDAs. Significant statistical differences between the hybrid GA and the Tree-EDA have been detected only for instances $s 3, s 5, s 6$, and $s 8$. All the EDAs have a better average of solutions, showing that the algorithm clearly outperforms the hybrid GA. Furthermore, as can be observed in Table X, EDAs find new best solutions for sequences $s 5, s 6$, and $s 8$. Notice that the average results for instances $s 1$ and $s 2$ degrade with regard to those shown in Table IX. We consider this fact may be due to the effect of the best elitism strategy that for small instances may lead to an early convergence of the algorithm. The average number of evaluations needed by EDAs before convergence was between $6 \cdot 10^{4}$ for the shortest instances and $10^{6}$ for the longest ones.

## D. Results for the Functional Model Protein

We have conducted experiments with the functional model protein in the two-dimensional lattice.

TABLE IX
Results of the EDAs, the Hybrid GA, and the IA in the Three-Dimensional Lattice

TABLE X
Results of the EDAs and the Hybrid GA in the Three-Dimensional Lattice

Initial results for the functional model protein instances [17] considered the number of fitness evaluations required by the best run for a given instance as a metric for comparing the performance of the algorithms. In [23], the success rate and the number of fitness evaluations are used to compare different variants of the IA. We follow the second approach and compare the results of EDAs with three of the variants of the IA presented in [23]. The variants of the IA selected were: IA with elitist aging, IA with pure aging, and IA using memory cells $\left(\tau_{B}=5, \tau_{B \text { mem }}=10\right)$. The other two variants for which results are shown in [23] do not improve the results of the IA variants selected.

For EDAs, we use a scheme conceived for situations wh2ere early convergence of the algorithm is detected. This scheme
works as follows: When the selected population is too homogenous (the number of different individuals is below a given threshold), all the individuals except the best solution are randomly generated. This scheme allows one the use of smaller population sizes. We use a population size $N=500$, and the minimal number of different individuals allowed was 50 . As in [23], a maximum of $5 \cdot 10^{6}$ evaluations were allowed to all the algorithms and 30 runs were done for each instance. Results are shown in Table XI.

In Table XI are shown, for all the algorithms, the success rate percentage and the average number of evaluations, which are the criteria we use to compare the algorithms. An initial analysis of the results shown in the table reveals that IA with elitism aging and IA with memory cells have the worst results among

TABLE XI
Results of the EDAs and the IA for the Functional Model Protem in the Two-Dimensional Lattice. $S$ : Percentage of Times the Best Solution Has Been Found, $\bar{g}$ : Average Number of Fitness Evaluations Needed to Find the Optimum


all the algorithms tested. However, there is not a clear winner among the rest of algorithms. $\mathrm{MT}-\mathrm{EDA}_{4}$ has the highest success rate of all the algorithms but for many instances it needs a higher number of function evaluations than IA with pure aging, which is the best of all the IA variants. Differences between EDAs are less evident. The MT - $\mathrm{EDA}_{4}$ and Tree-EDA only fail for one instance and the $\mathrm{MK}-\mathrm{EDA}_{2}$ for two. Some of the results shown in Table XI have been improved by using the $\mathrm{MK}-\mathrm{EDA}_{1}$ (data not shown). The results achieved for the functional model protein in the two-dimensional lattice show that for this type of problem, EDAs are very competitive algorithms.

## E. Results of the Protein Folding Simulations

In this section, we present results on the use of EDAs to simulate the protein folding in the HP model. We investigate to which extent EDAs are able to mimic some characteristic features of the protein folding mechanism. For all the simulation experiments, we use $\mathrm{MK}-\mathrm{EDA}_{2}$. In all the experiments, the population size was set at 2000 and the maximum number of generations was 20 .

1) Energy Landscape of the Model: In the first experiment, we investigate the energy landscape of the function for one of the 15545 functional model protein instances available. The goal of this experiment is to build some intuition about the fitness landscape of the functional model protein. Particularly, to illustrate the fact that as solutions share more of the protein native contacts, their fitness (energy) decreases.

The experiments consist of executing the EDA and storing all the conformations visited during the search. Sequence PHHPPHPPHHPPHPPHPPHHH was chosen for the experiment. For every conformation visited during the search, the total number of contacts $(K)$ and the number of native contacts $(Q)$ are calculated. We classify the conformations using these two parameters, and calculate the average energy of all conformations that share the parameters $(K, Q)$. The
![img-7.jpeg](img-7.jpeg)

Fig. 8. Energy landscape of the functional model protein corresponding to sequence PHHPPHPPHHPPHPPHPPHHH as sampled by $\mathrm{MK}-\mathrm{EDA}_{2}$.
native state of the sequence has nine native contacts. Therefore, $0 \leq K, Q \leq 9$.

Fig. 8 shows the average energy of all the sampled conformations grouped using the different values of $K$ and $Q$. The figure reveals that, as the number of native contacts increases in the conformations, the average energy decreases.

Throughout the evolution, $\mathrm{MK}-\mathrm{EDA}_{2}$ is able to explore the different regions of the energy landscape. Not only those regions with high energy which are abundant in the search space, but also those corresponding to low-energy values where the number of conformations is scarce. For example, $\mathrm{MK}-\mathrm{EDA}_{2}$ is able to locate the optimum which is unique.

To appreciate the characteristics of this landscape in detail, Fig. 9 shows the contour graph corresponding to the same experiment. Sets of conformations with similar average energy are

![img-8.jpeg](img-8.jpeg)

Fig. 9. Energy landscape contour graph of the functional model protein corresponding to sequence $P H H P P H P P H H P P H P P H P P H H H$ as sampled by $\mathrm{MK}-\mathrm{EDA}_{2}$.
joined in the graph by the same contour lines. Regions with lower energy are those with many native contacts.

The samples obtained by $\mathrm{MK}-\mathrm{EDA}_{2}$ make it possible to observe the correlation between the presence of native contacts in the conformations and the quality of the folding (low energy). This fact is expected in proteins that have evolved to diminish the degree of frustration and achieve a fast folding rate. However, it does not mean that, for every simplified energy function, the EDA will be able to move in the direction of the native configuration by augmenting the number of native contacts. First, the definition of realistic protein folding energy functions such that their only significant basin of attraction is the native state has been recognized as a very difficult task [38]. Second, the phenomenon of frustration can arise in the functional model protein and other energy functions, moving the $\mathrm{MK}-\mathrm{EDA}_{2}$ away from the native state.
2) Influence of the Contact Order in the Protein Folding Process: We investigate whether the EDA can reflect the influence of the contact order parameter in the protein folding process. As discussed in Section II-A, proteins with a large fraction of their contacts between residues close in sequence tend to fold faster than proteins with more nonlocal interactions. This section shows how the contact order of the functional model protein instances influences on the success rate and average number of generations needed by $\mathrm{MK}-\mathrm{EDA}_{2}$ to solve the problem.

As a preprocessing step, 100 executions of $\mathrm{MK}-\mathrm{EDA}_{2}$ are done for each of the 15545 functional model proteins instances. The goal of this step is to determine the easier instances for the EDA, and to calculate, for all instances, a set of statistics from the best solutions found at each run. Of the 15545 instances, $\mathrm{MK}-\mathrm{EDA}_{2}$ was able to find the optimum in 12588 instances at least once. For 703 instances, the algorithm found the optimum at least in 95 runs, and for 176 it found the optimum in 100 runs.

To evaluate the relationship between the contact order of the sequences and the average number of generations needed to
![img-9.jpeg](img-9.jpeg)

Fig. 10. Relationship between the contact order of the sequences where $\mathrm{MK}-\mathrm{EDA}_{2}$ has a success rate above 95 in 100 experiments and the average number of generations needed to convergence.
solve them, we consider those instances for which $\mathrm{MK}-\mathrm{EDA}_{2}$ has a success rate higher than or equal to 95 . The choice of this set is determined by the need to have an accurate estimate of the average number of generations. From this set of instances, the Spearman's rank correlation coefficient is calculated between the contact order and the average number of generations. The Spearman's rank correlation is the statistic of a nonparametric test usually employed to test the direction and strength of the relationship between two variables.

With a confidence level of 0.01 , the test accepted the hypothesis that the two measures have a positive correlation equal to 0.3939 . In Fig. 10, the average generation and contact order for the set of selected instances are plotted. Additionally, the figure shows the average number of generations calculated from instances with similar contact order. It can be seen in the figure that the number of generations needed to solve the problem grows with the contact order.

Using the test based on the Spearman's rank correlation coefficient with the same confidence level, we have evaluated the relationship between the contact order of the sequences where $\mathrm{MK}-\mathrm{EDA}_{2}$ found the optimum at least once, and the success rate achieved by the algorithm for these instances. The test rejected the hypothesis that the observed correlation was due to random effects. The parameter of the correlation provided by the test was equal to -0.2848 . This means that, as the contact order of the instance grows, the success rate of the algorithm diminishes. Fig. 11 shows the average success rate for instances with similar contact order.

The analysis of the EDA-based protein folding model has shown that similarly to the real protein folding process, low contact order optimal conformations are easier and faster to find. This behavior has been observed in other optimization algorithms such as Rosetta [48], which is one of the best algorithms for protein folding in the CASP competitions. In Rosetta, the structures sampled by local sequences are approximated by the distribution of structures seen for short sequences and related

![img-10.jpeg](img-10.jpeg)

Fig. 11. Relationship between the contact order of the sequences where $\mathrm{MK}-\mathrm{EDA}_{2}$ found the optimum at least once, and the success rate achieved by the algorithm for these instances.
sequences in known protein structures. Using Rosetta, high contact order proteins can take up to six orders of magnitude longer to fold than do low contact order proteins [80].
3) Difference in the Contact Accessibility: In the following experiment, we investigate whether the EDA-based protein folding model is able to reproduce the difference in the rate of formation for different native contacts. Particularly, we will investigate whether the distance between contacting residues has an effect on their formation. As discussed in Section II-A, local interactions are more likely to form earlier in the real folding process than nonlocal interactions.

Given a protein instance that is optimized using $\mathrm{MK}-\mathrm{EDA}_{2}$, the experiment consists of computing, at each generation, the frequency of each native contact of the protein from the selected set of the EDA population. The frequency is calculated as the fraction of all selected solutions that contain that contact. The EDA is executed 100 times for each of the 176 instances for which $\mathrm{MK}-\mathrm{EDA}_{2}$ had previously found a $100 \%$ of success.

From the information obtained from the 17600 experiments, the frequencies of the contacts with the same contact separation (C.S.) at the same generation are averaged. The results are shown in Fig. 12. By selecting a set of instances, we intend to show that the observed effect are not particular of one single instance. On the other hand, by choosing the 176 instances for which $\mathrm{MK}-\mathrm{EDA}_{2}$ had previously found a $100 \%$ of success rate, it is guaranteed that the native state will be reached in all the runs with a very high probability.

Fig. 12 shows the evolution of the probabilities along the generations. Two aspects can be appreciated. First, the probability of contacts with low contact separation (C.S. $\leq 5$ ) is higher than the other probabilities since the first set of individuals is selected. Second, the difference in the rate of convergence determined by the contact separation is evident. While contacts with low contact separation rapidly increase their probability, those contacts with a higher contact separation (C.S. $\geq 15$ ) grow at a slower rate.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Relationship between the different contact separations and the evolution of their probabilities along the evolution of $\mathrm{MK}-\mathrm{EDA}_{2}$ for instances where it had a $100 \%$ of success rate.

The behavior of our model is once again consistent with what is observed in the real protein folding. Moreover, these results can support hypotheses that help to explain the correlation between the contact order of proteins and the success rate and average number of generations needed to find them. As the increase of the probability of contacts with high contact separation is slower, it will take a longer time to obtain native states with higher contact order. Additionally, it will also be more difficult to find the optimum for this type of instances as the algorithm will tend to get trapped in suboptimal solutions with lower contact order.

## VIII. CONCLUSION AND FURTHER WORK

The approach of using probabilistic dependencies to improve search efficiency has a strong theoretical basis. Its operational simplicity and applicability make it an advantageous method in relation to other widely applied evolutionary algorithms. The results of the experiments shown in this paper confirm that the EDA is a feasible alternative for the protein structure prediction problem. Particularly, we recommend the use of probabilistic models for the solution of coarse-grained protein folding problems, where Monte Carlo methods exhibit a poor performance.

There exist evolutionary and deterministic algorithms that exhibit similar or better results than EDAs for some of the HP and functional protein instances used in this paper. Some of these algorithms have been tuned for each of the instances or they implement local optimizers together with the main evolutionary method used. This is certainly an alternative that could be followed for EDAs too and might provide better results than those presented in the paper. Nevertheless, we have put the emphasis in the investigation of those factors that explain the behavior achieved by EDAs, and in which way problem knowledge can be obtained by inspecting the solutions found by the algorithms. We investigate the influence that different factors of the HP instances have on the behavior of the algorithm. The decision of not including other optimizers was also due to the interest to

simplify the analysis of the role played by probabilistic modeling in the search.

On the other hand, in comparison to other optimization algorithms such as PERM, which has only been applied to the HP-model, EDAs are general optimization strategies that have been extended to solve protein problems with more complex protein models [61], [62], [81]. Nevertherless, this work and other recent successful applications of EDAs in bioinformatics [27], [82]-[85] refer to the use of EDAs as optimization methods. One of the aims of this paper has been to highlight that EDAs can also be employed as simulation tools of biological processes.

The most distinguished feature of the EDA model of protein folding lies in its ability to represent, by means of probability models, relevant interactions between the protein conformations. This representation can be used in broader contexts. For instance, in the Rosetta algorithm, short fragments of known proteins are assembled by a Monte Carlo strategy to yield na-tive-like protein conformations. While Monte Carlo sampling of only one fragment at a time allows the native structures to be smoothly constructed, the existence of probability dependencies between the different local conformations seems clear. These dependencies could be exploited during the search applying probability models in a context similar to EDAs.

We have shown that EDAs can mimic some features of the actual protein folding process. Our approach to the protein folding process in the HP simplified model has paid attention to how the order parameters such as the contact order influence on the behavior of EDAs. Such an analysis is scarce in previous na-ture-inspired approaches to the HP problem.

The experiments that simulate the protein folding process presented in this paper have only investigated a number of the potential issues that can be studied with the model. The analysis of EDA simulations lead to the study of other features exhibited by the model. One example is the emergence of nucleation events in protein folding.

It is generally accepted that some sort of nucleation event is a key to the protein folding mechanism. This means that some local partial structures are generally formed before the configuration of the whole protein. However, there are different ways to explain how this mechanism operates. Two opposite explanations are the "many delocalized nuclei" and the "specific nucleus" ideas. The former states that each conformation in the ensemble contains a different locally structured region. The second idea suggests that the transition state ensemble is comprised of conformations that share the same set of essential contacts, which form a compact core inside the native state (the specific nucleus) [40].

Emergence of nucleation events in protein folding can be approached by the study of the marginal probability distributions associated with the local configurations. By adding a priori information about the local structure configurations to the probabilistic model, the EDA protein folding model can also be harnessed to test the "specific nucleus" or "many delocalized nuclei" hypothesis.

While the application of the model to real folding problems is clearly constrained by the nature of the HP energy model and the specificities of EDAs, we recall that different applications
of protein models require different levels of accuracy. Some models can be used to study catalytic mechanisms, while other are more suitable to find functional sites by 3-d motif searching [86]. Furthermore, as shown in this paper, simple models can be analyzed in detail over a wide range of instances and parameters.

Finally, we point out that measures associated with the protein folding process, such as the contact order and the degree of frustration in proteins, are of interest for the design and study of hardness measures (e.g., fitness distance correlation, epistasis variance, etc., [87]) for evolutionary algorithms.

## ACKNOWLEDGMENT

The authors thank C. Cotta for providing the programming code used in the comparison between EDAs and the hybrid GA. They also thank two anonymous reviewers whose comments have contributed to improve a previous version of this paper.
