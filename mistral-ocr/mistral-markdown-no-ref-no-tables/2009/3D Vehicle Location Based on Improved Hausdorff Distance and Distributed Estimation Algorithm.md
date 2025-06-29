# 3D Vehicle Location Based on Improved Hausdorff Distance and Distributed Estimation Algorithm 

Ying Chen, Zhicheng Ji<br>Institute of Electrical Automation Jiangnan University<br>Wuxi, China<br>\{chenying, zcji\}@jiangnan.edu.cn


#### Abstract

3D model is used for vision based vehicle location. An improved Hausdorff distance based on edge-strength is proposed to evaluate the similarity between 3D model projection and image feature, and to establish location optimization function In order to avoid local minimum during optimization, estimation of distribution algorithm concerning related multi-variables is used. The relationship between matching parameters are described with a probability model, and the distribution of parameter evolves towards the direction of dominant character through probability model learning and the corresponding operation, which is proposed to solve the problem of overmany iteration and slow constringency velocity. The experiments show that the optimal matching parameters between 3D model and 2D image feature can be found accurately and efficiently, and the algorithm outperforms other approaches in both accuracy and rapidity.


Key words - object location; image matching; distributed estimation; optimization algorithm

## I. INTRODUCTION

The localization of three-dimensional (3D) objects from single monocular intensity image is principle in vision-based traffic surveillance system, and is also one of the fundamental problems in image analysis and computer vision. The key of localization is to establish the correspondence relationship between object image and model projection. Traditional algorithms ${ }^{[1]}$ have involved an initial stage of extracting features from 2D image, and localization is then achieved by establishing a match between sets of 2D image features and 3D model, which are error-prone and time-consuming, and are very difficult to be applied on line.

In [2], Tan et al. used Point-to-Line-Segment Distance (PLS Distance) to obtain translation parameter of localization, while the rotation parameter is determined by geometric change

[^0]of angle which constituted by image projections of arbitrary three points which do not lie in the plane parallel to Ground Plane (GP). Therefore, the method need search the image pixels corresponding to the points on model projection lines, which requires model initial pose should be close to the correct one, or matching result would be heavily affected.

An accurate 3D vehicle localization method is proposed, combining weighted Hausdorff distance with multi-variable estimation of distributed algorithm. The weighted Hausdorff distance, whose weights are determined by edge strength, is used to establish matching function between 2D image feature and 3D model projection. A probability model is used to model the optimal solution in matching space, which leads to accurate matching parameters for localization.

## II. HAUSDORFF DISTANCE BASED ON EDGE STRENGTH

## A. Hausdorff distance and its modification

Given two finite point sets $\boldsymbol{M}=\left\{m_{1}, m_{2}, \cdots, m_{p}\right\}$, $\boldsymbol{T}=\left\{t_{1}, t_{2}, \cdots, t_{q}\right\}$, the Hausdorff distance is defined as

$$
H(\boldsymbol{M}, \boldsymbol{T})=\max (h(\boldsymbol{M}, \boldsymbol{T}), h(\boldsymbol{T}, \boldsymbol{M}))
$$

in which

$$
h(\boldsymbol{M}, \boldsymbol{T})=\max _{m \in M} \min _{m T}||m-t \|, h(\boldsymbol{T}, \boldsymbol{M})=\max _{m T} \min _{m \in M} \| t-m \|
$$

and $\left\|_{0}^{2}\right\|$ is the Euclidean norm of the points $m_{i}$ and $t_{j}$. The function $h(\boldsymbol{M}, \boldsymbol{T})$ is called the directed Hausdorff distance from $\boldsymbol{M}$ to $\boldsymbol{T}$. It identifies the point $m_{i} \in \boldsymbol{M}$ that is the farthest from any point of $\boldsymbol{T}$ and measures the distance from $m_{i}$ to its nearest neighbor in $\boldsymbol{T}$. The Hausdorff distance $H(\boldsymbol{M}, \boldsymbol{T})$ is the maximum of $h(\boldsymbol{M}, \boldsymbol{T})$ and $h(\boldsymbol{T}, \boldsymbol{M})$. Thus, it measures the degree of mismatch between two sets by measuring the distance of the point of $\boldsymbol{M}$ that is farthest from any point of $\boldsymbol{T}$, and vice

[^1]
[^0]:    Sponsors: China Postdoctoral Science Foundation (No. 20080430161), Jiangsu Postdoctoral Science Foundation (No. 0801008B)

[^1]:    (C) computer

versa.
HD defined in (1) relies on the distance between one point set to the worst point of another point set, which makes it sensitive to outlier points. Dubuisson and Jain ${ }^{[3]}$ investigated 24 forms of different Hausdorff distance measures and indicated that a modified Hausdorff distance measure has the best performance. The directed MHD is defined as

$$
h_{M H D}(\boldsymbol{M}, \boldsymbol{T})=\frac{1}{P} \sum_{m_{i} \in M} \min _{\left.t_{i} \in T^{\prime}\right]}\left\|m_{i}-t_{j}\right\|
$$

where $P$ is the number of points in $\boldsymbol{M}$.
In [4], MHD is modified and employed to match dominant points rather than binary pixels. Dominant point representation is more computationally efficient and more noise tolerant than binary image matching. A new Modified Hausdorff Distance $\left(\mathrm{M}^{2} \mathrm{HD}\right)$ is proposed by introducing the weight value of each dominant point into the computation of the Hausdorff distance. The directed $\mathrm{M}^{2} \mathrm{HD}$ is defined as

$$
h_{M^{2} H D}(\boldsymbol{T}, \boldsymbol{M})=\frac{1}{\sum_{t_{i} \in T} w_{t_{i}}} \sum_{t_{i} \in T} w_{t_{i}} \min _{\left.t_{i} \in M\right]}\left\|_{j}-m_{i}\right\|
$$

where $w_{t_{i}}$ denotes the merit of point $t_{i}$. When $t_{i}$ is edge point, the value of $w_{t_{i}}$ is large. Otherwise, $w_{t_{i}}=1$ (or delete $t_{i}$ from $T$ to save computation cost).

In (4), the determination of weight is principle, which definitely affects the accuracy of model matching. The problem is solved by an edge strength based weight computation method that is helpful to improve the accuracy and speed of the algorithm.

## B. Weight computation

Image edges are fundamental in shape-based object location and recognition. In this paper, canny is used for edge point extraction, then a modified 8 -connection edge tracking algorithm is used for edge curve extraction. Based on that, parameters of each edge curve are computed, which finally determine the weight of each edge.

## 1) Modified edge tracking

Compared with other methods for edge extraction, canny operator has better performance on SNR (Signal noise ratio), location accuracy and uniqueness ${ }^{[5]}$. So it is adopted to extract edge points. In order to describe the edge feature, an edge tracking algorithm is used to obtain object edge curve. Different from general closed edge extraction method, the presented one considers the starting and terminal points of each curve. The modified edge tracking algorithm is described as follow:
a) Use canny operator to compute the gradient of each pixel in $f, 0 \leq f(i, j) \leq 1$. An edge binary image is obtained by gradient thresholding, in which the gray value of object is 1 .
b) Scan the binary image from up to bottom and from left to right.
c) Scan and search for object points in the 8 -neighbor of the current pixel if its value is 1 . Once an object point is found,
break out the 8 -neighbor scan. Record the object point number of neighbor ( 0 or 1 ) and the coordinate of the point $\left(x_{i}, y_{i}\right)$.
d) If the object point number of neighbor is 0 , that means the current pixel is a terminal point of an edge curve. Set the value of the current pixel to 0 to avoid repeat scan, set terminal flag to 1 and turn to (6); else turn to (5).
e) If the starting flag is 0 , set it to 1 . Put the current pixel to the chained list, and set the value of current pixel to 0 to avoid repeat scan; if the starting flag is 1 , put the current pixel to the chained list, set the value of current pixel to 0 , and take neighbor pixel as current pixel.
f) If the terminal flag is 0 , turn to (3); else turn to (2), until scan is completed.

## 2) Weight computation based on edge strength

Edge strength computation should consider three aspects, i.e, edge length, edge gradient and edge completeness.
a) Edge length $L$ : The number of pixels in edge chained list. The longer is the edge length, the bigger is the portion of the edge in the whole edge image. That means its function on edge-based object localization is more important, and its corresponding weight should be larger.
b) Edge gradient $G$ : The average gradient of pixels in edge chained list. The larger is the gradient, the more obvious is the abrupt change of the pixel. That means it is more likely to be the object edge, and its weight value should be larger.
c) Edge completeness $B$ : This is the closet degree of the edge, and is denoted by central angle of the circle fitted by pixels of the edge. As illustrated in Fig. 1, the circle is fitted using square law fitting ${ }^{[6]}$, and the central angle formed by edge starting point and its terminal point reflects the closet degree of the edge. The bigger is the angle, the closer is the edge to a closed curve. When the central angle is $360^{\circ}$, the edge curve is a closed one.

As to any curve $i$, its edge strength $S_{i}$ obtained by considering the above three points:

$$
S_{i}=L_{i} * G_{i}+B_{i}
$$

Then the weight of the edge is:

$$
w_{i}=S_{i} / \sum_{i=1}^{M} S_{i}
$$

where $M$ is the number of the edge curve. In order to improve the speed of the location, the curve quits the location matching when its corresponding weight is less than a fixed threshold which is usually $0.05-0.2$.
![img-0.jpeg](img-0.jpeg)

Figure1. Edge fitting and central angle

## III. OPOTIMIZATION BASED ON ESTIMATION OF DISTRIBUTION ALGORITHMS

In this section, we present a novel optimization approach called EDA and show how to use this approach on recovering pose parameters of vehicle models.

EDAs (Estimation of Distribution Algorithms) were first introduced in evolutionary computation by $\mathrm{M}^{\prime \prime}$ ulenbein and Paaö in [7]. Unlike Genetic Algorithms, neither crossover nor mutation operators are necessary in EDAs. Instead, it samples a new population of individuals from a probability distribution, which is estimated from a database containing selected Individuals of the previous generation. The interrelations between variables are explicitly expressed through a joint probability distribution. The differences between genetic algorithm and EDA are illustrated in Fig. 2.

There are several Estimation of Distribution Algorithms. Here we choose a specific continuous EDA approach called EMNA $_{\text {global }}$ (Estimation of Multivariate Normal Algorithm -global) ${ }^{[8]}$. In this approach, the joint distribution of parameters is assumed to be a multivariate normal distribution and the weighted hausdorff distance is used as a criteria for choosing better individuals. The flow of EMNA $_{\text {global }}$ is as follows:

1) Generate $M$ individuals as original generation $D_{i} D_{i}$, $l=0$;
2) If terminal condition is met, end the algorithm, else turn to (3);
3) Select $N<M$ individuals as priority to produce new generation $D_{i}^{N}$;
4) Assumed the joint distribution of parameters is a multivariate normal distribution. Probability model $f_{j}(x)$ is
![img-4.jpeg](img-4.jpeg)

Figure 2. Difference between generic algorithm and EDA
established with new priority generation $D_{i}^{N}$ :

$$
f_{j}(x)=f\left(x \mid D_{i}^{N}\right)=\mathrm{N}\left(x ; \hat{\mu}_{j}, \hat{\Sigma}_{j}\right)
$$

where

$$
\begin{gathered}
\hat{\mu}_{j}=\left\{\hat{\mu}_{j, j}, i=1,2, \ldots . n\right\}=\left\{\frac{1}{N} \sum_{i=1}^{N} x_{i, r}^{j}, i=1,2, \ldots . n\right\} \\
\hat{\Sigma}_{j}=\left\{\hat{\alpha}_{i j, j}^{2}\right\}=\left\{\frac{1}{N} \sum_{i=1}^{N}\left(x_{i, r}^{j}-\hat{\mu}_{j, j}\right)\left(x_{j, r}^{i}-\hat{\mu}_{j, j}\right), i, j=1,2, \ldots . n\right\}
\end{gathered}
$$

where $n$ is the number of the variable in objective function.
5) Sample $M$ new individuals according to the estimated probability model, generate new generation, and return 2).

The terminal condition of the algorithm include three, i. e, loop times exceeds a threshold, the difference of function value between two sequential generations are less than a threshold, or variance value of each parameter in probability model is less than a threshold, which means the difference between current individuals is litter, and corresponding function value is close to the global optimal one.

## IV. EXPERIMENTAL RESULTS

3D Wire-frame model is illustrated in Fig. 3(a), and object for location is shown as Fig. 3(b) in which region of interest (ROI) obtained by an adaptive window algorithm ${ }^{[9]}$ is in the rectangle. According to GPC (Ground Plane Constrain), the location parameter is $(x, y, \alpha)$, in which $(x, y)$ is translation of the two directions, and $\alpha$ is the orientation of the vehicle ${ }^{[9]}$.
![img-4.jpeg](img-4.jpeg)
(a) 3D model
(b) Object image for location

Figure 3. 3D model and object image
![img-4.jpeg](img-4.jpeg)
(c)
![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)
(a) edge before weighting process
(b) edge after weighting process

Figure 5. Edge image before and after weighting process
![img-6.jpeg](img-6.jpeg)
(b) final pose

Figure 6. Pose evolution during localization
The evolution process of localization is illustrated in Fig. 4, the edge image before and after weighting process is illustrated in Fig. 5, and model pose in different evolution stage is illustrated in Fig. 6. From Fig. 5, it is clear that the weight process can not only eliminate the disturbance of the background noises, but also reduce the data quantity, which help to improve the location speed.

Table 1 shows the comparison between traditional and improved Hausdorff distance. It is clear that the performance of the proposed algorithm is better than traditional one in both location accuracy and evolution convergence speed.

In order to test the optimization performance of the EDA, 30 frame of object image with different pose are used for testing. Table 2 shows the comparison between simulated annealing algorithm (SAA) and EDA. It is not surprising that the EDA outperforms SAA in both accuracy and speed.

Table 1 COMPARISON BETWEEN TRADITIONAL AND IMPROVED HAUSDORFF DISTANCE

Table 2 PERFORMANCE COMPARISON BETWEEN TWO ALGORITHMS

## V. CONCLUSION

Recognition based on 3D model is robust to the variation of pose, scale and illumination. A weighted improved Hausdorff distance for matching function is presented in order to cover the shortage of traditional one to background noise, and the weight computation method based on three factors affecting edge strength is also proposed. An EDA is combined with improved Hausdorff distance to avoid local minimum, which use probability model to describe the relationship between location parameters, and the accurate parameters can be found according to evolution process of priority samples.
