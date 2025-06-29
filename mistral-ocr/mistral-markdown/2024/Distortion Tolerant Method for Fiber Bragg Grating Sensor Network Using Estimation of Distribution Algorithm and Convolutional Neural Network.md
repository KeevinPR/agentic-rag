# Distortion Tolerant Method for Fiber Bragg Grating Sensor Network Using Estimation of Distribution Algorithm and Convolutional Neural Network 

Yuemei Luo ${ }^{\ominus}$, Member, IEEE, Chenxi Huang ${ }^{\oplus}$, Chaohui Lin ${ }^{\ominus}$, Yuan Li ${ }^{\oplus}$, Jing Chen ${ }^{\ominus}$, Xiren Miao ${ }^{\ominus}$, and Hao Jiang ${ }^{\ominus}$


#### Abstract

In this article, we proposed a distortion-tolerant method for fiber Bragg grating (FBG) sensor networks based on the estimation of distribution algorithm (EDA) and convolutional neural network (CNN). Addressing the parameter reconstruction of the reflection spectrum, an objective function is formulated to pinpoint the Bragg wavelength detection problem, with the optimal solution acquired via EDA. By incorporating spectral distortion into the objective function, the EDA-based method effectively manages distorted spectrums, ensuring the fidelity of wavelength data. Further, CNN aids in extracting features from the entire FBG sensor network's wavelength information, facilitating the creation of the localization model. By sending the reliable wavelength data obtained by EDA to the trained model, swift identification of the load position is achieved. Testing revealed that under conditions of spectral distortion, EDA can adeptly detect the Bragg wavelength. Additionally, the CNN-trained localization model outperforms other machinelearning techniques. Notably, experimental results demonstrate that the proposed EDA surpasses the second-ranked method, i.e., the maximum method, achieving a root mean square error (RMSE) of merely $1.4503 \mathbf{~ m m}$ which is substantially lower than the 6.2463 mm achieved by the maximum method. The average localization error remains under 2 mm when 5 out of 9 FBGs' reflection spectra are distorted. Furthermore, Bragg wavelength detection error stays below 1 pm amid spectral distortion. Consequently, our method offers promising application prospects for long-term FBG sensor network monitoring, ensuring high accuracy and robustness in detecting structural damage.


Index Terms-Bragg wavelength detection, convolutional neural network (CNN), estimation of distribution algorithm (EDA), fiber Bragg grating (FBG) sensor network, spectral distortion.

## I. INTRODUCTION

N RECENT decades, optical sensing technique based on fiber grating has been developed rapidly [1]. Compared to

Manuscript received 25 December 2023; revised 19 March 2024; accepted 29 March 2024. Date of publication 8 May 2024; date of current version 22 May 2024. This work was supported by the National Key Research and Development Program of China under Grant 2023YFC3402800. The Associate Editor coordinating the review process was Dr. Rajarshi Gupta. (Corresponding author: Hao Jiang.)
Yaemei Luo is with the Institute for AI in Medicine, School of Artificial Intelligence, Nanjing University of Information Science and Technology, Nanjing 210044, China (e-mail: luoyuemei@nuist.edu.cn).
Chenxi Huang is with the Institute of Systems Science, National University of Singapore, Singapore 119615 (e-mail: chenxihuang@u.nus.edu).
Chaohui Lin, Jing Chen, Xiren Miao, and Hao Jiang are with the College of Electrical Engineering and Automation, Fuzhou University, Fuzhou 350108, China (e-mail: 1046717035@qq.com; chenj@fzu.edu.cn; mxv@fzu.edu.cn; jiangh@fzu.edu.cn).
Yuan Li is with the School of Computer Science, Nanjing University of Information Science and Technology, Nanjing 210044, China (e-mail: rrilyuan@163.com).
Digital Object Identifier 10.1109/TIM.2024.3398101
traditional electrical sensors, fiber Bragg grating (FBG), as a wavelength-modulated fiber sensor, has various advantages, such as small size, strong anti-electromagnetic interference, strong anti-radiation, high stability, and multichannel reusability [2]. FBG sensors are widely used in civil engineering, power industry, aerospace, biomedical, and other fields, especially in the structural health monitoring (SHM) system of infrastructure [3], [4], [5]. In the SHM system, multiple FBG sensors embedded in the structure constitute the FBG sensor network with certain network topology and realize the distributed measurement of structural physical quantities by reuse technology [6], [7]. Since the sensing information collected by FBG sensors can be used to identify the structure damage, its reliability is crucial to enable SHM systems to evaluate the operation status of the structure accurately.

FBG usually works in demanding conditions such as complex strain, high temperature, and irradiation, which inevitably leads to a gradual degradation of their performance over time [8]. This degradation typically manifests as a distortion in the FBG's reflected wavelength spectrum, indicating a failure in the FBG due to aging effects. In addition, arising from long-term cyclic loading, the strain concentration occurs in the cracks inside FBG, resulting in an uneven internal strain distribution [9]. The reflection spectra are distorted with these issues, further impairing the accuracy of sensing information transmission.

FBG sensor networks are often integrated into the infrastructure of the system they monitor. In such configurations, when an FBG sensor is deemed to have failed-defined specifically as an FBG whose waveform distortion is directly linked to the aging of the component-it needs intervention. Repairing or replacing a failed FBG is problematic as it involves disrupting the entire structure in which the FBG network is embedded. Such interventions can result in significant economic losses and potentially induce secondary damages. Consequently, it is necessary to design an effective mechanism that can tolerate distorted spectra without changing and destroying the entire FBG network structure to ensure the long-term stability of SHM systems.

In this article, we propose a load localization method with self-healing capability based on estimation of distribution algorithm (EDA) and convolutional neural network (CNN) for FBG sensor networks in the case of reflection spectral distortion. To improve the accuracy and reliability of wavelength measurement, the demodulation of the reflection

spectrum is converted into a function optimization problem according to the theoretical model which can characterize the distorted spectrum. We choose EDA, a powerful evolutionary algorithm that owns excellent optimization performance, to find the appropriate solution to the problem. After fully considering the characteristics of the distorted spectrum in the constructed objective function, EDA can obtain wavelength information accurately in the case of spectral distortion. Besides, we construct a CNN model by extracting the deep features of the Bragg wavelength data of all FBGs in the sensor network. The complicated relationship between Bragg wavelength and load position can be effectively captured with the nonlinear fitting ability of the convolution layer in CNN. After completing the localization model training, the position of the load can be calculated from the wavelength data reflecting the variation information of the monitored strain object. The proposed EDA-CNN method ensures that the FBG sensing information can be accurately acquired after spectral distortion, thereby achieving efficient and reliable load position recognition.

The key contributions of this article can be summarized as follows.

1) To address the reflection spectral distortion in FBG sensor networks, we propose a load localization method with self-healing capability based on EDA and CNN by transforming the demodulation into a function optimization problem.
2) For accurate wavelength measurement under spectral distortion, we apply EDA to detect Bragg wavelength information, enhancing both accuracy and reliability.
3) We develop a CNN localization model to extract deep features of Bragg wavelength data and capture the relationship between the Bragg wavelength and the load position, compensating for distortion errors for real time and scalable self-healing.

## II. Related Works

Currently, the studies of FBG sensor networks with self-healing ability are the development trend to improve the stability and reliability of the FBG sensor network. Hayle et al. [10] have designed a self-healing FBG sensor network that uses an optical switch and a deep learning technique to improve the multipoint strain sensing performance and reliability. Subsequently, Hayle et al. [11] presented a novel self-healing fiber/free-space optics communication and sensor network that uses a coarse wavelength-division multiplexer, a scanning-laser interrogation system, and a radial basis function neural network algorithm to achieve cost-effective, flexible, and accurate transmission and sensing of optical signals. Furthermore, Chang and Tsai [12] introduced a novel large-scale three-layer-ring optical fiber sensor network that uses optical switches and remote nodes to achieve reconfigurable routing and robust self-healing functions. Yuan et al. [13] used a passive ladder-shaped sensor network that uses FBGs and optocouplers to perform strain sensing and failure detection. Overall, these methods use a special topology to make the FBG sensor network self-healing.

However, they not only increase the complexity of the FBG sensor network and the cost of the system layout but also bring new hidden dangers due to additional optical devices and link structures.

Some researchers have applied advanced data processing methods to achieve the restoration of failed FBG sensors. Manie et al. [14] proposed a novel deep learning method for improving the accuracy and capacity of a self-healing FBG sensor network that uses intensity wavelength division multiplexing (IWDM). The authors demonstrated that their gated recurrent unit algorithm could measure the strain-sensing signals of overlapping FBGs with high precision and lowcomputational time. Hu et al. [15] presented a new FBG sensor network model that enhanced its self-healing ability using graph theory and optical switching. The study compared three self-short-circuit algorithms and found that the shortest-path faster algorithm achieved a high repair accuracy of nearly $90 \%$ and had an average repair time of 0.103 s , the shortest in this study. Dey et al. [16] employed a machine learning approach to analyze the optical properties of different types of FBGs using artificial neural networks (ANNs). The authors showed that their model could predict the output spectrum accurately and quickly for various device parameters. Hu et al. [17] introduced a deep learning method based on a long short-term memory neural network for demodulating the signals of FBG sensors. The method could achieve high accuracy, low error, fast speed, and distorted spectrum recognition for a large number of sensors. However, these repair method can only complete the reconstruction of the model in the offline stage and has no ability for real-time processing. With the increase of failed FBG sensors, the number of models needed to be constructed increased.

## III. METHODS

## A. Self-Healing Function for Failed FBG

According to the strain sensing principle of FBG, the FBG Bragg wavelength has a linear relationship with the strain [18]. Through the analysis of wavelength data of all FBGs, we learn the strain distribution in the structure and indirectly determine the position of the external load. The dimension of wavelength data depends on the scale of the FBG sensor network. The more FBGs embedded in the structure, the higher the dimension of wavelength data. The weight of all dimensions in wavelength data should occupy the same component that the detection region of each FBG in the structure is different. The wavelength data are not suitable for dimensionality reduction. To avoid the computational difficulty caused by the high dimension of data, and to prevent sensing information loss, the convolution layer and pooling layer in CNN are used to extract the feature of the wavelength information [19], [20]. The output of our CNN is the predicted value of the load position $(x, y)$, which is a continuous value rather than a discrete category or class, aligning with the use of CNN as a regressor instead of a classifier. The error between the predicted and the actual value of the load position can be calculated and is used to continuously update the weights and biases of the CNN through backward propagation. After

training, the CNN parameters are fixed, and the localization model is obtained.

FBG sensor inevitably suffers from performance degradation in the external harsh environment and the long-term effect of alternating load, and the reflection spectrum produces a certain degree of distortion. This can cause a deviation between the detection result of Bragg wavelength deviates and the actual values, and decrease the reliability of the sensing information. The scale of the FBG sensor network embedded in the structure is usually large. Limited by the layout technology and the economic cost, it is difficult to repair and replace the failed FBGs. Hence, to ensure the reliability of sensing information, the EDA is used to obtain the Bragg wavelength based on the idea of function optimization [21], [22], [23]. First, multiple sets of reflection spectra constructed by theoretically distorted spectrum models constitute the initial population. According to the similarity between the constructed spectrum and the actual spectrum, Individuals with large deviations are eliminated. Next, the corresponding probabilistic model is generated based on the remaining excellent individuals and the population is expanded by sampling the probabilistic model. Lastly, We update and sample the probabilistic model continuously until the optimization process is over. The optimal solution can accurately describe the variation of the monitored strain object under the spectral distortion and realize the self-repair of the failed FBG.

The schematic of applying the FBG sensor network to identify the position of external load is shown in Fig. 1. The reflection spectra of all FBGs are collected by an optical spectrum analyzer (OSA) through a 3 dB optical coupler and sent to the personal computer (PC) for spectral analysis and localization model training. In the proposed method, the identification of load positions can be mainly divided into two stages, offline training and online localization. At the offline training stage, the Bragg wavelengths obtained by demodulating the normal spectra are used as the input, and the corresponding load position is used as the label to train CNN to build the localization model. At the online localization stage, when the unknown external load acts on the monitored structure, EDA detects the Bragg wavelength of the collected reflection spectra to ensure its accuracy, no matter whether the reflection spectra are normal or distorted. Then, the wavelength data are sent to the well-trained CNN model to predict the load position.

## B. Load Localization Model Based on CNN

The localization precision of external load, one of the important evaluation indexes in the SHM system, determines the accuracy of the damage identification and affects the reliability of the system evaluating the structural safety degree. The key of load localization is to find the mapping relationship between the wavelength data as input and the load position as output. The Bragg wavelength offsets generated by FBG at different positions under the same external load are different, and the Bragg wavelength offsets generated by the same FBG are also different while the magnitude or position of the external load is different. If each FBG is regarded as a pixel and the Bragg wavelength takes the corresponding gray value,
![img-0.jpeg](img-0.jpeg)

Fig. 1. Schematic of load localization based on FBG sensing network. OSA: optical spectrum analyzer. PC: personal computer.
the wavelength data of the whole FBG sensor network can be abstracted into an image. According to the experience of image processing, the localization model can be established by extracting the deep features of FBG Bragg wavelength data.

Based on the above theoretical analysis, CNN is used to establish the localization model. The dataset required to train the model can be expressed as

$$
D=\left(P_{1}, T_{1}\right), \ldots,\left(P_{k}, T_{k}\right), \ldots,\left(P_{N}, T_{N}\right)
$$

where $P_{k}=\left(\lambda_{1 k}, \lambda_{2 k}, \ldots, \lambda_{L k}\right)$ is the Bragg wavelength for all FBG under the $k$ th load, $L$ is the number of FBG in the entire FBG sensor network, $T_{k}=\left(x_{k}, y_{k}\right)$ is the corresponding position of the $k$ th load. The reflection spectra of FBG are collected by applying strain to different positions of the structure object. A large amount of training data can be obtained by detecting the wavelength of all collected spectra. And the wavelength data are sent into CNN for deep feature extraction. The network eventually generates a set of 2-D data, representing the load position predicted by CNN. The prediction results of each generation are compared with the actual values to adjust the weight of the whole network. After continuous learning, the error between the predicted and the actual values tends to be stable, and the training process of the CNN model is completed.

CNN is a multi-layer supervised learning neural network. Different from the ordinary deep neural network, the connection of neurons in CNN has the characteristics of local connection and weight sharing, it can avoid many unnecessary calculations of model parameters in the training process and dramatically reduce the complexity of the network. CNN is suitable for a large number of data feature learning to find the appropriate weights that respond to the mapping relationship between input and output. The basic structure of CNN mainly includes three modules: convolution layer, pooling layer, and output layer. As shown in Fig. 2, for an image sample, a feature vector can be calculated to represent the deep-seated features of the original image information through the feature

![img-3.jpeg](img-3.jpeg)

Fig. 2. Basic structure of CNN.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Schematic of convolution operation process.
extraction of the convolution layer and the pooling layer. The feature vector is transmitted to an output layer consisting of a fully connected layer to calculate the corresponding prediction result.

The convolution layer is the core of CNN, and its function is to extract the features of the input. The process of convolution operation is shown in Fig. 3, assuming an input image size of $5 \times 5$, a convolution kernel size of $3 \times 3$, and a step size of 1 . The convolution operation starts from the upper left corner of the image. According to the order from left to right and from top to bottom, the convolution window slides with a fixed step length. When the convolution kernel completes the traversal process of the whole image, a new feature map is generated. The formula for each convolution window sliding operation can be expressed as

$$
y_{i}^{l}=f\left(\sum_{i \in M_{j}} x_{i}^{l-1} * k_{i j}^{l}+b_{j}^{l}\right)
$$

where $x_{i}^{l}$ is the $i$ th feature map of the $l$ th convolution layer, $k_{i j}^{l}$ is the convolution kernel of the $j$ th feature map of the $l$ th convolutional layer, $M_{j}$ is the set of feature maps of the input layer, $b_{j}^{l}$ is the bias vector corresponding to the $j$ th feature map of the $l$ th convolutional layer, and $f(\cdot)$ is the sigmoid activation function.

The dimension of new feature map after convolution operation is still relatively large. The purpose of the pooling layer is to filter out redundant information from the convolution layer. Different from the convolution layer, the operation of the pooling layer uses the mean or maximum value of local region characteristics to replace this region. The specific process is shown in Fig. 4. A $2 \times 2$ pooling kernel is used to slide on the input image, and the step size is set to 2 . When the pooling kernel slides to a certain region, the maximum pooling takes the maximum value of the region as the output, and the
![img-3.jpeg](img-3.jpeg)

Fig. 4. Schematic of pooling operation process.
average pooling takes the average value of the region as the output.

As the last layer of CNN, the output layer mainly maps the feature vector to the label space. The input vector of this layer is a feature vector $x$ obtained by performing multiple continuous convolution and pooling operations on the original input image. The output of this layer $y=\left(y_{1}, y_{2}, y_{3}, \ldots, y_{n}\right)$ can be computed as

$$
y_{j}=f\left(w_{j}^{l} x^{l-1}+b_{j}^{l}\right)
$$

where $n$ is the number of categories, $w_{j}^{l}$ is the weight of the $j$ th neuron in the $l$ th fully connected layer, and $b_{j}^{l}$ is the bias of the $j$ th neuron in the $l$ th fully connected layer. For regression problems, the output value $y_{j}$ is the final result, and for classification problems, the output value $y_{j}$ needs to be brought into the Softmax function to calculate the probability of each category.

## C. Self-Healing Optimization Based on EDA

The accuracy of load localization depends not only on the CNN model but also on reliable sensing information. Generally, the physical parameters of FBG monitoring are linear with Bragg wavelength. This means that the detection accuracy of Bragg wavelength determines the reliability of sensing information. The traditional maximum method realizes the tracking of Bragg wavelength by identifying the position of the reflection spectrum peak power. When the reflection spectrum is distorted, the spectral pattern is correspondingly deformed. The wavelength corresponding to the spectral peak power is not the Bragg wavelength. To make sure the localization accuracy of the CNN model not be affected by distorted spectra, the wavelength data should reflect the actual variation of the monitored strain object correctly. Thus, we construct a theoretical spectrum by the error between the mathematical model of distorted spectrum and actual spectrum. The Bragg wavelength can be searched by minimizing the error as the objective function. There are three types of distorted spectrum: light intensity attenuation, main peak broadening, and waveform asymmetry, as shown in Fig. 5. The asymmetric generalized Gaussian distribution function is chosen to characterize the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Spectral shapes of normal and distorted spectra.
distorted spectrum, as shown in the following formula:
$g\left(\lambda, \lambda_{B}\right)=\varepsilon I_{r}\left\{\begin{array}{l}\exp \left[-2^{\tau} \ln 2\left(\frac{\lambda-\lambda_{B}}{\alpha \Delta \lambda_{B}}\right)^{\tau}\right], \quad \lambda \geq \lambda_{B} \\ \exp \left[-2^{\tau} \ln 2\left(\frac{\lambda-\lambda_{B}}{\Delta \lambda_{B}}\right)^{\tau}\right], \quad \lambda<\lambda_{B}\end{array}\right.$
where $\varepsilon, \tau$, and $\alpha$ are the attenuation factor, broadening parameter, and asymmetric parameter, respectively. The attenuation factor reflects the attenuation degree of reflected spectral light intensity, which is a constant not greater than 1. The broadening parameter corresponds to the main peak broadening of the reflection spectrum, which is an even number greater than 0 . The asymmetry parameter indicates the degree of difference between left and right spectral patterns of the reflection spectrum, which is a constant greater than 1 . When $\varepsilon=1 ; \tau=2 ; \alpha=1$, (4) is the mathematical model representing the normal reflection spectrum.

Based on the mathematical model of the distorted spectrum, the theoretical reflection spectra function of the FBG sensor network can be constructed as follows:

$$
r(\lambda, s, \varepsilon, \tau, \alpha)=\sum_{i=1}^{n} R_{i} g_{i}\left(\lambda, s_{i}\right)
$$

where $s_{i}$ is the Bragg wavelength to be detected of the $i$ th FBG in the FBG sensor network. According to the actual spectra collected by OSA, it can be expressed as

$$
r_{0}(\lambda)=\sum_{i=1}^{n} R_{i} g_{i}\left(\lambda, \lambda_{B i}\right)+N_{\text {noise }}(\lambda)
$$

The objective function is constructed from the perspective of minimizing the difference between the theoretical spectra and the actual spectra, which can be expressed as

$$
\begin{aligned}
\operatorname{Min} D(s) & =\int_{0}^{\infty}\left|r_{0}(\lambda)-r(\lambda, s, \varepsilon, \tau, \alpha)\right| \mathrm{d} \lambda \\
s_{i} & \in\left[\lambda_{i \min }, \lambda_{i \max }\right], \quad i=1,2,3, \ldots, n \\
\varepsilon_{i} & \in(0,1], \quad i=1,2,3, \ldots, n \\
\tau_{i} & \in[2,4,6, \ldots), \quad i=1,2,3, \ldots, n \\
\alpha_{i} & \in[1, \infty], \quad i=1,2,3, \ldots, n
\end{aligned}
$$

where $\left[\lambda_{i \min }, \lambda_{i \max }\right]$ is the operational region of the $i$ th FBG. In this article, EDA is selected to solve the optimization problem.

EDA is a simple yet powerful evolutionary algorithm whose core is in the updating and sampling of probabilistic model. A probabilistic model that can describe the set of excellent individuals is constructed through statistical learning and other means. The set of excellent individuals is obtained by evaluating the current population. The new population consists of the new individuals sampled from the probabilistic model and the excellent individuals from the parent population. According to the complexity of the probabilistic model and the different sampling strategies, EDA has many different implementation methods [24]. Given the high dimension feature of solution space of reflection spectra, we use the learning method of the Gaussian mixture model to create the probabilistic model of an excellent individual set. The excellent individual set of the population screened based on Elitism is subdivided into multiple clusters by the clustering algorithm. Each cluster is represented by Gaussian model with different model parameters. Finally, we obtain a probabilistic model generated by a weighted combination of the Gaussian probability density function of all clusters. In this way, the high-dimensional population is divided into several low-dimensional parts, which shortens the optimization time of the algorithm. The flowchart of FBG distorted spectrum Bragg wavelength restoration based on EDA is shown in Fig. 6. It mainly includes four links: population initialization, selection of dominant individuals, learning of probabilistic model, and generation of a new population.

Step 1: Select the Bragg wavelength randomly within a certain range to construct the initial population based on the existing detection results, and generate the theoretical spectrum of each individual according to (4), where the population size is $N_{P}$ and the maximum number of iterations is set to $T$.

Step 2: Calculate the fitness function value of each individual according to (7), and select $M\left(M \leq N_{P}\right)$ dominant individuals by sorting the fitness values.

Step 3: Generate the probabilistic model using the learning method of the Gaussian mixture model based on the dominant individual set, where the Gaussian mixture model is shown in the following equation:

$$
P(X)=\sum_{b=1}^{t} \frac{p_{b}}{\sqrt{2 \pi} \sigma_{b}} \exp \left[-\left(x-\mu_{b}\right) / \sigma_{b}^{2}\right]
$$

where $x$ is the dominant individual value, $p_{b}$ represents the probability of the $b$ cluster in all clusters ( $l$ clusters), $\mu_{b}$ and $\sigma_{b}$ represent the mean and standard deviation of the Gaussian model of the $b$ cluster, respectively.

Step 4: Generate $N\left(N=N_{P}-M\right)$ new individuals by sampling the probabilistic model, and the new generation population is composed of the new individuals and the selected dominant individuals.

Step 5: Compare the number of iterations $t$ with $T$, if $t$ is less than $T$, repeat Steps 2 to $4, t=t+1$. Otherwise, finish the iteration. The final output solution of EDA represents the optimal detection result of the distorted spectrum.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Flowchart of EDAs.

## IV. RESULTS

## A. Experimental Setup and Dataset

To validate the proposed method's effectiveness, we conducted experiments on a $210 \times 210 \times 20 \mathrm{~mm}$ aluminum plate. The FBG sensor network, consisting of nine uniformly distributed FBG sensors, detected the position of an externally applied load simulated by a steel ball, as shown in Fig. 7. In the FBG sensor system, the broadband source with FWHM of 50 nm and a power of 100 mW . The FWHM of the used FBG sensor is 0.2 nm . According to Fig. 1, spectral data corresponding to the load-induced changes in the FBGs were acquired using an OSA (AQ6370D, 10 pm resolution) and sent to a PC (Intel Core i7-6850K CPU, NVIDIA GeForce GTX 1080 Ti GPU, and 16 GB RAM) for EDA demodulation of the Bragg wavelength and then CNN load localization. Our EDA and CNN were developed in MATLAB and Python, respectively.

This setup was operated in a constant temperature environment to mitigate temperature-induced spectral distortions. To simulate FBG failure, we made several distorted FBGs in advance for the subsequent experiments. Here, we use a rapid temperature change test chamber to subject the FBGs to high-low temperature cycles ranging from $-10{ }^{\circ} \mathrm{C}$ to $110{ }^{\circ} \mathrm{C}$. The primary consideration for this specific temperature profile was to induce a significant thermal cycling effect, which is known to accelerate the aging process of FBG sensors. A temperature differential of approximately $120^{\circ}$ provides a substantial variance to assess the effects of highand low-temperature fluctuations on the aging characteristics of the FBGs. Note that different studies employed various temperature ranges for FBG aging experiments, such as
$20^{\circ} \mathrm{C}-50^{\circ} \mathrm{C}$ [25] and $15^{\circ} \mathrm{C}-90^{\circ} \mathrm{C}$ [26]. These variations in temperature profiles across different studies indicate that the temperature range selected for aging experiments can vary based on specific research goals and the desired speed of aging acceleration. FBGs with different degradation degrees are extracted every 25 cycles.

In the $200 \times 200 \mathrm{~mm}$ monitored region, the position of applied load is distributed every 10 mm in the length and the width direction, with a total of 400 load points. Therefore, our dataset comprised 400 samples, each including nine EDA-demodulated Bragg wavelength values and the corresponding load position $(x, y)$, making the dimension of each sample $1 \times 11$. Of these, 319 samples were used for training and 81 for testing, with the Bragg wavelength feature range being $1550-1552 \mathrm{~nm}$.

Note that our study is half-physical and half-simulation, rather than being fully physical. Specifically, the aging experiment was a physical process, while the load localization experiment was simulation-based. For an aging experiment, we utilized a variable temperature chamber to accelerate the aging of FBG sensors and construct typical distorted FBG spectra. This allowed us to determine the distortion parameters (attenuation factor, broadening parameter, and asymmetric parameter) in formula (4) and their respective ranges. This experimental methodology is analogous to the study in [27]. These distortion-sensing data were then used for the subsequent load localization experiments.

For the load localization experiment, similar to experimental methodology in the study [28], we used the finite element analysis software Abaqus to simulate the force distribution on an aluminum plate under various load conditions and recorded the sensing data, load sizes, load point positions, and the layout of multiple strain FBG sensors arranged on the plate's surface. This initial dataset represented the sensing data collected by the FBG sensor network under normal operating conditions.

To simulate network node failure conditions, we replaced the sensing data from undistorted FBGs with the distorted and aged FBG sensing data, ensuring that the degree of spectral distortion corresponded to the strain size. This allowed us to construct new datasets representing different numbers and positions of failed FBG nodes within the network.

The remainder of this section is organized as follows. In Section IV-B, the localization model was trained and tested using wavelength data from properly functioning FBGs. Section IV-C explored the model's resilience by swapping a single failed FBG with each of the other eight in the network, assessing the impact of the sensor's position. In Section IV-D, we further tested our model's robustness against FBGs with varying degrees of spectral distortion, simulating aging effects through high-low temperature cycling. In Section IV-E, we assessed the localization system's robustness by incrementally increasing the number of failed FBG sensors from one to five. Section IV-F compared the proposed EDA method against traditional detection methods like the maximum, centroid, and polynomial fitting methods, demonstrating EDA's effectiveness in handling distorted spectra. Section IV-G benchmarked the CNN's performance with other sophisticated machine learning and deep learning techniques, including BP neural networks,

![img-6.jpeg](img-6.jpeg)

Fig. 7. Distribution of FBG sensors and external load points.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Waveform samples detected by the nine FBGs.

SVR, ELM, and advanced architectures like [29] and [30], ResNet-18 [31], [32], VGG-16 [33], [34], and EfficientNetV2 [35], affirming the proposed method's superior localization performance.

## B. Localization Model Training and Performance Testing

We first train and test our CNN localization model with data collected by properly functioning FBGs. The structural parameters of CNN are set as shown in Table I. In Section IV, we conducted experiments on a $210 \times 210 \times 20 \mathrm{~mm}$ aluminum plate with nine evenly spaced FBG sensors. Loads were applied at 10 mm intervals along both length and width. Fig. 8 shows one data sample in experiments (including the spectrums of the nine FBGs). The CNN inputs are EDA-demodulated Bragg wavelengths from these FBGs, forming a feature set with dimensions of $1 \times 9$. Our CNN's first convolution layer has an input size of $3 \times 3 \times 1$, matching the experimental setup's topology. The evaluation index for CNN training uses the average root mean square error (RMSE) between the predicted and true values of all load positions in the training set, which can be expressed as

$$
\operatorname{RMSE}_{L}=\frac{1}{p} \sum_{i=1}^{p} \sqrt{\left(\left(x_{i}-\hat{x}_{i}\right)^{2}+\left(y_{i}-\hat{y}_{i}\right)^{2}\right) / 2}
$$

TABLE I
Structural Parameters of CNN Network

| Layers | Input size | Channel | Kernels | Output size |
| :--: | :--: | :--: | :--: | :--: |
| Conv1 | $3 \times 3 \times 1$ | 32 | $2 \times 2$ | $3 \times 3 \times 32$ |
| Conv2 | $3 \times 3 \times 32$ | 64 | $2 \times 2$ | $3 \times 3 \times 64$ |
| Conv3 | $3 \times 3 \times 64$ | 128 | $2 \times 2$ | $3 \times 3 \times 128$ |
| Max-pooling | $3 \times 3 \times 128$ | 128 | $2 \times 2$ | $2 \times 2 \times 128$ |
| Fully-connected | $2 \times 2 \times 128$ | 512 | - | 512 |
| Output | 512 | 1 | - | 2 |

![img-8.jpeg](img-8.jpeg)

Fig. 9. Training process of load localization model: RMSE versus CNN learning epoch.
where $\left(x_{i}, y_{i}\right)$ is the true position of the $i$ th load, $\left(\hat{x}_{i}, \hat{y}_{i}\right)$ is the localization results of CNN for the $i$ th load, $p$ is the number of samples in the training set.

The training process of CNN model is shown in Fig. 9. In the early stage of training process, the model evaluation index $\mathrm{RMSE}_{L}$ fluctuates significantly, but as the number of iterations increases, the $\mathrm{RMSE}_{L}$ overall shows a downward trend. After 200 generations, the variation of $\mathrm{RMSE}_{L}$ reduces obviously. And it tends to be stable after 600 generations. The optimal CNN model is obtained in the 887th generation. At this time, the training $\mathrm{RMSE}_{L}$ is 0.0296 mm , and the test $\mathrm{RMSE}_{L}$ is 1.4764 mm .

The trained CNN model can be used to predict the unknown load position without repeated training. The localization errors of $75.31 \%$ of the test results are less than 2 mm , and the $\mathrm{RMSE}_{L}$ is 1.4495 mm . The position of most test samples can be accurately predicted, indicating that the CNN model can realize the recognition of load position.

To check the localization performance of the proposed method when the FBG fails, we replaced the FBG1 with a failed FBG. And the spectra are collected again to get the test samples, where the position and magnitude of the applied load remain unchanged. For the distorted spectrum generated by the failed FBG, the corresponding Bragg wavelength is detected by EDA. We set the EDA parameter as follows: population size $N$ is 50 , selection number is 5 , and the maximum number of iterations is 40 . RMSE evaluates the detection accuracy of Bragg wavelength between the predicted and the actual values, which can be expressed as

$$
\operatorname{RMSE}_{E}=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(\lambda_{i}-\lambda_{i}^{\prime}\right)^{2}}
$$

![img-9.jpeg](img-9.jpeg)

Fig. 10. Localization results of external load under FBG1 reflection spectral distortion.
![img-10.jpeg](img-10.jpeg)

Fig. 11. $\mathrm{RMSE}_{L}$ and $\mathrm{RMSE}_{E}$ of failed FBG sensor at different positions.
where $\lambda_{i}$ is the predicted value of Bragg wavelength for the $i$ th $\mathrm{FBG}, \lambda_{i}^{\prime}$ is the actual value of the Bragg wavelength for the $i$ th FBG, and $n$ is the amount of FBG in the sensor network. The wavelength data are sent into the CNN model, and the load prediction results are shown in Fig. 10. The localization errors of $75.31 \%$ of the test results are less than 2 mm , and the $\mathrm{RMSE}_{L}$ is 1.4503 mm . The results show that the localization result of CNN with failed FBG1 is close to that with normal FBG1. Hence, the proposed method can still have good localization accuracy when a single FBG has a distorted spectrum.

## C. Localization Performance of Failed FBG at Different Positions

To analyze the influence on localization performance of failed FBG at different positions, we exchanged the failed FBG with the remaining eight FBGs in turn and compared the prediction results of CNN under the failed FBG1 to FBG9 respectively. The relations between the RMSE $_{L}$ and the position of the failed FBG are shown in Fig. 11.

When the FBG at different positions fail, the corresponding $\mathrm{RMSE}_{L}$ is not significantly different. The $\mathrm{RMSE}_{L}$ with FBG3 fails is the smallest, which is 1.4459 mm . The $\mathrm{RMSE}_{L}$ with
![img-11.jpeg](img-11.jpeg)

Fig. 12. Reflection spectra with different distorted degrees. (a) Light intensity attenuation. (b) Waveform asymmetry. (c) Slight spectral distortion. (d) Main peak broadening distortion.

FBG5 fails is the largest, which is 1.4631 mm , and the error fluctuation range is within 0.03 mm . The experimental results show that the proposed method has the same high-precision identification of the load position when the FBGs fail at different positions in the FBG sensor network. The Bragg wavelength detection accuracy $\mathrm{RMSE}_{E}$ of FBG at different positions under the same strain is shown in Fig. 11, which are all below 1 pm . It shows that even if the position of failed FBG is different, the difference in the wavelength data that are finally sent to the localization model is small. This indicates that the position of the failed FBG has little influence on the localization performance of CNN model.

## D. Localization Performance of Different Distorted Degrees

To analyze the influence of the distorted degrees of FBG reflection spectrum on the model localization performance, the high-low temperature change test chamber is used to accelerate the aging of FBG. FBGs with different degradation degrees are produced by simulating the aging process of FBG. When the degradation degree of the failed FBG is different, the distorted characteristics of the collected reflection spectrum are also different. FBG1 is replaced by these failed FBGs to compare the localization accuracy of the CNN model with different FBG distorted spectra. The reflection spectra of FBG1 under four different cases are shown in Fig. 12. The distorted reflection spectrum of each case has three typical distorted characteristics, light intensity attenuation, main peak broadening, and waveform asymmetry. However, the distorted spectral pattern has obvious differences. In Fig. 12(a), the light intensity attenuation of the reflection spectrum is most serious. In Fig. 12(b), the waveform asymmetry of the reflection spectrum is most obvious, and the main peak broadening of the reflection spectrum in Fig. 12(d) is significantly larger. Fig. 12(c) is the case that the distorted degree of the reflection spectrum is lightest.

According to the detection method based on EDA, the wavelength data in the above four cases are obtained and sent to the CNN model. The RMSE $_{L}$ for the four cases are 1.4567, $1.4502,1.4496$, and 1.4608 mm respectively. The results show

TABLE II
RMSE $_{L}$ Under Different Number of Failed FBGs

| Failed FBG number | 1 | 2 | 3 | 4 | 5 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| RMSE $_{L}(\mathrm{~mm})$ | 1.4631 | 1.4863 | 1.5383 | 1.6100 | 1.6888 |

that the proposed method has the same high localization accuracy for FBG reflection spectra with different distorted degrees. Given that the distortion of the reflection spectrum mainly affects the detection accuracy of Bragg wavelength, the experimental results actually indicate that EDA can effectively ensure the reliability of sensing information when the FBG reflection spectrum has different degrees of distortion.

## E. Localization Performance of Different Numbers of Failed $F B G$

To further investigate the localization performance of the proposed method in FBG sensor networks with multiple failed FBGs, we compare the load localization result of the CNN model with the number of failed FBGs increasing from 1 to 5 . Table II lists the RMSE $_{L}$ of different number of failed FBGs.

When the number of failed FBGs increases from 1 to 2, the RMSE $_{L}$ increases from 1.4665 to 1.4863 mm , and the increase rate of RMSE $_{L}$ is $1.58 \%$. When three FBGs failed, the RMSE $_{L}$ rises to 1.5383 mm , and the increase rate is $3.49 \%$. When four FBGs are failed, the RMSE $_{L}$ rises to 1.6100 mm and the increase rate is $4.66 \%$. When there are five failed FBGs, the RMSE $_{L}$ is 1.6888 mm , which is significantly greater than that with four failed FBGs, and the increase rate is $4.89 \%$. It is obvious that the RMSE $_{L}$ increases with the number of the failed FBG increasing. As the performance of the CNN model is not affected by the position of the failed FBG, when multiple FBGs appear distorted spectrum, the localization error will not increase if the detection accuracy of Bragg wavelength does not decrease. The experimental results show that the wavelength detection error of EDA in dealing with multiple distorted spectra will increase. That is why the localization accuracy of the CNN model decreases. The proposed method can tolerate a single failed FBG without affecting the localization performance. If more failed FBGs need to be tolerated, it will be at the expense of decreasing the localization accuracy of the model. When the number of failed FBGs increases, the localization performance of the model becomes worse.

## F. Localization Performance of Different Detection Methods

To verify the validity of EDA, the maximum method, centroid method, and polynomial fitting method of traditional detection methods are chosen for comparison. The experiment is conducted under the same condition with the reflection spectrum of FBG1 being distorted. Given the great difference in detection errors of different methods, the RMSE $_{E}$ of the detection results obtained by the four methods are logarithmically processed, denoted as $\lg \mathrm{RMSE}_{E}$, and analyzed by quartile diagram, as shown in Fig. 13.

The maximum value of the EDA is close to 0.2 , and the minimum value is close to -2.2 . The lower and upper digits
![img-12.jpeg](img-12.jpeg)

Fig. 13. Comparisons of Bragg wavelength detection errors for different methods.

TABLE III
LOCALIZATION PERFORMANCE COMPARISON OF DIFFERENT DETECTION METHODS

| Detection method | Maximum | Centroid | Polynomial | Proposed |
| :--: | :--: | :--: | :--: | :--: |
| RMSE $_{L}(\mathrm{~mm})$ | 6.2463 | 10.5268 | 7.9503 | 1.4503 |

are between -1.2 and 0.7 , significantly better than the result of other methods. The maximum values of the three traditional detection methods are all greater than 2 , and the minimum values are all higher than 0.2 . The lower and upper digits of the maximum method are between 0.8 and 1.7 , the lower and upper digits of the centroid method are between 1.6 and 2.2 , and the lower and upper digits of the polynomial method are between 1.4 and 2.1. The wavelength detection accuracy of EDA is relatively high when the reflection spectrum of FBG is distorted.

Table III shows the RMSE $_{L}$ of four different methods. When the FBG1 fails, the RMSE $_{L}$ are $6.2463,10.5268,7.9503$, and 1.4503 mm for the maximum method, the centroid method, the polynomial method, and the proposed method, respectively. Compared to the results obtained by the traditional detection methods, the proposed method has the best localization performance. This indicates that the detection approach based on EDA can acquire reliable sensing information, allowing the CNN model to identify the load position with high precision continuously.

## G. Localization Performance of Different Training Algorithms

To evaluate the performance of CNN, the proposed method is compared to backpropagation (BP) neural network, support vector regression (SVR), extreme learning machine (ELM), DenseNet [29], [30], ResNet-18 [31], [32], VGG-16 [33], [34], and EfficientNetV2 [35] under the same conditions. In the experiment, the reflection spectrum of FBG1 is distorted, and other FBGs are normal. The same training samples and test samples used by the eight different supervised learning algorithms are selected. Architectures and hyperparameters

TABLE IV
Architectures and Hyperparameters of Different Training Methods

| Training method | Architecture Details | Hyperparameters |
| :--: | :--: | :--: |
| CNN | 3 Convolutional layers (32, 64, 128 filters), 1 FC layers | Learning rate: 0.001, Epochs: 1000 |
| BP Neural Network | 3 Hidden layers (50, 100, 50 neurons), Sigmoid activation | $\mathrm{l} r: 0.01$, Momentum: 0.9 |
| SVR | Radial Basis Function (RBF) kernel | Cost (C): 1.0, Epsilon: 0.1 |
| ELM | Single hidden layer (1000 neurons), Sigmoid activation | Regularization parameter: 0.001 |
| DenseNet | 121 layers, Growth rate: 32 | Dropout rate: 0.2 , Batch size: 16 |
| ResNet-18 | 18 layers (2x Convolutional blocks per layer) | $\mathrm{l} r: 0.001$, Batch Normalization |
| VGG-16 | 16 layers (13 Convolutional layers, 3 FC layers) | $\mathrm{l} r: 0.001$, Weight decay: 0.0005 |
| EfficientNetV2 | B0 variant, Scaling coefficient: 1.1 | $\mathrm{l} r: 0.002$, Dropout rate: 0.3 |

![img-13.jpeg](img-13.jpeg)

Fig. 14. Comparisons of cumulative percentile of localization errors for different training algorithms.
are detailed in Table IV. The cumulative percentile curve of the positioning errors of these algorithms is shown in Fig. 14. In the test, $75.31 \%$ of the localization results based on CNN are below 2 mm . The cumulative percentile of localization errors of below 2 mm are $4.94 \%, 6.17 \%$, and $6.17 \%$ for BP neural network, SVR, and ELM, respectively. Compared to other algorithms, CNN has higher cumulative probability under the same accuracy requirements, indicating that CNN is superior to BP, SVR, and ELM in statistical characteristics.

For the condition of reflection spectral distortion of FBG1, the RMSE $_{L}$ of BP neural network, SVR, ELM, DenseNet, ResNet-18, VGG-16, and EfficientNetV2 are 12.625, 9.5198, $8.2725,15.749,17.298,8.000$, and 9.325 mm , respectively. The RMSE $_{L}$ of CNN is 1.4503 mm and significantly better than other algorithms. Larger-scale network models cannot achieve better results due to the low dimension of the spectral demodulated data. On the contrary, on the limited number of training samples, the performances of those complex models are not as good as those of CNN. Using CNN with stronger feature learning ability for wavelength data to train the model can obtain higher localization accuracy and further improve the reliability of FBG sensor networks.

## V. DISCUSSION

In this article, we address a crucial aspect of FBG sensing networks: the challenge of spectral data distortion.

In real-world applications, devices often experience gradual wear-out or degradation rather than a binary workingfailed state. Our focus is on these intermediate failure conditions, particularly in the context of long-term measurements in FBG networks.

The core of our approach lies in effectively handling spectral distortions that arise over time. These distortions, while not rendering the FBGs completely inoperative, can significantly impair measurement accuracy. By analyzing collected spectral data and utilizing the combined strengths of our MATLAB and Python programs, we can integrate this analysis directly into the hardware system. This method allows for a more nuanced understanding of the FBG sensors' condition, acknowledging that they often do not fail outright but degrade progressively.

One of the key advantages of our approach is its practical applicability. We do not process raw spectra; instead, we focus on analyzing already collected data. This is done using an OSA that sends spectral data to a computer for calculation. This method makes it feasible to detect and correct spectral distortions, thereby enhancing the accuracy of long-term measurements in FBG networks.

However, it is important to acknowledge the limitations of our method. As the number of distortions in the FBG network increases, our method's effectiveness diminishes. It is primarily suited for networks with a small number of distorted FBG nodes. In such scenarios, it can play a significant role in extending the measurement system's life and maintaining accuracy. But, when distortions become too concentrated, or if there is a significant increase in the number of distorted nodes, the system's measurement error increases correspondingly.

## VI. CONCLUSION

In this article, we present a localization technique with self-healing ability based on EDA and CNN for FBG sensor networks with distorted spectra. To ensure the reliability of the sensing information, EDA is utilized to determine the Bragg wavelength of the distorted spectrum caused by FBG failed from the perspective of function optimization. The CNN model is trained by learning from the wavelength data of FBGs in the sensor network and applied to quickly identify the position of external load based on the detection results of EDA. The experimental results show that the average localization error of the proposed method is less than 2 mm when the reflection spectra of five FBGs are distorted in nine-FBGs sensor network. The sensing information can be accurately

obtained with the Bragg wavelength detection error of below 1 pm in spectral distortion. In addition, compared to BP neural network, SVR, and ELM, CNN obviously has a better localization performance. The proposed method can effectively improve the reliability and survivability of the FBG sensing network by enhancing the tolerance for distorted spectra and the recognition ability of structural damage.

## REFERENCES

[1] M. A. Riza, Y. I. Go, S. W. Harun, and R. R. J. Maier, "FBG sensors for environmental and biochemical applications-A review," IEEE Sensors J., vol. 20, no. 14, pp. 7614-7627, Jul. 2020.
[2] Y. Li, F. Chen, T. Guo, R. Wang, and X. Qiao, "Sensitivity enhancement of fiber Bragg grating accelerometer based on short grating," IEEE Trans. Instrum. Meas., vol. 71, pp. 1-5, 2022.
[3] M. D. L. D. Vedova, P. C. Berri, P. Maggiore, and G. Quattrocchi, "Design and development of innovative FBG-based fiber optic sensors for aerospace applications," J. Phys., Conf. Ser., vol. 1589, no. 1, Jul. 2020, Art. no. 012012.
[4] F. De Tommasi, D. L. Presti, M. A. Caponero, M. Carassiti, E. Schena, and C. Massaroni, "Smart mattress based on multipoint fiber Bragg gratings for respiratory rate monitoring," IEEE Trans. Instrum. Meas., vol. 72, pp. 1-10, 2023.
[5] H. Wang et al., "Design of a modular 3-D force sensor with fiber Bragg gratings for continuum surgical robot," IEEE Trans. Instrum. Meas., vol. 72, pp. 1-11, 2023.
[6] M. Majumder, T. K. Gangopadhyay, A. K. Chakraborty, K. Dasgupta, and D. K. Bhattacharya, "Fibre Bragg gratings in structural health monitoring-Present status and applications," Sens. Actuators A, Phys., vol. 147, no. 1, pp. 150-164, Sep. 2008.
[7] G. C. Kahandawa, J. Epaarachchi, H. Wang, and K. T. Lau, "Use of FBG sensors for SHM in aerospace structures," Photonic Sensors, vol. 2, no. 3, pp. 203-214, Sep. 2012.
[8] Z. Zhou, Z. Wang, and L. Shao, "Fiber-reinforced polymer-packaged optical fiber Bragg grating strain sensors for infrastructures under harsh environment," J. Sensors, vol. 2016, pp. 1-18, Oct. 2016.
[9] J. Ang, H. C. H. Li, I. Herzberg, M. K. Bannister, and A. P. Mouritz, "Tensile fatigue properties of fibre Bragg grating optical fibre sensors," Int. J. Fatigue, vol. 32, no. 4, pp. 762-768, Apr. 2010.
[10] S. T. Hayle et al., "Reliable self-healing FBG sensor network for improvement of multipoint strain sensing," Opt. Commun., vol. 499, Nov. 2021, Art. no. 127286.
[11] S. T. Hayle et al., "Self-healing integration of fiber/FSO communication and sensor network for improving survivability," Opt. Fiber Technol., vol. 74, Dec. 2022, Art. no. 103090.
[12] C.-H. Chang and C.-H. Tsai, "A large-scale optical fiber sensor network with reconfigurable routing path functionality," IEEE Photon. J., vol. 11, no. 3, pp. 1-11, Jun. 2019.
[13] L. Yuan, Q. Wang, and Y. Zhao, "A passive ladder-shaped sensor architecture with failure detection based on fiber Bragg grating," Opt. Fiber Technol., vol. 81, Dec. 2023, Art. no. 103540.
[14] Y. C. Manie et al., "Enhancement of the multiplexing capacity and measurement accuracy of FBG sensor system using IWDM technique and deep learning algorithm," J. Lightw. Technol., vol. 38, no. 6, pp. 1589-1603, Mar. 15, 2020.
[15] X. Hu, H. Si, J. Mao, and Y. Wang, "Self-healing and shortest path in optical fiber sensor network," J. Sensors, vol. 2022, pp. 1-9, Aug. 2022.
[16] K. Dey, V. Nikhil, P. R. Chaudhuri, and S. Roy, "Demonstration of a fast-training feed-forward machine learning algorithm for studying key optical properties of FBG and predicting precisely the output spectrum," Opt. Quantum Electron., vol. 55, no. 1, p. 16, Nov. 2022.
[17] J. Hu, K. Di, D. Ren, Y. Deng, and J. Zhao, "Recognition and localization of asymmetric spectra in FBG sensing networks," Opt. Esp., vol. 31, no. 6, p. 10645, Mar. 2023.
[18] M. Liu, W. Wang, H. Song, S. Zhou, and W. Zhou, "A high sensitivity FBG strain sensor based on flexible Hinge," Sensors, vol. 19, no. 8, p. 1931, Apr. 2019.
[19] J. Kim, A.-D. Nguyen, and S. Lee, "Deep CNN-based blind image quality predictor," IEEE Trans. Neural Netw. Learn. Syst., vol. 30, no. 1, pp. 11-24, Jan. 2019.
[20] L. Lu, Y. Yi, F. Huang, K. Wang, and Q. Wang, "Integrating local CNN and global CNN for script identification in natural scene images," IEEE Access, vol. 7, pp. 52669-52679, 2019.
[21] S. Gao and C. W. de Silva, "Estimation distribution algorithms on constrained optimization problems," Appl. Math. Comput., vol. 339, pp. 323-345, Dec. 2018.
[22] H. Jiang, Q. Zhou, J. Chen, and X. Miao, "Wavelength detection optimization of fiber Bragg grating sensing networks based on distortion spectrum," Acta Optica Sinica, vol. 39, no. 10, 2019, Art. no. 1006002.
[23] H. Jiang et al., "Wavelength detection of model-sharing fiber Bragg grating sensor networks using long short-term memory neural network," Opt. Exp., vol. 27, no. 15, pp. 20583-20596, Jul. 2019.
[24] Q. Yang, W.-N. Chen, Y. Li, C. L. Chen, X.-M. Xu, and J. Zhang, "Multimodal estimation of distribution algorithms," IEEE Trans. Cybern., vol. 47, no. 3, pp. 636-650, Mar. 2017.
[25] G. Yao, Y. Yin, Y. Li, and H. Yi, "High-precision and wide-wavelength range FBG demodulation method based on spectrum correction and data fusion," Opt. Esp., vol. 29, no. 16, p. 24846, 2021.
[26] V. Anfnogentov et al., "Algorithm of FBG spectrum distortion correction for optical spectra analyzers with CCD elements," Sensors, vol. 21, no. 8, p. 2817, Apr. 2021.
[27] Q. Shang, S. Fan, W. Qin, and G. Yao, "Pink noise removal and spectral distortion correction based fiber Bragg grating demodulation algorithm," Opt. Esp., vol. 30, no. 2, p. 1066, 2022.
[28] J. Jiang et al., "Distortion-tolerated high-speed FBG demodulation method using temporal response of high-gain photodetector," Opt. Fiber Technol., vol. 45, pp. 399-404, Nov. 2018.
[29] J. Hemalatha, S. Roseline, S. Geetha, S. Kadry, and R. Damaševičius, "An efficient DenseNet-based deep learning model for malware detection," Entropy, vol. 23, no. 3, p. 344, Mar. 2021. [Online]. Available: https://www.mdpi.com/1099-4300/23/3/344
[30] N. Hasan, Y. Bao, A. Shawon, and Y. Huang, "DenseNet convolutional neural networks application for predicting COVID-19 using CT image," Social Netw. Comput. Sci., vol. 2, no. 5, p. 389, Jul. 2021, doi: 10.1007/s42979-021-00782-7.
[31] Y. Liu, G.-R. She, and S.-X. Chen, "Magnetic resonance image diagnosis of femoral head necrosis based on ResNet18 network," Comput. Methods Programs Biomed., vol. 208, Sep. 2021, Art. no. 106254. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S016926072100328X
[32] B. Huang, J. Liu, Q. Zhang, K. Liu, K. Li, and X. Liao, "Identification and classification of aluminum scrap grades based on the Resnet18 model," Appl. Sci., vol. 12, no. 21, p. 11133, Nov. 2022. [Online]. Available: https://www.mdpi.com/2076-3417/12/21/11133
[33] W. Tan et al., "Classification of COVID-19 pneumonia from chest CT images based on reconstructed super-resolution images and VGG neural network," Health Inf. Sci. Syst., vol. 9, no. 1, p. 10, Feb. 2021, doi: 10.1007/s13755-021-00140-0.
[34] D. Hong et al., "Genetic syndromes screening by facial recognition technology: VGG-16 screening model construction and evaluation," Orphanet J. Rare Diseases, vol. 16, no. 1, p. 344, Aug. 2021, doi: 10.1186/s13023-021-01979-y.
[35] M. Tan and Q. V. Le, "EfficientNetv2: Smaller models and faster training," in Proc. 38th Int. Conf. Mach. Learn., vol. 139. Proceedings of Machine Learning Research, pp. 10096-10106.
![img-14.jpeg](img-14.jpeg)

Yuemei Luo (Member, IEEE) received the B.Eng. degree in mechatronics engineering from the University of Electronic Science and Technology of China (UESTC), Chengdu, China, in 2011, and the Ph.D. degree from the School of Electrical and Electronic Engineering, Nanyang Technological University (NTU), Singapore, in 2018.

She is currently an Associate Professor with the School of Artificial Intelligence, Nanjing University of Information Science and Technology (NUIST), Nanjing, China. Her main research focuses on high-resolution optical coherence tomography (OCT), including endoscopic probes for clinical applications in gastrointestinal and cardiovascular fields, and automatic detection of early disease via machine learning.

![img-15.jpeg](img-15.jpeg)

Chenxi Huang received the B.Eng. degree in software engineering from Northeastern University, Shenyang, China, in 2022, and the M.Tech. degree in intelligent systems from the National University of Singapore, Singapore, in 2023.
Her current research interests include data analysis, machine learning, and medical image processing.
![img-16.jpeg](img-16.jpeg)

Jing Chen received the B.S. degree in automation, the M.S. degree in system engineering, and the Ph.D. degree in control theory and control engineering from Xiamen University, Xiamen, Fujian, China, in 2010, 2013, and 2016, respectively.
She is currently an Associate Professor with the College of Electrical Engineering and Automation, Fuzhou University, Fuzhou, China. Her research interests include fault diagnosis and artificial intelligence.
![img-17.jpeg](img-17.jpeg)

Chaohui Lin received the B.S. degree in electrical engineering and automation from Fujian University of Technology, Fuzhou, China, in 2019, and the M.S. degree in control science and engineering from Fuzhou University, Fuzhou, in 2022.
His research interests include FBG sensor networks.
![img-18.jpeg](img-18.jpeg)

Xiren Miao received the B.S. degree in gyroscope and inertial navigation system from Beihang University, Beijing, China, in 1986, and the M.S. degree in electric appliance and the Ph.D. degree in electrical machinery and appliance from Fuzhou University, Fuzhou, China, in 1989 and 2000, respectively.
He is currently a Professor with the College of Electrical Engineering and Automation, Fuzhou University. His research interests include electrical and its system intelligent technology, online monitoring, and diagnosis of electrical equipment.
![img-19.jpeg](img-19.jpeg)

Yuan Li received the B.Eng. degree in medical information engineering from the University of South China, Hengyang, China, in 2022. He is currently pursuing the master's degree with the School of Computer Science, Nanjing University of Information Science and Technology (NUIST), Nanjing, China.
His research interests include automatic early disease detection based on machine learning and medical image segmentation.
![img-20.jpeg](img-20.jpeg)

Hao Jiang received the B.S. degree in automation and the Ph.D. degree in control theory and control engineering from Xiamen University, Xiamen, Fujian, China, in 2008 and 2013, respectively.
He is currently a Professor with the College of Electrical Engineering and Automation, Fuzhou University, Fuzhou, China. His research interests include artificial intelligence and machine learning.