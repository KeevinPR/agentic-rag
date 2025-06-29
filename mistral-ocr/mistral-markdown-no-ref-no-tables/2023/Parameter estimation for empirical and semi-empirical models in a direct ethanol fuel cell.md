# Research paper 

## Parameter estimation for empirical and semi-empirical models in a direct ethanol fuel cell

Luis Blanco-Cocom ${ }^{\text {a }}$, Salvador Botello-Rionda ${ }^{\text {a }}$, L.C. Ordoñez ${ }^{\text {b }}$, S. Ivvan Valdez ${ }^{\text {c, }}$<br>${ }^{a}$ Centro de Investigación en Matemáticas, A.C., Jalisco S/N, Col. Valenciana CP: 36023, Guanajuato, Gto, Apartado Postal 402, CP 36000, Mexico<br>${ }^{\text {b }}$ Unidad de Energía Renovable, Centro de Investigación Científica de Yucatán. Parque Científico Tecnológico de Yucatán, Mérida, Yucatán, CP 97302, Mexico<br>${ }^{c}$ CONACYT-Centro de Investigación en Ciencias de Información Geoespacial, CENTROGEO, A.C., C.P. 76703, Querétaro, Mexico

## A R T I C L E I N F O

## Article history:

Received 25 April 2023
Received in revised form 22 June 2023
Accepted 3 July 2023
Available online 11 July 2023
Dataset link: https://github.com/penfc-tea
m-CMCGCY/DEFC_SE.git

## Keywords:

Direct ethanol fuel cell (DEFC)
Empirical mathematical model
Semi-empirical mathematical model
Parameter estimation
UMDA ${ }^{\text {C }}$

## A B S T R A C T

Experimental data from a Direct Ethanol Fuel Cell (DEFC) provides a general perspective about its performance; nevertheless, it does not provide information about the cell's physical characteristics nor information to improve its performance. On the other hand, numerical simulation can be used to test the cell's design and boost its performance but requires a set of physical parameters. In this proposal, we introduce a novel modification to an empirical model for a Direct Methanol Fuel Cell to make it suitable for DEFC simulations at different temperatures by a new semi-empirical mathematical model. In addition, we introduce temperature-depending parametric forms of several terms to reduce the number of possible parameters to estimate from the DEFC. Then, we combined the models with an estimation of distribution algorithm to find the numerical simulation that best reproduces the experimental polarization curve. The method is validated by estimating the parameters to reproduce the experimental data at different temperatures reported in the literature, and with data obtained in an in-house open-cathode DEFC, recorded at a scan rate of $10 \mathrm{mVs}^{-1}$, using as fuel $\mathrm{CH}_{3} \mathrm{CH}_{2} \mathrm{OH} 1 \mathrm{M}$ at $25^{\circ} \mathrm{C}$ and $60^{\circ} \mathrm{C}$. From the estimation results at temperature set $T_{1}=\left(T_{1 \mathrm{a}}, T_{1 \mathrm{c}}\right)^{\circ} \mathrm{C}$, the same parameters are used for a simulation at $\widehat{T}_{2}=\left(T_{2 \mathrm{a}}, T_{2 \mathrm{c}}\right)^{\circ} \mathrm{C}$, demonstrating that it reproduces the two experimental polarization curves. Hence, the models and methods presented here can be used to reduce physical experimentation and to test different designs and operation settings.
(C) 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 1. Introduction

In recent years, there has been an increase in the study of alternative energy generation sources. Among them, fuel cells have been widely studied for their use in the transport and industrial sectors (Wang et al., 2018).

Mathematical modeling is an essential tool for fuel cells' analysis in virtue of understanding the key parameters that control their performance and identifying different operating or configuration conditions that could increase the overall efficiency. The model complexity depends on their level of precision to reproduce the phenomena. In the literature, there exists a variety of mathematical models: those based on algebraic expressions to describe physical relations that occur in the fuel cell, they are called empirical or semi-empirical models, and we obtain the behavior of the polarization curves by setting a set of empirical or semi-empirical parameters through non-linear regression methods (Zhang and Sanderson, 2009; Ohenoja and Leiviskä, 2010;

[^0]Outeiro et al., 2008). Interface models, this kind of models describe the diffusion processes through the anode, membrane, and cathode using diffusion equations (assuming that the catalytic layer is negligible) (Lu et al., 2002; Berning and Djilali, 2003a,b). Macro-homogeneous models consist of a set of non-linear ordinary differential equations; they assume that the main reactions occur in the catalytic layers, and describe the physical compositions of the materials (Tiedemann and Newman, 1975; Marr and Li, 1999; You and Liu, 2001; Song et al., 2004; Khajeh-HosseiniDalasm et al., 2010b; Heidary et al., 2016); Agglomerated models, these formulations are conformed by a set of partial differential equations, model diffusion in the cell, provide a description of the physical composition, porosity, and conglomerates of the catalytic layers of the fuel cell. Secanell et al. (2007), Shah et al. (2007) and Wang et al. (2007).

In general, to simulate a DEFC using models in 2D and 3D, it is necessary to create or adapt sophisticated computational tools such as a finite element method, finite volume method, and computational fluid dynamics (CFD), among others. The numerical simulation depends on the geometry of the different layers of the fuel cell, which often require fine meshes, hence increasing


[^0]:    * Corresponding author.

    E-mail address: sergio.valdez@conacyt.mx (S.I. Valdez).

## List of important variables for mathematical models

the computational time (Blanco-Cocom et al., 2022b). Regarding optimization and parameter estimation, simpler mathematical models are better suited for the thousand of evaluations of the objective function (Blanco-Cocom et al., 2021), but some of the estimated parameters could be useful for a variety of models with different complexities.

Mathematical models where the transport and diffusion of the species are considered through the different layers in alcohol fuel cells are found in Gomes and De Bortoli (2016), Pinto et al. (2018), Gomes et al. (2018), Sun et al. (2018), Gomes et al. (2019) and Sun et al. (2020b). Nevertheless, for the purpose of reducing computation cost, simple models are often used as surrogate models (Fan et al., 2022; Lan et al., 2020; Tirnovan et al., 2008); they have the potential to speed up the numerical simulation without significantly sacrificing accuracy in the output of interest, for instance, the polarization curve, and may reduce numerical instability, which contributes to calibration and uncertainty analysis (Cai et al., 2021; Christelis et al., 2019; Asher and Crokei, 2015; Viana et al., 2009), hence, speeding up the testing of different parameter values.

Regarding the estimation of parameters, several optimization techniques have been explored to analyze the behavior of fuel cells, such as the Farmland Fertility Optimization Algorithm (FFA) (Menesy et al., 2021), the Owl search algorithm (OSA) (Zhang et al., 2020), the Shuffled frog-leaping algorithm
![img-0.jpeg](img-0.jpeg)

Fig. 1. Direct ethanol fuel cell scheme.
(SFLA), the firefly optimization algorithm (FOA), and imperialist competitive algorithm (ICA) (Kandidayeni et al., 2019) which are employed to extract parameters of a semi-empirical model for a PEMFC; in Yakout et al. (2022), authors studied four different evolutive optimizers, Gorilla troops optimizer (GTO), Honey badger algorithm (HBA), African vultures optimization algorithm (AVOA), and Chimp optimization algorithm (ChOA), which are applied to estimate parameters in a SOFC. Nevertheless, a comparison of several metaheuristics for parameter estimation in a semi-empirical mathematical model for a PEMFC is presented in Blanco-Cocom et al. (2021), in this research, the best results were obtained by the Genetic Algorithm (GA), the Particle Swarm Optimization (PSO), and the Univariate Marginal Distribution Algorithm with Gaussian models (UMDA ${ }^{\mathrm{L}}$ ). In addition, the latest algorithm has been successfully applied to optimize parameters to the macro-homogeneous (Blanco-Cocom et al., 2022c) and reaction-convection-diffusion (Blanco-Cocom et al., 2022a) mathematical models for PEMFCs, with the advantages of having an stopping criterion based on convergence, instead of an arbitrary number of iterations.

Direct alcohol fuel cells convert the alcohol chemical energy into electrical energy, heat, and other products. Direct ethanol fuel cells (DEFCs) have been studied in recent years due to ethanol being non-toxic fuel, renewable, and can be easily produced by fermentation of sugar-containing raw materials (Andreadis et al., 2006, 2009). In addition, open-cathode fuel cells are an alternative since they reduce the use of auxiliary systems for the supply of oxygen from the air increasing the global system energy efficiency. The ethanol oxidation reaction at the DEFC anode is,
$\mathrm{CH}_{3} \mathrm{CH}_{2} \mathrm{OH}+3 \mathrm{H}_{2} \mathrm{O}=2 \mathrm{CO}_{2}+12 \mathrm{H}^{+}+12 e^{-}$
and the oxygen reduction reaction at the cathode is,
$3 \mathrm{O}_{2}+12 \mathrm{H}^{+}+12 e^{-}=6 \mathrm{H}_{2} \mathrm{O}$
corresponding to the global reaction, see Fig. 1,
$\mathrm{CH}_{3} \mathrm{CH}_{2} \mathrm{OH}+3 \mathrm{O}_{2}=2 \mathrm{CO}_{2}+3 \mathrm{H}_{2} \mathrm{O}$
A diversity of reported mathematical models describes the profile of the polarization curves of alcohol fuel cells (Argyropoulos et al., 2002; Scott et al., 2006; Pramanik and Basu, 2010; Sun et al., 2020a; Gomes and De Bortoli, 2016). A general mathematical formulation for a Direct Methanol Fuel Cell (DMFC) is found in Argyropoulos et al. (2003) and Scott et al. (2006), and it is given

by,

$$
\begin{aligned}
E_{\text {cell }}= & E_{\text {Ocell }}-R_{n} j-\frac{R T}{F}\left(\frac{1}{\alpha_{s}}+\frac{1}{\alpha_{c}}\right) \ln j-\frac{R T}{\alpha_{c} F} \\
& \times\left[\ln \frac{C_{O}^{\text {ref }}}{j_{\text {oc }}\left(C_{O}\right)^{N_{O}}}-N_{O} \ln \left(1-\frac{j}{n F k_{10} C_{O}}\right)\right]-\frac{R T}{\alpha_{s} F} \\
& \times\left[\ln \frac{C_{\text {Met }}^{\text {ref }}}{j_{\text {loc }}\left(C_{\text {Met }}\right)^{N}}-N \ln \left(1-\frac{j}{n F k_{\text {eff }} C_{\text {Met }}}\right)\right]
\end{aligned}
$$

where $E_{\text {Ocell }}$ is the standard potential for the DMFC overall reaction, which theoretically is given by the Nernst equation, $j_{m}, j_{\text {oc }}$ are the exchange current at reference concentration in the anode and cathode, $\alpha_{s}, \alpha_{c}$ are the electronic transfer coefficients at the anode and cathode catalyst surfaces, respectively. $C_{\text {Met }}$ is the methanol concentration, $C_{\text {Met }}^{\text {ref }}$ is the reference methanol concentration, $N$ and $N_{O}$ are the orders of reactions, $k_{o}, k_{\text {eff }}$ are the mass transport coefficients for the cathode and anode, respectively. This model is successfully applied to reproduce experimental data on a small-scale DMFC in Scott et al. (2006).

Due DEFC have similar behavior to DMFC, in this paper, we propose surrogate (semi-)empirical mathematical models based on the model showed in Eq. (4) to describe the polarization curve for a DEFC.

We consider the following assumptions for the DEFC mathematical models implementation: The system was steady-state and isothermal, the fluids are incompressible, the gases are considered ideal, the cell components are isotropic and homogeneous, and the membrane is fully hydrated.

In Section 2, we describe two mathematical models, the first model, used to simulate the performance of a DMFC (Argyropoulos et al., 2002, 2003; Scott et al., 2006), is modified to simulate the performance of a DEFC in this paper, and the second model is a proposed adaptation of the standard model presented in Scott et al. (2006). We also present the parameter estimation problem. In Section 3, experimental settings and conditions for a laboratory DEFC are presented. Results and discussion are described in Section 4. Finally, a general conclusion is presented in Section 5.

## 2. Mathematical formulations

In this section, two mathematical models to describe the performance of a DEFC are presented as surrogate models of the previous mathematical formulation for a DMFC in Eq. (4).

### 2.1. Empirical formulation

To model the performance of the DEFC, as the first surrogate approach, we propose to use the empirical formulation to model Direct Methanol Fuel Cells (DMFC) studied in Argyropoulos et al. (2002, 2003) and Scott et al. (2006), the mathematical expression is presented in Eq. (5). The voltage $E_{\text {cell }}$ is described as,
$E_{\text {cell }}=E_{\mathrm{O}}^{*}-b_{\text {cell }} \log j-R_{n} j+C_{1} \ln \left(1-C_{2} j\right)$
where
$b_{\text {cell }}=\frac{2.303 R T}{F}\left(\frac{1}{\alpha_{s}}+\frac{1}{\alpha_{c}}\right), C_{1}=\frac{6 R T}{\alpha_{s} F}, C_{2}=\frac{1}{n F k_{\text {eff }} C_{\text {Etoft }}}$
$E_{\mathrm{O}}^{*}=E_{\text {Ocell }}-\frac{R T}{\alpha_{c} F} \ln \left(\frac{C_{O}^{\text {ref }}}{j_{\text {loc }}\left(C_{O}\right)^{N_{O}}}\right)-\frac{R T}{\alpha_{s} F} \ln \left(\frac{C_{\text {Met }}^{\text {ref }}}{j_{\text {loc }} C_{\text {Etoft }}^{\text {ref }}}\right)$
The main idea is to estimate the set of parameters $\left\{E_{o}^{*}, b_{\text {cell }}, R_{e}\right.$, $\left.C_{1}, C_{2}\right\}$, that best fit the experimental polarization curve for a DEFC.

This model has been successfully applied to study DMFCs in Argyropoulos et al. (2002). In general, the analysis of mathematical models must consider the whole possible range and domain, for instance, applying logarithmic functions can generate
complex values that must be avoided. In particular, in Eq. (5), the expression $\ln \left(1-C_{2} j\right)$ should be a real number, $\forall j>0$, to obtain this and then, to avoid numerical errors or incorrect solutions, the necessary condition is that
$0<1-C_{2} j, \leftrightarrow C_{2}<1 / j, \quad \forall j>0$.
Then, in particular, $C_{2}<1 / J_{f i m}$, where $J_{f i m}$ the limit current density of the DEFC at temperature $T$, due $j<J_{f i m}, \forall j>0$. Additionally, with this condition, we obtain an upper bound for $C_{2}$ that preserves the expected behavior in the profiles of $E_{\text {cell. }}$.

### 2.2. Semi-empirical formulation

The mathematical model in Eq. (4) contains different parameters that cannot be obtained straightforwardly and require expertise and laboratory time, for instance, $\alpha_{s}, \alpha_{c}$, that depend on physical properties that are measurable with high uncertainty. The simulation of a design of fuel cells must be temperaturedependent because of temperature limits the performance of the DEFC, for this reason, a model that reproduces the behavior under different temperatures is an actual topic in the fuel cell area (Kamarudin et al., 2013; Pinto et al., 2018; Li et al., 2022). In this subsection, we present a proposed surrogate semi-empirical expression of Eq. (4), based on previous work in Scott et al. (2006), our proposal integrates the temperature and is suited for simulating a DEFC at different temperatures in the anode and cathode:
$E_{\text {cell }}(\widehat{T})=E_{O}^{*}(\widehat{T})-b_{\text {cell }}(\widehat{T}) \log j-R_{e}(\widehat{T}) j$

$$
+C_{1}(\widehat{T}) \ln \left(1-C_{2}(\widehat{T}) j\right)
$$

with algebraic expressions in terms of the temperature $\widehat{T}=$ $\left(T_{a}, T_{c}\right)$, where $T_{a}$ and $T_{c}$ are the temperatures in the anode and cathode, respectively, and,

$$
\begin{gathered}
b_{\text {cell }}(\widehat{T})=\frac{2.303 R}{F}\left(\frac{T_{a}}{\alpha_{s}}+\frac{T_{c}}{\alpha_{c}}\right) \\
C_{1}(\widehat{T})=\frac{N R T_{a}}{\alpha_{s} F} \\
C_{2}(\widehat{T})=\frac{1}{n F k_{\text {eff }}\left(T_{a}\right) C_{\text {Etoft }}} \\
E_{O}^{*}(\widehat{T})=E_{\text {Ocell }}-\frac{R T_{c}}{\alpha_{c} F} \ln \left(\frac{k_{1}}{j_{0, c}}\right)-\frac{R T_{a}}{\alpha_{s} F} \ln \left(\frac{k_{2}}{j_{0, a}}\right)
\end{gathered}
$$

where $k_{1}=\frac{C_{\text {met }}^{\text {ref }}}{C_{\text {Etoft }}}$, and $k_{2}=\frac{C_{\text {met }}^{\text {ref }}}{C_{0}}$, were selected because the reference concentrations are complicated to measure experimentally, then we include the related parameters as simple constants.

The resistivity is correlated with the temperatures in the anode and cathode by a modified expression based on the reported in (Scott et al., 2006),
$R e(\widehat{T})=R_{0} \exp \left(\frac{2 B}{T_{a}+T_{c}}-\frac{B}{T_{0}}\right)$
where $R_{0}\left(\Omega \mathrm{~cm}^{2}\right)$ and $T_{0}(\mathrm{~K})$, are the base resistance and the base temperature, respectively, and the constant $B \approx 3724$ is a constant.

The effective mass coefficient is depending on the anode temperature and ethanol concentration, and is described by,
$k_{\text {eff }}\left(T_{a}\right)=k_{\text {lo }} C_{\text {Etoft }} \exp \left(-\frac{H}{T_{a}}\right)$
where $k_{\text {lo }}$, and $H$ are constants (Scott et al., 2006). The parameters $j_{\text {loc }}, j_{\text {oc }}$ are described by,
$j_{0, a}=A_{a} i_{0, a}^{\text {ref }} j_{0, c}=A_{c} i_{0, c}^{\text {ref }}$

These parameters are in the order of $1 \times 10^{-10}$ (Song et al., 2004). The specific reaction surface area of the catalyst layer is related to the Pt loading, $m_{\mathrm{Pt}}$, and the catalyst layer thickness, $L$, as follows (Khajeh-Hosseini-Dalasm et al., 2010a):
$A=A_{0} \frac{m_{\mathrm{Pt}}}{L}$
where $A_{0}$ is the catalyst surface area per unit mass of the catalyst (Marr and Li, 1999).

Notice that previous expressions in this subsection depend on temperature $\bar{T}$, while the other parameters are constant for different temperatures; hence a valid simulation model must reproduce the outputs for different temperatures using the same remaining parameters. In this article, we use that fact for the validation of the model and estimated parameters, that is to say, we propose to estimate the values of the set of parameters $\theta=\left\{\alpha_{a}, \alpha_{c}, \int_{a, a}^{e d}, \int_{b, c}^{e d}, k_{1}, k_{2}, R_{0}, k_{1 e}, H\right\}$ to fit the experimental polarization curve at temperatures $\bar{T}_{1}=\left(T_{1 a}, T_{1 c}\right)$, and then, using the estimated parameters, if the model is valid, it must reproduce the experimental polarization curve at temperatures $\bar{T}_{2}=\left(T_{2 a}, T_{2 c}\right)$, which dataset is not used for the fitting process, using the estimated parameters. Hence, in computational terminology, the experimental data at $\bar{T}_{1}$ is the training data, while the experimental data at $\bar{T}_{2}$ is the validation data.

### 2.3. Parameter estimation problem

To obtain a set of estimated parameters for the empirical and semi-empirical models, we use the Univariate Marginal Distribution Algorithm with Gaussian models (UMDA ${ }^{\mathrm{G}}$ ); this numerical strategy is a kind of Estimation of Distribution Algorithm (Larrañaga et al., 2000a) that assumes that the probabilistic distribution of the populations of $n$ variables is an $n$-dimensional joint probability function that is factored as a product of univariate and independent probability functions, that following a convergence criterion, the algorithm evolves until reaching a result of the parameter estimation problem in a region with high probability, more details for implementation and robustness in Valdez et al. (2010) and Blanco-Cocom et al. (2021), see diagram 2. In this work, the UMDA ${ }^{\text {G }}$ uses the objective function as the sum of the absolute error between experimental data obtained from a polarization curve and the output of the model,
$\min S A E(\hat{\theta})=\sum_{s=1}^{N}\left|V^{F C}\left(j_{s}\right)-V\left(j_{s} ; \hat{\theta}\right)\right|$
where $N$ is the number of the experimental data, $V^{F C}\left(j_{s}\right)$ and $V\left(j_{s} ; \hat{\theta}\right)$ are the $\hat{s}$-th experimental datum and the voltage output of the mathematical model, respectively, at current density $j_{s}$. We apply a stopping criteria given by a function of the variance of the population presented in Blanco-Cocom et al. (2021).

## 3. Experimental settings

In this section, we present experimental data from two experimental direct ethanol fuel cells, the first dataset was obtained from Pramanik and Basu (2010), and the second dataset was obtained with an experimental DEFC in-house design.

### 3.1. Pramanik and basu experimentation

In Pramanik and Basu (2010), the authors used a single fuel cell with a MEA of $5 \mathrm{~cm}^{2}$ electrode area with a serpentine-type channel geometry of $2 \mathrm{~mm} \times 2 \mathrm{~mm}$, for both the anode and the cathode. The catalysts were $\mathrm{Pt} / \mathrm{Ru}(40: 20 \mathrm{wt} \%$ )/C and high surface area (HSA) platinum black (Johnson Matthey Inc., UK). The chamber's pressure was set at 1 bar. The fuel cell was fed with ethanol
![img-1.jpeg](img-1.jpeg)

Fig. 2. General diagram of the UMDA ${ }^{\text {G }}$ algorithm, more details in Blanco-Cocom et al. (2021).

1M at a rate of $1.2 \mathrm{~mL} \mathrm{~min}^{-1}$, Nafion ${ }^{\circledR}$ (SE-5112, DuPont, USA) was the membrane. Pure oxygen ( $99.99 \%$ by volume) was used. Hydrogen peroxide and $\mathrm{H}_{2} \mathrm{SO}_{4}$ (E. Merck) were used for cleaning and protonation of the fused membrane, in addition, isopropanol (E. Merck) was used as diluent. Temperature controllers were used to setting different values of temperature at the anode and cathode, respectively, more details in Pramanik and Basu (2010).

### 3.2. In-house experimentation

The experimental tests were obtained with an open-cathode DEFC designed in our laboratory, see Fig. 4. The anode has a serpentine flow pattern with a 1.5 mm channel width, 1.5 mm rib, 1.5 mm channel depth, $50 \%$ electrical contact to electrode area. The cathode has an architecture open to the atmosphere with rhombohedral pins as electric contacts, a 2.12 channel width, 1.5 mm channel depth, and $61 \%$ of electrical contact with respect to the area of the electrode. Both electrodes have an active area of $9 \mathrm{~cm}^{2}$. Nafion ${ }^{\circledR} 117$ membrane was the electrolyte. We used a PtRu/C catalyst at the cathode with a metal loading of 1 mgPt $\mathrm{cm}^{-2}$. At the anode side, we use a combination of two catalyst layers: one inner catalyst layer of $\mathrm{PtSn} / \mathrm{C}$ deposited directly onto the membrane with a metal loading of $0.5 \mathrm{mgPt} \mathrm{cm}^{-2}$, plus an outer catalyst layer of $\mathrm{PtRu} / \mathrm{C}$ deposited on the carbon cloth diffuser with a metal loading of $0.5 \mathrm{mgPt} \mathrm{cm}^{-2}$. Before testing the cell, the membrane-electrode-assembly (MEA) was activated by flowing $1.5 \mathrm{~mL} \mathrm{~min}^{-1}$ of deionized water through the anode side for 3 h at $60^{\circ} \mathrm{C}$. Then the voltage was fixed at 100 mV for 1800 s . After that, it was changed to 600 mV for 300 s . DEFC polarization curves were recorded at 25 and $60^{\circ} \mathrm{C}$ with a scan rate of 10 $\mathrm{mV} \mathrm{s}^{-1}$ and using a $\mathrm{CH}_{3} \mathrm{CH}_{2} \mathrm{OH} 1 \mathrm{M}$ solution, more details about experimentation in Moreno-Jiménez et al. (2015).

## 4. Results and discussion

The parameters for the UMDA ${ }^{\mathrm{G}}$ are given by $\operatorname{Max}_{\text {iter }}=1000$ with a population size of 200 individuals and a convergence tolerance of $1 \times 10^{-5}$.

The search space for the empirical mathematical model with the upper and lower bounds for each parameter is presented in Table 2, these values were obtained from the reported results in Argyropoulos et al. (2003). For the semi-empirical model, the search space for parameter estimation with upper and lower

![img-2.jpeg](img-2.jpeg)

Fig. 3. Results of the parameter estimation of the semi-empirical model in this research compared with the results of the semi-empirical model used by Pramanik and Basu (2010) and with the experimental data at: (a) $40^{\circ} \mathrm{C}-40^{\circ} \mathrm{C}$; (b) $70^{\circ} \mathrm{C}-50^{\circ} \mathrm{C}$; (c) $90^{\circ} \mathrm{C}-60^{\circ} \mathrm{C}$. Figure (d): The power curves generated with the estimation, validations, and experimental data.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Physical design for the experimental DEFC.
bounds for each parameter was obtained from the reported results in Scott et al. (2006), Song et al. (2004) and Khajeh-HosseiniDalasm et al. (2010a), see Table 1. These intervals were fixed following information from the literature, $\alpha_{d}$ and $\alpha_{c}$ have values between 0.5 (Guo et al., 2017; Ge and Liu, 2006) and 1.5 (García et al., 2004), the range for $R e$ and $k_{1 o}$ was obtained from Scott et al. (2006), $k_{1}$ and $k_{2}$ was obtained considering $C_{O}^{o f f}=1 e^{-3}$ $\mathrm{mol} \mathrm{cm}^{-3}$, and $C_{O}^{o f}=0.5 \times 10^{-6} \mathrm{~mol} \mathrm{~cm}^{-3}$, half of the reported value in Song et al. (2004), Khajeh-Hosseini-Dalasm et al. (2010a)

Table 1
Search space: lower and upper bounds.

Table 2
Search space: lower and upper bounds.

and Marr and Li (1999) and similar to the reference value reported in Andreadis et al. (2006) and Ge and Liu (2006), the range of values of the exchange current densities was selected following results in Rosenthal et al. (2012).

### 4.1. Pramanik model vs. semi-empirical model

To validate our proposal of the semi-empirical model, the results obtained from the parameter estimation with the UMDA ${ }^{C}$ were compared with the results presented in Pramanik and Basu (2010). In this research, the authors presented a semi-empirical model to describe experimental data at different configurations of temperatures for the anode and cathode, $40^{\circ} \mathrm{C}-40^{\circ} \mathrm{C}, 70^{\circ} \mathrm{C}-$ $50^{\circ} \mathrm{C}$ and $90^{\circ} \mathrm{C}-60^{\circ} \mathrm{C}$, respectively.

For this case, we use the dataset of the configuration of $40^{\circ} \mathrm{C}-$ $40^{\circ} \mathrm{C}$ for the parameter estimation procedure, and then, we

Table 3
Result for parameter estimation using the semi-empirical model at $42^{\circ} \mathrm{C}-42^{\circ} \mathrm{C}$ (anode-cathode).
Table 4
Results of estimation.

use the set of the estimated parameters in the proposed semiempirical model and change the anode and cathode temperatures to reproduce the experimental dataset at configurations of $70^{\circ} \mathrm{C}-50^{\circ} \mathrm{C}$ and $90^{\circ} \mathrm{C}-60^{\circ} \mathrm{C}$, we called these evaluations as "validations". The results for parameter estimations are shown in Table 3.

In Fig. 3, we plotted the polarization curves as a result of the estimation and the validation results. We observe that with the $U M D A^{2}$, we reached a set of parameters that fits the experimental data better than the semi-empirical Pramanik and Basu model in Pramanik and Basu (2010). For validations, we observed that the polarization curves reproduce the behavior of the experimental data al configurations of $70^{\circ} \mathrm{C}-50^{\circ} \mathrm{C}$ and $90^{\circ} \mathrm{C}-60^{\circ} \mathrm{C}$. We also plotted the power curves, and the profiles are very similar to the expected from the experimental data.

### 4.2. In-house experimentation vs. empirical model

In this case, we use the results of our experimental DEFC, and we present the results of the parameter estimation of the empirical model presented in Section 2.1. Table 2 shows the search space with upper and lower bounds for each parameter; Table 4 presents the estimated parameters obtained with the UMDA ${ }^{2}$. We can observe that simulations have the expected behavior compared with the experimental results for both experimental sets at $25^{\circ} \mathrm{C}$ and $60^{\circ} \mathrm{C}$, see Fig. 5. The estimated parameters are similar to those reported for a DMFC in Argyropoulos et al. (2003) and Scott et al. (2006).

### 4.3. In-house experimentation vs. the proposed semi-empirical model

We present the results of the semi-empirical formulation in Section 2.2. The numerical experiment consists of analyzing the effect of the temperature in the semi-empirical model using our experimental data at two different temperatures. We estimate the set of parameters using the experimental data of $60^{\circ} \mathrm{C}$, and we reproduce the profile of the second experimental data set evaluating only the temperature of $25^{\circ} \mathrm{C}$ in the semi-empirical model. The value of $L=0.0118 \mathrm{~cm}$ was considered as the following result in Song et al. (2004), and $A_{0}=112 \mathrm{~m}^{2} / \mathrm{g}$ was considered for the catalyst type at $20 \mathrm{wt} \% \mathrm{Pt}$ on carbon black (Marr and Li, 1999).

The estimated parameters obtained are presented in Table 5. Fig. 6, shows the comparative plots of the results applying the semi-empirical model. We observe that simulations are comparable in both experimental cases, at $60^{\circ} \mathrm{C}$ with the parameter estimation and at $25^{\circ} \mathrm{C}$ in the validation; this is, with our proposed model we reproduce the profile of the polarization curve at $25^{\circ} \mathrm{C}$ using the results of the parameter estimation with data at $60^{\circ} \mathrm{C}$.

The power curves obtained from the estimated parameters are presented in Fig. 7. Estimation with the empirical model approximates the expected behavior for the data at $25^{\circ} \mathrm{C}$ and $60^{\circ} \mathrm{C}$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparative results of simulations of the empirical model and experimental measurements.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Comparative results of the semi-empirical model with the experimental measurements: parameter estimation with data of $60^{\circ} \mathrm{C}$, and validation with data of $25^{\circ} \mathrm{C}$.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Comparative results for power curves.

Table 5
Result for parameter estimation using the semi-empirical model at $60^{\circ} \mathrm{C}$.
However, with the semi-empirical model, we obtain a better approximation to the experimental power curves; this is, with the estimation at $60^{\circ} \mathrm{C}$, it is possible to recover the appropriate profile for the power curve at $25^{\circ} \mathrm{C}$, showing that the proposal in this article reproduces adequately the experimental data.

Despite the two presented models having different complexities, the semi-empirical model recovers the values for the parameters of the empirical model; this is, with the estimated parameters in the semi-empirical estimation, we recover similar values of $E_{o v}=0.14698, b=0.14503$ and $C_{2}=16.434$ for the empirical model, see Table $4-60^{\circ} \mathrm{C}$. With this result, we unify the two mathematical models.

The advantage of our methodology is that our mathematical proposals reproduce the expected profiles of the polarization and power curves by changing the operating temperatures in a DEFC by only using the results of a set of estimated parameters with the UMDA ${ }^{G}$, with this, the limitations, as a surrogate mathematical model, are that the modeling of the DEFC is defined by the number of parameters to estimate, but this is the idea of a surrogate mathematical model, to give us a feasible simulation to describe the performance of a physical problem as simple as possible conserving the physical expected behavior (Asher and Crokei, 2015).

## 5. Conclusions

The numerical simulation of DEFC requires accurate models and precise parameters to reproduce its performance. Some of these parameters are not directly measured in the laboratory; hence a method for estimating them is needed. We present a study case of the parameter estimation of empirical and semiempirical models as surrogate models for the mathematical model in expression in Eq. (4) to describe the performance of the experimental DEFC. The proposal in this article is the assembly of numerical techniques to reproduce experimental data by a numerical model via an optimization problem with a meta-heuristic. The estimations for the empirical model reproduce successfully the profiles of the experimental polarization curves at $25^{\circ} \mathrm{C}$ and $60^{\circ} \mathrm{C}$ from our in-house DEFC. In addition, we found parameters with the semi-empirical model using the experimental data at $60^{\circ} \mathrm{C}$, then we use the very same model and parameters for $25^{\circ} \mathrm{C}$, and the model still fits the experimental data at this temperature; hence we have strong evidence that the estimated parameters are those of the physical fuel cell, and that the numerical model reproduces the fuel cell behavior at different temperatures, as in the comparison with the Pramanik and Basu model and its experimental data. If the fuel cell function is reproduced by the numerical model, thus it can be used for analyzing the cell performance under different conditions, even for proposing changes in operational or design parameters, reducing the experimental costs.

In future work, we will explore the feasibility to include of the crossover current density in our surrogate semi-empirical model to describe the physical performance of a DEFC, in addition, this type of numerical experimentation will permit us to generate more complex simulations with Computational Fluid Dynamics (CFD) to analyze fluxes or transport of species in the channels of the anode or cathode with more precision.

# CRediT authorship contribution statement 

Luis Blanco-Cocom: Investigation, Methodology, Software, Writing, Salvador Botello-Rionda: Methodology (numerical simulation of cells), Conceptualization, Supervision, Resources (Post-doctoral Advisor of Luis Blanco). L.C. Ordoñez: Validation (verifying that results are physically plausible and congruent), Methodology (Range of input parameters for searching, expert on fuel cells), Writing - review \& editing. S. Ivvan Valdez: Conceptualization (optimization methods and objective functions), Analysis, Methodology, Supervision (co-advisor of Luis Blanco), Writing - review \& editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

https://github.com/ pemfc-team-CMCGCY/DEFC_SE.git.

## Acknowledgments

This article was supported by CONACYT, Mexico under grant 3588040. S. Ivvan Valdez is supported by IxM-CONAHCYT grant 7795. Thanks to CONACYT-sustentabilidad energética grant 254667.
