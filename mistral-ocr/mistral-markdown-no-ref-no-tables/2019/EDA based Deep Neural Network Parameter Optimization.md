# EDA based Deep Neural Network Parameter Optimization 

Qingyang Xu*<br>School of Mechanical, Electrica \& Information Engineering<br>Shandong University<br>Weihai, Shandong 264209, China<br>qingyangxu@sdu.edu.cn

## Anbang Liu

School of Mechanical, Electrica \& Information Engineering<br>Shandong University<br>Weihai, Shandong 264209, China<br>keithliumail@gmail.com


#### Abstract

Deep neural network has been applied in kinds of areas due to the excellent performance. The capacity of deep neural network relies on the parameter training algorithm which is always based on the gradient information. However, for deep neural network, it is harder and harder for training due to depth of the neural network and a large number of parameters. Therefore, kinds of techniques are proposed to cope with this problem. However, the training algorithm is almost based on the gradient information with inherent defect. Evolutionary algorithm has the advantage of global optimization capability, independent of gradient information etc. Estimation of distribution algorithm (EDA) is a typical evolutionary algorithm which relies on the probability model of population. Therefore, the EDA is adopted to train the weight and bias of deep neural network in his paper. However, the large scale optimization capability of EDA is limited. Thereby, an improved strategy is proposed to enhance the large scale optimization capability of EDA. In the improved scheme, a random selection strategy is carried out to select partial variables for probability modeling instead of all of the variables, in order to reduce the computing time and the probability of combination explosion. A simulation is carried out to exhibit the validity of the improved algorithm.


## CCS CONCEPTS

- Computing methodologies - Machine learning - Machine learning approaches $\cdot$ Neural networks


## KEYWORDS

Deep neural network, Optimization, EDA, Training

[^0]
## 1 Introduction

Artificial neural network is inspired by the connection mechanism of biological neural network[1]. The training of ANN is based on the training algorithm, such as BP algorithm. The training algorithm makes use of the gradient information which comes from minimizing the loss function. However, the gradient information maybe disappears with the increasing depth of neural network. The gradient information may disappear in the smaller layer. Therefore, the deep learning technique is proposed and some new activation functions are proposed[2]. However, the training of deep neural network is also a challenge due to the combination of large scale parameters. Another direct way is based on the evolutionary algorithm which uses the objective function instead of gradient information for optimization[3]. The evolutionary algorithm has two types of individual updating strategy. A typical way is the gene operation which adopts selection, recombination and mutation operators to pass the genes to the next generation, such as the genetic algorithm. The parameters and architecture of the neural network are encoded as the gene for individuals. Current neural network architecture searching system is almost based on it[4]. Another evolutionary algorithm is based on the probability modeling of population, such as estimation of distribution algorithm, which has a strong global optimization ability. However, the optimization capability of EDA is limited due to the curse of dimension[5]. In this paper, an improved EDA is proposed for the parameters optimization of artificial neural network. In the improved algorithm, a random strategy is adopted for the variables. The probability model of selected variables will be updated by the statistics information of the promising individuals. And then, a new population is generated according to the sampling of probability model.

## 2 Stacked Autoencoder

Autoencoder is a typical unsupervised learning algorithm, and it can be used for the task of representation learning[6, 7]. It also provides a compression of knowledge representation of the original input. A reconstruction of the original input $x$ is generated $x^{\prime}$, and the reconstruction error is used to train the neural network. The architecture of autoencoder is shown in Figure 1, for any new input $x$, we can compute the output of the hidden units $a$. The autoencoder often ends up learning a low-


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from Permissions@acm.org.
    CSAE 2019, October 22-24, 2019, Sanya, China
    (c) 2019 Association for Computing Machinery.

    ACM ISBN 978-1-4503-6294-8/19/10$X 15.00$
    https://doi.org/10.1145/3331453.3362048

dimensional representation which often gives a better representation of the input than the original raw input $x$.

Autoencoder makes use of encoding and decoding process to train the deep neural network.

$$
\begin{aligned}
& a=f\left(W^{T} x+b\right) \\
& y=g\left(W a+b^{\prime}\right)
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1: Autoencoder.

For the encoding layer, $a$ is the output of hidden layer, $W$ is the weight matrix, $b$ is the threshold value, and $f$ is the activation function of hidden layer. For the decoding layer, $a$ is the output of hidden layer, $W$ is the weight matrix, $b^{\prime}$ is the threshold value, and $g$ is the activation function of reconstruction layer. $x$ and $y$ is the input and the reconstruction of $x$.

The loss function always consists of reconstruction error and sparse penalty as the following equation.

$$
J=\|x-y\|^{2}+\mu \sum a
$$

$J$ is the loss function, $\mu$ is the coefficient of sparse penalty. $a$ is the output of hidden layer.

The deep neural network can be trained by autoencoer, which is always called stacked autoencoder as shown in Figure 2.

In BP neural network, only one hidden layer exists in the neural network. However, for deep neural network, there will be many hidden layers, and the training of deep neural network is invalid using BP algorithm. Therefore, the layer wised pretraining strategy is proposed for deep neural network training. Thereby, the first hidden layer 'Hidden layer 1' is trained by autoencoder of 'Hidden layer 1-Decoder 1'. After the training of hidden layer 1, the hidden layer 2 can be trained by 'Hidden layer 2-Decoder 2' which adopts the output of hidden layer 1 as the input of hidden layer 2. When the pre-training of all hidden layers is finished, a fine-tuning process can be carried out to train the whole neural network according to the labelled data, the loss function is shown as equation (4).

$$
E=\left\|y_{o}-y_{l}\right\|^{2}
$$

$y_{o}$ is the prediction output, $y_{l}$ is the labelled data.
![img-1.jpeg](img-1.jpeg)

Figure 2: Diagram of Pre-training.

## 3 Improved Estimation of Distribution Algorithm

### 3.1 Traditional EDA

Compared with GA building gene blocks, EDA relies on the probability model of population evolution[8]. The probability model is built based on the statistical information of the most promising individual, and then the probability model is used for sampling to generate the new individuals. Meanwhile, the probability model is updated in each generation according to the new population. therefore, the population evolves, and finally search the optimal solutions. The diagram of the EDA is shown in Figure 3.

The most important step of EDAs is the construction of probabilistic model, and the Gaussian distribution of individuals is assumed to model and estimate the distribution of solutions[9, 10]. Therefore, mean and variance of promising individuals are computed according to the maximum likelihood. There the probability distribution $P\left(x_{1}, x_{2} \cdots x_{m}\right)$ of the vector $\left(x_{1}, x_{2} \cdots x_{m}\right)$ of m variables is a product of the distributions of individual variables:

$$
P\left(x_{1}, x_{2} \cdots x_{m}\right)=\prod_{i=1}^{m} P\left(x_{i}\right)
$$

The mean and covariance parameters of the normal pdf can be estimated according to the promising individuals[11].

$$
\widehat{\mu}_{i}(k)=\frac{1}{N} \sum_{s=1}^{N} x_{i}^{s}(k)
$$

$$
\sigma_{i}^{2}(k)=\frac{1}{N} \sum_{n=1}^{B N}\left(x_{i}^{n}(k)-\bar{\mu}_{i}(k)\right)\left(x_{i}^{n}(k)-\bar{\mu}_{i}(k)\right)^{T}
$$

$\bar{\mu}_{i}(k)$ is the mean of $i$ th variable in kth iteration, BN is the selected individuals size. $\sigma_{i}^{2}(k)$ is the covariance of $i$ th variable in $k$ th iteration.
![img-2.jpeg](img-2.jpeg)

Figure 3: Flowchart of Traditional EDA.
The normal pdf $N\left(\mu_{i}, \sigma_{i}\right)$ is defined as equation (8).

$$
N\left(x_{i}, \mu_{i}, \sigma_{i}\right)=\frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}\right)^{2}}{2 \sigma_{i}^{2}}}
$$

The probability distribution $P\left(x_{1}, x_{2} \cdots x_{m}\right)$ can be described as equation (9).

$$
P\left(x_{1}, x_{2}, \cdots x_{m}\right)=\prod_{i=1}^{m} \frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-\mu_{i}\right)^{2}}{2 \sigma_{i}^{2}}}
$$

The $\left(\mu_{i}, \sigma_{i}\right)$ have been estimated according to the promising individuals, and they are updated in every iteration.

### 3.2 Random Variable Selection Based EDA

For the neural network parameter optimization system, the number of the parameter is huge which is a typical large scale optimization problem. For traditional EDA, it is hard to obtain a solution due to the curse of dimensionality[12]. A large scale of dimensionality will increase the sampling time and the probability of combinational explosion. Therefore, a random strategy is proposed. For the random strategy, a group of variables are selected and the probability model of theses variables are updated by the statistics information of the
promising individuals. In the improved EDA, the updating of variables is sampled by the probability model of corresponding variable partially instead of generating all variables by sampling as traditional EDA. The flowchart of the algorithm is shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4: Flowchart of Improved EDA.

## 4 Simulation

In this paper, the MNIST database is adopted to verify the validation of the proposed algorithm, which contains 60,000 handwritten digits training images and 10,000 testing images [13]. In order to do a comparison, the layer by layer pre-training and fine-tuning based on traditional SGD algorithm is carried out, and then the layer by layer pre-training, two layers pretraining meanwhile and fine-tuning based on the proposed algorithm are testified. The structure of the neural network is 784-250-100-10, which contains two hidden layers with 250 and 100 neurons. The neurons of input and output layer are the pixels of input image and categories out. The configuration of the hardware is i5-8400 CPU, 8G RAM, GTX 1080TI GPU. NVIDIA GPU is adopted to accelerate the calculation. The code is programmed under MATLAB. Some comparisons are carried out to exhibit the validation of the proposed algorithm.

Firstly, a layer by layer pre-training is adopted traditional style as the SGD based algorithm. The EDA is adopted to pretrain the hidden layer 1 , and then the hideden layer 2 is pretrained. Compared with the traditional SGD based algorithm as Figure 5, the performance of EDA is better than SGD based algorithm. Although, the performance of EDA in layer by layer

pre-training is promising, the time consumption is unsatisfactory. Therefore, the two hidden layers are considered to pre-train meanwhile. The results in shown in Figure 6. We can see that the performance of the two-layer pre-training meanwhile is promising. Hence, the EDA has the capability of searching the parameters of deep neural network meanwhile without layer by layer pre-training way. In Figure 7, we also compare the testing results in the fine-tuning process. We can see that the final classification accuracy is similar. Therefore, we can say that the proposed algorithm is effective to solve the large scale optimization problem of deep neural network. In order to testify the time consumption of the prosed algorithm, the consumption in each iteration is recoded which is shown in Figure 8. The two layers pre-training meanwhile consumes little longer than the layer by layer pre-training time. However, the sum of layer by layer pre-training time consumption is larger than EDA. Therefore, the time consumption of EDA is favorable in the training of deep neural network.
![img-4.jpeg](img-4.jpeg)

Figure 5: Layer by Layer Pre-training based on EDA and SGD.
![img-5.jpeg](img-5.jpeg)

Figure 6: Layer by Layer Compared with Two Layer Meanwhile Pre-training based on EDA
![img-6.jpeg](img-6.jpeg)

Figure 7: Testing Results in Fine-tuning based on EDA and SGD.
![img-7.jpeg](img-7.jpeg)

Figure 8: Time Consumption of Layer by Layer and two Layers Meanwhile Pre-training.

## 5 Conclusions

According to the simulation, the proposed scheme is valid for the optimization of deep neural network. The layer-wised pretraining is carried out for the gradient based training algorithms. For the EDA based algorithm, we can see that the optimization of the whole deep neural has the same performance as the layerwised pre-training scheme. Therefore, the EDA algorithm can be used for the optimization of deep neural network conveniently, which also can overcome the disadvantage of gradient dependence.

## ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China under Grants (61603214, 61573213, 61673245, 61803227), National Key Research and Development Plan of China under Grant 2017YFB1300205, Shandong Province Key Research and Development Plan under Grants (2018GGX101039,2016ZDJS02A07), China Postdoctoral Science Foundation under Grant 2018M630778 and Independent Innovation Foundation of Shandong University under Grant 2018ZQXM005.
