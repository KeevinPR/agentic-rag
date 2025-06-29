# Data-driven topology design using a deep generative model 

Shintaro Yamasaki ${ }^{1}$ (1) $\cdot$ Kentaro Yaji ${ }^{1} \cdot$ Kikuo Fujita ${ }^{1}$

Received: 8 June 2020 / Revised: 8 March 2021 / Accepted: 7 April 2021
(c) The Author(s) 2021


#### Abstract

In this paper, we propose a sensitivity-free and multi-objective structural design methodology called data-driven topology design. It is schemed to obtain high-performance material distributions from initially given material distributions in a given design domain. Its basic idea is to iterate the following processes: (i) selecting material distributions from a dataset of material distributions according to eliteness, (ii) generating new material distributions using a deep generative model trained with the selected elite material distributions, and (iii) merging the generated material distributions with the dataset. Because of the nature of a deep generative model, the generated material distributions are diverse and inherit features of the training data, that is, the elite material distributions. Therefore, it is expected that some of the generated material distributions are superior to the current elite material distributions, and by merging the generated material distributions with the dataset, the performances of the newly selected elite material distributions are improved. The performances are further improved by iterating the above processes. The usefulness of data-driven topology design is demonstrated through numerical examples.


Keywords Data-driven design $\cdot$ Topology optimization $\cdot$ Deep generative model $\cdot$ Sensitivity-free methodology $\cdot$ Multi-objective methodology $\cdot$ Estimation of distribution algorithm

## 1 Introduction

Structural design is to determine the structural shape and topology of artifacts on the basis of physics, mathematics, designer intuition, and so on. Among previously proposed methodologies for structural design, topology optimization originated by Bendsøe and Kikuchi (1988) is a promising one because of its potential to yield high-performance structures while considering both shape and topology.

There are two basic concepts in topology optimization (Bendsøe and Sigmund 2003). One is replacing a structural design problem with a material distribution problem in a given design domain. The other is exploiting the optimal, or at least local optimal material distribution using sensitivitybased mathematical programming under a given objective function and constraints, that is, a given formulation.

[^0]Topology optimization has been applied to various engineering problems and has achieved immense success. However, on the other hand, it includes some intrinsic difficulties. Major one is the applicability to strongly nonlinear topology optimization problems. That is, it is hard to directly solve some types of topology optimization problems because of their nonlinearity. Representative problems are flow channel design problems under a turbulent flow (Kontoleontos et al. 2013; Dilgen et al. 2018), and compliant mechanism design problems taking the geometric nonlinearity and the maximum stress into account (De Leon et al. 2020). Although a limited number of studies address solving these problems using sensitivity-based mathematical programming, it is also valuable to research alternative approaches.

Some sensitivity-free approaches may seem to be promising as alternative approaches. For example, Chapman et al. (1994), Wang and Tai (2004), Aguilar Madeira et al. (2006), and Tai and Prasad (2007) proposed updating the structural shape and topology utilizing genetic algorithms (GAs). Similarly, Shim and Manoochehri (1997) and Wu and Tseng (2010) proposed the use of simulated annealing and differential evolution, respectively. Whereas they exploit solutions without the sensitivity exactly, their applicability is limited to relatively small-scale problems, as Sigmund (2011) pointed out. This limitation derives from the fact


[^0]:    Responsible Editor: Xu Guo
    2 Shintaro Yamasaki
    yamasaki@mech.eng.osaka-u.ac.jp

    1 Department of Mechanical Engineering, Osaka University, 2-1 Yamadaoka, Suita 565-0871, Japan

that it is difficult for sensitivity-free approaches to find optimal or satisfactory solutions within a realistic computational time, except for small-scale problems.

In other words, sensitivity-free approaches are useful if promising material distributions can be generated with a limited number of design variables. On the basis of this point of view, Wang and Tai (2004) and Tai and Prasad (2007) introduced a graph-theoretic chromosome model to represent material distributions. That is, in their approach, a parametric model representing material distributions is prepared in advance by considering the characteristics of the respective structural design problems. However, introducing such a parametric model often means that the degree of freedom for representing material distributions is significantly restricted, which spoils the advantage of topology optimization.

Deep generative models (Kingma and Welling 2013; Goodfellow et al. 2014) are promising to resolve this problem. They are a type of generative models based on deep neural networks that include a low-dimensional space constructed with a small number of variables, called latent variables. Features of training data are extracted through unsupervised learning, and similar but different data are generated by sampling in the aforementioned space called the latent space. Because of the ability of deep neural networks, deep generative models can generate various material distributions with a large degree of freedom from a small number of latent variables.

Here, we consider training a deep generative model with diverse and promising material distributions. The trained deep generative model generates material distributions that are diverse, while inheriting the features of the material distributions used as the training data. Therefore, it is expected that some of them will be superior to the training data. That is, a deep generative model has potential as an implicit parametric model for generating more promising material distributions by considering the latent variables as the design variables.

There are three important advantages of utilizing a deep generative model. First, it is possible to conduct a solution search without the sensitivity information because of a small number of the latent variables, that is, the design variables. Second, it is also possible to generate material distributions with a large degree of freedom, as described above. Third, although it is expected that the relationship between the latent variables and the generated material distributions is very complex when satisfying both the above two points, this relationship is implicitly constructed through training.

As described above, our idea of utilizing a deep generative model relies on diverse and promising material distributions. Here, we simply assume the multi-objective problem and regard material distributions whose non-dominated ranks are high (hereafter, we refer to them as high-rank material distributions) as diverse and promising material
distributions. That is, our idea discussed here is for multiobjective problems.

To obtain satisfactory solutions for multi-objective problems, we further introduce a data-driven approach. That is, we scheme to update the training data by removing lowperformance data entities and by adding high-performance data entities of the generated data. We also scheme to iterate the data generation by a deep generative model and the update of the training data by the generated data. When considering the training data as the elite data, the performances of the elite data will be gradually improved through the iteration, and the finally obtained elite data will be satisfactory solutions as a result of the performance improvement.

On the basis of the above discussions, in this paper, we propose to iteratively conduct the following processes after providing initial material distributions according to a certain policy: generating material distributions using a deep generative model trained with the current high-rank material distributions, merging the generated material distributions with the current high-rank material distributions, and newly selecting high-rank material distributions from the merged material distributions. We call this sensitivity-free and multi-objective design methodology data-driven topology design, because it aims to obtain satisfactory solutions rather than the optimal solutions and is based on a data-driven approach. We demonstrate the usefulness of data-driven topology design by solving strongly nonlinear problems with an implemented method.

The rest of this paper is organized as follows. We briefly introduce related studies in Section 2 and describe the framework in Section 3. Next, we detail its implementation in Section 4 and provide numerical examples in Section 5. Finally, we provide some concluding remarks in Section 6.

## 2 Related studies

### 2.1 Topology optimization based on deep learning

Recently, deep learning has gained significant attention from researchers in various fields, and some studies incorporating it into topology optimization have been proposed. Ulu et al. (2016) proposed to predict optimized material distributions of the minimum compliance problem using a neural network. In their study, various optimized material distributions were prepared using topology optimization while changing the load boundary condition. The network is then trained under the load boundary condition as the input and the corresponding optimized material distribution as the output. Using the trained network, the optimized material distribution for a given load boundary condition is predicted.

Zhang et al. (2019b) also proposed to predict the optimized material distributions of the minimum compliance

problem using a neural network. In their study, the displacement and strain fields of the initial material distributions are used as the inputs, the corresponding optimized material distributions are used as the outputs, and the neural network is trained using the input and output data. When an initial material distribution and its displacement and strain fields are given, the optimized material distribution is predicted using the trained network. They demonstrated that their proposed method covers a change in the location where the displacement fixed boundary condition is imposed, in addition to the load boundary condition.

Some studies have focused on computational efficiency when predicting the optimized material distributions of the minimum compliance problem. Cang et al. (2019) proposed to add training data entities on the basis of the Karush-KuhnTucker conditions for improving the prediction accuracy while suppressing the computational cost. Lei et al. (2019) proposed to utilize the framework of moving morphable components (MMC) (Guo et al. 2014). Because MMC can represent structural shape and topology with a small number of design variables, it is expected that the computational cost for learning is reduced. As a related study of Zhang et al. (2019b), Nie et al. (2020) proposed the utilization of stress and strain energy density fields of the initial material distributions as the input data. In their study, a conditional generative adversarial network (cGAN) (Mirza and Osindero 2014) is used to improve computational efficiency.

Similar to the above studies, Yu et al. (2019) proposed a prediction method for the minimum compliance problem. Optimized material distributions are predicted through two steps in their study. First, an optimized material distribution under a given boundary condition is predicted in a lowresolution mesh, such as that described in the studies of Ulu et al. (2016) and Zhang et al. (2019b). Next, the predicted material distribution is refined in a high-resolution mesh using cGAN.

Abueidda et al. (2020) applied the concept of predicting optimized material distributions to nonlinear structural mechanics, in which nonlinear material is targeted. Their proposed method predicts an optimized material distribution when the location, magnitude, and angle of the load are input.

As another notable application, Tan et al. (2020) proposed a prediction method for the design of microstructural materials. Their method predicts microscale structures corresponding to the input material properties. The design target of Zhang and Ye (2019c) is mask patterns in the photolithography process. They trained the relationship between the mask patterns and the processed patterns using a variational autoencoder (VAE) (Kingma and Welling 2013), and predicted the mask patterns corresponding to the desired patterns after the photolithography process.

The design target of Sasaki and Igarashi (2019) is rotor structures of inner permanent magnet motors (IPMs).

In their study, quasi-optimal material distributions are exploited using a GA. Although topology optimization incorporating a GA is generally time-consuming, it reduces the computational costs by utilizing a neural network that predicts the performance of IPMs.

Whereas many prediction methods for optimized material distributions focus on two-dimensional structural design problems, Banga et al. (2018) proposed a prediction method for three-dimensional problems.

Although these studies utilized deep learning for regression, some studies have focused on deep generative models. Oh et al. (2019) proposed a topology optimization method for a wheel design problem in which the diversity of the optimized material distributions is ensured by referring to the material distributions generated by a generative adversarial network (GAN) (Goodfellow et al. 2014). They also used an autoencoder (Hinton and Salakhutdinov 2006) to evaluate the novelty of the optimized material distributions.

Guo et al. (2018) proposed a structural design method for the thermal compliance minimization problem, which consists of two steps. First, a VAE is trained using various material distributions, which are obtained using topology optimization while changing the boundary conditions. Next, the latent space of the trained VAE is exploited using a GA, and as a result of the exploitation, quasi-optimal material distributions are obtained. In addition, a style transfer network (Gatys et al. 2016) was used to reduce the noise included in the material distributions generated by the VAE.

Zhang et al. (2019a) proposed a structural design method for the three-dimensional shape of a glider. In their study, a VAE is trained using airplane models registered in a threedimensional structure database (Wu et al. 2015), and the latent space of the trained VAE is exploited using a GA in a manner similar to that of Guo et al. (2018).

Data-driven topology design may seem to be similar to the above studies, particularly the studies of Oh et al. (2019), Guo et al. (2018), and Zhang et al. (2019a). However, its novelty can be clearly explained using estimation of distribution algorithm (EDA) (Larrañaga and Lozano 2001). Therefore, we introduce the EDA in the next section.

### 2.2 Estimation of distribution algorithm

Because of the generative nature for structures, data-driven topology design may seem to be an image-based GA in which only elite individuals are selected. Indeed, this can be regarded as an EDA, which is a type of GA, on the basis of the following two points: (i) probabilistic models are constructed with elite individuals, and new individuals are generated using these models, and (ii) this generative process is iteratively performed. Recently, Garciarena et al. (2018) and Bhattacharjee and Gras (2019) proposed the

adoption of a VAE as a probabilistic model of an EDA, although their targets are well-studied test problems in the field of the GA rather than structural design problems. The EDAs incorporating a VAE work well in their studies, which reinforces the validity of data-driven topology design.

Whereas the initial individuals are randomly generated in numerous studies on EDAs, data-driven topology design requires a policy for providing initial material distributions, which is explained in detail in Section 3.1. This is an important distinction between many studies conducted on EDAs and data-driven topology design. Because the latter deals with material distributions represented with a large degree of freedom (typically, several thousands or more), it is difficult to prepare suitable initial material distributions using a random number generator.

### 2.3 Novelty of data-driven topology design

As discussed in Section 2.2, data-driven topology design is novel in terms of its application to structural design and the policy for providing the initial individuals, when compared to previously proposed EDAs incorporating a deep generative model (Garciarena et al. 2018; Bhattacharjee and Gras 2019).

Furthermore, data-driven topology design can be clearly distinguished from the studies of Oh et al. (2019), Guo et al. (2018), and Zhang et al. (2019a), from the viewpoint of an EDA. That is, the former can be regarded as a type of EDA, whereas the latter cannot. This is because a deep generative model is trained only by high-rank material distributions in the former, whereas various material distributions are used for training in the latter. This is a critically important difference for our purpose, and we investigate the results caused by such a difference in Section 5.

## 3 Framework

### 3.1 Basic concept

In this section, we explain the basic concept of data-driven topology design in detail. We illustrate it in Fig. 1. As described in Section 1, data-driven topology design aims to generate higher-performance material distributions from already known high-rank material distributions in a multiobjective function space. Figure 1a shows an example of the already known high-rank material distributions, that is, the current elite data, in a structural design problem. The elite data are used to train a deep generative model, and as a result, a latent space is constructed. Figure $1 b$ shows an image of the latent space. The elite data are located according to the probability distribution, and material distribution data are newly generated by sampling the latent space. The generated data are evaluated in the multi-objective function space, and these with higherperformances are accepted as new elite data, as shown in Fig. 1c. Furthermore, old elite data dominated by the new elite data are removed from the elite data. By doing so, we update the elite data. These are further used as the training data to generate higher-performance material distributions.

As shown in Fig. 1, the generated data are different from the training data, whereas they inherit the features of the training data. It will be very difficult to construct an explicit parametric model with a small number of parameters, which can represent all of the training and generated data; however, we can construct such a parametric model implicitly by utilizing deep generative models.

On the other hand, data-driven topology design requires a policy for providing initial material distributions that are regular to a certain degree. This is because deep genera-
![img-0.jpeg](img-0.jpeg)

Fig. 1 Basic concept of data-driven topology design: a current elite data (high-rank material distributions) in multi-objective function space, $\mathbf{b}$ latent space constructed by training with elite data in $\mathbf{a}$ and generated data by sampling in this space, and $\mathbf{c}$ new elite data selected
from generated data in $\mathbf{b}$. The height direction of $\mathbf{b}$ indicates the probability distribution of data, blue and red dotted circles indicate being on the invisible side, and $z_{1}$ and $z_{2}$ are latent variables

tive models fail to capture meaningful features from randomly generated material distributions, which are usually extremely irregular.

To resolve this issue, we prepare material distributions by solving various topology optimization problems and select promising material distributions according to the optimality of the multiple objective functions. Concretely, we propose two policies in this paper.

One is utilizing the outputs of a formulation support system, which was proposed by Yamasaki et al. (2019) to support trial-and-error for determining an appropriate formulation of a topology optimization problem. The formulation support system has a database constructed by collecting material distributions, which were obtained by solving various topology optimization problems. A system user inputs multiple objective functions, and then the formulation support system outputs material distributions whose non-dominated rank is one (hereafter, we call them rank-one material distributions) by referring to the database. Because material distributions in the database are results of topology optimization, it can be expected that these are regular to a certain degree.

The other is preparing material distributions by solving a topology optimization problem, which is easy to solve directly and is correlated with the target strongly nonlinear problem. For example, if the target problem is a compliant mechanism design problem taking the geometric nonlinearity into account, we solve a compliant mechanism design problem assuming the linear strain while changing some parameters, such as the upper limits of constraints. Then, we select promising material distributions from the viewpoint of optimality of the target problem. In this policy,
it is also expected that the selected material distributions are regular to a certain degree.

These policies stand on the viewpoint actively utilizing achievements in the field of topology optimization for solving strongly nonlinear problems. In this paper, we use the former policy as the first choice, and if we fail to prepare sufficient initial material distributions by it, we use the latter policy.

### 3.2 Overall procedure

In this section, we describe the overall procedure of datadriven topology design. This is schemed to obtain highperformance material distributions to a given design problem, which is defined by the shape of the design domain, boundary conditions, and multiple objective functions. The data process flow starts from the preparation of the material distributions in the design domain, which are called the initial data. The initial data are provided according to a policy as described in Section 3.1.

After preparing the initial data, these are processed as follows according to the indication in Fig. 2.

Step 1 Evaluate the performances of the initial data by computing the values of the multiple objective functions. Here, the data including the performance values are called the evaluated data.
Step 2 Select high-rank data entities from the evaluated data. The selected data are called the elite data. Copies of the selected data are stored for merging with the generated data (see Step 6). Note that, although we select
![img-1.jpeg](img-1.jpeg)

Fig. 2 Data process flow of data-driven topology design

![img-2.jpeg](img-2.jpeg)

Fig. 3 Example of material distribution conversion using DDM: a material distribution in the design domain, and $\mathbf{b}$ converted material distribution conforming to the reference domain, where the material and void are shown in black and white, respectively
only the rank-one data entities in the implementation of this paper, it is also possible to include other high-rank data entities.
Step 3 Judge whether the elite data satisfy the convergence criterion (see details in Appendix A). If so, the current elite data are output as the final results. Otherwise, the material distributions of the elite data are converted to conform to a normalized reference domain, which is a $1 \times$ 1 square or $1 \times 1 \times 1$ cube in a two- or three-dimensional problem. Such a conversion is applied because the normalized domain is suitable for image-based learning. The design domain mapping (DDM) proposed by Yamasaki et al. (2019) is used for the conversion. Figure 3 shows an example of the material distribution conversion using the DDM.
Step 4 Train a deep generative model using the converted material distributions and newly generate material distributions using the trained deep generative model. These material distributions are called the generated data.
Step 5 Inversely convert the generated data to conform to the design domain, using the DDM.
Step 6 Evaluate the performances of the generated data, in the same manner as step 1. The generated data, including the performance values, are merged with the stored data of step 2. The merged data are regarded as the evaluated data at the next iteration. Then, we return to step 2 .

Through the above iterative procedure, we aim to obtain high-performance material distributions.

## 4 Implementation details

Although many deep generative models have recently been proposed, VAEs and GANs are representative. When compared to a GAN, a VAE is suitable for data-driven topology design because its neural network architecture is
relatively simple and a VAE is therefore robust (Atienza 2018). This robustness is particularly important because we train the neural network many times while updating the training data. We therefore adopt a VAE as a deep generative model for the implementation.

Regarding the utilization of the VAE, some important implementation details are described in the following.

### 4.1 Normalization of material distributions

In data-driven topology design, we use two domains, that is, the design and reference domains, as described in Section 3.2. In the design domain $D$, the material distributions are represented using the density function $\rho(\mathbf{x})$, where $\mathbf{x}$ are the coordinates of an arbitrary point in $D . \rho(\mathbf{x})$ is continuous and takes a value of 0 to 1 , and $\rho(\mathbf{x})=0$ and 1 correspond to the void and material, respectively. In contrast, $0<\rho(\mathbf{x})<1$ corresponds to an intermediate state, according to the conventional manner of density-based topology optimization (Bendsøe 1989). Similarly, the material distributions are represented using the density function $\rho(\boldsymbol{\xi})$ in the reference domain $\tilde{D}$, where $\boldsymbol{\xi}$ are the coordinates of an arbitrary point in $\tilde{D}$.

When using the above representation model, we must consider the preferable features of the training data for the VAE. In conventional density-based topology optimization, it is necessary to reduce the intermediate state while maintaining the smoothness of the material distribution. From this perspective, the material distributions in Fig. 3, for example, are preferable. In contrast, it is thought that the intermediate state has a positive effect when training the VAE because it provides information regarding the outline of the structure. In fact, MNIST (Deng 2012), one of the most important dataset in the field of deep learning, includes thousands of grayscale images of handwritten digits.

Therefore, we blur the outline in the reference domain $\tilde{D}$ as follows. First, we compute a scalar function $\phi(\boldsymbol{\xi})$ as
$\phi(\boldsymbol{\xi})=2 \rho(\boldsymbol{\xi})-1$.
Next, we give $\phi(\boldsymbol{\xi})$ the signed distance characteristic to the iso-contour of $\phi(\boldsymbol{\xi})=0$, using a geometry-based reinitialization scheme (Yamasaki et al. 2010). Finally, we update $\rho(\boldsymbol{\xi})$ using the following equation:
$\rho(\boldsymbol{\xi})= \begin{cases}0 & (\phi(\boldsymbol{\xi})<-h) \\ H(\phi(\boldsymbol{\xi})) & (-h \leq \phi(\boldsymbol{\xi}) \leq h) \\ 1 & (h<\phi(\boldsymbol{\xi}))\end{cases}$
where $h$ is the parameter for the bandwidth of the transition zone from the void to the material, and $H(\phi)$, which is differentiable in $[-h, h]$ and $\frac{\mathrm{d} H}{\mathrm{~d} \phi}=0$ at $\phi=-h$ and $h$, is given as follows:
$H(\phi)=\frac{1}{2}+\frac{15}{16}\left(\frac{\phi}{h}\right)-\frac{5}{8}\left(\frac{\phi}{h}\right)^{3}+\frac{3}{16}\left(\frac{\phi}{h}\right)^{5}$.

![img-3.jpeg](img-3.jpeg)
a
![img-4.jpeg](img-4.jpeg)
b

Fig. 4 Example of material distributions including wide transition zones: a material distribution normalized from that in Fig. 3b, and b material distribution in the design domain, which is inversely converted from that in a

This process is a type of normalization to the material distribution; as an example, the material distribution in Fig. 3b is processed, as shown in Fig. 4a by setting $h$ to 0.08 .

Because of the normalization, the material distributions of the training data include wide transition zones from the void to the material (see Fig. 4a). Therefore, it is expected that the material distributions generated by the VAE also include wide transition zones. If such material distributions are inversely converted into the design domain, the wide transition zones still remain, as shown in Fig. 4b. Because such wide transition zones often cause fatal numerical errors in the forward analysis, we need to binarize the material distributions in the design domain. This is conducted by applying the normalization process described earlier to the design domain by setting $h$ to a small value.

We set $h$ to 0.08 for the normalization in the reference domain on the basis of a preliminary study. As demonstrated in Section 5.1, the normalization method discussed here contributes to the generation of smooth material distributions.

### 4.2 Details of data generation using VAE

Figure 5 shows the architecture of the VAE used in the numerical examples of Section 5. As shown in the figure, this is a type of multilayer perceptron that includes two hidden layers. The reference domain $\tilde{D}$ is discretized with $50 \times 50$ square elements, and the material distributions in $\tilde{D}$ are represented using the values of the density function $\rho(\boldsymbol{\xi})$ at the lattice points. Therefore, the input layer has 2601, that is, $51 \times 51$ neurons. This input layer is fully connected to a hidden layer having 512 neurons. We referred the study of Atienza (2018) to determine the size of the hidden layer.

After activating these neurons using the ReLU function, this layer is also fully connected to two layers having 8 neurons, one corresponds to $\boldsymbol{\mu}$, which is the mean value vector of the latent variables $\mathbf{z}$, and the other corresponds
![img-5.jpeg](img-5.jpeg)

Fig. 5 Architecture of VAE
to $\log (\boldsymbol{\sigma} \circ \boldsymbol{\sigma})$, where $\boldsymbol{\sigma}$ is the variance vector of $\mathbf{z}$, and - represents the element-wise product. We then obtain the latent variables $\mathbf{z}$ as follows:
$\mathbf{z}=\boldsymbol{\mu}+\boldsymbol{\sigma} \circ \boldsymbol{\varepsilon}$,
where $\boldsymbol{\varepsilon}$ is a random vector according to the standard normal distribution. The number of the latent variables $N_{\mathrm{ll}}$ is an important parameter and we set it to 8 on the basis of a preliminary study. The influence of this parameter to the obtained results is investigated in Appendix B.

The layer of the latent variables $\mathbf{z}$ is further fully connected to a hidden layer having 512 neurons. After activating these neurons using the ReLU function, this layer is fully connected to the output layer having 2601 neurons, and outputs are obtained after sigmoid activation. The outputs are interpreted as material distributions in $\tilde{D}$ in the same manner as the inputs. Note that the architecture described in this section is for two-dimensional problems. If extending the architecture to three-dimensional problems, we may need additional dimensionality reduction techniques for larger inputs and outputs.

The VAE with the above architecture is trained using the elite data as the inputs and outputs, and the latent space composed of the latent variables is constructed through training. In more detail, the training is conducted by minimizing the following loss function $L$ using the Adam optimizer (Kingma and Ba 2014):
$L:=L_{\text {recon }}+L_{\mathrm{KL}}$,
where $L_{\text {recon }}$ is the reconstruction loss measured by the mean-squared error, and $L_{\mathrm{KL}}$ is a term corresponding to the Kullback-Leibler (KL) divergence. $L_{\mathrm{KL}}$ is computed as follows:
$L_{\mathrm{KL}}=-\frac{1}{2} \sum_{i=1}^{N_{\mathrm{ll}}}\left(1+\log \left(\sigma_{i}^{2}\right)-\mu_{i}^{2}-\sigma_{i}^{2}\right)$,

where $\mu_{i}$ and $\sigma_{i}$ are the $i$ th components of $\boldsymbol{\mu}$ and $\boldsymbol{\sigma}$, respectively. The mini batch size and the learning rate are set to 20 and $1 \times 10^{-3}$, respectively.

Because the dimensionality is drastically reduced from the input and output layers into a low-dimensional latent space, it is expected that important features of the training data are extracted into this space. Furthermore, the range of the latent space that we should focus on is restrictive because the latent variables corresponding to the training data do not take extremely large or small values according to the probability distribution $N(0,1)$.

On the basis of the above discussion, we generate material distributions by random sampling in the latent space. The sampling vectors are composed of uniformly distributed random numbers in $[-4,4]$, and the material distributions are output from the sampling vectors using the trained VAE. Thus, we generate 400 material distributions that are diverse and inherit the important features of the training data.

### 4.3 Training and validation data for VAE

In data-driven topology design, the VAE is iteratively trained while updating the training data. Therefore, it is preferable to prepare a constant number of training data at every iteration. By doing so, we can use the same parameter settings through the iterations for training the VAE.

For this reason, we provide 400 material distributions as the training data at every iteration. If the number of elite data entities is over 400, we reselect 400 data entities according to the crowding distance (Deb et al. 2002) in the objective function space, as the elite data. Otherwise, we make up for the shortage by making copies.

It should also be described that we do not prepare the validation data in the implementation discussed here. In general, the validation data are used to avoid overfitting the training data. On the other hand, VAE originally has a mechanism to avoid overfitting, as pointed out by Rocca (2019); that is, the regularization by introducing the KL divergence in (5).

In addition, the number of elite data entities is often extremely small (less than 100) in early iterations, and therefore, the number of training data entities further decreases if we prepare validation data. In such a situation, it is almost meaningless to monitor the loss function $L$ of the validation data. Figure 6 shows the histories of the loss function at iteration 0 of example 1, which is investigated in Section 5.1. The blue line indicates the case in which all elite data are used as the training data. As shown in this figure, the loss function of the training data converges almost smoothly. In contrast, when half of the elite data are used as the validation data, the loss function of the
![img-6.jpeg](img-6.jpeg)

Fig. 6 Learning histories at iteration 0 of an example: loss function $L$ of the training data when all elite data are used as the training data (blue), and that of the validation data when half of the elite data are used as the validation data (red)
validation data violently vibrates, as indicated by the red line. In this case, it is almost impossible to judge whether the VAE is appropriately trained or not. Therefore, we simply train the VAE for 400 epochs without the validation data at every iteration.

## 5 Numerical examples

In this section, we provide three numerical examples to demonstrate the usefulness of data-driven topology design. In example 1, we solve a high-stiffness and lightweight structure design problem, namely, the well-studied minimum compliance problem, to investigate the basic potential of data-driven topology design. In this example, the formulation support system is used to provide the initial material distributions.

In example 2, we solve a low-stress and light-weight structure design problem as a strongly nonlinear problem. The formulation support system is used to provide the initial material distributions, similar to example 1. Whereas the main purpose of data-driven topology design is to obtain higher-performance material distributions from the initially provided material distributions, it brings secondary but important utility to the formulation support system itself. We also discuss this utility.

Finally, in example 3, we tackle a compliant mechanism design problem taking the geometric nonlinearity and the maximum stress into account, as a further strongly nonlinear

problem. It was difficult for the current version of the formulation support system to provide a sufficient number of initial material distributions that function as compliant mechanisms. Therefore, in this example, a simple compliant mechanism design problem assuming the linear strain is solved to provide the initial material distributions.

In all numerical examples, we use the International System of Units, assume the plane stress condition, and set the value of $h$ in (2) to 0.025 to binarize the material distributions in the design domain. All numerical examples are computed using a workstation, which has 384 GB memory and 36 cores. The CPU model is Intel Xeon Gold 6240 .

### 5.1 Example 1

As described above, we solve the simple high-stiffness and light-weight structure design problem in example 1, the design domain and boundary conditions of which are shown in Fig. 7. As shown in this figure, a vertical load is applied to the bottom-right boundary and the displacement is fixed on the left-side boundary of the design domain. The design domain is discretized with $128 \times 96$ square elements, and the magnitude of the applied load per unit area is set to 1. Young's modulus of the structural material is set to 1 and is set to $1 \times 10^{-6}$ in the void to avoid the singular stiffness matrix, and Poisson's ratio is set to 0.3 . In this example, two objective functions are set: one is the volume of the structure, and the other is the logarithm of the mean compliance to the applied load.

We construct the database of the formulation support system in a manner similar to that of Yamasaki et al. (2019) and convert the material distributions in the database to conform to the design domain using the DDM. By doing so, we provide 2271 material distributions as the initial data. In step 1, we evaluate the volume and mean compliance of these material distributions using the finite element method (FEM) and obtain the evaluated data. In step 2,
![img-7.jpeg](img-7.jpeg)

Fig. 7 Design domain and boundary conditions of example 1
![img-8.jpeg](img-8.jpeg)

Fig. 8 Material distributions of the elite data at iteration 0 in example 1
we select the rank-one data entities from the evaluated data to obtain the elite data, and store their copies for the merging at step 6 . The material distributions of the elite data are shown in Fig. 8. In step 3, we convert these material distributions to conform to the reference domain using the DDM. In step 4, material distributions are generated using the VAE, as described in Section 4.2. In step 5, we inversely convert the generated material distributions to conform to the design domain using the DDM. In step 6, we evaluate the performances of the generated material distributions and merge them with the stored data and then return to
![img-9.jpeg](img-9.jpeg)

Fig. 9 Performances of elite solutions in example 1: iteration 0 (blue), iteration 1 (green), iteration 5 (orange), and iteration 38 (red)

step 2. We iterate the above data generation procedure until the convergence criterion is satisfied at iteration 38. The computational time per iteration is about 4 minutes.

Figure 9 shows that the performances of the elite solutions gradually improve when iterating the data generation. Because the performances are clearly improved after iteration 1, iterating the data generation procedure is significantly important for obtaining high-performance material distributions.

Figure 10 shows representative material distributions of the elite solutions at iterations 0 and 38. As shown in this figure, the final material distributions obtained seem to be reasonable and similar to the well-known optimized structures of the minimum compliance problem, as discussed later, whereas the material distributions at iteration 0 are low-performance and therefore seem to be unreasonable.

Next, we discuss the importance of training the VAE using only the elite data. For this purpose, we provide a case study where eliteness-based data selection is deactivated. Figure 11 shows the result of this case study. Clearly, the performances of the obtained elite solutions are inferior to those obtained by the proposed implementation. More importantly, the finally obtained elite material distributions seem to be very poor; in particular, some of them remain as elite material distributions from beginning to end. These results indicate the disadvantage of training a VAE using all material distributions. If a VAE is trained using all material distributions, various features of low-performance
![img-10.jpeg](img-10.jpeg)

Fig. 10 Performances and representative material distributions of elite solutions at iteration 0 in example 1 (blue) and at iteration 38 (red)
![img-11.jpeg](img-11.jpeg)

Fig. 11 Performances of elite solutions obtained by the proposed implementation in example 1 (red) and those obtained using a VAE trained with all of the material distributions (black), and representative material distributions of the latter
material distributions will be reflected in the latent space. Therefore, it is extremely difficult to expect a VAE to efficiently generate high-performance material distributions with a limited number of sampling points. Thus, the results shown in Fig. 11 indicate the importance of training a VAE using only the elite data.

Next, we investigate the usefulness of the normalization method introduced in Section 4.1. Figure 12 shows
![img-12.jpeg](img-12.jpeg)

Fig. 12 Performances of elite solutions obtained by the proposed implementation in example 1 (red) and those obtained without the normalization method described in Section 4.1 (black), and representative material distributions of the latter

the performances of the elite solutions obtained by the proposed implementation and those obtained without the normalization method. As shown in this figure, the latter is superior to the former when the volume is less than 0.36 . However, the material distributions of the latter are noisy images and include many intermediate states. Because such characteristics are not preferable, we adopt the normalization method for data-driven topology design.

Finally, we compare the results obtained by the proposed implementation with those obtained by density-based topology optimization. The elite solutions colored with black in Fig. 13 are obtained by directly solving the wellknown minimum compliance problem, while changing the allowable upper limit of the volume from 0.02 to 1.90 in increments of 0.02 . These material distributions are normalized in the same manner as those obtained by the proposed implementation, and therefore, the performances of material distributions that include many elements in intermediate states are significantly deteriorated. As a result, these material distributions are omitted from the elite solutions. It is observed when the volume is less than 0.25 .

The solutions displayed with black in Fig. 13 are close to the theoretically optimal solutions, and the elite solutions obtained by the proposed implementation are also close to them when the volume is greater than 0.5 and less than 0.18. Furthermore, the representative material distributions shown in Figs. 10 and 13 are also similar. On the other hand, the proposed implementation fails to generate
![img-13.jpeg](img-13.jpeg)

Fig. 13 Performances of elite solutions obtained by the proposed implementation in example 1 (red) and those obtained using densitybased topology optimization (black), and representative material distributions of the latter
wire-like slender structures as material distribution A in Fig. 13. Therefore, we consider that data-driven topology design has sufficient potential for generating high-performance material distributions although the above issue exists in the current implementation. The material distributions encircled with the blue dotted line in Fig. 8 are slightly similar to the material distributions in Fig. 13, and we therefore assume that data-driven topology design updates elite solutions while propagating and improving these material distributions.

### 5.2 Example 2

In this section, we solve a low-stress and light-weight structure design problem, the design domain and boundary conditions of which are given in Fig. 14. As shown in this figure, a vertical load is applied to the center-right boundary and the displacement is fixed on the top boundary of the design domain.

For this design problem, two objective functions are set: the volume of the structure and the logarithm of the maximum value of the von Mises stress generated in the structure. Furthermore, the mean compliance is imposed as a constraint to ensure the mechanical connection from the displacement fixed boundary to the load imposed boundary, which is crucial to obtain meaningful structures, as discussed by Yamasaki et al. (2019).

Although some studies have focused on the stress constraint or minimization problem, almost all of these studies introduce some type of approximation to avoid the point-wise constraints or min-max problem. For example, Allaire and Jouve (2008), Holmberg et al. (2013), and De Leon et al. (2015) used global p-norm based stress measures, and Amstutz and Novotny (2010) also proposed a domain integral-type approximation. These techniques are approximations, and it is often difficult to appropriately determine the artificial parameters used in
![img-14.jpeg](img-14.jpeg)

Fig. 14 Design domain and boundary conditions of example 2

them. Furthermore, these studies allow intermediate states of material existence, although the stress on an intermediate state is often physically meaningless, as Holmberg et al. (2013) pointed out. Because the stress usually takes the maximum value on the structural surface, intermediate states are originally unsuitable for the stress constraint or minimization problem. Thus, the design problem discussed in this section is a difficult and strongly nonlinear problem because of the pointwise nature of the stress, when solving it in a strict manner.

The design domain is discretized with 78,282 triangular elements with the representative length of 0.005 , and the magnitude of the applied load per unit area is set to 1 . The material properties are set to the same values as in example 1. In this example, we use conforming meshes to structural boundaries proposed by Yamasaki et al. (2017) to accurately compute the von Mises stress.

We prepare the initial data in the same manner as in example 1 and compute the performances of the material distributions of the initial data, that is, the volume, maximum value of the von Mises stress, and mean compliance. Next, we select the rank-one material distributions regarding the volume and maximum value of the von Mises stress under a constraint in which the mean compliance is less than 10. Figure 15 shows the material distributions selected as the elite data. In the same manner as in example 1, we iterate the data generation procedure until the convergence criterion is satisfied at iteration 50, and obtain the result shown in Fig. 16. The computational time per iteration is about 7 minutes.

As shown in this figure, the performances of the elite solutions are drastically improved by data-driven topology design. Furthermore, the obtained material distributions are reasonable, whereas some unreasonable material distributions exist at iteration 0 . For example, two holes of material distribution A seem to be useless for avoiding stress concentration. Material distribution B also seems to be unreasonable because the narrow part on the top side of the design domain is not suitable to avoid stress concentration. In material distributions C and E , the material at the bottom-side of the design domain is not needed to support the load. Furthermore, material distributions C and D include an obvious singular point of the stress.

These unreasonable material distributions are suppressed as a result of the performance improvement of the elite
![img-15.jpeg](img-15.jpeg)

Fig. 15 Material distributions of the elite data at iteration 0 in example 2
![img-16.jpeg](img-16.jpeg)

Fig. 16 Performances and representative material distributions of elite solutions at iteration 0 in example 2 (blue) and those at iteration 50 (red)
solutions, and we can find some design knowledge from the results of data-driven topology design. For example, structures such as the mirror writing of the letter "J" are preferable for avoiding stress concentration at the inner corner. Furthermore, it is effective to reduce the material volume on the top-side of the design domain for weight saving.

The above results indicate that data-driven topology design provides an important utility to the formulation support system. As described in Section 3.1, the formulation support system is used to support the designer's trial-anderror for determining appropriate formulations of topology optimization problems. That is, the designer sets multiple objective functions as the candidates of the objective and constraint functions in a topology optimization problem (the formulation candidate), and then, the formulation support system outputs the rank-one material distributions from the database as the blue solutions in Fig. 16. By referring to these material distributions, the designer judges whether the formulation candidate is appropriate or not.

In the above situation, if useful design knowledge is obtained from reasonable material distributions as a result of the performance improvement by data-driven topology design, the designer can judge the appropriateness of the input formulation candidate with confidence. Otherwise, the appropriateness of the input formulation candidate should be doubted. In addition, design knowledge itself is useful for designers. Therefore, we consider that data-driven topology design has potential, not only to obtain higher performance material distributions but also to enhance the formulation support system.

### 5.3 Example 3

In example 3, we tackle a compliant mechanism design problem in which both the geometric nonlinearity and the maximum stress are considered. Compliant mechanisms are well-studied design targets in the field of topology optimization; however, only a limited number of studies consider the geometric nonlinearity (Luo and Tong 2008; Liu et al. 2017; Chen et al. 2019; Dunning 2020; Kumar et al. 2020), despite the large deformation of compliant mechanisms. Similarly, only a limited number of studies consider the maximum stress as a constraint (De Leon et al. 2015; Lopes and Novotny 2016), although it is necessary to constrain the maximum stress in the real world. Instead of constraining the maximum stress, many studies avoid the stress concentration in an indirect manner, for example, setting an artificial spring in the input port, constraining the stiffness to the input load, and so on.

The study of De Leon et al. (2020) is the most challenging because the proposed method considers both the geometric nonlinearity and the maximum stress. However, in their method, the maximum stress is approximately evaluated using the global p-norm, similar to Allaire and Jouve (2008), Holmberg et al. (2013), and De Leon et al. (2015).

The above indicates that the compliant mechanism design problem that considers both the geometric nonlinearity and the maximum stress is a strongly nonlinear problem, particularly when considering the maximum stress in a strict manner. We tackle this challenging problem with data-driven topology design.

Figure 17 shows the design domain and boundary conditions of example 3. Here, we aim to design compliant grippers that transmit force on the input port to an object set on the output port. In this example, a horizontal load is applied to the input port, and an artificial spring is set on the output port to represent the reaction force from the object. The magnitude of the applied load per unit area is set to
![img-17.jpeg](img-17.jpeg)

Fig. 17 Design domain and boundary conditions of example 3
0.08 and the spring coefficient of the artificial spring per unit area is set to 10 . The upper half domain is treated as the actual design domain by imposing a symmetric boundary condition. In this example, we introduce three objective functions: the material volume, the maximum value of the von Mises stress, and the reaction force on the output port.

The design domain is discretized with 49,736 triangular elements with the representative length of 0.005 . Concerning the constitutive law, we use the Kirchhoff-Saint Venant material model, and Young's modulus and Poisson's ratio are set to 1 and 0.3 , respectively. Similar to example 2 , we use conforming meshes to structural boundaries to accurately compute the stress. In addition, we completely deactivate the elements in the void domain because weak materials set in the void domain may cause numerical instabilities in the geometric nonlinear analysis (De Leon et al. 2020). That is, we extract the structural boundary in the design domain and conduct a geometric nonlinear analysis using only the material domain.

It is worth noting that the VAE may generate material distributions in which an FEM solver cannot find the solution because of the geometric nonlinearity. Then, we can ignore these material distributions because we focus only on promising material distributions. This is a great advantage of datadriven topology design when compared with sensitivitybased topology optimization methods, because halting the computation before convergence is fatal in these methods.

As described at the beginning of Section 5, we prepare the initial material distributions by solving a simple compliant mechanism design problem assuming the linear strain because we could not prepare a sufficient number of material distributions that function as compliant mechanisms from the database of the formulation support system used in examples 1 and 2. In the simple problem, we use the design domain and boundary conditions shown in Fig. 17 and maximize the reaction force on the output port while constraining the material volume. In addition, we constrain the displacement on the input port to avoid forming extremely thin hinges, instead of strictly constraining the maximum stress. We implement a simple density-based topology optimization method to solve this problem and obtain 196 material distributions while
![img-18.jpeg](img-18.jpeg)

Fig. 18 Material distributions of the elite data at iteration 0 in example 3

changing the magnitude of the input load and the allowable upper limit of the volume. Then, we evaluate these material distributions using the three objective functions under the geometric nonlinear analysis. As a result, the material distributions shown in Fig. 18 are selected as the initial material distributions according to the optimality of the three objective functions.

We conduct data-driven topology design using these initial material distributions and obtain 400 material distributions, as shown in Fig. 19, after 50 iterations. Their performances are shown in Fig. 20. The computational time per iteration is about 20 minutes. Here, three points should be noted. First, we constrain the volume, maximum value of the von Mises stress, and reaction force by the respective
![img-19.jpeg](img-19.jpeg)

Fig. 19 Material distributions of the elite data at iteration 50 in example 3

![img-20.jpeg](img-20.jpeg)

Fig. 20 Performances and representative material distributions of elite solutions at iteration 0 in example 3 (blue) and at iteration 50 (red)
worst values at iteration 0 . Second, the volume shown in Fig. 20 indicates the amount of material in the upper half domain. Third, the reaction force is shown with a negative sign corresponding to the minimization.

As shown in Fig. 20, the performances of the material distributions are drastically improved after conducting datadriven topology design. To further investigate the obtained results, we focus on the four material distributions shown in Fig. 20, that is, material distributions A, B, C, and D. Material distribution A is a balanced material distribution at iteration 0 , and material distributions $\mathrm{B}, \mathrm{C}$, and D at iteration 50 are completely superior to material distribution A. Among them, material distribution B is specialized to the volume. Similarly, material distributions C and D are specialized to the maximum value of the von Mises stress and reaction force, respectively.

Figure 21 shows the contour plots of the von Mises stress with the exact deformations concerning these material distributions. As shown in this figure, the von Mises stress concentrates in the area circled with the red dotted line in material distribution A. On the other hand, in material
distributions B, C, and D, the von Mises stress distribution is well balanced on the hinge part and the displacement support boundary by rounding the area circled with the red dotted lines and adjusting the hinge width. In particular, material distributions B and D succeed in approximately evenly distributing the von Mises stress on the three parts. These results seem to be sufficiently reasonable.

If we ignore the geometric nonlinearity by assuming the linear strain, we obtain 400 high-performance material distributions under this assumption as a result of datadriven topology design. Figure 22 shows a part of them. Although these may seem to be reasonable as compliant mechanisms, we cannot conduct a geometric nonlinear analysis of 284 material distributions, including those in Fig. 22. In other words, the linear strain assumption does not hold at least for $71 \%$ of the total material distributions. Furthermore, whereas the maximum reaction force in the remaining 116 material distributions is $2.92 \times 10^{-3}, 35$ material distributions achieve a higher reaction force when considering the geometric nonlinearity, as shown in Fig. 20. Thus, the geometric nonlinearity is not negligible, and a

![img-21.jpeg](img-21.jpeg)

Fig. 21 Contour plots of von Mises stress with exact deformations for material distributions shown in Fig. 20: a-d material distributions A-D
solution search based on a high-fidelity analysis is needed for strongly nonlinear problems, as demonstrated in this example.

At the end of this section, we discuss the relationship between data-driven topology design and multifidelity topology design originated by Yaji et al. (2020). It is a design methodology to indirectly solve a strongly nonlinear topology optimization problem, which is difficult to solve
![img-22.jpeg](img-22.jpeg)

Fig. 22 Material distributions obtained under linear strain assumption in example 3 (these are a part of the whole)
directly and only forward analysis can be conducted, using material distributions obtained by solving another problem, which is easy to solve directly and is correlated with the strongly nonlinear problem. In their study, the best material distribution among the prepared material distributions was simply selected. That is, the aim of their study corresponds to obtaining the initial elite solutions in example 3. In contrast, data-driven topology design can obtain higherperformance elite solutions, as shown in Fig. 20. Therefore, example 3 indicates that data-driven topology design has potential to be an improved version of multifidelity topology design.

## 6 Conclusion

In this paper, we proposed data-driven topology design, which is a sensitivity-free and multi-objective structural

design methodology. It generates higher-performance material distributions from initially provided material distributions using a deep generative model, on the basis of a data-driven manner. Because of its characteristic, datadriven topology design has potential to enhance a support system for determining an appropriate formulation of a topology optimization problem, and also has potential as a new version of multifidelity topology design. We demonstrated its usefulness through three numerical examples. However, some issues remain.

A major one is applying data-driven topology design to various strongly nonlinear problems. In this paper, we targeted two types of strongly nonlinear problems in structural mechanics as the first investigation of data-driven topology design. However, there are many other strongly nonlinear design problems. A representative one is the turbulent flow problem, as described in Section 1. Therefore, we plan to apply data-driven topology design to the turbulent flow problem.

As another issue, it is necessary to investigate another deep generative model, despite our adoption of a VAE in this paper; more suitable deep generative models may exist for datadriven topology design. In addition, a suitable architecture for the VAE should be further investigated. Although we adopted the architecture shown in Fig. 5 on the basis of the results of a preliminary study, there may be room for improvement. Furthermore, the theoretical backbone of data-driven topology design should be further investigated. We plan to tackle these issues in future studies and aim to develop more sophisticated data-driven topology design.

## Appendix A

The convergence criterion of the proposed implementation is based on the area outside of the elite solutions in the objective function space. If the area does not decrease after incrementing the iteration, or if the iteration number reaches 50 , we terminate the data generation procedure.

The area outside the elite solutions is approximately computed on the basis of the number of fixed grid points that are not dominated by the elite solutions. Figure 23 shows an example of the fixed grid points for the approximate computation. In this figure, the red grid points are dominated by the blue elite solutions, and the green grid points are not dominated. The area outside the blue elite solutions is approximately computed by counting the number of green grid points.

In example 1, the fixed grid points are set by discretizing the objective function space with $400 \times 400$ in the range from 0 to 1.92 for the volume and -1 to 6 for the mean
![img-23.jpeg](img-23.jpeg)

Fig. 23 An example of fixed grid points for approximately computing the area outside elite solutions colored with blue
compliance. In example 2, these are set by discretizing the objective function space with $400 \times 400$ in the range from 0 to 0.7 for the volume and 0 to 1.8 for the von Mises stress. In example 3, these are set by discretizing the objective function space with $400 \times 400 \times 400$ in the range from 0.1 to 0.4 for the volume, 0.1 to 1.0 for the von Mises stress, and $-4.0 \times 10^{-3}$ to $-0.5 \times 10^{-3}$ for the reaction force.

Figure 24 shows the convergence histories of examples 1, 2 , and 3 . Note that the number of grid points outside the non-dominated solutions is normalized by the initial values in the respective examples.
![img-24.jpeg](img-24.jpeg)

Fig. 24 Convergence histories of example 1 (blue), example 2 (green), and example 3 (red)

## Appendix B

The number of latent variables $N_{\mathrm{B}}$ is an important parameter that should be determined carefully. Here, we investigate its impact on the performances of generated material distributions. Figure 25 shows how $N_{\mathrm{B}}$ influences obtained results in example 1. As shown in this figure, the elite solutions are obviously improved by increasing $N_{\mathrm{B}}$. Now, we cannot theoretically explain it, but consider that the twoor four-dimensional latent space is too small to capture features of elite material distributions. On the other hand, if $N_{\mathrm{B}}$ is set to a larger value, it will be difficult to generate meaningful material distributions by finite random sampling on a large latent space. Therefore, we assume that there is a suitable range for setting $N_{\mathrm{B}}$ and adopt $N_{\mathrm{B}}=8$ for the numerical examples in this paper.
![img-25.jpeg](img-25.jpeg)

Fig. 25 Performances of elite solutions obtained while changing the number of the latent variables $N_{\mathrm{B}}$ in example 1: $N_{\mathrm{B}}=2$ (blue), $N_{\mathrm{B}}=4$ (green), and $N_{\mathrm{B}}=8$ (red)

## Compliance with ethical standards

Conflict of interest The authors declare that they have no conflict of interest.

Replication of results The necessary information for a replication of the results are presented in the manuscript. Interested readers may contact the corresponding author for further details regarding the implementation.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not
included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

## References

Abueidda DW, Koric S, Sobh NA (2020) Topology optimization of 2D structures with nonlinearities using deep learning. Comput Struct 106283:237. https://doi.org/10.1016/j.compstruc.2020.106283
Aguilar Madeira J, Rodrigues HC, Pina H (2006) Multiobjective topology optimization of structures using genetic algorithms with chromosome repairing. Struct Multidiscip Optim 32(1):31-39. https://doi.org/10.1007/s00158-006-0007-0
Allaire G, Jouve F (2008) Minimum stress optimal design with the level set method. Eng Anal Bound Elem 32(11):909-918. https://doi.org/10.1016/j.enganabound.2007.05.007
Amstutz S, Novotny AA (2010) Topological optimization of structures subject to Von Mises stress constraints. Struct Multidiscip Optim 41(3):407-420. https://doi.org/10.1007/s00158-009-0425-x
Atienza R (2018) Advanced deep learning with keras: apply deep learning techniques, autoencoders, GANs variational autoencoders, deep reinforcement learning, policy gradients, and more. Packt Publishing
Banga S, Gehani H, Bhilare S, Patel S, Kara LB (2018) 3D topology optimization using convolutional neural networks. arXiv:1808.07440
Bendsøe MP, Kikuchi N (1988) Generating optimal topologies in structural design using a homogenization method. Comput Methods Appl Mech Eng 71(2):197-224
Bendsøe MP (1989) Optimal shape design as a material distribution problem. Struct Optim 1(4):193-202
Bendsøe MP, Sigmund O (2003) Topology optimization: theory methods and applications. Springer, Berlin
Bhattacharjee S, Gras R (2019) Estimation of distribution using population queue based variational autoencoders. In: Proceedings of 2019 IEEE Congress on Evolutionary Computation. IEEE, Wellington, pp 1406-1414. https://doi.org/10.1109/CEC.2019.87 90077
Cang R, Yao H, Ren Y (2019) One-shot generation of near-optimal topology through theory-driven machine learning. Comput Aided Des 109:12-21. https://doi.org/10.1016/j.cad.2018.12.008
Chapman CD, Saitou K, Jakiela MJ (1994) Genetic algorithms as an approach to configuration and topology design. J Mech Des 116(4):1005-1012. https://doi.org/10.1115/1.2919480
Chen Q, Zhang X, Zhu B (2019) A 213-line topology optimization code for geometrically nonlinear structures. Struct Multidiscip Optim 59(5):1863-1879. https://doi.org/10.1007/s00158-018-213 8-5
De Leon DM, Alexandersen J, Fonseca JSO, Sigmund O (2015) Stressconstrained topology optimization for compliant mechanism design. Struct Multidiscip Optim 52(5):929-943. https://doi.org/ 10.1007/s00158-015-1279-z

De Leon DM, Goncalves JF, de Souza CE (2020) Stress-based topology optimization of compliant mechanisms design using geometrical and material nonlinearities. Struct Multidiscip Optim 62(1):231-248. https://doi.org/10.1007/s00158-019-02484-4
Deb K, Pratap A, Agarwal S, Meyarivan T (2002) A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Trans Evol Comput 6(2):182-197. https://doi.org/10.1109/4235.996017
Deng L (2012) The MNIST, database of handwritten digit images for machine learning research. IEEE Signal Process Mag 29(6):141142. https://doi.org/10.1109/MSP.2012.2211477

Dilgen CB, Dilgen SB, Fuhrman DR, Sigmund O, Lazarov BS (2018) Topology optimization of turbulent flows. Comput Methods Appl Mech Eng 331:363-393. https://doi.org/10.1016/j.cma.2017. 11.029

Dunning PD (2020) On the co-rotational method for geometrically nonlinear topology optimization. Struct Multidiscip Optim 62(5):2357-2374. https://doi.org/10.1007/s00158-020-02605-4
Garciarena U, Santana R, Mendiburu A (2018) Expanding variational autoencoders for learning and exploiting latent representations in search distributions. In: Proceedings of the Genetic and Evolutionary Computation Conference, Kyoto, pp 849-856, https://doi.org/10.1145/3205455.3205645
Gatys LA, Ecker AS, Bethge M (2016) Image style transfer using convolutional neural networks. In: Proceedings of 2016 IEEE Conference on Computer Vision and Pattern Recognition. IEEE, Las Vegas, pp 2414-2423. https://doi.org/10.1109/CVPR.2016.265
Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, Courville A, Bengio Y (2014) Generative adversarial nets. In: Ghahramani Z, Welling M, Cortes C, Lawrence ND, Weinberger KQ (eds) Advances in neural information processing systems, vol 27. Curran Associates, Inc., pp 2672-2 680
Guo X, Zhang W, Zhong W (2014) Doing topology optimization explicitly and geometrically: A new moving morphable components based framework. J Appl Mech 81(8):081009. https:// doi.org/10.1115/1.4027609
Guo T, Lohan DJ, Allison JT, Cang R, Ren Y (2018) An indirect design representation for topology optimization using variational autoencoder and style transfer. In: Proceedings of AIAA/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conference. AIAA, Kissimmee. https://doi.org/10. 2514/6.2018-0804
Hinton GE, Salakhutdinov RR (2006) Reducing the dimensionality of data with neural networks. Science 313(5786):504-507. https://doi.org/10.1126/science. 1127647
Holmberg E, Torstenfelt B, Klarbring A (2013) Stress constrained topology optimization. Struct Multidiscip Optim 48(1):33-47. https://doi.org/10.1007/s00158-012-0880-7
Kingma DP, Welling M (2013) Auto-encoding variational bayes. arXiv:1312.6114
Kingma DP, Ba J (2014) Adam: A method for stochastic optimization. arXiv:1412.6980
Kontoleontos EA, Papoutsis-Kiachagias EM, Zymaris AS, Papadimitriou DI, Giannakoglou KC (2013) Adjoint-based constrained topology optimization for viscous flows, including heat transfer. Eng Optim 45(8):941-961. https://doi.org/10.1080/0305215X. 2012.717074

Kumar P, Schmidleithner C, Larsen NB, Sigmund O (2020) Topology optimization and 3D printing of large deformation compliant mechanisms for straining biological tissues. Struct Multidiscip Optim. https://doi.org/10.1007/s00158-020-02764-4
Larrañaga P, Lozano JA (2001) Estimation of distribution algorithms: a new tool for evolutionary computation, genetic algorithms and evolutionary computation. Springer, US
Lei X, Liu C, Du Z, Zhang W, Guo X (2019) Machine learningdriven real-time topology optimization under moving morphable component-based framework. J Appl Mech 86(1):011004. https://doi.org/10.1115/1.4041319
Liu L, Xing J, Yang Q, Luo Y (2017) Design of large-displacement compliant mechanisms by topology optimization incorporating modified additive hyperelasticity technique. Math Probl Eng 2017:1-11. https://doi.org/10.1155/2017/4679746
Lopes CG, Novotny AA (2016) Topology design of compliant mechanisms with stress constraints based on the topological
derivative concept. Struct Multidiscip Optim 54(4):737-746. https://doi.org/10.1007/s00158-016-1436-z
Luo Z, Tong L (2008) A level set method for shape and topology optimization of large-displacement compliant mechanisms. Int J Numer Methods Eng 76(6):862-892. https://doi.org/10.1002/nme. 2352
Mirza M, Osindero S (2014) Conditional generative adversarial nets. arXiv:1411.1784
Nie Z, Lin T, Jiang H, Kara LB (2020) TopologyGAN: Topology optimization using generative adversarial networks based on physical fields over the initial domain. arXiv:2003.04685
Oh S, Jung Y, Kim S, Lee I, Kang N (2019) Deep generative design: Integration of topology optimization and generative models. J Mech Des 141(11):111405-1-111405-13. https://doi.org/10.1115/1.4044229
Rocca J (2019) Understanding variational autoencoders (VAEs). https://towardsdatascience.com/understanding-variational-autoen-coders-vaes-f70510919f73 . Accessed 4 March 2021
Sasaki H, Igarashi H (2019) Topology optimization accelerated by deep learning. IEEE Trans Magn 55(6):1-5. https://doi.org/ 10.1109/TMAG.2019.2901906

Shim PY, Manoochehri S (1997) Generating optimal configurations in structural design using simulated annealing. Int J Numer Methods Eng 40(6):1053-1069
Sigmund O (2011) On the usefulness of non-gradient approaches in topology optimization. Struct Multidiscip Optim 43(5):589-596. https://doi.org/10.1007/s00158-011-0638-7
Tai K, Prasad J (2007) Target-matching test problem for multiobjective topology optimization using genetic algorithms. Struct Multidiscip Optim 34(4):333-345. https://doi.org/10.1007/s00158-006-0082-2
Tan RK, Zhang NL, Ye W (2020) A deep learning-based method for the design of microstructural materials. Struct Multidiscip Optim 61(4):1417-1438. https://doi.org/10.1007/s00158-019-02424-2
Ulu E, Zhang R, Kara LB (2016) A data-driven investigation and estimation of optimal topologies under variable loading configurations. Comput Methods Biomech Biomed Eng Imaging Vis 4(2):61-72. https://doi.org/10.1080/21681163.2015.1030775
Wang S, Tai K (2004) Graph representation for structural topology optimization using genetic algorithms. Comput Struct 82(20):1609-1622. https://doi.org/10.1016/j.compstruc.2004.05.0 05

Wu CY, Tseng KY (2010) Topology optimization of structures using modified binary differential evolution. Struct Multidiscip Optim 42(6):939-953. https://doi.org/10.1007/s00158-010-0523-9
Wu Z, Song S, Khosla A, Yu F, Zhang L, Tang X, Xiao J (2015) 3D ShapeNets: a deep representation for volumetric shapes. In: Proceedings of 2015 IEEE Conference on Computer Vision and Pattern Recognition. IEEE, Boston, 1912-1920. https://doi.org/10. 1109/CVPR.2015.7298801
Yaji K, Yamasaki S, Fujita K (2020) Multifidelity design guided by topology optimization. Struct Multidiscip Optim 61(3):10711085. https://doi.org/10.1007/s00158-019-02406-4

Yamasaki S, Nishiwaki S, Yamada T, Imai K, Yoshimura M (2010) A structural optimization method based on the level set method using a new geometry-based re-initialization scheme. Int J Numer Methods Eng 83(12):1580-1624. https://doi.org/10.1002/nme. 2874
Yamasaki S, Yamanaka S, Fujita K (2017) Three-dimensional grayscale-free topology optimization using a level-set based rrefinement method. Int J Numer Methods Eng 112(10):14021438. https://doi.org/10.1002/nme. 5562

Yamasaki S, Yaji K, Fujita K (2019) Knowledge discovery in databases for determining formulation in topology optimization. Struct Multidiscip Optim 59(2):595-611. https://doi.org/10.1007/s00158-01 8-2086-0

Yu Y, Hur T, Jung J, Jang IG (2019) Deep learning for determining a near-optimal topological design without any iteration. Struct Multidiscip Optim 59(3):787-799. https://doi.org/10.1007/ s00158-018-2101-5
Zhang W, Yang Z, Jiang H, Nigam S, Yamakawa S, Furuhata T, Shimada K, Kara LB (2019a) 3D shape synthesis for conceptual design and optimization using variational autoencoders. In: Proceedings of ASME 2019 International Design Engineering Technical Conferences \& Computers and Information in Engineering Conference, ASME, Anaheim, DETC2019-98525

Zhang Y, Chen A, Peng B, Zhou X, Wang D (2019b) A deep convolutional neural network for topology optimization with strong generalization ability. arXiv:1901.07761
Zhang Y, Ye W (2019c) Deep learning-based inverse method for layout design. Struct Multidiscip Optim 60(2):527-536. https://doi.org/10.1007/s00158-019-02222-w

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.