# Quantitative optimization of interoperability during feature-based data exchange 

D.J. Zhang ${ }^{\mathrm{a}}$, F.Z. He ${ }^{\mathrm{a}, *}$, S.H. Han ${ }^{\mathrm{b}}$ and X.X. $\mathrm{Li}^{\mathrm{c}}$<br>${ }^{a}$ School of Computer Science and Technology, Wuhan University, Wuhan, Hubei, China<br>${ }^{\mathrm{b}}$ Division of Ocean Systems Engineering, Korea Advanced Institute of Science and Technology, Daejeon, Korea<br>${ }^{\text {c }}$ College of Science, Huazhong Agricultural University, Wuhan, Hubei, China


#### Abstract

Sharing feature-based computer-aided design (CAD) models is a challenging problem that is frequently encountered among heterogeneous CAD systems. In this work, a new asymmetric strategy is presented to enrich the theory of feature-based interoperability, particularly when addressing a singular feature or singular sketch. This paper analyzes the semantic asymmetry singular feature interoperability (SA-SFI) and parameter asymmetry singular sketch interoperability (PA-SSI) in detail. We pay special attention to the problem of PA-SSI, which is universally significant in collaborative product development (CPD). The objective of PA-SSI is to develop an optimized model to exchange a singular sketch (spline) to ensure that the exchanged model both maintains high geometric fidelity and can be effectively edited in the target CAD system. The proposed method applies the estimation of distribution algorithm (EDA) to automatically solve this problem, and a Gaussian mixture model (GMM) is built according to the promising solutions. Furthermore, Hausdorff distance is adopted to calculate the fitness, and a local optimization operator is designed to enhance the global search capability of the population. Experimental results demonstrate that the proposed approach can maintain a sufficiently high geometric fidelity, and ensure that the exchanged model of the target CAD system can be parametrically edited.


Keywords: CAD/CAE, feature-based data exchange, interoperability, estimation of distribution algorithm, hausdorff distance, performance evaluation

## 1. Introduction

With the development of economic globalization, CPD (Collaborative Product Development) has become state of the art method in developing product, which involves process simulation and CAD (Computer-Aided design)/CAE (Computer-Aided Engineering) systems $[76,79,80]$.

Collaboration helps individual users and companies to manage, share and view CAD projects without the cost and complexity of purchasing an entire PDM (Product Data Management) or PLM (product lifecycle management) solution. It makes more companies in the supply chain specialized, and also enhances cor-

[^0]poration among involved companies which are located in different areas through dynamic alliance.

Design reuse is particularly important in engineering applications because many common subparts of different CAD models are reused [13,81]. It is estimated that approximately $80 \%$ of designs are variant and/or adaptive designs [28]. Because of the differences in history development and cultural background, different companies often adopt different CAD systems to develop products. Even within a company, designers apply different CAD systems because of the differences among the different design domains and stages. Therefore, establishing a CSCW (Computer-Supported Cooperative Work) based CAD system [27,36] and applying interoperability among heterogeneous CAD systems have become inevitable technological problems. The interoperability among heterogeneous CAD systems is a challenge for both industrial and academic fields, which includes two keys points:

ISSN 1069-2509/16/535.00 (c) 2016 - IOS Press and the author(s). All rights reserved
This article is published online with Open Access and distributed under the terms of the Creative Commons Attribution Non-Commercial License.


[^0]:    *Corresponding author: F.Z He, School of Computer Science and Technology, Wuhan University, Wuhan, Hubei, China. E-mail: fzhe@whu.edu.cn.

- How to ensure that the exchanged model maintains a high geometric fidelity.
- How to ensure that the exchanged model can be effectively edited in the receiving CAD system.
Feature-based interoperability among heterogeneous CAD systems is a hot topic in the study of CPD. However, some of the well-known methods, which are reviewed in Section 2, still lack the ability to exchange a singular feature or singular sketch (See Definitions 8 and 14). And a singular feature or singular sketch is replaced (such as "rewrite method" of UPR in [64-66]) with its geometry representation. Therefore the target users who receive the model must work with 'frozen model' [16], and the original intent from source designers cannot be understood by target users. A new asymmetric method of the semantic asymmetry singular feature interoperability (SA-SFI) and the parameter asymmetry singular sketch interoperability (PA-SSI) is presented to overcome this limitation in this paper.

This paper focuses on analyzing the singular sketch of the interoperability problem and also on establishing a relevant optimization model. Then, the estimation of distribution algorithm (EDA) is adopted, and a Gaussian mixture model (GMM) is built according to the selected individual. In addition to applying the Hausdorff distance to calculate the fitness [14,21,41,73], a local optimization operator is designed to enhance the global search capability of the population. A set of experiments have been conducted on both simulated and real test models to validate the effectiveness of the proposed method. The proposed method can maintain a sufficiently high geometric fidelity and ensure that the exchanged model of the receiving CAD system can be parametrically edited. The major contributions and highlights of this paper are as follows:

- A formal method to completely describe featurebased interoperability is adopted.
- An asymmetric strategy for singular feature interoperability is presented.
- An optimization model to tackle typical singularity is introduced.
- Efficient algorithm to recover singular parameters in target CAD system.
- Detailed analysis of the efficiency and accuracy of the proposed algorithm.
The remainder of this paper is organized as follows: In Section 2, the related work is briefly reviewed. Sections 3, 4 and 5 embody the major contributions of this work. Since the issue of feature-based interoperability was not clearly defined in existing literatures,

Section 3 adopts a formal method to completely describe the related definitions and analyze the framework and problems in feature-based interoperability. Section 4 presents a new approach to solve the problems based on asymmetric feature-based interoperability. Section 5 proposed an EDA method which solves the singular sketch of interoperability problem in detail. Section 6 demonstrates and analyzes a series of experiments. Finally, the conclusions of this study are discussed in Section 7.

## 2. Related works

Existing CAD data exchange methods can be divided into two categories [71]: geometry-based data exchange (GBDE) and feature-based data exchange (FBDE).

Currently, among different software packages, GB DE is typically implemented using neutral file formats (IGES [31] or STEP [60]) or proprietary formats without losing the original legacy data archives. To make designers more creative, commercial CAD systems provide the feature-based modeling technique, which is an extension of Constructive Solid Geometry (CSG) [69]. Commercial CAD systems have advanced solid modeling capabilities, so that GBDE cannot satisfy the requirements of CPD because it only exchanges the boundary representation of a model. The design intents, which include the construction history, parameters, constraints, and features, may be lost during the exchange process [23].

The second class of CAD data exchange method, FBDE is desirable because it ensures that the CAD models obtained after exchange are editable and may avoid the geometric tolerance problem of GBDE.

According to the theory of representations for rigid solids [67], the representations of solid modeling are unambiguous and unique, and this mathematically unambiguous theory has constituted the basis of neutral representation standards and centralized architecture for GBDE. The theory indicates the existence of unambiguous representations of geometry although GBDE must consider the precision of the representation and computing of a computer [62,63]. In contrast, most of the modern commercial CAD systems provide a feature modeling technique, but there is no uniform standard on the feature modeling technique. Even if they represent identical geometric effects, the representations of the feature-based parametric modeling are diverse. In other words, there is no unique representation

of feature modeling among heterogeneous CAD systems. This complexity makes it difficult to establish an unambiguous standard for FBDE; thus, the problem of interoperability of a singular feature or singular sketch is more prominent in FBDE.

All modern CAD systems are based on the featurebased design paradigm, also called parametric design and history based design [29]. Hoffmann and Juan [30] proposed a high-level, generative, textual representation for feature based solid modeling, which is called Erep (editable representation, Erep). Erep is a specification for the representation of sequential featurebased design processes. Hoffmann et al. [18-20] also proposed a method of exchanging CAD models in terms of their construction history. Although this work was a theoretical breakthrough, it did not explore the corresponding practical applications.

ISO created the Parametrics Group of Working Group 12 (WG12), which has been led by Pratt in the mid-1990s to conduct the research on ISO-FBDE methods [40,57-59,61]. ISO-FBDE attempts to expand the STEP (Standard for the Exchange of Product) capabilities by adding new parts that support FBDE, such as 10303-55 [32], 10303-108 [33,39], 10303111 [34], 10303-112 [35]. These parts of the STEP standards provide the STEP neutral format for ISOFBDE. Because the representations of feature modeling among heterogeneous CAD systems is not unique; thus, ISO-FBDE made slow progress. Although the Parametrics Group of WG12 was established in 1994, either examples or implemented systems supported by the work results were limited until 2007. Compared to ISO-FBDE, ISO-GBDE (STEP) took about 10 years from the beginning of standardization to be more broadly adopted among the modern commercial CAD systems. Furthermore, the ISO-FBDE method does not specify how to handle singular feature or singular sketch.

The macro-parametric approach [22,23,38,46,54], inspired by the data recovery mechanism of database systems where log files are used for the recovery, is based on the macro information. The macro information is a neutral representation of the modeling commands sequence or modeling history, which is not unique either. Thus, the macro-parametric approach encounters the same problem as ISO-FBDE. The main advantage of the macro-parametric approach is its ability to exchange the design intents, but it cannot exchange singular feature or singular sketch among the heterogeneous CAD systems.

In addition, similar studies have been performed for the parametric exchange of "round shapes" be-
tween a mechanical CAD system and a ship CAD system [45,47]. This paper proposes a method to resolve the problem that occurs when exchanging data between two CAD systems of two different domains: featurebased CAD systems (mechanical CAD systems) and a non-feature-based CAD system (the AVEVA Marine system).

Although the macro-parametric approach enables the mapping among different terminologies with an identical meaning but different syntax, the mapping is performed syntactically, not semantically. To consider the semantic aspect, Seo et al. [68] extended this approach by developing an ontology based on the macroparametric approach to achieve semantic interoperability between feature-based CAD models. In addition, Samer et al. [1] proposed a method to share CAD models based on the construction of a common design features ontology, which also considered semantic interoperability of knowledge in feature-based CAD models.

The universal product representation (UPR) [64-66] presented an improved centralized architecture that is a union of the data types supported by commercial CAD systems instead of their intersection. The contributions of the UPR method are shown in two aspects:

- Union of the data. When creating the neutral feature information, UPR uses a union of the data instead of attempting to find the unambiguous representation, which overcomes a major problem in ISO-FBDE and the macro-parametric approach.
- Feature rewrite. UPR uses a geometric model when the data types cannot be exchanged using only the parametric information, which is a compromise mechanism to prevent the problem from occurring during the interoperability of a singular feature or singular sketch.

The aforementioned studies (ISO-FBDE, macroparametric approach, UPR) focus on the representation of feature modeling, which is the most common issue in FBDE. Another important issue is how to retrieve the modeling process; no efficient method is available for this purpose. Li et al. [48,49] proposed a procedure recovery approach (PRA) method to attempt to resolve this problem; they presented a two-stage mechanism to recover the modeling process of a feature model in the source system and subsequently used the exchange procedure to simulate a human modeler to reconstruct the feature model in the receiving system.

This paper attempts to resolve the problem of interoperability for a singular feature or singular sketch based on the theory of PRA. According to the geome-

try of a singular feature or singular sketch in the source CAD heterogeneous system, the equivalence of geometry of a feature or sketch in the receiving CAD system can be automatically recovered. Com-pared with ISO-FBDE and the macro-parametric approach, this paper specifies the interoperability of a singular feature or singular sketch among heterogeneous CAD systems. Compared with UPR, this paper surpasses the geometry replacement method in which the singular features are replaced with geometry [64-66]. Under the premise of sufficiently high geometric fidelity, the exchanged model of the receiving CAD system can be parametrically edited.

The work in this paper is also related with design automation because the feature-based model in target CAD system is automatically reconstructed. Design automation of one-of-a-kind engineering systems is considered a particularly challenging problem. Adeli and his associates have been working on novel design theories and computational models with four categories: (1) interactive representation systems [4,5,8]; (2) knowledge engineering [2,3,6,55,70]; (3) software engineering [7,10,24]; (4) relational databases [78].

## 3. The theory of feature-based interoperability

### 3.1. Formalization method for feature-based interoperability

Although the research focus of feature interoperation in this paper is different from that of feature-based multi-resolution model in [42,44], this section takes advantage of the formal method to describe the problem.

It is well known that the modeling procedure is a series of operations on features and sketches, but the issue of feature-based interoperability was not clearly defined in existing literatures. According to the characteristic of feature-based interoperability between heterogeneous CAD systems, a set of formal definitions related to feature-based interoperability is provided.

- Definition 1: Feature model. The feature model consists of a series of features (such as: Extrusion, Pocket, Hole and Fillet); the definition is provided as follows:

$$
M=\bigcup_{i=1}^{n} f_{i}
$$

where $M$ describes a CAD feature model and $f_{i}$ is the $i$ th feature in $M$.

- Definition 2: Feature. A feature consists of one or more sketches and the related feature parameters; the definition is provided as follows:

$$
f=\left\{\bigcup_{i=1}^{n} S_{i}, p\right\}
$$

where $S_{i}$ is the $i^{\text {th }}$ sketch in $f$ and $p$ denotes the corresponding parameters related to $f$.

- Definition 3: Sketch. A sketch consists of a series of elements (such as: Line Segment, Rectangle, Circle, Ellipse and Spline) and related constraints (such as: parallelism, symmetry and coincidence); the definition is provided as follows:

$$
S=\left\{\bigcup_{i=1}^{m} s_{i}, \bigcup_{j=1}^{n} c_{j}\right\}
$$

where $S$ describes the sketch, $s_{i}$ is the $i$ th element in $S$, and $c_{j}$ is the $j$ th constraint in $S$.
The feature model includes many features and the corresponding design intent, which belongs to an implicit type. Unlike feature representations, which contain the design intent, the boundary representation uses geometrical information to unambiguously and completely represent the object. Therefore, the feature model will ultimately be translated into boundary representations, which belong to the explicit type.

- Definition 4: The geometric effects of feature model. Let $\operatorname{Brep}(M)$ denote the boundary representation of the CAD feature model; thus, the geometry of CAD feature model is $g(M)=$ $\operatorname{Brep}(M)$.
- Definition 5: Feature-based interoperability. The goal of feature-based interoperability is to seek a list of features to create a feature-based target CAD model $M^{\prime}$ using features that are as similar as possible to the source CAD model $M$, whose geometry is equivalent to that of $M$. Then, the following equation holds:

$$
g(M)=g\left(M^{\prime}\right)
$$

- Definition 6: Non-singular feature. If a feature $f$ in the source CAD system has a 1:1 feature in target CAD system, the feature $f$ is called a nonsingular feature in the source CAD system relative to target CAD system, denoted as $f^{\mathrm{D}}$.
- Definition 7: Semi-singular feature. If a feature $f$ in the source CAD system does not have a 1:1 feature in target CAD system, but it has $1: n$ features in target CAD system, the feature $f$ is called a semi-singular feature in the source CAD system relative to target CAD system, denoted as $f^{\mathrm{I}}$.

- Definition 8: Singular feature. If a feature $f$ in the source CAD system has neither a 1:1 feature nor 1: $n$ features in target CAD system. Then, the feature $f$ is called a singular feature in the source CAD system relative to target CAD system, denoted as $f^{\mathrm{S}}$.
- Definition 9: Direct feature interoperability. Given a non-singular feature $f$ in the source CAD system, a feature $f^{\prime}$ in the target CAD system can be found according to the rule $\mathrm{D}^{f}$ while maintaining the geometry of $f$ equivalent to that of $f^{\prime}$. Then, $\mathrm{D}^{f}$ is called $D F I$, which is represented as

$$
f \rightarrow \mathrm{D}^{f}\left(f^{\prime}\right), \text { s.t. } g(f)=g\left(f^{\prime}\right)
$$

- Definition 10: Indirect feature interoperability. Given a semi-singular feature $f$ in the source CAD system, $n(n>1)$ features $f^{\prime}$ (with identical semantics to $f$ ) in the target CAD system can be found according to the rule $\mathrm{I}^{f}$ while maintaining the geometry of $f$ equivalent to that of $n(n>1)$ $f_{i}^{\prime}$. Then, $\mathrm{I}^{f}$ is called $I F I$, which is represented as

$$
f \rightarrow \mathrm{I}^{f}\left(\bigcup_{i=1}^{n} f_{i}^{\prime}\right), \text { s.t. } g(f)=g\left(\bigcup_{i=1}^{n} f_{i}^{\prime}\right)
$$

- Definition 11: Singular feature interoperability. Given a singular feature $f$ in the source CAD system, there is no feature or feature set that has identical semantics according to the rules $\mathrm{D}^{f}$ and $\mathrm{I}^{f}$. According to a particular rule $\mathrm{S}^{f}, n(n \geqslant 1)$ features $f^{\prime}$ (with different semantic from $f$ ) in the target CAD system can be found while maintaining the geometry of $f$ equivalent to that of $n(n \geqslant$ 1) $f_{i}^{\prime}$. Then, $\mathrm{S}^{f}$ is called $S F I$, which is described as

$$
f \rightarrow \mathrm{~S}^{f}\left(\bigcup_{i=1}^{n} f_{i}^{\prime}\right), \text { s.t. } g(f)=g\left(\bigcup_{i=1}^{n} f_{i}^{\prime}\right)
$$

- Definition 12: Non-singular sketch. If an element $s$ in the source CAD system has a 1:1 element in target CAD system, the element $s$ is called a nonsingular sketch in the source CAD system relative to target CAD system, denoted as $s^{\mathrm{D}}$.
- Definition 13: Semi-singular sketch. If an element $s$ in the source CAD system does not have a 1:1 element in target CAD system, but it has 1: $n$ elements in target CAD system, the element $s$ is called a semi-singular sketch in the source CAD system relative to target CAD system, denoted as $s^{\mathrm{I}}$.
- Definition 14: Singular sketch. If an element $s$ in the source CAD system has neither a 1:1 element nor 1: $n$ elements in target CAD system. Then, the element $s$ is called a singular sketch in the source CAD system relative to target CAD system, denoted as $s^{\mathrm{S}}$.
- Definition 15: Direct sketch interoperability. Given a non-singular sketch $s$ in the source CAD system, an element $s^{\prime}$ in the target CAD system can be found according to the rule $\mathrm{D}^{s}$ so that the source feature $f$ with element $s$ and the target feature $f^{\prime}$ with element $s^{\prime}$ have identical geometries. Then, $\mathrm{D}^{s}$ is called $D S I$, which is represented as

$$
s \rightarrow \mathrm{D}^{s}\left(s^{\prime}\right), \text { s.t. } g(f)=g\left(f^{\prime}\right)
$$

- Definition 16: Indirect sketch interoperability. Given a semi-singular sketch $s$ in the source CAD system, $n(n>1)$ elements $s^{\prime}$ in the target CAD system can be found according to the rule $\mathrm{I}^{s}$, such that source feature $f$ with element $s$ and the target feature $f^{\prime}$ with $n$ elements $s_{i}^{\prime}$ have identical geometries. Then, $\mathrm{I}^{s}$ is called $I S I$, which is represented as

$$
s \rightarrow \mathrm{I}^{s}\left(\bigcup_{i=1}^{n} s_{i}^{\prime}\right), \text { s.t. } g(f)=g\left(f^{\prime}\right)
$$

- Definition 17: Singular sketch interoperability. Given a singular sketch $s$ (the parameters of the element in the target CAD system are singular) in the source CAD system, an element $s^{\prime}$ in the target CAD system can be found according to the rule $\mathrm{S}^{s}$ so that the source feature $f$ with element $s$ and the target feature $f^{\prime}$ with element $s^{\prime}$ have approximately similar geometries. Then, $\mathrm{S}^{s}$ is called SSI, which is represented as

$$
s \rightarrow \mathrm{~S}^{s}\left(s^{\prime}\right), \text { s.t. } g(f)=g\left(f^{\prime}\right)
$$

### 3.2. The frame of feature-based interoperability

The geometry is the basic function of CAD models. The UPR uses geometry replacement to target model $M^{\prime}$ which is functionally equivalent to source model $M$. In this paper, the proposed method uses feature replacement to target model $M^{\prime}$ which is functionally equivalent to source model $M$. As illustrated in Fig. 1, the frame of feature-based interoperability includes three parts:

- A source CAD system;
- An interoperability module;

![img-0.jpeg](img-0.jpeg)

Fig. 1. Framework of feature-based interoperability.

- A target CAD system.

Therefore, sharing a feature model from the source CAD system to the target CAD system consists of the following major steps:

- Using APIs from the source CAD system to retrieve the features and sketches of source model $M$;
- Exporting an XML [12,74] representation of the source model to the interoperability module;
- Converting an XML representation of the source model to an XML representation of the equivalent target model in the interoperability module;
- Importing an XML representation of the target model to the target CAD system;
- Using APIs from the target CAD system to reconstruct target model $M^{\prime}$.
- Computing the Hausdorff distance between source model $M$ and target model $M^{\prime}$.
In this framework, the feature-based interoperability clearly depends on the interoperability of the feature and sketch. Therefore, exchanging the featuremodeling procedure from a source CAD system to a target CAD system requires the aforementioned DFI, IFI, SFI, DSI, ISI and SSI. Without loss of generality, the steps to manipulate the feature-based interoperability among heterogeneous CAD systems are as follows.
- First, to classify the feature. Suppose that source feature model $M$ includes three types of features $f^{\mathrm{D}}, f^{\mathrm{I}}$, and $f^{\mathrm{S}}$, and their numbers are $a, b-a$, and $c-b$, respectively, where $0 \leqslant a \leqslant b \leqslant c$. Thus, $M$ is represented as

$$
M=\bigcup_{i=1}^{c} f_{i}=\bigcup_{i=1}^{a} f_{i}^{\mathrm{D}} \cup \bigcup_{i=a+1}^{b} f_{i}^{\mathrm{I}} \cup \bigcup_{i=b+1}^{c} f_{i}^{\mathrm{S}}
$$

- Second, to exchange the feature data. Manipulating Eq. (11) according to DFI, IFI, and SFI, another form of $M$ is

$$
\begin{aligned}
M & \rightarrow \bigcup_{i=1}^{a}\left(\mathrm{D}^{f}\left(f_{i}^{\prime}\right)\right) \\
& \cup \bigcup_{i=a+1}^{b}\left(\mathrm{I}^{f}\left(\bigcup_{j=1}^{n_{i}} f_{i j}^{\prime}\right)\right) \\
& \cup \bigcup_{i=b+1}^{c}\left(\mathrm{~S}^{f}\left(\bigcup_{j=1}^{v_{i}} f_{i j}^{\prime}\right)\right) \\
& =\quad \bigcup_{i=1}^{a+\sum_{i=a+1}^{b} n_{i}+\sum_{i=b+1}^{c} v_{i}} f_{i}^{\prime}=M^{\prime}
\end{aligned}
$$

- Third, to classify the sketch. Suppose that feature $f$ in source model $M$ belongs to the sketch-based feature. Simultaneously, suppose that a sketch $S$ includes three types of elements $s^{\mathrm{D}}, s^{\mathrm{I}}, s^{\mathrm{S}}$, and their numbers are $\alpha, \beta-\alpha, \gamma-\beta$, respectively, where $0 \leqslant \alpha \leqslant \beta \leqslant \gamma$. This paper focuses on studying the translation of the functions and parameters of the sketch and ignores the effect of the constraints on the sketch interoperability. Thus, $S$ can be simply described as

$$
S=\bigcup_{i=1}^{\gamma} s_{i}=\bigcup_{i=1}^{\alpha} s_{i}^{\mathrm{D}} \cup \bigcup_{i=\alpha+1}^{\beta} s_{i}^{\mathrm{I}} \cup \bigcup_{i=\beta+1}^{\gamma} s_{i}^{\mathrm{S}}
$$

- Fourth, to exchange the sketch data. Manipulating Eq. (13) according to DSI, ISI, and SSI, another form of $S$ is

$$
\begin{aligned}
S & \rightarrow \bigcup_{i=1}^{\alpha}\left(\mathrm{D}^{*}\left(s_{i}^{\prime}\right)\right) \\
& \cup \bigcup_{i=\alpha+1}^{\beta}\left(\mathrm{I}^{*}\left(\bigcup_{j=1}^{g_{i}} s_{i j}^{\prime}\right)\right) \\
& \cup \bigcup_{i=\beta+1}^{\gamma}\left(\mathrm{S}^{*}\left(s_{i}^{\prime}\right)\right) \\
& =\bigcup_{i=1}^{\alpha+\sum_{i=\alpha+1}^{\beta} g_{i}+\gamma-\beta} s_{i}^{\prime}=S^{\prime}
\end{aligned}
$$

After the featured-based interoperability on source CAD model $M$, under the premise of sufficiently high

Table 1
General examples of feature-based interoperability
geometric fidelity, $c$ source features of $M$ can be replaced with $a+\sum_{i=n+1}^{b} u_{i}+\sum_{i=b+1}^{c} v_{i}$ target features of $M^{\prime}$. Meanwhile, $\gamma$ source elements of $S$ can be replaced with $\alpha+\sum_{i=\alpha+1}^{\beta} \theta_{i}+\gamma-\beta$ target elements of $S^{\prime}$. The feature representations of the target CAD model $M^{\prime}$ can be obtained by substituting $S^{\prime}$ (Eq. (14)) into $f^{\prime}$ (Eq. (12)) according to the relationship between feature and sketch (Eq. (2)).

### 3.3. Feature-based interoperability: Problem statement

Many studies have been conducted regarding the four problems (DFI, IFI, DSI and ISI) and have obtained satisfactory results. For example, for the featurebased interoperability between CatiaV5 and Pro/E, some general examples based on these methods (DFI, IFI, DSI and ISI) are provided in Table 1.

Table 1 shows that the cut and fillet features in CatiaV5 have a 1:1 feature in Pro/E (cut and round, respectively); thus, they can be processed using DFI. However, the extrusion feature in CatiaV5 does not have a 1:1 feature in Pro/E, but it can be represented by a feature set (Extrusion $\cup$ Datum plane) in Pro/E; thus, it can be processed by using IFI. Similarly, the line and circle in CatiaV5 has a 1:1 element (Line and Circle, Respectively) in Pro/E; thus, they can be processed using DSI. However, the Polygon in CatiaV5 does not have a 1:1 element in Pro/E, but it can be represented by an element set $\left(\cup_{i=1}^{n} \operatorname{Line} v_{i}\right)$; thus, it can be processed using ISI.

To our knowledge, the target CAD system does not have a semantic feature that is identical to the singular feature of the source CAD system; thus, the singular feature cannot be processed using DFI or IFI. Similarly, because the parameters of a sketch in the target CAD system have a singular form in the source CAD system, the singular sketch cannot be processed using DSI or ISI. In previous studies [64-66], the singular feature or singular sketch is replaced by its geometry representation to avoid the problem of SFI and SSI. As a result, the exchanged models cannot be readily

Table 2
SA-SFI among different CAD systems
edited, and the original intent of the designer is lost. Therefore, with these four problems (DFI, IFI, DSI and ISI) solved, SFI and SSI become the largest bottleneck for the development of feature-based interoperability.

## 4. Asymmetric feature-based interoperability

In this section, a new approach to solve the aforementioned problems based on asymmetric featurebased interoperability is proposed.

### 4.1. Semantics-asymmetry singular feature interoperability

Because the popular commercial CAD systems provide a feature-based design technique, the feature model is represented as a list of features. Some features can be processed using DFI or IFI because there is a feature or feature set with identical semantics in the target CAD system. Because of the systems' history, innovation and competition, different CAD systems have different respective singular features. As a result, there is no feature or feature set with identical semantics (which is also considered semantics symmetry) in the target CAD system to source the singular feature.

To make the exchanged singular features editable and have high geometric fidelity, these singular features can be replaced by a feature or feature set with different semantics (which is also considered semantics asymmetry). Therefore, the SA-SFI method is proposed based on Eq. (7). According to this method, some examples of processing the singular feature among different CAD systems are provided in Table 2.

Table 2 shows that some case studies among heterogeneous CAD systems are provided later on in this paper. Because SA-SFI among different CAD systems belongs to different cases, the solution also varies among the cases. In contrast, because SSI is more generally applicable to SA-SFI, continuing to study SSI is particularly important. The remainder of this paper focuses on studying the problem of SSI.

Table 3
High-level parameters of a spline in different CAD systems

### 4.2. Parameter-asymmetry singular sketch interoperability

### 4.2.1. Difficulty of singular-sketch interoperability

To our knowledge, the spline is a typical singular element in the sketch layer among heterogeneous CAD systems because different CAD systems introduce different parameters for the spline; thus, some wellknown FBDE methods cannot exchange the spline of the sketch. The analysis presented below shows the practical and theoretical problem of spline interoperability for FBDE.

In mathematics, a spline is a numeric function that is piecewise-defined by polynomial functions, which have a sufficiently high degree of smoothness where the polynomial pieces connect (which are known as knots) [37]. Compared to the spline in mathematics [56], the spline of the sketch in mechanical CAD systems is generated by CAD tools. Sophisticated splines can be created in the CAD system by manipulating CAD tools with high-level parameters that conveniently reflect the designer's intent. The investigation and analysis of high-level parameters of the spline among heterogeneous CAD systems are shown in Table 3, where " $\sqrt{ }$ " indicates that the CAD system provides the parameter and " $\times$ " indicates that the parameter is not available.

Table 3 shows that the high-level parameters of a spline vary in different CAD systems. When attempting to exchange the spline parameters among different CAD systems, it is impossible to find all high-level parameters in one CAD system that are identical with the parameters from another CAD system, which causes difficulties for SSI.

Figure 2 shows a typical example of processing the spline among heterogeneous CAD systems. For example, the machine part [75] contains a spline in the source CAD system (SolidWorks) as shown in Fig. 2(a). By reviewing related literature regarding
![img-1.jpeg](img-1.jpeg)

Fig. 2. Exchange complex model with spline. (a) Machine part in SolidWorks; (b) Exchanged model in datia; (c) Exchanged model in UG; (d) Exchanged model in Pro/E.

FBDE, it is apparently impossible to address this type of complex model using DSI and ISI. When attempting to exchange this model using DSI (the interpolation of high-level parameters was used as an FBDE intermediate), Figs 2(b)-(d) show the exchanged models in CatiaV5, UG and PRO/E, respectively. The four parameters of the model are identical, and the shapes are inconsistent with one another. The experimental result shows that the similarity between the original model in the source CAD system and the reconstructed model in the target CAD system is too low to be observed with the naked eye.

### 4.2.2. Optimized model of PA-SSI

Similar to the singular feature, the spline cannot be processed by either DSI or ISI and cannot be reconstructed using identical parameters (which are also considered as parameter symmetry) in the target CAD system. To make the exchanged spline editable and achieve high geometric fidelity, a PA-SSI method is proposed based on the idea of SA-SFI. The approximate spline geometry in the target CAD system can be automatically recovered according to the geometry of the spline in the source CAD system.

In this paper, PA-SSI is derived from Eq. (10) and formulated as an optimization problem $Q$, which is computationally solvable. Given a set of ordered points of the spline in the source CAD system, a group of random points (interpolations) must be selected to create a spline in the target CAD system to minimize the error between the splines of the two CAD systems.

The mathematical model is provided as follows: Given the source spline $s, P=\left\{p_{1}, p_{2}, \ldots, p_{m}\right\}$ is a set of $m$ discrete points in $s$, the target spline is $s^{\prime}$, and $T=\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ is a set of $n$ interpolations (the interpolation of high-level parameters was used as an FBDE intermediate) for $s^{\prime}$; then, problem $Q$ is described as

$$
\begin{aligned}
& \text { Minimize: } \mathrm{H}\left(P, P^{\prime}\right)=\max \left(\mathrm{h}\left(P, P^{\prime}\right), \mathrm{h}\left(P^{\prime}, P\right)\right) \\
& \text { s.t. } T \rightarrow s^{\prime}, \quad T \subset P
\end{aligned}
$$

where

$$
\begin{aligned}
& \mathrm{h}\left(P, P^{\prime}\right)=\max _{p \in P}\left(\min _{p^{\prime} \in P^{\prime}} \operatorname{dist}\left(p, p^{\prime}\right)\right) \\
& \mathrm{h}\left(P, P^{\prime}\right)=\max _{p \in P}\left(\min _{p^{\prime} \in P^{\prime}} \operatorname{dist}\left(p, p^{\prime}\right)\right)
\end{aligned}
$$

where $P^{\prime}=\left\{p_{1}^{\prime}, p_{2}^{\prime}, \ldots, p_{m}^{\prime}\right\}$ is a set of $m$ discrete points in $s^{\prime}$, the sign " $\rightarrow$ " represents reconstructing a spline in the target CAD system, $\operatorname{dist}(.,$.$) denotes the$ Euclidean distance operator in $\mathrm{R}^{3}, \mathrm{~h}\left(P, P^{\prime}\right)$ denotes the one-sided Hausdorff distance from $P$ to $P^{\prime}$ [9], and $\mathrm{h}\left(P^{\prime}, P\right)$ denotes the one-sided Hausdorff distance from $P^{\prime}$ to $P$. The two-sided Hausdorff distance between $P$ and $P^{\prime}$ is the maximum distance between $\mathrm{h}\left(P, P^{\prime}\right)$ and $\mathrm{h}\left(P^{\prime}, P\right) . \mathrm{H}\left(P, P^{\prime}\right)$ measures the shape similarity between $P$ and $P^{\prime}$. A smaller distance corresponds to a closer resemblance between $s$ and $s^{\prime}$. If $\mathrm{H}\left(P, P^{\prime}\right)=0$, then the two geometry are nearly identical.

Given a source spline $s(P$ is a set of $m$ discrete points in $s$ ), the interpolation set $T$ has $C_{m}^{n}$ combinations, one of which minimizes $\mathrm{H}\left(P, P^{\prime}\right)$.

Because there is a huge search space to solve the optimization problem, it is generally impossible for a human being to find an optimal $T$ that satisfies Eq. (15) through human-computer interactions.

This paper uses computation power to automatically determine the optimized locations and counts of the interpolation set. EDA is robust for solving complex, large-scale, nonlinear optimization problems. The EDA method is adopted and a local optimization operator is presented to the EDA to solve the problem.

According to current state of research, no other system or approach adopts EDA to address the problem of singular feature interoperability. In the next section, the implementation of the EDA is described in further detail.

## 5. The estimation-of-distribution algorithm for optimization problem $Q$

Recently optimization problems have recently been studied in both industrial and scientific contexts [9,15, 43,52,72]. It is essential to select the appropriate optimization algorithm for practical engineering purposes.

The EDA, which was introduced by Mühlenbein and Paaß [53], is a population-based optimization algorithm. In brief, an EDA estimates the probability distribution of the most promising solutions and generates new offsprings by sampling the probabilistic model. In contrast to a genetic algorithm (GA), which uses the crossover and mutation operators to generate solutions, the EDA does not use crossover or mutation. Because the EDA uses a probabilistic model to guide the evolutionary process, it can avoid the blindness and randomness of crossover of the GA, which improves the searching efficiency and can quickly and reliably resolve many problems that are difficult for a GA. In addition, the EDA is a new optimization technique that has been successfully applied to optimization, engineering, cluster analysis, machine learning and design problems [11].

### 5.1. Coding and initialization rules

In this section, an initial strategy is proposed to solve this problem. The following two equations can be assumed:

$$
\begin{aligned}
X & =\left(\begin{array}{ccc}
v_{11} & \ldots & v_{1 D} \\
\vdots & \ddots & \vdots \\
v_{L 1} & \ldots & v_{L D}
\end{array}\right) \\
x_{i} & =\left\{v_{i 1}, v_{i 2}, \ldots, v_{i D}\right\}
\end{aligned}
$$

From this expression, the initial population $X$ contains $L$ individuals, and each individual contains $D$ variables. Furthermore, each individual $x_{i}$ represents a candidate solution of interpolation set $T$ in target spline $s^{\prime}$.

In particular, three criteria are used for the initial population:

- A number of initial individuals $x_{i}$ are uniformly distributed in point set $P$, and individual $x_{i}$ should be selected according to point set $P$ after the first iteration.
- Individual $x_{i}$ cannot contain identical variables, and the variables in individual $x_{i}$ must be arranged in ascending order.

- The initial population $X$ consists of $L$ individuals, where a large $L$ indicates with a wide search area but low efficiency, and a small $L$ indicates with an increased risk for local optimum but high efficiency. In order to strike a balance among these considerations, $L=300$ is recommended.


### 5.2. Fitness estimation

Fitness evaluation is the criteria for whether the individual in the population is promising, and it can directly affect the quality of promising individuals. According to the coding rule, there is a one-to-one correspondence between individual $x_{i}$ and interpolation set $T$; thus, computing the fitness of individual $x_{i}$ is computing the Hausdorff distance between source spline $s$ and target spline $s^{\prime}$ [73]. Thus, the fitness function is defined as

$$
\mathrm{F}\left(x_{i}\right)=\mathrm{H}\left(P, P^{\prime}\right)
$$

where $P$ is a set of $m$ discrete points in $s$ and $P^{\prime}$ is a set of $m$ discrete points in $s^{\prime}$. In each generation, the fitness of every individual in the population is evaluated. The better individuals receive lower fitness values, whereas the relatively worse solutions higher fitness values. Based on the fitness value, the best $l(l<$ $L)$ candidates are selected to generate a promising individual set $x^{b}=\left\{x_{1}, x_{2}, \ldots, x_{l}\right\}$ using truncation selection, and the distribution probability of $x^{b}$ is estimated subsequently.

### 5.3. Construction of the probabilistic model

The probabilistic model is the core of the EDA [50]. However, estimating the probability distribution from the selected individuals is a complex problem. Compared with a single Gaussian distribution, a GMM can avoid trapping in local optima when addressing multimodal problems; thus, a GMM is adopted to describe the probability distribution of variables in the population [51].

For each individual $x_{i}$ in the promising individual set $x^{b}$, its GMM is a weighted sum of $K$ (number of mixture components) component Gaussian densities as provided by the equation

$$
\mathrm{P}\left(x_{i} \mid \Theta\right)=\sum_{k=1}^{K} \pi_{k} \mathrm{p}_{k}\left(x_{i} \mid \theta_{k}\right)
$$

where $x_{i}$ is a D-dimensional vector, $\pi_{k}$, where $k=$ $1, \ldots, K$ is the mixture weight, which satisfies the fol-
lowing constraint:

$$
\sum_{k=1}^{K} \pi_{k}=1, \quad 0<\pi_{k}<1
$$

where $\Theta=\left\{\theta_{1}, \theta_{2}, \ldots, \theta_{K}\right\}$ is a vector of parameters. $\theta_{k}=\left(\mu_{k}, \Sigma_{k}\right)$ with mean vector $\mu_{k}$ and covariance matrix $\Sigma_{k}$.
The most popular and well-established method to estimate the parameters of the GMM is the expectation maximization (EM) method [25]. The basic idea of the EM algorithm is as follows:

- Beginning with an initial model $\Theta_{0}$, estimate a new model $\hat{\Theta}$ such that $\mathrm{P}(X \mid \hat{\Theta})>\mathrm{P}\left(X \mid \Theta_{0}\right)$.
- Then, the new model becomes the initial model for the next iteration.
- And the process is repeated until the model converges.


### 5.4. Local optimization

EDA generates a new population by sampling the probabilistic model of promising individuals in each iteration. However, the individuals of the new population are not the final solution; according to the characteristics of spline interoperability, the quality of the population is further improved by changing the position of some variables in the individuals.

Therefore, in addition to the EDA, a local optimization operator is introduced to the EDA (LO-EDA), and the definitions of local optimization are as follows.

- Definition 18: Candidate variable. Given a spline $s, P$ is a set of discrete points of $s$. Spline $s^{\prime}$ is reconstructed by individual $x_{i}$, and $P^{\prime}$ is a set of discrete points of $s^{\prime}$. The $\hat{p}$ of $P$ is obtained by solving the following maximization problem:

$$
\hat{p}=\arg \max _{p \in P}\left(\min _{p^{\prime} \in P^{\prime}}\left\|p-p^{\prime}\right\|\right)
$$

then, $\hat{p}$ is the candidate variable of individual $x_{i}$, denoted as $\hat{v}$.

- Definition 19: Debased variable. Given the candidate variable $\hat{v}$, if some variable $v_{i d}, v_{i d} \in x_{i}$, of individual $x_{i}$ makes $\hat{x}_{i}$ satisfy the following equation:

$$
\begin{gathered}
\hat{x}_{i}=\left(x_{i}-\left\{v_{i d}\right\}\right) \cup\{\hat{v}\} \\
\text { s.t. } \mathrm{F}\left(\hat{x}_{i}\right)<\mathrm{F}\left(x_{i}\right)
\end{gathered}
$$

then $v_{i d}$ is the debased variable of individual $x_{i}$.

The procedure to apply local optimization to individuals is composed of three steps.

- First, the candidate variable $\hat{v}$ is calculated using Eq. (23).
- Second, whether there is a debased variable in individual $x_{i}$ is determined according to Eq. (24).
- Finally, if there is a debased variable $v_{i d}$, it is replaced by a candidate variable $\hat{v}$; if it does not exist, no operation is executed.


### 5.5. Major steps of the LO-EDA algorithm

The major steps of the LO-EDA algorithm for optimization problem $Q$ are presented as follows:

```
Algorithm 1. Pseudocode version of the LO-EDA
    \(t \leftarrow 0\)
    while (not termination criteria) do
        if \(t=0\) then
            \(X_{0} \leftarrow\) Generate \(L\) individuals at random.
        else
            \(X_{t} \leftarrow\) Generate \(L\) individuals by sampling \(\mathrm{M}\left(X_{t-1}^{h}\right)\).
            for \(i, i=1, \ldots, L\) do
            \(\hat{v} \leftarrow \arg \max _{p \in P}\left(\min _{p^{\prime} \in P^{\prime}}\left\|p-p^{\prime}\right\|\right)\).
            if \(\mathrm{F}\left(\hat{x}_{i}\right)<\mathrm{F}\left(x_{i}\right)\) then
                \(x_{i}=\left(x_{i}-\left\{v_{i d}\right\}\right) \cup\{\hat{v}\}\).
            end if
        end for
    end if
    \(\mathrm{F}\left(X_{t}\right) \leftarrow\) Evaluate all individuals base on Eq. (20).
    \(X_{t}^{h} \leftarrow\) Select \(n\) promising individuals from \(X_{t}\).
    \(\mathrm{M}\left(X_{t}^{h}\right) \leftarrow\) Estimate the probabilistic model of \(X_{t}^{h}\).
    \(t \leftarrow t+1\)
    end while
```


## 6. Experimental results

A number of experiments are conducted to verify the efficiency and effectiveness of the asymmetric featurebased interoperability.

- First, a set of experiments was conducted on both mathematical curves and a spline in a CAD system to assess the effectiveness of the proposed algorithm (LO-EDA).
- Then, many examples of SA-SFI and PA-SSI were analyzed based on the FBDE prototype system of this paper.
- All experiments were executed on an Inter(R) core(TM) i7-4470 (3.4 GHz), 8.00 GB, Windows 7.


### 6.1. Analysis of EDA algorithm

To evaluate the performance of the LO-EDA method, it was applied to several examples from differ-

Table 4
Test functions used in this paper: Mathematical definition

ent fields. Example 1 focuses on applying the LO-EDA method to mathematical curves. Example 2 discusses the spline interoperability in the case study of PA-SSI.

### 6.1.1. Example 1: Mathematical curves

To enable the reader to easily validate the proposed method, the LO-EDA method is first applied to mathematical curves instead of the spline of a CAD system; thus, it is a typical simulation experiment using MATLAB. Without loss of generality, the LO-EDA is tested on selected examples from the literature mathematical formulation $[26,77]$. To keep the paper at manageable size, only four of them are considered here. Table 4 shows their corresponding mathematical equations and associated domains. The table also includes pointers to the bibliographic entries of which they have been taken.

To evaluate the performance of the LO-EDA method, the standard EDA and uniform distribution algorithm (UDA) were selected for comparison. The difference between LO-EDA and EDA is that the latter does not use a local optimization operator. The UDA differs from the LO-EDA and EDA in that the placement of interpolations is based only on an equal length distribution of the source curve.

The steps of the UDA are as follows:

- Divide the source curve into $D-1$ equal length segments.
- Obtain $D$ interpolations from $D-1$ segments of the source curve.
With the different search dimensionality and method, the result is shown in Table 5. For each column from left to right, the total number of interpolations are $6,8,10,12,14$ and 16 , respectively. And in each condition curves are fitted to the original mathematical curves (Table 4) in three different ways, namely UDA, EDA and LO-EDA. In Table 5, the values represent the related fitness value. The EDA and LO-EDA were run 50 times, and the results were averaged. By comparing different row, it is obvious that the fitting precisions of EDA and LO-EDA are much better than that of UDA. The precision rankings of these three methods are LO-EDA $>$ EDA $>$ UDA. While the

![img-2.jpeg](img-2.jpeg)

Fig. 3. Comparison of the spline approximation with the original mathematical curve.
comparison between different columns demonstrates the fact that the greater the number of interpolations, the smaller of the spline fitting error.

Take $g_{4}(x)$ as an example, the fitting results of the comparison experiment with different search dimensionalities and methods are shown in Fig. 3. In these figures, the brown dashed line represents the original mathematical curve, the blue " $x$ " markers represent the interpolations of the fitting curve, and the blue solid line represents the approximation of the corresponding spline. For each row from top to bottom, the total number of interpolations are 6,10 and 14 , respectively. And in each condition curves are fitted to the original mathematical curve in three different ways, namely UDA, EDA and LO-EDA.

As the reader can see, the proposed method yields optimal spline fitting curves in all cases. The experiment results are as follows:

- With a given number of interpolations, the LOEDA method consistently achieves the best results of all compared methods.
- When LO-EDA is adopted and the number of interpolations is 10 , the approximation of the spline in Fig. 3(f) is superimposed onto the original mathematical curve.
Compared with the EDA, the LO-EDA improves the fitting precision by substituting a debased variable with a candidate variable.

To further examine the effectiveness of LO-EDA with a given search dimensionality $(D=10)$, the graph

Table 5
Comparison of average fitness among three algorithms
![img-3.jpeg](img-3.jpeg)

Fig. 4. Fitness versus generation for $\mathrm{g}_{4}(\mathrm{x})$.
of the fitness according to the generations is shown in Fig. 4. In this figure, the red line represents the best fitness value, and the blue dots represent the average value from 50 trials. The entire population reaches the near-optima region in each iteration, but the population diversity remains constant. Eventually, they converge to the global near-optima.

### 6.1.2. Example 2: A spline in a CAD system

Example 2 discusses the spline interoperability in the case study of PA-SSI between two mainstream CAD systems is shown in Fig. 5, which is based on secondary development API for CAD systems. Figure 5(b) shows the original spline of the complex model (model a) (Fig. 5(a)) in SolidWorks.

Applying the DSI method (the interpolation of highlevel parameters are used as the FBDE intermediate), the reconstructed sketch in CatiaV5 (Fig. 5(c)) is different than the original one (Fig. 5(b)) because the ends of this curve become less straight. The exchanged
spline using PA-SSI in CatiaV5 is shown in Fig. 5(d), which is visually indistinguishable from the original curve.

Figure 5(e) shows the reconstructed model (model b) which is exchanged by DSI method in CATIA, and Fig. 5(f) shows the reconstructed model (model c) which is exchanged by PA-SSI method in CATIA. There is a significant difference between model $a$ and model $b$ because the Slot feature in model $b$ is bent more severely than the Cut feature in model $a$. In contrast, the curvature between the Slot feature in model $c$ and the Cut feature in model $a$ are nearly consistent. In addition, the HD (Hausdorff distance) between model $a$ and model $b$ is 4.873 , while the HD between model $a$ and model $c$ is 0.0989 . The good performance demonstrates the advantage of PA-SSI method.

To further examine the effectiveness of LO-EDA with a given search dimensionality $(D=13)$, the graph of the fitness according to generations is shown in Fig. 6(a). This result shows that the entire population reaches the near-optima region after each iteration, but the diversity of the population remains constant. Eventually, the populations converge at the global nearoptima.

As previously described, the aforementioned three methods (UDA, EDA and LO-EDA) were applied to compute an appropriate location of interpolations for comparison. The results for the different search dimensionalities and methods are shown in Fig. 6(b). To obtain better performance, the search dimensionality $D$ is varied from 6 to 13. As expected from Fig. 6(b), the LO-EDA method consistently achieves the best results among the compared methods.

The LO-EDA can obtain better fitness by increasing the search dimensionality of the individuals. An excessive number of interpolations for the spline in the tar-

![img-4.jpeg](img-4.jpeg)

Fig. 5. Case study of CAD spline interoperability.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Performance analysis for case study of CAD spline interoperability. (a) Fitness versus generation for LO-EDA; (b) Comparison of the fitness evaluations.
get CAD system introduce inconveniences for the designer editing the spline. Therefore, an adequately exchanged spline should be obtained with the smallest possible number of interpolations. In this example, the geometry error of interoperability is acceptable when the number of interpolations is 13 .

The above tests with standard mathematical functions and the real CAD case study verify that the proposed approach leads to the best fitting result. Superior to traditional geometric way, the proposed method accomplishes exchanging spline sketches with parametric information; the curves maintain optimal geometrical similarity compared with the results of DSI and UDA.

### 6.2. Case study of feature-based interoperability

### 6.2.1. Case study of SA-SFI

According to the SA-SFI method, as investigated by our research, at least six examples of processing the singular feature among different CAD systems are listed in Table 2. Because SA-SFI among different CAD systems belongs to different cases, the solution also varies among the cases. For conciseness, this section presents two examples of SA-SFI from a source CAD system (SolidWorks) to other CAD systems (CatiaV5 and Pro/E).

As shown in Fig. 7(a), a nut contains a singular feature (Dome) in the original CAD system (SolidWorks).

Table 6
Case studies of PA-SSI among different CAD systems
![img-6.jpeg](img-6.jpeg)

To our knowledge, the Dome feature can be replaced only by its geometry representation, because there is no feature or feature set with an identical semantic in the target CAD system. As a result, the exchanged models cannot be readily edited.

To solve this problem, according to the SA-SFI method, the Dome feature in the source CAD system (SolidWorks) can be replaced by the Shaft feature in the target CAD systems (CatiaV5 and Pro/E), and the exchanged models are shown in Figs 7(b) and (c), respectively.

Similarly, the Flex feature in the source CAD system (SolidWorks) is shown in Fig. 7(d), which can be replaced by a Chamfer feature in the target CAD systems (CatiaV5 and Pro/E), and the exchanged models are shown in Figs 7(e) and (f), respectively.

Thus, the SA-SFI method can maintain a sufficiently high geometric fidelity and ensure that the exchanged model of the target CAD system can be effectively edited parametrically.

### 6.2.2. Case study of PA-SSI

This section provides four case studies of PA-SSI from the source CAD system to the other CAD system. To evaluate the performance of PA-SSI, the DSI (the interpolation of high-level parameters was used as an FBDE intermediate) was selected for comparison. Section 6.1.1 describes the first case in detail.

In the second case which is shown in the third row of Table 6, the original model (Cup) in CatiaV5 is on the left-hand side, the exchanged model obtained using DSI is in the middle, and the exchanged model obtained using PA-SSI is on the right-hand side. They

![img-7.jpeg](img-7.jpeg)

Fig. 7. Exchange Dome (Flex) feature from SolidWorks to CatiaV5 and Pro/E. (a) Dome feature; (b) Shaft feature; (c) Shaft feature; (d) Flex feature; (e) Chamfer feature; (f) Chamfer feature.
![img-8.jpeg](img-8.jpeg)

Fig. 8. An example for collaborative design.
are called model $a$, model $b$, and model $c$ for short. There is a significant difference between model $a$ and model $b$ because the handle in model $a$ is bent more severely than the handle in model $b$. In contrast, the geometry shape between the Rib feature in model $c$ and the Sweep feature in model $a$ are nearly consistent. To conduct a quantitative analysis between the DSI and PA-SSI methods, the HD of model $b$ and model $c$ with model $a$ are compared; the results are $H(a, b)=1.740$ and $H(a, c)=0.2540$.

In the third case which is shown in the fourth row of Table 6, the original model in SolidWorks is on the lefthand side, which is called the compressor rotor blank, the exchanged model obtained using DSI is in the middle, and the exchanged model obtained using PA-SSI is on the right-hand side. They are called model $a$, model $b$, and model $c$ for short. As shown in these results, the difference between model $a$ and model $b$ is larger
than that between model $a$ and model $c$ because model $a$ and model $b$ have different outline curvatures, and the curvatures of the outlines of model $a$ and model $c$ are rather similar. In addition, the HD between model $a$ and model $b$ is $H(a, b)=1.076$, whereas the Hausdorff distance between model $a$ and model $c$ is $H(a, c)=$ 0.0348 .

In the fourth case which is shown in the fifth row of Table 6, the original model in CatiaV5 is on the lefthand side, which is called the Handle, the exchanged model obtained using DSI is in the middle, and the exchanged model obtained using PA-SSI is on the righthand side. They are called model $a$, model $b$, and model $c$ for short. As shown in these results, the similarity between the model $a$ and model $b$ is clearly too low, even as observed with the naked eyes. The model $c$ is visually indistinguishable from the model $a$. In addition, the HD between model $a$ and model $b$ is $H(a, b)=$

1.232, whereas the Hausdorff distance between model $a$ and model $c$ is $H(a, c)=0.0273$. From this result, it is clear that model $a$ are different from model $b$, and it is similar with model $c$.

To summarize, the solution results and comparison in Table 6 show the feasibility of PA-SSI for asymmetric feature-based interoperability regardless of the type of function for the spline among heterogeneous CAD systems.

### 6.2.3. Case study of assembly

In the collaborative production, OEM needs to acquire the related parts from different suppliers and assemble them to get the final product model. Suppliers may use various CAD systems for model design, thus converting the heterogeneous CAD model parts into neutral files is critical in real assembly. The neutral files, which cannot be edited and modified by the designers, are represented as geometric models in the CAD system. Their transparency to users leaves an obstacle for collaborative design.

Finally, a collaborative assembly experiment was designed to verify the validity of the proposed method in actual collaborative production, design and the superiority compared to traditional method. As illustrated in Figs 8(a), (c) and (d) are three parts: cam lever, spring and base for assembling model. They are designed in SolidWorks (cam lever) and CATIA (spring, base) respectively. In a traditional way, the heterogeneous CAD system files should be converted to neutral files for later assembly. More specifically, the homogeneous spring and base files can be loaded into the CATIA directly to assemble model, while the cam lever designed in SolidWorks has to be converted to neutral STEP file and then loaded into CATIA for assembly. The assembly result is illustrated in Fig. 8(f), the cam lever part in the assembly model is a geometric model and it is unable to be edited and modified as shown in Fig. 8(e).

By contrast, the proposed method first conducts parametric data exchange on heterogeneous CAD model parts and then makes them homogeneous for model assembly. Figure 8(b) shows the exchanged cam lever feature model in CATIA system from SOLIDWORKS system using the proposed method. As shown in Figs 8(a) and (b), the model shape is consistent with the original one after conversion. The final assembly result is illustrated in Fig. 8(g), the converted model can be used to complete the parts assembly successfully. Figure 8(h) shows the original design information has been fully preserved. Also, the exchanged
model in CATIA is still represented as feature model, which can be further edited and modified.

The experimental results demonstrate that the proposed approach can maintain a sufficiently high geometric fidelity and ensure that the exchanged model of the target CAD system can be effectively parametrically edited.

## 7. Conclusion

In this paper, a new asymmetric method with SASFI and PA-SSI is developed, which is considered an improvement to the theory of feature-based interoperability. Compared with ISO-FBDE and the macroparametric approach, this paper specifies the interoperability of the singular features or singular sketches among heterogeneous CAD systems. Compared with UPR, the proposed approach surpasses the feature rewrite method in which the singular features are replaced with geometry. The main contributions of this paper can be summarized as follows:
(1) The theoretical aspect of feature-based interoperability. This paper adopts a formal method to completely describe and analyze feature-based interoperability in FBDE. From the perspective of the fundamental difference between FBDE and GBDE, the reason why FBDE is more challenging than GBDE and several key points in FBDE are seriously investigated. The proposed method of asymmetric feature-based interoperability constitutes a promising and useful extension for the theory of feature-based interoperability among heterogeneous CAD systems.
(2) The aspect of technology innovation. Using two types of asymmetric methods (SA-SFI and PASSI), the problems of feature-based interoperability caused by heterogeneous representations have been effectively solved. Specifically, according to the geometry of a singular feature or singular sketch in the source CAD system, the equivalence of the geometry of the feature or sketch in the receiving CAD system can be automatically recovered.
(3) The aspect of computing method. An optimized model to solve the problem of PA-SSI is established, and this problem is solved by using the EDA. In addition, a local optimization operator is introduced to enhance the global search capability of the algorithm according to the characteristic of interoperability of the spline among heterogeneous CAD systems.

(4) The experimental results demonstrate that the proposed asymmetric method is effective in addressing a singular feature or singular sketch under the framework of feature-based interoperability. It can maintain a sufficiently high geometric fidelity of a singular feature model in target CAD system and ensure that the exchanged model can be parametrically edited by target CAD user.
Therefore, the proposed idea can be adopted by engineering and industry in future work.

Also in the future, at least 4 following issues should be investigated furthermore: (1) feature interoperation of grouped elements (matching of $m: n$ ); (2) potential applications to 3D printing and the interplay between STL format and CAD format; (3) ontologybased method after absorbing valuable information from reference [74]; (4) integration of security issues from reference [17] into FBDE.

## Acknowledgments

This paper is supported by the National Science Foundation of China (Grant No. 61472289) and Hubei Province Science Foundation (Grant No. 2015CFB25 4).
