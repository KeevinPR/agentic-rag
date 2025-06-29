# A Novel Multi-objective Optimization-based Image Registration Method 

Meifeng Shi<br>College of Computer<br>Science, Chongqing Univ. Chongqing 400044, China $+8613983701748$ shishating@163.com

Zhongshi He*<br>College of Computer<br>Science, Chongqing Univ. Chongqing 400044, China $+8613062356757$ zshe@cqu.edu.cn

## ABOURS

The RANSAC is widely used in image registration algorithms. However, the RANSAC becomes computationally expensive when the number of feature points is large. And also, its high errormatching ratio caused by the large number of iterations always raises the possibility of false registration. To deal with these drawbacks, a novel multi-objective optimization-based image registration method is proposed, named MO-IRM. In MO-IRM, a multi-objective estimation model is built to describe the feature matching pairs (data set), with no need for the pre-check process that is necessary in some improved RANSAC algorithms to eliminate the error-matching pairs. Moreover, a full variate Gaussian model-based RM-MEDA without clustering process (FRM-MEDA) is presented to solve the established multi-objective model. FRM-MEDA only requires a few iterations to find out a correct model. FRM-MEDA can not only greatly reduce the computational overhead but also effectively decrease the possibility of false registration. The proposed MO-IRM is compared with RMMEDA, NSGA- $\square$ and the RANSAC based registration algorithm on the Dazu grottoes image database. The experiment results demonstrate that the proposed method achieves ideal registration performances on both two images and multiple images, and greatly outperforms the compared algorithms on the runtime.

Keywords: Multi-objective Optimization, Full variate Gaussian Model, Estimation of Distribution Algorithm, Image Registration, RANSAC

## 1. INTRODUCTION

Image mosaic method has become popular in the fields of image processing, computer vision and computer graphics so far. Feature based mosaic methods include five steps: feature extraction, feature description, feature matching, model estimation and image fusion. The first four steps are referred as image registration. Image registration has a significant impact on the performance of image mosaic and thus is the key and core of image mosaic.

For image registration, feature extraction, feature description and feature matching have been widely explored but the model estimation is not studied well. Generally speaking, there are many inevitable mismatching feature points in the feature matching step.

[^0]PRang Zhang College of Computer Science, Chongqing Univ. Chondqing 400044, China $+8613594000667$ chenziyu@cqu.edu.cn

## Hang Zhang

College of Computer
Science, Chongqing Univ.
Chongqing 400044, China
+86 13594000667
328444597 @qq.com

If the transformation model is directly fit to the raw feature data set, we will get great deviation or incorrect transformation parameters. Random sampling consensus (RANSAC) [1] is the most popular algorithm to apply a transformation model into the data set of feature points by dividing the points into inliers and outliers. This algorithm has been used to estimate the homography and the fundamental matrix to match two images with wide or short baseline.

The advantages of the RANSAC algorithm are its reliability, stability and accuracy. However, the conventional RANSAC algorithm also faces several challenges. RANSAC becomes computationally expensive when the number of feature points (data set) from large-size input image is large. On the other hand, the high error-matching ratio caused by the large number of iterations before finding a correct model always increases the possibility of false registration [2-4]. In recent years, researchers have made great efforts to address these shortcomings. These studies can be divided into two general categories. One category is to optimize the process of model checking. Specifically, pre check is applied to check the model on a portion of the data before checking it on the whole data set [5-7]. Another category is to discover or modify the sampling process to generate more efficient hypothesis [8-9]. A summary about the comparison between RANSAC and its variants given by Zhao et al. indicates that these strategies show promise but are ineffective in both accuracy and computing time [4].

To address these drawbacks, a novel multi-objective optimization-based image registration method is presented in this paper, named MO-IRM, where a multi-objective optimization based estimation model is built to depict the feature data set and a full variate Gaussian model-based RM-MEDA without clustering process (FRM-MEDA) is applied to solve the multi-objective model. The contribution of the MO-IRM in image mosaic algorithms is illustrated by Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. The contribution of the MO-IRM to image mosaic algorithms
As seen in Figure 1, we transform the traditional image mosaic algorithm into a multi-objective optimization one.


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from Permissions@acm.org.
    GECCO '16, July 20-24, 2016, Denver, CO, USA
    (C) 2016 ACM. ISBN 978-1-4503-4206-3/16/07... $\$ 15.00$.

    DOI: http://dx.doi.org/10.1145/2908812.2908931

In addition, we apply the proposed MO-IRM into the Dazu Rock Carvings, a world-famous site of grottoes culture in China, for establishing a virtual panorama museum of the Dazu Rock Carvings and also demonstrating its performance.
The rest of this paper is organized as follows. Section 2 detailedly describes the multi-objective optimization based estimation model and it's solving method, FRM-MEDA. The proposed MO-IRM is presented in Section 3. Section 4 gives the experimental results and analysis of MO-IRM in comparison with other algorithms on the Dazu grottoes image database. Finally, Section 5 concludes the paper.

## 2. MULTI-OBJECTIVE ESTIMATION MODEL AND ITS SOLVING METHOD

In this Section, a multi-objective optimization based estimation model is proposed to describe the data set without pre checking process and a full variate Gaussian model-based RM-MEDA without clustering process, FRM-MEDA, is presented to reduce the number of iterations and improve the performance of image registration.

### 2.1 Multi-objective estimation model

The aim of establishing multi-objective optimization based estimation model is to find the transformation matrix called homography matrix ( $H$ for short) here. Accuracy and robustness are the two important indicators to evaluate $H$. Therefore, to insure the accuracy of the transformation matrix, one objective of the multiobjective model is to minimize the mean distance $\bar{d}$ between the obtained Hand the corresponding data set. The first objective can be formulated as:
$\operatorname{minimize} f_{1}(\mathrm{X})=\bar{d}(H, P)$
As for the robustness of the transformation matrix, we introduce the inliers and outliers inspired by the RANSAC to divide the data set into two parts. The transformation matrix containing more inliers is a more robust model when the mean distance $\bar{d}$ is given. In order to improve the robustness of the transformation matrix as far as possible, the second objective of the multi-objective model is to minimize the threshold distance $d_{T}$ which can maximize the number of inliers on the basis of the given $\bar{d}$. The corresponding formulation is presented as:
$\operatorname{minimize} f_{2}(\mathrm{X})=\arg \max \left(N_{i n}(\bar{d} ; \bar{d})\right)$
In formulation (2), $N_{i n}$ is the function of $d_{T}$ to count the number of inliers. The $N_{i n}$ is affected by the $\bar{d}$ in $f_{l}$.

According to the previous analysis, we think that two objectives are necessary and enough to estimate the transformation matrix. Thus, the proposed multi-objective optimization based estimation model can be formulated as follows:
$\operatorname{minimize} F(\mathrm{X})=\left(f_{1}(\mathrm{X}), f_{2}(\mathrm{X})\right)^{T}$
subject to $\mathrm{X}=\left(x_{1}, x_{2}, \ldots x_{n}\right) \in S$
In the model, we have 2 objectives $f_{1}(\mathrm{X}): R^{n} \rightarrow R$ to be minimized simultaneously. The decision variable vector X belongs to the feasible region $S$.

### 2.2 Solving method: FRM-MEDA

The estimation of distribution algorithm (EDA) is used to solve the multi-objective model. EDA was originally formed in 1996 and developed rapidly [10-13]. It has become a hotspot in the research field of evolutionary computation and used to solve many engineering MOPs [10]. EDA provides a novel macroscopical evolutionary paradigm in which an explicit probabilistic distribution model is built to describe the movements of population and the population then evolves by iteratively learning and sampling the built model.

A regularity model-based multi-objective estimation of distribution algorithm (RM-MEDA) is an excellent multi-objective estimation of distribution algorithm proposed in recent years [11]. However, the performance of the RM-MEDA is seriously affected by its clustering process. In order to avoid the influence of the clustering process, this paper presents a novel full variate Gaussian model-based RM-MEDA without clustering process (FRM-MEDA) to solve the multi-objective model. In FRM-MEDA, the clustering process is removed from the original algorithm and the full variate Gaussian model (FGM) is introduced to keep the population diversity and make up the loss of the performance caused by removing the clustering process.

To solve the multi-objective optimization based estimation model using FRM-MEDA, we refer to the data set as the population and every transformation models as the individuals. On the basis of EDA, the data can be described by the probability model and transformation model can be estimated by sampling the built model. Assume that $(\mathrm{x}, \mathrm{y})$ is the coordinate of a point in the first image, and $\left(x^{\prime}, y^{\prime}\right)$ is the coordinate of its corresponding point in the second image. The first image will undergo perspective transformation to coordinates of the second image. The perspective transformation can be written in matrix form as:

$$
\left[\begin{array}{c}
x^{\prime} \\
y^{\prime} \\
1
\end{array}\right]=\left[\begin{array}{lll}
h: & h: & h: \\
h s & h: & h s \\
h: & h: & 1
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
1
\end{array}\right]
$$

The above-mentioned matrix is called homography matrix in which we need get all the eight unknown parameters $\mathrm{h}_{1}-\mathrm{h}_{6}$. As seen in the homography matrix, there are nine parameters in total. Therefore, each variable in EDA is set to nine dimensions and each dimension corresponds to a parameter in the homography matrix. The variable is given as:

$$
x=\left(h:,, h:,, h:,, h:,, h:,, h:,, h:,, h_{4}, 1\right)
$$

Under the variable description, the unknown parameters of perspective transformation are obtained by using the FRM-MEDA.

## 3. MO-IRM: THE PROPOSED METHOD

The whole process of MO-IRM can be summarized as follows: firstly, SIFT is used to obtain the matched feature points of these images after reading two or more image; secondly, a multi-objective optimization based estimation model is built to describe the matched feature points; and next, the FRM-MEDA is applied to solve the model and then get the transformation matrix for image registration; finally, we fuse the aligned images to get the stitched image. The proposed method MO-IRM works as follows:
![img-1.jpeg](img-1.jpeg)

Figure 2. The framework of the proposed MO-IRM within image mosaic algorithm

Next in this section, the multi-objective optimization algorithm FRM-MEDA is presented in details. Firstly, the normal distribution of FGM is given by Formula (6):

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\frac{1}{(2 \pi)^{n / 2}|\Sigma|^{1 / 2}} \exp (-1 / 2(x-\mu)^{T} \Sigma^{-1}(x-\mu))
$$

Where $X=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is the population of each generation, $\mu$ and $\Sigma$ are the free model parameters and the $\Sigma$ can be calculated as
$\Sigma=\left[\begin{array}{ccc}\sigma_{11} & \ldots & \sigma_{1 n} \\ \vdots & \ddots & \vdots \\ \sigma_{n 1} & \ldots & \sigma_{n n}\end{array}\right]$
By bringing FGM into RM-MEDA, we propose the FRM-MEDA shown as Algorithm 1:

## Algorithm 1. FRM-MEDA procedure

Step 0 Initialization: Set $t=0, K=1$. Create an initial population $P_{0}$.
Step1Modeling: Establish the probabilistic model by the ( $m-1$ )-D local PCA and select elitist solutions ( $10 \%$ of the solutions in the paper) to build the FGM for estimating the distribution of the candidate solutions in $P_{T}$.
Step 2Sampling: Create the offspring population $Q_{i, t}$ by sampling the ( $m-1$ )-D PCA and $Q_{i, t}$ by sampling the FGM. Calculate the fitness value of each candidate solution in $Q_{i, t}$ and $Q_{i, t}$.
Step 3 Selection: Select $N$ solutions from $Q_{i, t}, Q_{i, t}$ and $P_{T}$ to create the population $P_{T}+I$ for the next generation.
Step4StoppingCondition: If the stopping criterion is met, stop and return the fitness vectors of the nondominated solutions of the obtained population, otherwise set $t=t+1$ and then go to Step 2.

The framework of FRM-MEDA is given as Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The general framework of FRM-MEDA
In the FRM-MEDA, the cluster number, $K$, is fixed at 1 during the evolution. The steps of modeling, sampling and selection related to ( $m-1$ )-DPCA are the same as in RM-MEDA. Additionally, $10 \%$ of the solutions based on non-domination sorting in the population are selected for building FGM. Sampling FGM is to generate a random sequence $x$ and $x \sim(\mu, \Sigma)$.

After getting the final population by FRM-MEDA, the unique solution for image registration is selected from the final solutions as follows: firstly, calculate the distance of
solutions between each other; secondly, choose the nearest two solutions and then calculate their average solution. Hence, the average solution is used as the final unique solution for image registration process.

## 4. EXPERIMENTAL STUDY

Listed as a World Heritage Site, the Dazu Rock Carvings are made up of 75 protected sites containing some 50,000 statues, with over 100,000 Chinese characters forming inscriptions and epigraphs. A virtual museum needs to be established to show the panoramic image of Dazu Stone Carvings. The proposed MO-IRM, NSGA- II [17], RM-MEDA [11], and RANSAC [1] based registration method are applied to the Dazu grottoes images registration. The modeling and sampling methods are implemented using the Matlab toolbox for EDAs (MatEDA) [15].

### 4.1 Experimental setting

Before giving the experiment results, the several parameters of MOIRM, RM-MEDA and NSGA- $\square$ need to be determined. First of all, the dimension of variable is set as 9 to fit the size of homography matrix that own 9 parameters. By comparison, the matching threshold is set as the value 0.6 given in RANSAC. The population size and the iterations must be determined experimentally based on two evaluation indicators GD [16] and $\Delta$ [17]. The selectable ranges of the two parameters are $4-10$ (even number only) and $2-5$, respectively.

The GD is employed for measuring the convergence quality. The generational distance between P and $P^{*}$ is defined by the formula (9):

$$
G D=\frac{\sqrt{\sum_{i=1}^{N} d\left(P_{i}, P^{*}\right)^{2}}}{|P|}
$$

Where $d\left(P i, P^{*}\right)$ denotes the minimum Euclidean distance of $P_{i}$ to $P^{*}$. GD shows the mean distance of the points in an approximation to the true PF. The specific data of the performance indicator GD and its statistical results are shown in Table 1. "Mean GD" and "Std Dev" represent the mean and standard deviation of GD in 20 independent runs.

The $\Delta$ metric is proposed to measure solution diversity. The $\Delta$ metric can be described as follows:

$$
\Delta=\frac{d_{f}+d_{i}+\sum_{j}^{N}\left|d_{i}-\bar{d}\right|}{d_{f}+d_{i}+(N-1) d}
$$

Where $N$ is the population size, $d_{f}$ and $d_{i}$ are the distances of the extreme solutions that need to be calculated firstly by adjusting a curve parallel to that of the PF. The specific data of the performance indicator $\Delta$ and its statistical results are shown in Table 2. "Mean $\Delta$ " and "Std Dev" represent the mean and standard deviation of $\Delta$ in 20 independent runs.

To get a better look at the results of GD and $\Delta$, the line charts related to Table 1 and Table 2 are given as Figure 4. As seen from Table 1, Table 2 and Figure 4, the MO-IRM obtains the best and the most stable performance when the size of population and the iterations are set as 4 and 4 , respectively.

### 4.2 Two images registration

After discussing all the parameters for the proposed method, we compose images into one big image to observe the registration results of the MO-IRM, RANSAC, RM-MEDA and NSGA- II. The matching results of feature points are ignored here since nothing is done in the matching process in this paper. Firstly, the image

registration experiment is conducted with two images obtained in the same situation. Figure 5 shows that the stitched images obtained by all the algorithms are both smooth and seamless. In this case, the fusion process can be ignored during image mosaic.

However, for images taken under different situation, the registration results of these four algorithms are different. Images (a) and (b) in Figure 6 are all different in resolution, illumination and view of the camera. Obviously, the stitched image (c) is much better than (d), (e) and (f). In image (c), the registration result is acceptable even though there are still some flaws like the mis-alignment in the eye of the Buddha. As can be seen from the red circles in image (d), (e) and (f), only a few parts of the registration result are acceptable. Thus, the proposed MO-IRM is superior to RANSAC, RM-MEDA and NSGA- II.

### 4.3 Multiple images registration

Here, we will make some attempts in multiple image registration. Firstly, we choose one image with the biggest correlation with other images as the referenced image and calculate the number of matching point-pair (NOMP for short) between the referenced image and the rest successively. Secondly, an ascending sorted table about NOMP named priority table is made out to guide the multiple image registration. To some extent, the ascending sort can improve the registration accuracy. Then, the two images with the highest priority are registered. The two images are aligned to generate a larger view of the referenced image. Next, registration between the stitched image and new images are carried out one by one according to the priority table. What should be noted here is that the new image is jointed to the referenced image after every round of registration. The flowchart of the registration steps is given in Figure 7.

Table1. The "Mean GD $\pm$ Std Dev" of different population sizes and the iterations
Table2. The "mean $\Delta \pm$ Std Dev" of different population sizes and the iterations
![img-3.jpeg](img-3.jpeg)

Figure 4. The line charts of GD (a) and $\Delta$ (b) in Table 1 and Table 2
![img-4.jpeg](img-4.jpeg)

Figure 5 Continued

![img-5.jpeg](img-5.jpeg)

Figure 5. (a) and (b) are two input images obtained under the same situation. (c) (f) are aligned images of the proposed MO-IRM, RANSAC, RM-MEDA and NSGA-, respectively.
![img-6.jpeg](img-6.jpeg)

Figure 6 Continued.

![img-7.jpeg](img-7.jpeg)

Figure 6. (a) and (b) are two input images obtained under different situations. (c) - (f) are aligned images of the proposed MO-IRM, RANSAC, RM-MEDA and NSGA- $\square$, respectively.
![img-8.jpeg](img-8.jpeg)

Figure 7. The flowchart of multiple images registration
The following experiment is carried out and tested on multiple images taken under various conditions. As can be seen in Figure 8, there four images need to be aligned. Table 3 is the priority table of these images.

Table 3. Priority table

Table 3 shows that image (a) is chosen as the referenced image. Then multiple images registration is carried out following the flowchart in Figure 7. As shown in Figure 8, (e-1) and (e-2) are the two intermediate registration results, and (e-3) is the final registration result. It is clearly observed that the result of multiple images registration is also very good. The defects in the intermediate results like (e-1) can be amended in the further registration.

The runtime is also an important performance metric in image registration. Table 4 and Figure 9 show the runtimes of the multiobjective optimization process in comparison to the corresponding time for RANSAC to estimate the homography matrix. "Mean t" and "Std Dev" represent the mean and standard deviation of the runtimes in 20 independent runs. NOFP and NOMP stand for the number of the feature point obtained by SIFT and the number of matching point-pair.

Table 4 and Figure 9 indicate that the proposed MO-IRM and the RM-MEDA require a similar and minimum of time for model estimation in image registration process. Compared with RANSAC, the increasing time along with the number of feature points is not so obvious in the model estimation process of MO-IRM and RMMEDA. Although it decreases the runtime, NSGA- $\square$ is still need more time than MO-IRM and RM-MEDA.

![img-9.jpeg](img-9.jpeg)

Figure 8. (a),(b),(c) and (d) are input images obtained different situations. (e) Aligned images. (e-1) is the registration result of (a) and (d); (e-2) is the registration result of (e-1) and (c); (e-3) is the registration result of (e-2) and (b).

Table4. The "mean $\mathbf{t} \pm$ Std Dev" of model estimation process
![img-10.jpeg](img-10.jpeg)

Figure 9. The "mean $\mathbf{t} \pm$ Std Dev" of model estimation process

## 5. CONCLUSION

This article presents a novel image registration method based on the multi-objective optimization. Firstly, the model estimation process of image registration is transformed into a bi-objective optimization problem. The first objective is to insure the accuracy and the other is to enhance the robustness of the transformation matrix. To solve the model, a full variate Gaussian model-based RM-MEDA without clustering process is proposed.

The grottoes images from the world-renowned Dazu Stone Carvings in China are used as the image database of the registration experiments. The experimental results show that the proposed MOIRM can obtain great performances on the registration of Dazu grottoes images taken under both the same situation and different situation. Meanwhile, the use of FRM-MEDA greatly reduces the number of iterations, which makes the MO-IRM robust and efficiency to find the optimal homography matrix.

For the sake of practical project, a multiple images registration flowchart is given in the paper. A priority table is produced based on the number of feature matching pairs to guide the registration process. The registration results demonstrate that the proposed multiple images registration flowchart is entirely feasible.

## 6. ACKNOWLEDGMENTS

This work is supported by the Chongqing University Postgraduates' Innovation Project with no.CYS14018 and the Project of Science and Technology for Graduate Students with no.CDJXS12180003.
