# Novel Absorber Based on Pixelated Frequency Selective Surface Using Estimation of Distribution Algorithm 

Mengyun Zhao, Xiaowei Yu, Qiao Wang, Peng Kong, Yun He, Ling Miao, and Jianjun Jiang


#### Abstract

A novel design method for absorber is presented, based on pixelated FSS with common effect of metallic pixels and lumped resistors. Considering the relative position of resistors and pixelated patches, the estimation of distribution algorithm is firstly employed to optimize the absorbing performance. Optimization process demonstrates its availability and high-efficiency. An absorption band ( $3.08-6.00 \mathrm{GHZ}$ ) below -6 dB formed with two strong absorption peaks is achieved, compared with the poor absorption performance in pixelated FSS without resistors. The simulated surface current distributions suggest that the loaded resistors are the main source for energy loss of incident electromagnetic wave, and provide an intuitive explanation to the correlation of optimized unit cell geometry and corresponding absorption peaks. The designed absorber is fabricated and the measured reflectivity curve fits well with the simulated results, which indicates that the availability of novel design method.


Index Terms-Frequency selective surfaces (FSSs), microwave absorbers and optimization methods.

## I. InTRODUCTION

ABSORBER is a kind of function device for applications in special fields, such as radar systems, and military utilities. With the development of radar detection and anti-stealth technology, the new demands for improving the low-frequency performance of absorber are badly needed. As a potential candidate of high performance absorber, the frequency selective surface (FSS) has been the subject of intensive investigation in the past forty decades [1]-[9].

Currently, two methods are most used to design the geometry of the FSS, the one is adopt the basic patterns of varying size such as square patch, crisscross or ring [1], [2], [4], [9]. Youquan Li et al. presented a method to reduce radar cross section by application of periodic array of metallic patches [9]. The other is design the geometry of a FSS by splitting the unit cell area up into smaller pixels [5], [7], [8], [10]-[12]. Genovesi et al. put forward the design of a pixelated FSS by using a specifically derived particle swarm optimization procedure [10]. Unlike a conventional FSS, the pixelated FSS optimization pro-

[^0]cedure allows for a vast amount of flexibility and thereby improves thechance of finding a desired unit cell geometry. Meanwhile, some researchers presented that the absorber can result in a wide absorption bandwidth by the selection of the appropriate values of lumped resistors [2], [3], [13]. The means of loading resistors has been shown to be very effective due to its ability to change the original absorbing mechanism and enhance the bandwidth. However, absorber with common effect of metallic pixels and lumped resistors is rarely reported because traditional algorithms cannot deal with position matching problem.

In order to achieve novel absorber, the estimation of distribution algorithm (EDA) will be used for the first time on account of its algorithmic simplicity and prefect performance in variate dependency problems. EDA has a theoretical foundation in probability theory [14] and already been used to tackle various problems in science and engineering [15]-[19].

This letter proposes a new design method for absorber based on resistors loaded pixelated FSS (RPFSS) and a RPFSS design for $2-6 \mathrm{GHZ}$ is obtained. The performance of this absorber is firstly optimized using EDA, considering the position matching between metallic pixels and loaded resistors. We analyze optimization process and result of EDA. The absorbing mechanism is also presented through the simulation of surface current distribution. The corresponding absorber structure is fabricated and measured to verify our design finally.

## II. DESIGN METHODOLOGY

As shown in Fig. 1, the absorber structure is comprised of four layers, FSS layer, substrate layer, dielectric layer and metallic ground layer. Its absorption performance mainly depends on the FSS unit cell geometry, which is pixelated into a $10 \times 10$ grid here. Each pixel is represented by a binary bit, indicating the presence, " 1 ", or absence, " 0 ", of perfect electric conducting (PEC) metal. Considering the symmetry of unit cell, only one eighth triangular part is encoded to 15 bits binary number [in Fig. 1(b)], represented by $\boldsymbol{F}_{\text {position }}$. So this absorber is obviously independent on the polarization of an incident wave. Furthermore, a resistor " $\boldsymbol{R}$ " is introduced to a " 0 " position between two " 1 " positions, to achieve new loss mechanism and enhance the bandwidth. The resistor position $\boldsymbol{R}_{\text {position }}$, and the resistor value $\boldsymbol{R}_{\text {value }}$ are encoded with real numbers in following optimization process.

In this letter, our design method is used to achieve a novel absorber in 2-6 GHZ. In the simulations (using High Frequency Structure Simulator software) and fabrications, the substrate $(0.8 \mathrm{~mm})$ is FR4 with a permittivity of 4.4 and a loss tangent of 0.02 . Honeycomb is chosen as the dielectric layer ( 3.2 mm )

[^0]:    Manuscript received February 09, 2015; accepted March 05, 2015. Date of publication March 24, 2015; date of current version July 01, 2015. This work was supported in part by the National Natural Science Foundation of China under Grant 61172003.

    The authors are with the School of Optical and Electronic Information, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: miaoling@mail.hust.edu.cn).

    Color versions of one or more of the figures in this letter are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/LAWP. 2015.2411692

![img-0.jpeg](img-0.jpeg)

Fig. 1. (a) Side view of FSS based absorber structure. (b) Top view of an example of RPFSS and its unit cell geometry.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Simulated model of unit cell geometry of RPFSS.
since its high strength and low-density with a permittivity of 1.07 and a loss tangent of 0.0017 . The total thickness of novel absorber ( $\boldsymbol{h}$ ) is 4 mm . As shown in Fig. 2, the size of FSS unit cell is $36 \mathrm{~mm} \times 36 \mathrm{~mm}$, and the size of pixel is $3.6 \mathrm{~mm} \times 3.6 \mathrm{~mm}$ correspondingly. It should be noted that the diagonal connection of two pixels is cut off to avoid the difficulty in fabrication and the resistor pixel is specially handled to match with adjacent metallic pixels (in Fig. 2).

## III. EDA Optimization Process

The RPFSS unit geometry is optimized to improve the absorption performance. We have found that the application of EDA to RPFSS design is promising from several points of view. First of all, EDA has unique advantages in variate dependency problems. Applying the joint probability distribution, EDA can abide by dependence relationship between metallic pixel position and resistor position in the whole process. Secondly, it is potential of EDA to perform hybrid encoding in optimization, where resistor position and resistor value are encoded with real
![img-2.jpeg](img-2.jpeg)

Fig. 3. Our EDA optimization process with interrelation of parameters.
numbers while metallic pixel position is encoded with a binary number. In addition, EDA is simple to understand and can be easily implemented.

The three parameters to be optimized are metallic pixel position ( $\boldsymbol{F}_{\text {position }}$ ), resistor position ( $\boldsymbol{R}_{\text {position }}$ ) and resistor value ( $\boldsymbol{R}_{\text {value }}$ ). Their interrelation is illustrated on the left side of Fig. 3. As shown in Fig. 3, our EDA optimization process can be summarized as following:

1) Initialize a population of N individuals randomly $(\mathrm{N}=$ 600 here).
2) Simulate the reflectivity curve of each individual by using HFSS software and calculate corresponding fitness value, according to the fitness function

$$
\boldsymbol{F}=\boldsymbol{B} \boldsymbol{W} \times 10+\boldsymbol{S}_{\text {mean }} / \boldsymbol{D} \boldsymbol{E} \boldsymbol{P}
$$

Here. $\boldsymbol{B} \boldsymbol{W}$ is the bandwidth (in GHZ) of reflectivity curve below the threshold value $\boldsymbol{D E P}(-6 \mathrm{~dB})$, and $\boldsymbol{S}_{\text {mean }}$ is the average reflectivity in desired frequency band ( $2-6 \mathrm{GHZ}$ in our research). Both the magnitude and bandwidth of the reflectivity are taken account of in this fitness function. The increase of $\boldsymbol{B} \boldsymbol{W}$ provides the main contribution to the maximum of the fitness function.
3) Sort all N individuals in descending order by their fitness values, and select the forefront M individuals ( $\mathrm{M}=180$ here).
4) Rebuild probability distributions of $\boldsymbol{R}_{\text {value }}, \boldsymbol{R}_{\text {position }}$ and $\boldsymbol{F}_{\text {position }}$ under the condition $\boldsymbol{R}_{\text {position }}$ (that is, $\boldsymbol{P}\left(\boldsymbol{R}_{\text {value }}\right), \boldsymbol{P}\left(\boldsymbol{R}_{\text {position }}\right)$ and $\boldsymbol{P}\left(\boldsymbol{F}_{\text {position }} \mid \boldsymbol{R}_{\text {position }}\right)$ ) through calculating frequency of corresponding ones in the previous M individuals.
Here, $\boldsymbol{R}_{\text {position }}$ is an integer (varies from 1 to 6 ) and $\boldsymbol{R}_{\text {value }}$ value is chosen from $[1.0,5.1,10.0,30.0,100.0$, $300.0,510.0,750.0,910.0,2000.0]$ ohm.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Optimization process for RPFSS.
5) Generate $\mathrm{N}-\mathrm{M}$ new individuals based on the sampling from $\boldsymbol{P}\left(\boldsymbol{R}_{\text {value }}, \boldsymbol{R}_{\text {position }}, \boldsymbol{F}_{\text {position }}\right)$, which can be obtained through the following formula

$$
\begin{aligned}
& \boldsymbol{P}\left(\boldsymbol{R}_{\text {value }}, \boldsymbol{R}_{\text {position }}, \boldsymbol{F}_{\text {position }}\right) \\
& =\boldsymbol{P}\left(\boldsymbol{R}_{\text {value }}\right) \cdot \boldsymbol{P}\left(\boldsymbol{R}_{\text {position }}\right) \cdot \boldsymbol{P}\left(\boldsymbol{F}_{\text {position }} \mid \boldsymbol{R}_{\text {position }}\right)
\end{aligned}
$$

6) Unite the previous M individuals and $\mathrm{N}-\mathrm{M}$ new individuals to generate new population in next iteration, and repeat Steps 2)-5) until the stop criterion is met (Maximum iteration is 15 here).
The above-mentioned process is applied to the optimization problem of the RPFSS and its process with best individual for the each iteration is illustrated in Fig. 4. Both the best fitness value and the average fitness value increase continuously. It suggests that the RPFSS performance is constantly improved and proves the validity of the EDA. Meanwhile, the observed results that the RPFSS individual is varied with different the positions of the resistors and the pixelated patches in optimization process indicate that the EDA can sustain diversity in population efficiently. Furthermore, the best fitness value and the average fitness value are rapidly converged at seventh iteration and tenth iteration, respectively. The size of the population is only $0.24 \%$ of the total number of candidates which is 245760 . These shows that the high efficiency of the EDA.

## IV. Simulations and MEASUREMENTS

We next choose the RPFSS individual with best fitness value in above optimization process as our designed absorber. Its unit cell geometry is shown in Fig. 5(a) and the optimized parameter values are $\boldsymbol{R}_{\text {position }}=4, \boldsymbol{R}_{\text {value }}=100 \mathrm{ohm}$, and $\boldsymbol{F}_{\text {position }}=$ $\begin{array}{lllllllllllll}1 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1\end{array}$, respectively. Its reflectivity curve plotted in Fig. 5(c) is formed with two strong absorption peaks, whose reflectivity values are -8.67 dB at 3.64 GHZ and -9.77 dB at 5.86 GHz , respectively. For this result, EDA achieves good optimization performance.

A comparison between this optimized pixelated FSS with and without resistors in Fig. 5(b), is also presented to reveal the important role of loaded resistors. The reflectivity curve of designed pixelated FSS without resistors has only one weak absorption peak with reflectivity value of -3.54 dB at 6.13 GHZ ,

![img-4.jpeg](img-4.jpeg)

Fig. 5. Unit cell geometries of the optimized pixelated FSS (a) with and (b) without resistors, (c) corresponding reflectivity curves simulated by HFSS with distributions of surface current on optimized RPFSS (i) at 3.64 GHZ and (ii) at 5.86 GHZ.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Fabricated samples of pixelated FSS (a) with resistors and (b) without resistors, (c) the measured and simulated reflectivity curves.
and has little absorption (above -1 dB ) at the most frequency. Obviously, the loaded resistors could remarkably enhance the absorption performance in the desired frequency range.

To better understand the absorbing mechanism of this novel design, the surface current distributions are also simulated for the unit cell geometry of optimized RPFSS at 3.64 GHZ and 5.86 GHZ , as shown in Fig. 5. It is illustrated in Fig. 5 that the large electric currents are induced in the resistors, which cause the main loss. Fig. 5(i) indicates that the surface current is concentrated in four corners and resistors at first absorption peak ( 3.64 GHZ ). Meanwhile Fig. 5(ii) indicates that the surface current is concentrated in the central big square patch and resistors at second absorption peak ( 5.86 GHZ ). These intriguing phenomena provide intuitive explanations to the correlation of optimized FSS structure and corresponding absorption peaks. These results indicate EDA's ability to seek the perfect position matching between metallic pixels and loaded resistors.

We finally fabricate the designed RPFSS absorber, and measure its reflectivity curve in a microwave anechoic chamber for an electromagnetic wave with normal incidence to the surface over the frequency range of $2-8 \mathrm{GHz}$.

The fabricated RPFSS and corresponding reflectivity curves are shown in Fig. 6. For the pixelated FSS with resistors [in Fig. 6(a)], the measured absorption band (3.13-6.42 GHZ) below -6 dB is also formed with two strong absorption peaks. Its reflectivity values are -14.39 dB at 3.80 GHZ and -10.14 dB at 5.68 GHz . These measured results fit well with the simulated results, which indicates that the RPFSS achieves

the goal. Yet, the intensity of first peak in measured result is some different from that in simulated result. Similar features are observed in the sample without resistors [in Fig. 6(b)]. These results with different bandwidths have the same intensity and the same location of the absorption peak. The causes of inconsistent results may be attributed to the errors in the fabrications and measurements.

Little literature has been found on the research of absorber in 2-6 GHz. To estimate performance of the absorber, two regular and important indexes are considered: $\boldsymbol{f}_{\boldsymbol{H}} / \boldsymbol{f}_{\boldsymbol{L}}$ and $\boldsymbol{h}$ [20], [21]. The total thickness ( $\boldsymbol{h}$ ) is about $0.04 \boldsymbol{\lambda}$ of $\boldsymbol{f}_{\boldsymbol{L}}$ and $0.08 \boldsymbol{\lambda}$ of $\boldsymbol{f}_{\boldsymbol{H}}$. Meanwhile, $\boldsymbol{f}_{\boldsymbol{H}} / \boldsymbol{f}_{\boldsymbol{L}}$ reach up to 2.05 from measurement results. It means that this novel absorber is ultra-thin and wideband.

## V. CONCLUSION

This letter puts forward a new design method for absorber based on RPFSS and a novel absorber for 2-6 GHZ. The performance of this absorber is firstly optimized using the EDA, considering the position matching between metallic pixels and loaded resistors. The optimization process demonstrates the availability and high-efficiency of EDA. An absorption band (3.08-6.00 GHZ) below -6 dB formed with two strong absorption peaks is achieved in the simulated frequency range of $2-6 \mathrm{GHZ}$. The simulated results confirm the correlation of optimized FSS structure and corresponding absorption peaks and prove the availability of RPFSS design method. Through analyzing the simulated surface currents, it is found that the novel design has changed the absorbing mechanism by the application of the resistors. Finally, the corresponding absorber structure is fabricated and measured to verify our design. It is shown that the trend of the measurement result is identical to the design result. To summarize our studies, the RPFSS design method by application of EDA could achieve the desired results efficiently and the novel design with resistors cannot only generate the strong absorption peaks, but also enhance the bandwidth.
