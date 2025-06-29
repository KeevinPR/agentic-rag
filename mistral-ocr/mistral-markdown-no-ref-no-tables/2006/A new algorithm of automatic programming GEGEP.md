# A New Algorithm of Automatic Programming: GEGEP 

Xin $\mathrm{Du}^{1,2}$, Yueqiao $\mathrm{Li}^{1}$, Datong Xie ${ }^{1}$, and Lishan Kang ${ }^{1,3}$<br>${ }^{1}$ Department of Computer Science and Technology, China University of Geosciences, Wuhan, China<br>xindu79@126.com<br>${ }^{2}$ Department of Information and engineering, Shijiazhuang University of Economics, Shijiazhuang, China<br>xindu79@126.com<br>${ }^{3}$ State Key Laboratory of Software Engineering, Wuhan University, Wuhan, China<br>kang_whu@yahoo.com


#### Abstract

Gene Expression Programming (GEP) has wide searching ability, simple representation, powerful genetic operators and the creation of high levels of complexity. However, it has some shortcomings, such as blind searching and when dealing with complex problems, its genotype under Karva notation does not allow hierarchical composition of the solution, which impairs the efficiency of the algorithm. So a new automatic programming method is proposed: Gene Estimated Gene Expression Programming(GEGEP) which combines the advantages of Estimation of Distribution Algorithm (EDA) and basic GEP. Compared with basic GEP, it mainly has the following characteristics: First, improve the gene expression structure, the head of gene is divided into a head and a body, which can be used to introduce learning mechanism. Second, the homeotic gene which is also composed of a head, a body and a tail is used which can increase its searching ability. Third, the idea of EDA is introduced, which can enhance its learning ability and accelerate convergence rate. The results of experiments show that GEGEP has better fitting and predicted precision, faster convergence speed than basic GEP and traditional GP.


Keywords: Gene Expression Programming; Genetic Programming; Gene Estimated Gene Expression Programming,; Estimation of Distribution Algorithm.

## 1 Introduction

Gene Expression Programming(GEP) was first proposed by Candida Ferreira [1]. In this new syste- m , the complex computer programs (the phenotype) evolved by GEP are totally encoded in simple strings of fixed length (the genotype) .

GEP is the inheritance and development of GA and GP, it synthesizes the merits of basic GA and traditional GP and has stronger ability of solving problems [2][3]. However, the learning procedure of GEP can be improved upon when dealing with complex problems with respect to both time efficiency and solution quality. The biological evolutionary process has revealed the principle of evolving from a self-contained functional

single cell to a well- developed entity with numerous specialized components [4]. We are naturally inspired to assume that solutions to complex problems might be built up incremen- tally from simpler elements. Although the phenotype of expression trees in GEP has retained the struct- ural representation from GP, the linear representation of the genotype conforms to Karva notation, under which the genotype-phenotype mapping mechanism does not guarantee that the levels of functional complexity in the phenotype are also directly reflected in the genotype. Since it is the genotype that is subject to the different genetic operations, it is difficult to follow the approach of incrementally forming solutions with the original GEP. Moreover, an evolved good functional structure is very likely destroyed in the subsequent generations not only by mutations but also by recombination and transpositions, which may require much additional computation to recover before an optimal solution is found. In view of this weakness, we propose a Gene Estimated Gene Expression Programming ( GEGEP), it combines EDA with GEP . Compared with GEP, it mainly has the following characteristics: First, improve the gene expression structure, original gene structure is divided the head of chromosomes into a head and a body, which can be used to introduce the learning mechanism. Second, the homeotic gene which is also composed of a head, a body and a tail is used which can increase its searching ability. Third, the idea of EDA is introduced, which can enhance its learning ability and accelerate the convergence rate. We believe GEGEP benefits the evolution in terms of the convergence of a good functional structure.

The other parts of this article is organized as follows. Section2 explains GEGEP algorithm; Section3 proves the validity of the GEGEP algorithm through experiments; Section 4 presents some conclusions and ideas for future work.

# 2 Gene Estimated Gene Expression Programming 

### 2.1 The Improvement of GEGEP

### 2.1.1 Improve the Structure of Gene Expression Programming

In GEGEP, gene head in GEP is divided into a head and a body. The head contains only functions, the body like the head of GEP contains symbols representing both functions and terminals, whereas the length of the tail is a function of head, body and the number of arguments of the function with more arg- uments n(also called maximum arity) and is evaluated by the equation: tail $=($ head + body $) \times(\mathrm{n}-1)+1$.

### 2.1.2 Improve the Structure of Homeotic Gene

Homeotic genes have exactly the same kind of structure as conventional genes of GEGEP and are built using an identical process. They are also composed of a head,a body and a tail.The heads only contain linking functions. The bodys contain linking functions, a special class of terminals:genic terminals representing conventional gene and random numerical constants. The tails contain obviously random numerical constants and genic terminals.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Expression of chromosomes

The head, body and tail of homeotic gene are respectively represented as homo_head, homo_body, homo_tail.The method of computation of homeotic gene is same as conventional genes. So the length of gene individual is evaluated by the equation:
length=(head+body+tail) *n_gene+ homo_head +homo_body + homo_tail, where n_gene represents the number of genes. For example, if we choose head=2, body $=4, \mathrm{n}=2$, then tail $=$ (head + body $) *(2-1)+1=7$, the length of conventional genes is $2+4+7=13$. In this case ,if n_gene=3, homo_head $=1$,homo_body $=4$, then the length of homeotic gene is equal to 11 , the length of gene individual is equal to 50 .

One such gene individual is shown below:

$$
\begin{aligned}
& 01234567890120123456789012012345678901201234567890 \\
& +-\mathrm{d}+\text { adbc?d?c c SL+}-\mathrm{abc} ? \mathrm{aa} ? \mathrm{bc} \mathrm{LCa} * \mathrm{~b}-\mathrm{abd} ? \text { cca }+-20 / 21 ? 20 ?
\end{aligned}
$$

Where ? represents random numerical constant, $0 、 1 、 2$ respectively represent first、second、third conventional gene, L、C and S respectively represent $\ln 、 \cos$ and $\sin$ function. It codes for three conventional genes and one homeotic gene. The conventional genes code as usual for three different sub-ETs. The homeotic gene controls the interactions between the different sub-ETs. The homeotic gene and conventional genes have same functional set and terminal set. The corresponding phenotypes are shown in Figure1.

# 2.1.3 EDA 

EDA[5] is put forward from the viewpoint of statistics by MüHlenbein and Paaß, which is evolutionary algorithm based on probability analysis. EDA is similar to traditional genetic algorithm, the difference between them is that EDA selects evaluation and learning distribution to produce new offspring. New offspring are produced by Bayes network. The Bayes network is a directed acycline graph, which considers specific

interactions of the problem among the variables of chromosomes. It can make full use of realm knowledge and information of sampling datum with Bayes statistics. So it has strong learning ability and uses to model on discretional or continual polynomial in common.EDA contains three kinds of models: Univariate EDA Model, Bivariate EDA Model and Multivariate EDA Model which are shown in Figure2. Univariate EDA Model supposes that there have no interdependencies among variables. Bivariate EDA Model supposes that there have dependencies between pairs of variables. Multivariate EDA Model supposes that there have dependencies among variables greater than two.

For the convenience of computation, we only use Univariate EDA Model. The Model is shown in Figure 2(a). This basic thought of GEGEP is to carry on the statistics to the head and body department of each above operator of the conventional genes and homeotic gene, extracts its statistical probability, then carries on the mutation according to its statistical probability.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Graphical representation of probability model among variables

The procedure of updating statistical information is as follows:
(1) Initialize fitness table

The size of fitness table is $(\mathrm{n}+1)$ lines and L rows, where n expresses the size of function set, L expresses the total length of all he- ad and body added in the chromosome. For example: Function set $=\{+,-,{ }^{*}, /$, Exp, Log, Sin, Cos, Sqrt $\}$, the chromosome has 4 genes and 1 homeotic gene, the length of head of each gene is 3 , the length of body is 7 , then the size of total table is $(9+1) *(5 *(3+7))=10 * 50$. The initial value is $\varepsilon(\varepsilon=0.1)$ and initial frequency is once each generation.
(2) Initialize statistical information table

Statistical information table has the same size as fitness table, the initial value is also $\varepsilon(\varepsilon=0.1)$. The frequency is once every run.
(3) Renew fitness table

Renewing method is as follows: The fitness of each individual is added to the corresponding position of fitness table.

(4) Renew statistical information table

It directly adds the value of fitness table to original value of the corresponding position of statistical information table.

# 2.2 Fitness Function and Termination Condition 

The fitness reflects whether the individual is good or bad. In this paper, the following fitness function is used:

$$
f_{i}=\max \left(1000-\sum_{j=1}^{n}\left(\left|\frac{C_{i j}-T_{j}}{T_{j}}\right| \cdot \text { factor }\right), 0\right)
$$

Where n is the number of computation cases, Cij is the value returned by the individual program i for fitness case j and Tj is the target value for fitness case j. Factor is a proportional constant and is equal to 1000 dividing the number of records. Obviously, if the bigger fitness value is, then the better individual is.

The termination condition is the actual Evolutionary generation exceeding reserved evolutionary generation (Maxgenerations) or the best fitness having no change for L continuous generations :
If generation $\geq$ Maxgenerations1llunchange_generation $\geq \mathrm{L}$
Then Terminates
The best solution or the approximate best solution is what we wanted when terminates.

### 2.3 Algorithm

PROCEDURE GEGEP algorithm
begin
Initialize $\mathrm{P}(0)$;
Evaluate the fitness of $\mathrm{P}(0)$;
Renew statistical information table;
$\mathrm{t}:=0$;
repeat
$\mathrm{Pm}(\mathrm{t}):=$ mutation $\{\mathrm{P}(\mathrm{t})\}$ according to statistical information;
$\mathrm{Pc}(\mathrm{t}):=$ crossover $\{\mathrm{P}(\mathrm{t})\}$;
$\mathrm{Pt}(\mathrm{t}):=$ transpose $\{\mathrm{P}(\mathrm{t})\}$;
$\mathrm{P}(\mathrm{t}+1):=$ selection $\{\mathrm{P}(\mathrm{t})\}$;
Renew statistical information table;

$\mathrm{t}:=\mathrm{t}+1 ;$
until termination condition ;
output solution of Pbest;
end

# 3 Experiment 

In order to justify the advantage of GEGEP as compared to traditional GP and basic GEP , we first experimented on three algorithms with two function modeling. Later a suite of Symbolic Regression were conducted on the testing datasets .Last we experimented on another function modeling.
(1) Function modeling.

We select two cases from relevant references to check the validity of this method. Considering different impact of homeotic gene and conventional genes, the homeotic gene determines which gene is expressed in which cell and how they interact with one another. So the mutation rate is separated into homeotic gene rate and conventional generate.

The parameter setting of two experiments is same and is shown as Table1:

Table 1. Parameter Setting for GEGEP
The calculation result of Y by GP and GEP are respectively obtained from [6] and [7]. There are six main factors: the depth of coalface $\mathrm{x} 1(\mathrm{~m})$, the height of coalface x $2(\mathrm{~m})$, the amount of coalfaces $\mathrm{x} 3(\mathrm{~m} 3 / \mathrm{t})$, the layer interval between working coalface and neighboring coalface $\mathrm{x} 4(\mathrm{~m})$, average day progress of working face $\mathrm{x} 5(\mathrm{~m} / \mathrm{d})$ and average output per day $\mathrm{x} 6(\mathrm{t} / \mathrm{d})$ as the main input variates , the amount of gas emitted from coalfaces $(\mathrm{Y})$ as the output variate. So the termination set is defined as $\mathrm{T}=\{\mathrm{x} 1, \mathrm{x} 2, \mathrm{x} 3, \mathrm{x} 4, \mathrm{x} 5, \mathrm{x} 6, ?\}$, where ? represents random numerical constant and is chosen from the interval $[-10,10]$. The function set is defined as $\mathrm{F}=$ $\{+, \quad, \quad *, \quad \div, \quad$ sqrt, exp, sin, cos, $\ln \}$. The aim is to obtain a prediction function for Y with $\mathrm{x} 1, \mathrm{x} 2, \mathrm{x} 3, \mathrm{x} 4, \mathrm{x} 5$ and x 6 being the parameters: $\mathrm{Y}=\mu(\mathrm{x} 1, \mathrm{x} 2, \mathrm{x} 3, \mathrm{x} 4$,

x 5, x 6). Fifteen cases from sample 1 to 15 in table 2 are used as training datum to build the prediction model while three cases from sample 16 to 18 in table 3 are used as test datum.

The function evolved by GEGEP is :
$\mathrm{y}=\operatorname{Ln}(\operatorname{Exp}((\operatorname{Sin}((\operatorname{Sin}(((\operatorname{Exp}(\mathrm{x} 3)+\mathrm{x} 3)-\mathrm{x} 6)) / 2.3661))+\mathrm{x} 2)))+\operatorname{Exp}((\operatorname{Sqrt}(\operatorname{Sin}(\operatorname{Sin}(\operatorname{Ln}(\mathrm{x} 4))))$ $+(\operatorname{Exp}((\operatorname{Sin}(\operatorname{Sin}((\mathrm{x} 3 * \mathrm{x} 6)))+\operatorname{Sin}(\mathrm{x} 4))) /((\mathrm{x} 3-\operatorname{Ln}(\operatorname{Sin}(\operatorname{Sqrt}(\mathrm{x} 5))))+\mathrm{x} 4))))$

Table 2. Comparison of fitting results by GP ,GEP and GEGEP

Table 3. Comparison of predicted results by GP,GEP and GEGEP

From Table2, we can see that the largest relative errors of GP, GEP and GEGEP are $9.2 \%, 10.8 \%$ and $2.398 \%$ respectively. Meanwhile, among the 15 training samples, the result of GEP has smaller relative errors than the one of GP on 13 samples, and the result of GEGEP has smaller relative errors than the one of GEP on 13 samples. It's obvious that concerning the goodness of fit, GEP outperforms GP and GEGEP outperforms GEP.

From table3, we can see that GEGEP has the higher prediction results and a smaller relative error of Y than the one of GP and GEP on three and one sample respectively.
(2) Function modeling.

The data comes from paper[8], which describes the GDP of China in some periods.
The termination set is defined as $\mathrm{T}=\{\mathrm{K}, \mathrm{L}, ?\}$, where ? represents random numerical constant and is chosen from the interval $[-10,10]$.The function set is defined as $\mathrm{F}=\{+, \neg, *, \div$, sqrt, exp, $\sin , \cos , \ln , \tan \}$. The parameter setting is same as experiment1.

The aim is to obtain a prediction function for GDP with K and L being the parameters: GDP $=\mu(\mathrm{K}, \mathrm{L})$. Fifteen cases from the year 1980 to 1994 in table 4 are used as training datum to build the prediction model, while two cases from 1995 to 1996 in table 5 are used as test datum.

The second column ( K ) in table 3 and table 4 describes the sum of net value of fixed assets and the average balance of floating assets in the corresponding year. The third column ( L ) describes the number of employed person, including all kind of workers and peasants. The fourth column ( calculation result of GDP) describes the actual statistical data of GDP in the same year.From Table4, we can see that the largest relative errors of GP, GEP and GEGEP are $8.29 \%, 3.182 \%$ and $3.177 \%$ respectively. Meanwhile, among the 15 training samples, the result of GEP has smaller relative errors than the one of GP on 13 samples, and the result of GEGEP has smaller relative errors than the one of GEP on 6 samples. It's obvious that concerning the goodness of fit, GEP outperforms GP and GEGEP outperforms GEP.From table5, we can see that GEGEP has the higher prediction results and a smaller relative error of GDP than the one of GP and GEP on one sample.

Table 4. Comparison of fitting results by GP ,GEP and GEGEP

The function evolved by GP is:
GDP=exp $(\ln (\mathrm{K})-576.032 / \mathrm{L})-\ln (\mathrm{K}+\mathrm{L})$
The function evolved by GEP is:
GDP $=\tan (\sin (\sin (\mathrm{L}) / \cos (\mathrm{K})))+\sin (\tan (\mathrm{L}))^{*} 9.16+\log (\operatorname{abs}(\tan (\mathrm{L})))+K^{*} \log (\log (\operatorname{abs}$ $(\operatorname{sqrt}(L-6.44)+L-K))) / 6.32+\log (14.46 * \operatorname{sqrt}(L)+\sin (K)) / \sin (\log (K+L))+\tan (\log (L+5.08)$ *L3/-9.58)

The function evolved by GPGEP is:
GDP=2*((tan(-2.95022)*K)-sqrt((2*K)))-8.92026-2*(((cos(sqrt(((-0.36897)+K)))* $(-8.17927)) /(2.44667))-\tan (\ln (K-5.137215)))-(\tan (0.450852-K)-0.99622)+\tan (\exp (\cos$ $(\ln (\mathrm{K}))))+\exp (\tan (\mathrm{K})) / \cos (\cos (\mathrm{L}))+\tan (((\cos (\operatorname{sqrt}(\mathrm{K}-0.36897))^{*}(-8.17927)) /(2.44667))$ $-\tan (\ln (\mathrm{K}-5.137215)))$

Table 5. Comparison of fitting results by GP ,GEP and GEGEP
# 4 Conclusions 

This paper puts forward a new algorithm GEGEP, which takes GEP as foundation, improves gene structure and introduces the learning mechanism. The learning mechanism benefits preserving good structure which leads to a better evolutionary process. So it has the potential of identifying useful structural information emergent in the evolutionary process. Practical examples show that this alg- orithm possesses the advantages of automation of the modeling process, more flexible and various model structures, wider range of applications, faster speed of convergence and higher precision of fitting and predicted datum.

Future research on GEGEP will mainly focus on the following:
(1) Here we only consider Univariate EDA Model and do not consider Bivariate EDA Model and Multivariate EDA Model. So next we will try to use Bivariate EDA Model or Multivariate EDA Model. (2) The speed of algorithm has decreased because of large quantities of computation spending for statistics. We will adopt some methods to improve. (3)We will realize parallelism which can further improve the ability of solving complex problems. (4)Here we only realize one-layer call model, next we will realize multilayer call model.

# Acknowledgments 

This work is supported by the National Natural Science Foundation of China (Nos. 60473081, 60473037), the National Natural Science Foundation of Education Department of Hebei Province of China under Grant (Nos.2004454, 2005338) and the High Science and Technology Research of Hebei Province of China under Grant (No.05213567, 06213562).
