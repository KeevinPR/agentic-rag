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

| $F$ | Constant of Faraday ( $96485 \mathrm{C} \mathrm{mol}^{-1}$ ). |
| :--: | :--: |
| $R$ | Gas constant ( $\mathrm{J} \mathrm{K}^{-1} \mathrm{~mol}^{-1}$ ). |
| $T$ | Temperature (K). |
| $E_{\text {cell }}$ | Voltage of the DEFC (V). |
| $E_{\text {Ocell }}$ | Standard potential for the DEFC overall reaction (V). |
| $J_{m i}$ | Exchange current at reference concentration in the anode $\left(\mathrm{A} \mathrm{cm}^{-2}\right)$. |
| $J_{o c}$ | Exchange current at reference concentration in the cathode $\left(\mathrm{A} \mathrm{cm}^{-2}\right)$. |
| $J$ | Current density ( $\mathrm{A} \mathrm{cm}^{-2}$ ). |
| $J_{\text {lim }}$ | Limit current density ( $\mathrm{A} \mathrm{cm}^{-2}$ ). |
| $\alpha_{a}$ | Electronic transfer coefficient at the anode catalyst surface. |
| $\alpha_{c}$ | Electronic transfer coefficient at the cathode catalyst surface. |
| $C_{\text {EtoH }}$ | Ethanol concentration ( $\mathrm{mol} \mathrm{cm}^{-3}$ ). |
| $C_{\text {EtoH }}^{\text {ref }}$ | Reference ethanol concentration (mol $\mathrm{cm}^{-3}$ ). |
| $C_{0}$ | Oxygen concentration ( $\mathrm{mol} \mathrm{cm}^{-3}$ ). |
| $C_{0}^{\text {ref }}$ | Reference oxygen concentration (mol $\mathrm{cm}^{-3}$ ). |
| $N$ | Order of reaction at the anode. |
| $N_{O}$ | Order of reaction at the cathode. |
| $k_{\text {eff }}$ | Mass transport coefficients for the cathode. |
| $k_{o}$, | Mass transport coefficients for the anode. |
| $E_{O}^{*}$ | Empirical coefficient (V). |
| $b_{\text {cell }}$ | Empirical coefficient ( $\mathrm{V} \mathrm{dec}^{-1}$ ) |
| $C_{1}$ | Empirical coefficient (V) |
| $C_{2}$ | Empirical coefficient $\left(\mathrm{cm}^{2} \mathrm{~A}^{-1}\right)$ |
| Re | Empirical coefficient ( $\Omega \mathrm{cm}^{2}$ ) |

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

| Parameters | $\alpha_{d}$ | $\alpha_{c}$ | $\frac{C_{O}^{o f}}{C_{O}^{f}}$ | $\frac{C_{O}^{o f}}{C_{O}^{f}}$ | $k_{1}$ | $k_{2}$ | $R_{0}$ | $k_{1 o}$ | H |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Lower | 0.5 | 0.5 | $0.5 \times^{-12}$ | $0.5 \times^{-12}$ | 10 | 1.0 | 0.01 | 10.0 | 3000 |
| Upper | 1.5 | 1.5 | $1.5 \times^{-12}$ | $1.5 \times^{-12}$ | 13.0 | 3.0 | 3.0 | 15 | 3500 |

Table 2
Search space: lower and upper bounds.

| Parameters | $E_{o}^{*}$ | $b$ | $R_{0}$ | $C_{1}$ | $C_{2}$ |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Lower | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Upper | 0.5 | 0.2 | 1.0 | 0.14 | $1 / J_{0 m}$ |

and Marr and Li (1999) and similar to the reference value reported in Andreadis et al. (2006) and Ge and Liu (2006), the range of values of the exchange current densities was selected following results in Rosenthal et al. (2012).

### 4.1. Pramanik model vs. semi-empirical model

To validate our proposal of the semi-empirical model, the results obtained from the parameter estimation with the UMDA ${ }^{C}$ were compared with the results presented in Pramanik and Basu (2010). In this research, the authors presented a semi-empirical model to describe experimental data at different configurations of temperatures for the anode and cathode, $40^{\circ} \mathrm{C}-40^{\circ} \mathrm{C}, 70^{\circ} \mathrm{C}-$ $50^{\circ} \mathrm{C}$ and $90^{\circ} \mathrm{C}-60^{\circ} \mathrm{C}$, respectively.

For this case, we use the dataset of the configuration of $40^{\circ} \mathrm{C}-$ $40^{\circ} \mathrm{C}$ for the parameter estimation procedure, and then, we

Table 3
Result for parameter estimation using the semi-empirical model at $42^{\circ} \mathrm{C}-42^{\circ} \mathrm{C}$ (anode-cathode).

|  | $\alpha_{0}$ | $\alpha_{C}$ | $f_{0,0}^{\text {ref }}$ | $f_{0, c}^{\text {ref }}$ | $k_{1}$ | $k_{2}$ | $R_{0}$ | $k_{0 c}$ | H | SAE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1.20476 | 1.17952 | $0.94389 \times^{-12}$ | $1.43081 \times^{-12}$ | 11.539 | 2.5415 | 1.2905 | 11.037 | 3322.2 | 0.27594 |

Table 4
Results of estimation.

|  | $E_{n}^{\mathrm{a}}$ | $b_{\text {ref }}$ | $R_{n}$ | $C_{1}$ | $C_{2}$ | $S A E$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $25^{\circ} \mathrm{C}$ | 0.18840 | 0.11046 | 0.83490 | 0.86182 | 36.477 | 0.42098 |
| $60^{\circ} \mathrm{C}$ | 0.16119 | 0.13210 | 0.98073 | 0.46815 | 17.742 | 0.66425 |

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

| $\alpha_{a}$ | $\alpha_{c}$ | $\beta_{a, c}^{o l g}$ | $\beta_{a, c}^{o l g}$ | $k_{1}$ | $k_{2}$ | $R_{0}$ | $k_{0 c}$ | H | SAE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 0.89356 | 0.93056 | $1.0820 \times^{-12}$ | $1.3166 \times^{-12}$ | 11.279 | 2.0345 | 2.4715 | 13.769 | 3023.3 | 0.34618 |

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

## References

Andreadis, G., Podias, A., Tsiakaras, P., 2009. A model-based parametric analysis of a direct ethanol polymer electrolyte membrane fuel cell performance. J. Power Sources 194 (1), 397-407. http://dx.doi.org/10.1016/ j.jpowsour.2009.04.064, URL: https://www.sciencedirect.com/science/article/ pii/S0378775309007782. Xlth Polish Conference on Fast Ionic Conductors 2008.

Andreadis, G., Song, S., Tsiakaras, P., 2006. Direct ethanol fuel cell anode simulation model. J. Power Sources 157 (2), 657-665. http://dx.doi.org/10.1016/ j.jpowsour.2005.12.040, URL: https://www.sciencedirect.com/science/article/ pii/S0378775306000140. Selected papers presented at the Ninth Grove Fuel Cell Symposium.
Argyropoulos, P., Scott, K., Shukla, A., Jackson, C., 2002. Empirical model equations for the direct methanol fuel cell DMFCs. Fuel Cells 2 (2), 78-82. http://dx.doi.org/10.1002/fucc. 200290005.
Argyropoulos, P., Scott, K., Shukla, A., Jackson, C., 2003. A semi-empirical model of the direct methanol fuel cell performance: Part I. Model development and verification. J. Power Sources 123 (2), 190-199. http://dx.doi.org/10. 1016/S0378-7753(03)00558-5, URL: https://www.sciencedirect.com/science/ article/pii/S0378775303005585.
Asher, M., Crokei, B., 2015. A review of surrogate models and their application to groundwater modeling. Water Resour. Res. 51, 5957-5973. http://dx.doi. org/10.1002/2015V8016967.
Berning, T., Djilali, N., 2007a. A 3D, multiphase, multicomponent model of the cathode and anode of a PEM fuel cell. J. Electrochem. Soc. 150 (12), A1589. http://dx.doi.org/10.1140/1.1621412.
Berning, T., Djilali, N., 2003b. Three-dimensional computational analysis of transport phenomena in a PEM fuel cell a parametric study. J. Power Sources 124 (2), 440-452. http://dx.doi.org/10.1016/S0378-7753(03)00816-4, URL: http://www.sciencedirect.com/science/article/pii/S0378775303008164.
Blanco-Cocom, L., Botello-Rionda, S., Ordoñez, L., Valdez, S.I., 2021. Robust parameter estimation of a PEMFC via optimization based on probabilistic model building. Math. Comput. Simulation 185, 218-237. http://dx.doi.org/ 10.1016/j.matcom.2020.12.021, URL: https://www.sciencedirect.com/science/ article/pii/S0378475420304766.

Blanco-Cocom, L., Botello-Rionda, S., Ordoñez, L., Valdez, S.I., 2022a. Design optimization and parameter estimation of a PEMFC using nature-inspired algorithms. Soft Comput. http://dx.doi.org/10.1007/s00500-022-07520-y.
Blanco-Cocom, L., Botello-Rionda, S., Ordoñez, L., Valdez, S.I., 2022b. A reaction-convection-diffusion model for PEM fuel cells. Finite Elem. Anal. Des. 201, 103703. http://dx.doi.org/10.1016/j.fheel.2021.103703. URL: https: //www.sciencedirect.com/science/article/pii/S0168874X2100175X.
Blanco-Cocom, L., Botello-Rionda, S., Ordoñez, L., Valdez, S.I., 2022c. A selfvalidating method via the unification of multiple models for consistent parameter identification in PEM fuel cells. Energies 15, 885. http://dx.doi. org/10.3390/en15030885.
Cai, L., Ren, L., Wang, Y., Xie, W., Zhu, G., Gao, H., 2021. Surrogate models based on machine learning methods for parameter estimation of left ventricular myocardium. R. Soc. Open Sci. 8, 201121. http://dx.doi.org/10.1098/rsss. 201121.

Christelis, V., Kopsiattis, G., Mantoglou, A., 2019. Performance comparison of multiple and single surrogate models for pumping optimization of coastal aquifers. Hydrol. Sci. J. 64 (3), 336-349. http://dx.doi.org/10.1080/02626667. 2019.1584400.

Fan, W., Xu, B., Li, H., Lu, G., Liu, Z., 2022. A novel surrogate model for channel geometry optimization of PEM fuel cell based on Bagging-SVM Ensemble Regression. Int. J. Hydrogen Energy 47 (33), 14971-14982. http: //dx.doi.org/10.1016/j.ihydene.2022.02.239. URL: https://www.sciencedirect. com/science/article/pii/S0360319922009338.
García, B.L., Sethuraman, V.A., Weidner, J.W., White, R.E., Dougal, R., 2004. Mathematical model of a direct methanol fuel cell. J. Fuel Cell Sci. Technol. 1 (1), 43-48. http://dx.doi.org/10.1115/1.1782927, arXiv:https://asmedigitalcollection.asme.org/electrochemical/articlepdf/1/1/43/6890213/43_1.pdf.
Ge, J., Liu, H., 2006. A three-dimensional mathematical model for liquid-fed direct methanol fuel cells. J. Power Sources 160 (1), 413-421. http:// dx.doi.org/10.1016/j.jpowsour.2006.02.001. URL: https://www.sciencedirect. com/science/article/pii/S0378775306001856.
Gomes, R., De Bortoli, A., 2016. A three-dimensional mathematical model for the anode of a direct ethanol fuel cell. Appl. Energy 183, 1292-1301. http://dx.doi.org/10.1016/j.apenergy.2016.09.083. URL: https://www.sciencedirect. com/science/article/pii/S030626191631385X.
Gomes, R., De Souza, M., Bortoli, A.D., 2018. A model for direct ethanol fuel cells considering variations in the concentration of the species. Int. J. Hydrogen Energy 43 (29), 13475-13488. http://dx.doi.org/10.1016/ j.ihydene.2018.05.096. URL: https://www.sciencedirect.com/science/article/ pii/S0360319918316124.
Gomes, R., De Souza, M., Bortoli, A.D., 2019. Development of analytical and numerical solutions for direct ethanol fuel cells. Heat Mass Transf. 55, 3301-3316. http://dx.doi.org/10.1007/s00231-019-02666-2.
Guo, T., Sun, J., Zhang, J., Deng, H., Xie, X., Jiao, K., Huang, X., 2017. Transient analysis of passive vapor-feed DMFC fed with neat methanol. Int. J. Hydrogen Energy 42 (5), 3222-3239. http://dx.doi.org/10.1016/j.ihydene.2016.10.122. URL: https://www.sciencedirect.com/science/article/pii/S0360319916331937.
Heidary, N., Jafar Kermani, M., Khajeh-Hosseini-Dalasm, N., 2016. Performance analysis of PEM fuel cells cathode catalyst layer at various operating conditions. Int. J. Hydrogen Energy 41 (47), 22274-22284. http://dx.doi.org/ 10.1016/j.ihydene.2016.08.178. URL: http://www.sciencedirect.com/science/article/pii/S0360319916326726.
Kamarudin, M., Kamarudin, S., Masdar, M., Daud, W., 2013. Review: Direct ethanol fuel cells. Int. J. Hydrogen Energy 38 (22), 9438-9453. http://dx. doi.org/10.1016/j.ihydene.2012.07.059. URL: https://www.sciencedirect.com/ science/article/pii/S0360319912016369.
Kandidayeni, M., Macias, A., Khalatbarisoltani, A., Boulon, L., Kelouwani, S., 2019. Benchmark of proton exchange membrane fuel cell parameters extraction with metaheuristic optimization algorithms. Energy 183, 912-925. http:// dx.doi.org/10.1016/j.energy.2019.06.152. URL: http://www.sciencedirect.com/ science/article/pii/S0360544219312848.
Khajeh-Hosseini-Dalasm, N., Kermani, M., Moghaddam, D.G., Stockie, J., 2010a. A parametric study of cathode catalyst layer structural parameters on the performance of a PEM fuel cell. Int. J. Hydrogen Energy 35 (6), 2417-2427. http: //dx.doi.org/10.1016/j.ihydene.2009.12.111. URL: https://www.sciencedirect. com/science/article/pii/S0360319909820394.
Khajeh-Hosseini-Dalasm, N., Kermani, M., Moghaddam, D.G., Stockie, J., 2010b. A parametric study of the cathode catalyst layer structural parameters on the performance of a PEM fuel cell. Int. J. Hydrogen Energy 35, 2417-2427.
Lan, H., Yang, L., Zheng, F., Zong, C., Wu, S., Song, X., 2020. Analysis and optimization of high temperature proton exchange membrane (HT-PEM) fuel cell based on surrogate model. Int. J. Hydrogen Energy 45 (22), 12501-12513. http://dx.doi.org/10.1016/j.ihydene.2020.02.150.
Larrañaga, P., Etxeberria, R., Lozano, J.A., Peña, J.M., 2000a. Combinatorial optimization by learning and simulation of Bayesian networks. In: Boutilier, C., Goldszmidt, M. (Eds.), Uncertainty in Artificial Intelligence, UAI-2000, Vol. 1. pp. 343-352.

Li, Y., Li, D., Ma, Z., Zheng, M., Lu, Z., 2022. Thermodynamic modeling and performance analysis of vehicular high-temperature proton exchange membrane fuel cell system. Membranes 12 (1), 72. http://dx.doi.org/10.3390/ membranes12010072.
Lu, D., Djilali, N., Berning, T., 2002. Three-dimensional computational analysis of transport phenomena in a PEM fuel cell. J. Power Sources 106 (1-2), 284-294. ISI:000175342600040.
Marr, C., Li, X., 1999. Composition and performance modelling of catalyst layer in a proton exchange membrane fuel cell. J. Power Sources 77 (1), 17-27. http://dx.doi.org/10.1016/S0378-7753(98)00161-X. URL: http://www. sciencedirect.com/science/article/pii/S037877539800161X.
Menesy, A., Sultan, H., Korashy, A., Kamel, S., Jurado, F., 2021. A modified farmland fertility optimizer for parameters estimation of fuel cell models. Neural Comput. Appl. 33, 12369-12190. http://dx.doi.org/10.1007/s00521-021-05821-1.

Moreno-Jiménez, D., Pacheco-Catalán, D., Ordóñez, L., 2015. Influence of MEA catalytic layer location and air supply on open-cathode direct ethanol fuel cell performance. Int. J. Electrochem. Sci. 10 (11), 8808-8822.
Ohensija, M., Leiviska, K., 2010. Validation of genetic algorithm results in a fuel cell model. Int. J. Hydrogen Energy 35 (22), 12618-12625. http://dx.doi.org/ 10.1016/j.ihydene.2010.07.129. URL: http://www.sciencedirect.com/science/ article/pii/S036031991001517X.
Outeiro, M., Chibante, F., Carvalho, A., de Almeida, A., 2008. A parameter optimized model of a proton exchange membrane fuel cell including temperature effects. J. Power Sources 185 (2), 952-960.
Pinto, A.M., Oliveira, V.B., Falcão, D.S., 2018. 2 - Direct alcohol fuel cells basic science. In: Pinto, A.M., Oliveira, V.B., Falcão, D.S. (Eds.), Direct Alcohol Fuel Cells for Portable Applications. Academic Press, ISBN: 978-0-12-811849-8, pp. 17-80. http://dx.doi.org/10.1016/8978-0-12-811849-X.00002-4.
Pramanik, H., Basu, S., 2010. Modeling and experimental validation of overpotentials of a direct ethanol fuel cell. Chem. Eng. Process.: Process Internof. 49 (7), 635-642. http://dx.doi.org/10.1016/j.ceg.2009.10.015. URL: https://www.sciencedirect.com/science/article/pii/S0255278109002153. Process Intensification on Intensified Transport by Complex Geometries.
Rosenthal, N.S., Vilekar, S.A., Datta, R., 2012. A comprehensive yet comprehensible analytical model for the direct methanol fuel cell. J. Power Sources 206, 129-143. http://dx.doi.org/10.1016/j.jpowsour.2012.01.080. URL: https://www.sciencedirect.com/science/article/pii/S0378775312001796.
Scott, K., Jackson, C., Argyropoulos, P., 2006. A semi empirical model of the direct methanol fuel cell. Part II. Parametric analysis. J. Power Sources 161 (2), 885-892. http://dx.doi.org/10.1016/j.jpowsour.2006.04.147. URL: https: //www.sciencedirect.com/science/article/pii/S037877530600807X.
Secanell, M., Karan, K., Suleman, A., Djilali, N., 2007. Multi-variable optimization of PEMFC cathodes using an agglomerate model. Electrochim. Acta 52, $6318-6337$.
Shah, A., Kim, G.-S., Sui, P., Harvey, D., 2007. Transient non-isothermal model of a polymer electrolyte fuel cell. J. Power Sources 163 (2), 793-806. http://dx.doi.org/10.1016/j.jpowsour.2006.09.022. URL: http://www.sciencedirect. com/science/article/pii/S0378775306019264. Selected Papers presented at the FUEL PROCESSING FOR HYDROGEN PRODUCTION SYMPOSIUM at the 230th American Chemical SocietyNational Meeting Washington, DC, USA, 28 August - 1 September 2005.
Song, D., Wang, Q., Liu, Z., Navessin, T., Eikerling, M., Holdcroft, S., 2004. Numerical optimization study of the catalyst layer of PEM fuel cell cathode. J. Power Sources 126 (1), 104-111. http://dx.doi.org/10.1016/j.jpowsour.2003. 08.045.

Song, D., Wang, Q., Liu, Z., Navessin, T., Eikerling, M., Holdcroft, S., 2004. Numerical optimization study of the catalyst layer of PEM fuel cell cathode. J. Power Sources 126 (1), 104-111. http://dx.doi.org/10.1016/j.jpowsour.2003.08.043. URL: https://www.sciencedirect.com/science/article/pii/S0378775303010000.
Sun, S., Su, Y., Yin, C., Jermsittiparsert, K., 2020a. Optimal parameters estimation of PEMFCs model using Converged Moth Search Algorithm. Energy Rep. 6, 1501-1509. http://dx.doi.org/10.1016/j.egcr.2020.06.002. URL: http://www. sciencedirect.com/science/article/pii/S2352484720306697.
Sun, J., Zhang, G., Guo, T., Che, G., Jiao, K., Huang, X., 2020b. Effect of anisotropy in cathode diffusion layers on direct methanol fuel cell. Appl. Therm. Eng. 165, 114589. http://dx.doi.org/10.1016/j.applthermaleng.2019.114589, URL: https://www.sciencedirect.com/science/article/pii/S155943111934325X.
Sun, J., Zhang, G., Guo, T., Jiao, K., Huang, X., 2018. A three-dimensional multi-phase numerical model of DMFC utilizing Eulerian-Eulerian model. Appl. Therm. Eng. 132, 140-153. http://dx.doi.org/10.1016/j.applthermaleng. 2017.12.037. URL: https://www.sciencedirect.com/science/article/pii/ S1359431117364116.

Tiedemann, W., Newman, J., 1975. Maximum effective capacity in an obmically limited porous electrode. J. Electrochem. Soc. 122 (11), 1482-1485. http: //dx.doi.org/10.1149/1.2134046.
Trinovan, R., Giurgea, S., Miraoui, A., Cirrincione, M., 2008. Surrogate model for proton exchange membrane fuel cell (PEMFC). J. Power Sources 175 (2), 773-778. http://dx.doi.org/10.1016/j.jpowsour.2007.09.097. URL: https://www.sciencedirect.com/science/article/pii/S0378775307021040.

Valdez, S.L. Hernández, A., Botello, S., 2010. Efficient estimation of distribution algorithms by using the empirical selection distribution. In: Korosec, P. (Ed.), New Achievements in Evolutionary Computation. InTech, ISBN: 978-953-307-053-7.
Viana, F., Haftka, R., Steffen, V., 2009. Multiple surrogates: how cross-validation errors can help us to obtain the best predictor. Struct. Multidiscip. Optim. 39, 439-457. http://dx.doi.org/10.1007/s00158-008-0338-0.
Wang, G., Mukherjee, P.P., Wang, C.-Y., 2007. Optimization of polymer electrolyte fuel cell cathode catalyst layers via direct numerical simulation modeling. Electrochim. Acta 52 (22), 6367-6377. http://dx.doi.org/10.1016/j. electacta.2007.04.073, URL: http://www.sciencedirect.com/science/article/pii/ 50013468607005683.
Wang, J., Wang, H., Fan, Y., 2018. Techno-economic challenges of fuel cell commercialization. Engineering 4 (3), 352-360. http://dx.doi.org/10. 1016/j.eng.2018.05.007, URL: https://www.sciencedirect.com/science/article/ pii/S2095809917307750.

Yakout, A.H., Koth, H., AboRas, K.M., Hasanien, H.M., 2022. Comparison among different recent metaheuristic algorithms for parameters estimation of solid oxide fuel cell: Steady-state and dynamic models. Alex. Eng. J. 61 (11), 8507-8523. http://dx.doi.org/10.1016/j.aej.2022.02.009, URL: https://www. sciencedirect.com/science/article/pii/S1110016822000977.
You, L., Liu, H., 2001. A parametric study of the cathode catalyst layer of PEM fuel cells using a pseudo-homogeneous model. Int. J. Hydrogen Energy 26 (9), 991-999. http://dx.doi.org/10.1016/S0360-3199(01)00035-0, URL: http: //www.sciencedirect.com/science/article/pii/S0360319901000350.
Zhang, J., Sanderson, A., 2009. JADE: adaptive differential evolution with optional external archive. IEEE Trans. Evol. Comput. 13 (45), 945-958. http://dx.doi. org/10.1109/TEVC.2009.2014613.
Zhang, G., Xiao, C., Razmjooy, N., 2020. Optimal parameter extraction of PEM fuel cells by meta-heuristics. Int. J. Ambient Energy 1-10. http://dx.doi.org/ 10.1080/01430750.2020.1745276.