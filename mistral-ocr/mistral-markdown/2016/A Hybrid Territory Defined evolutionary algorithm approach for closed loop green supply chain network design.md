# A Hybrid Territory Defined evolutionary algorithm approach for closed loop green supply chain network design 

Anurag Tiwari ${ }^{\text {a }}$, Pei-Chann Chang ${ }^{\text {a,b,c, }}$, M.K. Tiwari ${ }^{\text {c }}$, Rishabh Kandhway ${ }^{\text {c }}$<br>${ }^{a}$ Department of Information Management, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan<br>${ }^{b}$ Innovation Center for Big Data Er Digital Convergence, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan<br>${ }^{c}$ Department of Industrial Engineering and Management, Indian Institute of Technology, Kharagpur, Kharagpur 721302, India

## A R T I C L E I N F O

Article history:
Available online 18 May 2016

Keywords:
SCM
GCLSP
EDA
NSGAII
EDATDEA

## A B S T R A C T

The Closed loop Supply chain network distribution is one of the most important problems with much real world application in supply chain management area. Presently climate change problem is one of the major concerns for Researchers. Closed loop green supply chain (GCLSC) problem is the extension of closed loop supply chain problem. Semiconductor industries are one of the major industries and a number of waste products in semiconductor industries are quite high. We have considered reducing the waste in semiconductor by recycling the useful waste electronic equipment. In GCLSC, we consider to maximize the profit in forward supply chain whereas we attempt to minimize the Carbon footprints at the same time. In this paper we used a hybrid of Estimation of distribution algorithm (EDA) and Territory Defined multi-objective algorithm to select the optimum number of facilities in the closed loop supply chain network. To examine the effectiveness of our Hybrid Territory Defined algorithm (EDATDEA), we compare the results with those obtained by NSGA II on a same GCLSC problem with different problem sizes and the same data sets.
(c) 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Climate change problem have become one of the major threats on earth. Many toxic gases such as Carbon dioxide, carbon mono oxide and many greenhouse gases are one of the biggest contributors to the threats. Dumb products are another major contribution to environment pollution. Today people, government, and business organization are more concerned about the climate change and reducing pollution and global warming.

In today's competitive and global market, the success of an industry is reliant upon the management of its supply chains. Supply chain network design includes all the internal and external components of supply chain management (SCM). Nowadays, customers want the products at the minimum possible cost, whereas firm has many objectives such as maximization of profit, reducing the carbon footprint and recycling the products. So it is important that a firm organizes the plants; retailer, supplier, distribution center and customer zone in such a manner that customer obtains the product at minimum cost and the firm should maintain their profit and minimize carbon footprint. Under these competitive missions,

[^0]firms are using different ways for environment protection. Few firms are considering satisfying the customer by development of green product which can be environmental friendly. Another way is to reduce the raw material by recycling the product. To reduce the environment damage, waste products, use the green raw material and reduce the carbon dioxide emission and push the firm to adopt the Green Supply chain. From this perspective, green supply chain can help companies to reach a more competitive position, higher profitability, and better performance by satisfying their customers more effectively Sarkis (2003). The reverse supply chain has been continually developed not only as a result of the associated economic profit but also because of the ecological motivation, Georgiadis and Vlachos (2004). Nakamura and Kondo (2006) proposed a waste input-output life-cycle cost analysis of the recycling of end-of-life electrical home appliances. Pohlen and Farris (1992) have investigated the reverse distribution channel structure in plastic recycling and analyzed the compaction and routing issues related to transportation in the RL process. The most important objectives of green supply chain management were reducing cost, increasing profit as well as protecting the environment by recycling, reusing, reworking, remanufacturing, refurbishing, reclaiming, and reducing to design reverse logistics by using closed loop supply chain management (Srivastava, 2007). Mutha and Pokharel (2009) proposed a Strategic network design for reverse


[^0]:    a Corresponding author at: Department of Information Management, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan.

    E-mail address: iepchang@uztorn.yzu.edu.tw (P.-C. Chang).

logistics and remanufacturing using new and old product modules. Closed-loop supply chain (CLSC) focuses on recycling the products by taking them back from the customers. Faccio, Persona, Sgarbossa, and Zanin (2011) apply different supply chain (SC) design approaches in the presence of reverse flows, analyzing the network structure where they considered flows are forward flow exclusively, or forward and reverse flows, or integral closed-loop flows. Last few years closed loop supply chain gained considerable attention of researchers as well as many companies. The definition of closed loop supply chain is the design, control, and operation of a system to maximize value creation over the entire life cycle of a product, with dynamic recovery of value from different types and volumes of returns over time Guide and Van (2009). Koh, Hwang, Sohn, and Ko (2002) proposed an optimal ordering and recovery policy for reusable items. The remanufacturing poses an interesting question with respect to the design and management of closed loop supply chain, Canan, Bhattacharya, Luk, and Wassenhove (2004). Traditional supply chains have been designed in single direction network, called forward logistic with the need of recycling products and decrease the waste products at the end of cycle. However, reverse and closed loop supply chain become as a most important tools for companies which is based on environmental concerns and regulations. The main application of reverse supply chain is to improve reclamation of the products at the end of their life cycle, Meade and Sarkis (2007). Past few years, the closed loop supply chain problem gains more attention. Many researchers have been proposed different closed loop supply chain models in different conditions. Abdolhossein et al. (2012) proposed an overview about closed loop supply chain, and authors discuss different aspects of closed loop supply chain and how it can help to protect the environment. Most of the researchers' concerns are about use of the few raw materials by using the recovery products. To collect the end-of-cycle product from the customers is a big problem. Canan et al. (2004) developed a closed loop supply chain model with product remanufacturing and proposed an idea about collecting recycle product in three different ways. They suggested that firms can collect product by themselves, or firms can provide a suitable incentives to an existing retailer, or firms can subcontract the collection activity to a third party. Lee and Lee (2013) proposed a modeling and optimization of closed-loop supply chain considering order or next arrival of goods.

Presently semiconductor manufacturing industries are one of the major industries. In 2010 Semiconductor market exceeded more than 300 billion USD worldwide. Semiconductor industries are one of the most energy intensive. Therefore it needs to be more environmental friendly and energy efficient. In Semiconductor Company the most important challenge is the complexity of the manufacture of integrated circuits and the role of globalization in their production. Due to the globalization and new inventions, industries need to manufacture the new products and replace their old products, which increase the number of dumb electronic products. In this paper we have considered the recycling the electronic waste equipments, which can minimize the total cost of closed loop supply chain as well as reduce the dumb electronic equipment. Author proposed a model that integrates forward and reverse logistic to satisfy the demand in case of limited recovery electronic materials. Özkir and Basligil (2013) proposed a multiobjective optimization of closed-loop supply chain in uncertain environment. Author examined the problem through product recovery chain regarding the consumer sourced returns, end-ofuse products and end-of-life products. A multi-objective model for a closed loop supply chain network design with uncertain parameters, such as cost coefficient and customer demands was proposed by Fallah, Sahraeian, Tavakkoli, and Moeinipour (2012).

Author proposed an interactive possibilities approach to solve the multi-objective mixed integer linear programming model. Kannan, Sasikumar, and Devika (2010) proposed a genetic algorithm approach for solving a closed loop supply chain a case study of battery recycling. The Closed loop green supply chain is the extension of closed loop supply chain. Last few year researchers concern more on Green supply chain. Yang, Lu, Haider, and Marlow (2013) proposed the effect of green supply chain management on green performance and firm competitiveness in the context of container shipping in Taiwan. Sustainable SC through the complete reprocessing of end-of-life products by manufacturers: A traditional versus social responsibility company perspective proposed by Faccio, Persona, Sgarbossa, and Zanin (2014). In this study, author introduced a linear programming model to minimize the total cost in forward supply chain with Environmental sustainability by the complete reprocessing of the re-use of components, an end-of life product, the disposal of unusable parts sent directly from the manufacturers, with a closed loop transportation system that maximizes transportation efficiency. Kannan and Popiuc (2014) proposed reverse supply chain coordination by revenue sharing contract; author discussed a case study of personal computer industry. Brandenburga, Kannan, Sarkis, and Seuring (2014) proposed quantitative models for sustainable supply chain management: Developments and directions. Lu, Qi, and Liu (2014) addressed about two important issues of recycling; they proposed that the industry contains small-scale and inefficient recycling firms and the output from recycling a multi-components wasted product has multiple recycling products that cannot be recycled efficiently by a single firm. Giovanni (2014) proposed Environmental collaboration in a closed-loop supply chain with a reverse revenue sharing contract. Author considered a closed-loop supply chain (CLSC) with a single manufacturer and a single retailer who invest in green advertising to build up the goodwill dynamic. To address these issue author proposed on the cooperation of recycling operation. In this paper we have proposed a new model for closed loop green supply chain in semiconductor industries, and we used nine echelons, five are in forward direction and four in reverse direction for carrying back used products and extracting value from it. We used a new approach EDATDEA to solve the 9 different closed loop green supply chain problems. EDA is a probabilistic based know evolutionary approach. Initial population generation is based on the EDA, which provides better chromosome from the starting of the procedure. After generating the initial population we have used territory defined evolutionary approach (TDEA) to solve the proposed model. Territory defined evolutionary approach selects the best solution during the nondominated sorting. We compared our result with the well know multi-objective algorithm NSGA II.

The paper is organized as follows: In Section 2 we have proposed the model and its mathematical formulation. Solution methodology is described in Section 3. Computation results are described in Section 4. Conclusion is described in Section 5.

## 2. Model descriptions

We have considered a closed loop supply chain with nine echelons, five are in forward direction and four in reverse direction for carrying back used products and extracting value from it (see Fig. 1). Case of coordinate supply chain was considered as it minimizes the supply chain cost. The costs that are considered in our analysis are, cost of raw material supplied by Supplier, cost of production by Manufacturer, repairing and recycling cost at Repairing Center, cost of disposing at Disposal Center, returns cost given by the Return Center to the customer as perk for returning the pro-

![img-0.jpeg](img-0.jpeg)

Fig. 1. Closed loop green supply chain.
duct and inventory holding cost for Distributor, Wholesaler and Centralized Collection Center. Suppliers supply multiple raw materials and Manufacturer produces multiple products, and each has different costs and material requirement. As shown in Fig. 2, at Recycling Center all the products coming from Centralized collection center are first inspected, and then they are divided in three categories, (1) products that are repairable, (2) products that are recyclable, and (3) products that have to be disposed. Repairable product are repaired, repacked and sent back to distribution center and supplied to the market as new products. Products that are recyclable are recycled and sent to manufacturing center where these are used as raw material along with those coming from Supplier, for manufacturing new products. The products that can neither be repaired nor be recycled are sent to Disposal Center and disposed of.

In past years many researcher have done sufficient work for product recovery. Gupta and Isaacs (1997) and Gungor and Gupta $(1998,1999)$ proposed a model for product recovery. Author has discussed about sequence planning for product with defective parts in product recovery and disposal strategies. Lambert (2002) proposed a model to determine optimum disassembly sequences in electronic equipment. The above described model is useful for a semiconductor manufacturing company; products such as RAM, Hard Disk, Processor, Screws, television, mobile phone, notebook are manufactures using different IC and different electronic material. Suppliers deliver different kinds of semiconductor material to manufacturing company and using this semiconductor material
company develops the final product. The material requirements can be specified with the help of bill of material for products. Similarly, when at Recycling Center the product is inspected, if some parts are damaged then those parts are replaced by new ones, repacking is done and the product is sent to Distributor. If many parts are damaged then the usable components are extracted and sent to Manufacturer where it is reused as raw materials for new Products. If the above two cases are not possible then the Product is sent to Disposal center where it is disposed of.

### 2.1. Assumptions

Various assumptions involved in the model are described below:

- Demand is deterministic i.e. demand for a period is known beforehand and the planning is done accordingly.
- Time taken to transfer a product is negligible.
- Inventory is not allowed at Supplier, Manufacturer, Disposal Center.
- Selling price of the product is inclusive of the inventory holding cost at the retailer.
- Inspection cost is negligible as compared to repairing, recycling and disposal cost.
- The supply chain model considered is a coordinated supply chain.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Recycling center model.

- Emission is majorly caused by the production of raw materials by the Supplier, manufacturing process by Manufacturer, recycling of products at Recycling Center and Disposal.


### 2.2. Notations

### 2.2.1. Indices

| $t$ | Index for time period |
| :-- | :-- |
| $a$ | Index for raw material |
| $b$ | Index for products |
| $i$ | Index for suppliers |
| $j$ | Index for manufacturers |
| $k$ | Index for distributors |
| $l$ | Index for whole sellers |
| $m$ | Index for retailers |
| $p$ | Index for collection center |
| $o$ | Index for centralized collection center |
| $n$ | Index for remanufacturing and inspection center |
| $q$ | Index for disposal center |

### 2.2.2. Parameters

| T | Total number of time periods |
| :--: | :--: |
| A | Total number of raw materials |
| B | Total number of products |
| I | Number of Suppliers |
| J | Number of Manufacturer |
| K | Number of Distributers |
| M | Number of Retailers |
| P | Number of Return Center |
| O | Number of Centralized Collection Center |
| N | Number of Recycling Center |
| Q | Number of Disposal Center |
| $P_{\text {sub }}$ | Price of Product $b$ at Retailer $m$ |
| $D_{\text {subt }}$ | Demand of Product $b$ at Retailer $m$ in period $t$ |
| $R_{\text {pbt }}$ | Returns of product $b$ at Return Center $p$ in period $t$ |
| $c t r a_{\text {ijb }}$ | Per unit transportation cost of raw material $a$ from Supplier $i$ to Manufacturer $j$ |
| $c t r a_{\text {jkb }}$ | Per unit transportation cost of product $b$ from Manufacturer $j$ to Distributor $k$ |
| $c t r a_{\text {klb }}$ | Per unit transportation cost of product $b$ from Distributor $k$ to Wholesaler $l$ |
| $c t r a_{\text {lnsb }}$ | Per unit transportation cost of product $b$ from Wholesaler $l$ to Retailer $m$ |
| $c t r a_{\text {puib }}$ | Per unit transportation cost of product $b$ from Return Center $p$ to Centralized Collection Center $o$ |
| $c t r a_{\text {onb }}$ | Per unit transportation cost of product $b$ from Centralized Collection Center $o$ to Recycling Center $n$ |
| $c t r a_{\text {nqb }}$ | Per unit transportation cost of unusable product $b$ from Recycling Center $n$ to Disposal Center $q$ |
| $c t r a_{\text {okb }}$ | Per unit transportation cost of repaired product $b$ from Recycling Center $n$ to Distributor $k$ |
| $c t r a_{\text {njb }}$ | Per unit transportation cost of recycled product $b$ from Recycling Center $n$ to Manufacturer $j$ |
| $c r m_{\text {ta }}$ | Per unit cost of raw material $a$ at Supplier $i$ |
| $c m f g_{j b}$ | Per unit manuals |

Manufacturer $j$
$c_{i b} v_{k b} \quad$ Per unit inventory holding cost of product $b$ at Distributor $k$
$c_{i n v_{l b}} \quad$ Per unit inventory holding cost of product $b$ at Wholesaler $l$
$c_{e t} t_{p b} \quad$ Per unit return cost of product $b$ at Return Center $p$ Per unit inventory holding cost of product $b$ at Centralized Return Center $o$
$c_{e t p_{n b}} \quad$ Per unit repairing cost of product $b$ at Recycling Center $n$
$c_{e c_{n b}} \quad$ Per unit recycling cost of product $b$ at Recycling Center $n$
$c_{d i s_{q b}} \quad$ Per unit disposing cost of product $b$ at Disposing Center $q$
$c_{a b} \quad$ Number of units of raw material $a$ required to make one unit of product $b$
$\propto \quad$ Proportion of returned products that go for repairing
$j i \quad$ Proportion of returned product that go for recycling
$c f p_{t a} \quad$ Per unit carbon emission for manufacturing of raw material $a$ at Supplier $i$
$c f p_{j b} \quad$ Per unit carbon emission for manufacturing of product $b$ at Manufacturer $j$
$c f p_{n b} \quad$ Per unit carbon emission for recycling of product $b$ at Recycling Center $n$
$c f p_{q b} \quad$ Per unit carbon emission for disposal of product $b$ at Disposal Center $q$
$k \quad$ Proportionality constant for converting transportation cost to carbon emission
supcap $_{n a} \quad$ Capacity of Supplier $i$ to supply raw material $a$
$m f g c a p_{j b} \quad$ Capacity of Manufacturer $j$ to manufacture product $b$
invcap $_{k b} \quad$ Inventory holding capacity of Distributer $j$ for product $b$
invcap $_{l b} \quad$ Inventory holding capacity of Wholesaler $i$ for product $b$
invcap $_{n b} \quad$ Inventory holding capacity of Centralized Collection Center $o$ for product $b$
repcap $_{n b} \quad$ Repairing capacity of Recycling Center $n$ for product $b$
reccap $_{n a} \quad$ Recycling capacity of Recycling Center $n$ for raw material $a$
discap $_{q b} \quad$ Disposing capacity of Disposal Center $q$ for product $b$

### 2.2.3. Decision variables

| $q_{i j a t}$ | Units of raw material a transported from Supplier $i$ to <br> Manufacturer $j$ in time period $t$ |
| :-- | :-- |
| $q_{j k b t}$ | Units of product $b$ transported from Manufacturer $j$ to <br> Distributer $k$ in time period $t$ |
| $q_{k d t}$ | Units of product $b$ transported from Distributer $k$ to <br> Wholesaler $l$ in time period $t$ |
| $q_{l m b t}$ | Units of product $b$ transported from Wholesaler $l$ to <br> Retailer $m$ in time period $t$ |
| $q t_{p o b t}$ | Units of product $b$ transported from Return Center $p$ <br> to Centralized Return Center $o$ in time period $t$ |
| $q t_{o n b t}$ | Units of product $b$ transported from Centralized |

(continued on next page)

Return Center $o$ to Recycling Center $n$ in period $t$
$q r_{n j b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Manufacturer $j$ after Recycling in period $t$
$q r_{n k b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Distribution Center $k$ after Repairing in period $t$
$q r_{n q b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Disposal Center $q$ after in period $t$
$q i n v_{k b t}$ Number of units of product $b$ stored at Distribution Center $k$ during period $t$
$q i n v_{l b t} \quad$ Number of units of product $b$ stored at Wholesaler $l$ during period $t$
$q i n v_{o b t} \quad$ Number of units of product $b$ stored at Distribution Center $o$ during period $t$

### 2.3. Objective function

The objective of analysis was to determine the combination of quantities of a product or raw material to be transferred between two stages such that total cost of the supply chain and carbon emissions in the supply chain is minimized. In Eq. (1) we use the forecasted value of demand which is assumed to be constant, so the revenue is calculated by multiplying the demand of a product to its price at a particular retailer. In Eq. (2) we calculate total transportation cost in the supply chain by multiplying quantity transferred from a particular route to per unit transportation cost for that route. In Eq. (3) we calculate the cost of raw material by multiplying per unit cost of raw material for a particular supplier with the number of units of raw material it provides. In Eq. (4) manufacturing cost is calculated in a similar manner as raw material cost. In Eq. (5) average inventory for a time period is calculated by adding the amount of inventory with a stakeholder to the amount of products that arrived in that period and subtracting the quantity that leaves. From Eqs. (6)-(9) the costs are calculated by multiplying the quantities on which the action is taken with the cost of taking that action. In a similar fashion in Eqs. (10)-(13), emissions are calculated by multiplying per unit carbon emission with the quantities supplied by Supplier, manufactured at Manufacturer, recycled in Recycling Center, and disposed in Disposal center. Eastern Research Group (1999, chap. 6) proposes alternative methods for estimating air emission from semiconductor manufacturing. EPA (United States Environmental Protection Agency (2005) discuss about emission facts. They have discussed the calculation of the carbon dioxide emission based on transport and fuel consumption.

The two objectives of analysis were formulated as follows:

1. Max Profit $=$ Revenue - Transportation Cost - Raw Material Cost - Manufacturing Cost - Inventory Holding Cost - Return Cost - Recycling Cost - Repairing Cost - Disposal Cost.
2. Min Emissions $=$ Emission of Supplier + Emission of Manufacturer + Emission of Recycling Center + Emission of Disposal Center.

The costs mentioned in the first objective function are defined below:
Revenue $=\sum_{i n=1}^{M} \sum_{b=1}^{B}\left(P_{o n b} * \sum_{t=1}^{T} D_{o n b t}\right)$

$$
\begin{aligned}
& \text { Transportation Cost }=\sum_{i=1}^{I} \sum_{j=1}^{J} \sum_{a=1}^{A}\left(c t r a_{j a} * \sum_{t=1}^{T} q_{j a t}\right) \\
& +\sum_{j=1}^{J} \sum_{k=1}^{K} \sum_{b=1}^{B}\left(c t r a_{j k b} * \sum_{t=1}^{T} q_{j k b t}\right) \\
& +\sum_{k=1}^{K} \sum_{b=1}^{I} \sum_{t=1}^{B}\left(c t r a_{k t b} * \sum_{t=1}^{T} q_{k t b t}\right) \\
& +\sum_{i=1}^{I} \sum_{a=1}^{M} \sum_{b=1}^{B}\left(c t r a_{a n b} * \sum_{t=1}^{T} q_{a n b t}\right) \\
& +\sum_{p=1}^{O} \sum_{n=1}^{B} \sum_{b=1}^{B}\left(c t r a_{p n b} * \sum_{t=1}^{T} q r_{p n b t}\right) \\
& +\sum_{n=1}^{O} \sum_{q=1}^{N} \sum_{b=1}^{B}\left(c t r a_{n q b} * \sum_{t=1}^{T} q r_{n q b t}\right) \\
& +\sum_{n=1}^{N} \sum_{k=1}^{K} \sum_{b=1}^{B}\left(c t r a_{n q b} * \sum_{t=1}^{T} q r_{n k b t}\right) \\
& +\sum_{n=1}^{N} \sum_{j=1}^{J} \sum_{b=1}^{B}\left(c t r a_{n j b} * \sum_{t=1}^{T} q r_{n j b t}\right) \\
& \text { Raw Material Cost }=\sum_{a=1}^{A} \sum_{i=1}^{I}\left(c r m_{i a} * \sum_{j=1}^{J} \sum_{t=1}^{T} q_{j a t}\right)
\end{aligned}
$$

Manufacturing Cost $=\sum_{b=1}^{B} \sum_{j=1}^{J}\left(c m f g_{j b} * \sum_{k=1}^{K} \sum_{t=1}^{T} q_{j k t t}\right)$
Inventory Holding Cost $=\frac{1}{2} *\left(\sum_{b=1}^{B} \sum_{i=1}^{I}\left(c i n v_{l b} * \sum_{t=1}^{T} q i n v_{l b t}\right)\right.$

$$
\begin{aligned}
& +\sum_{b=1}^{B} \sum_{t=1}^{B}\left(c i n v_{k b} * \sum_{t=1}^{T} q i n v_{k b t}\right) \\
& \left.+\sum_{b=1}^{B} \sum_{a=1}^{O}\left(c i n v_{o b} * \sum_{t=1}^{T} q i n v_{o b t}\right)\right)
\end{aligned}
$$

$$
\begin{aligned}
q i n v_{k b t} & =q i n v_{k b(t-1)}+\sum_{j=1}^{J} q_{j k b t}+\sum_{n=1}^{N} q r_{n k b t}-\sum_{l=1}^{L} q_{k l b t} . \quad q i n v_{l b t} \\
& =q i n v_{l b(t-1)}+\sum_{k=1}^{K} q_{k b t}-\sum_{m=1}^{M} q_{l m b t}
\end{aligned}
$$

$$
q i n v_{o b t}=q i n v_{o b(t-1)}+\sum_{p=1}^{P} q_{p n b t}-\sum_{n=1}^{N} q_{o n b t}
$$

Return Cost $=\sum_{b=1}^{B} \sum_{j=1}^{P}\left(\operatorname{cret}_{j b t} * \sum_{t=1}^{T} R_{j b t}\right)$
Recycling Cost $=\sum_{b=1}^{B} \sum_{a=1}^{N}\left(\operatorname{cret}_{o b} * \sum_{b=1}^{B} \sum_{t=1}^{T} q r_{o k b t}\right)$

Repairing Cost $=\sum_{b=1}^{B} \sum_{n=1}^{N}\left(c r e p_{n b}+\sum_{j=1}^{J} \sum_{t=1}^{T} q r_{n j b t}\right)$
Disposal Cost $=\sum_{b=1}^{B} \sum_{q=1}^{Q}\left(c d i s_{q b}+\sum_{n=1}^{N} \sum_{t=1}^{T} q r_{n j b t}\right)$
Emission of Supplier $=\sum_{b=1}^{B} \sum_{t=1}^{J}\left(c f p_{t b}+\sum_{j=1}^{J} \sum_{t=1}^{T} q_{t j b t}\right)$
Emission of Manufacturer $=\sum_{b=1}^{B} \sum_{j=1}^{J}\left(c f p_{j b}+\sum_{k=1}^{K} \sum_{t=1}^{T} q_{j k b t}\right)$
Emission of Recycling Center $=\sum_{b=1}^{B} \sum_{n=1}^{N}\left(c f p_{n b}+\sum_{k=1}^{K} \sum_{t=1}^{T} q_{n k b t}\right)$
Emission of Disposal Center $=\sum_{b=1}^{B} \sum_{q=1}^{Q}\left(c f p_{q b}+\sum_{n=1}^{N} \sum_{t=1}^{T} q_{n j b t}\right)$

## Subject to

### 2.4. Constraints

$\sum_{t=1}^{J} q_{\text {index }}=D_{\text {index }} \quad \forall m, b, t$
$\sum_{a=1}^{Q} q_{\text {index }}=R_{\text {jakt }} \quad \forall m, b, t$
$\sum_{j=1}^{J} q_{j a t} \leqslant \sup _{a p_{t a}} \quad \forall i, a, t$
$\sum_{k=1}^{K} q_{j k b t} \leqslant m f g c a p_{j b} \quad \forall j, b, t$
$\sum_{k=1}^{K} q r_{\text {nikht }} \leqslant r e p c a p_{n b} \quad \forall n, b, t$
$\sum_{j=1}^{J} q r_{\text {njat }} \leqslant r e c c a p_{n a} \quad \forall n, a, t$
$\sum_{n=1}^{N} q r_{\text {njat }} \leqslant \operatorname{discap}_{q b} \quad \forall q, b, t$
$q i n v_{\text {lekt }} \leqslant i n v c a p_{k b} \quad \forall k, b, t$
$q i n v_{\text {ikt }} \leqslant i n v c a p_{t b} \quad \forall l, b, t$
$q i n v_{\text {sikt }} \leqslant i n v c a p_{n b} \quad \forall o, b, t$
$\sum_{b=1}^{B}\left(c_{b u}+\sum_{k=1}^{K} q_{j k b t}\right)=\sum_{t=1}^{J} q_{j a t}+\sum_{n=1}^{N} q r_{n j b t} \quad \forall j, a, t$
$\sum_{k=1}^{K} q r_{\text {nikht }}=\alpha \sum_{a=1}^{Q} q r_{\text {onut }} \quad \forall n, b, t$
$\sum_{b=1}^{B}\left(c_{b u}+\beta \sum_{a=1}^{Q} q r_{\text {onkt }}\right)=\sum_{j=1}^{J} q r_{\text {njat }} \quad \forall n, a, t$
$\sum_{q=1}^{Q} q r_{\text {njkt }}=(1-\alpha-\beta) \sum_{a=1}^{Q} q r_{\text {onut }} \quad \forall n, b, t$
Constraint (14) shows that quantity of product delivered to retailer is equal to the demand of customer, (15) shows that quantity of product shipped from a retailer is equal to units returned. Constraints (16)-(20) are capacity constraints for supplier, manufacturer, recycling, repairing and disposal of products respectively. Constraints (21)-(23) show that inventory at distributor, wholesaler and centralized collection center respectively does not exceed inventory holding capacity. The flow conservation of products at manufacturer, distributor and recycling center is shown in constraints (24)-(27).

## 3. Solution methodology

The above described problem can be classified as a NP hard problem, so we have used meta-heuristics algorithm to solve the problem statement. Two multi-objective evolutionary algorithms were used, (1) Non-Dominated Sorting Genetic Algorithm II, Deb, Pratap, Agarwal, and Meyarivan (2002) and (2) Estimation of Distribution Algorithm, Larrañaga and Lozano (2002) with Territory Defining Evolutionary Algorithm, Karahan and Oksalan (2010), Shim, Tan, and Chia (2013) proposed a multi-objective Optimization with Estimation of Distribution Algorithm in a Noisy Environment. Sun, Zhang, and Edward (2005) developed EDA: A new evolutionary algorithm for global optimization. NSGA II is one of the oldest and robust multi-objective evolutionary algorithms, so we have used it as a benchmarking algorithm to compare the results of the algorithm developed by US. Both algorithms generate Pareto optimal solutions. In the following section we describe how the algorithms were used to solve the proposed problem.

### 3.1. Non-Dominated Sorting Genetic Algorithm II

### 3.1.1. Chromosome representation and initialization

The decision variables in the problem statement are in the form of a four dimensional matrix, so it was converted in a form of array with length equal to number of elements in the matrix. The initial population was generated by randomly selecting a value between upper and lower limit for each element.

### 3.1.2. Non-dominated sorting

Non-dominated set is in which a solution is not dominated by any other solution in that set. Non-dominated sorting is used to obtain different non-dominated sets, called as fronts within the given population for multi-objective problems. At first, the parent population $\left(P_{t}\right)$ and the offspring population $\left(Q_{t}\right)$ are united to form a temporary population, $\left(R_{t}\right)$ of size $2 N$. ' $t$ ' denotes the number of current generations.

For each individual pin $R_{t}$, we calculate $n_{p}$, number of solutions which dominate the solution $p$ and $S_{p}$, a set of solutions that the solution $p$ dominates. Now all the individuals whose $n_{p}$ value is zero (no solution dominates $p$ ) are added to the first nondominated front ( 1 is the best level). Now, for each solution $p$ with $n_{p}=0$, we visit each member of its set $S_{p}$ and reduce its domination count by one. In doing so, if for any member of the set $S_{p}$ domination count becomes zero, we put it in a separate list $Q$. These members are added to the second non-dominated front. Now, the above procedure is continued with each member of $Q$ and the third front is identified. This process continues until all fronts are identified. Thus the population $R_{t}$ of size $2 N$ is then sorted into nondominated Pareto fronts, $F_{1}$ being the best non-dominated front,

![img-2.jpeg](img-2.jpeg)

Fig. 3. NSGA II flow diagram.
$F_{2}$ the second one, and so on. An iteration of non-dominated sorting is as shown in Fig. 3.

### 3.1.3. Crowding distance

Crowding distance is the density estimator of the solutions surrounding a particular solution in the population. To estimate the crowding distance of a particular point (solution), we calculate the average distance of two points on either side of this point along each of the objectives. This quantity $I_{\text {distance }}$ serves as an estimate of the perimeter of the largest cuboid formed by the nearest neighbor's as the vertices enclosing the point $i$ without including any other point in the population. In Fig. 3 Deb et al. (2002), the crowding distance of the $i$ th solution in its front (marked with solid circles) is the average side length of the cuboid (with a dashed box) in the objective space.

The crowding-distance computation requires sorting the population according to each objective function value in ascending order of magnitude. Thereafter, for each objective function, the boundary solutions (solutions with smallest and largest function values) are assigned an infinite distance value. All other intermediate solutions are assigned a distance value equal to the absolute normalized difference in the function values of two adjacent solutions. This calculation is continued with other objective functions. The overall crowding distance value is calculated as the sum of individual distance values corresponding to each objective. Each objective function is normalized before calculating the crowding distance. For each front $F_{i}, n$ is the number of individuals.

### 3.1.4. Selection

Once the individuals are sorted based on non-domination and with crowding distance assigned, the selection is carried out using a crowded comparison-operator $\left(\prec_{n}\right)$. The comparison is carried out as below based on
(1) Non-domination rank $p_{\text {rank }}$ i.e. individuals in front $F_{i}$ will have their rank as $p_{\text {rank }} \neq i$.
(2) Crowding distance $F_{i}\left(d_{j}\right)$
$p \prec_{n} q$ if, prank $<$ qrank or if $p$ and $q$ belong to the same front $F_{i}$ then $F_{i}\left(d_{p}\right) \times F_{i}\left(d_{q}\right)$ i.e. the crowing distance should be more. The individuals are selected using a binary tournament selection with crowded comparison operator.

### 3.1.5. Genetic operators

Genetic operators are used in genetic algorithms to generate diversity (mutation-like operators) and to combine existing solutions into others (crossover-like operators). The main difference among them is that the former operate on one chromosome, that is, they are unary, while the latter are binary operators. To solve the described problem we have used Simulated Binary Crossover operator for crossover and Polynomial Mutation operator for mutation.
3.1.5.1. Simulated binary crossover. Simulated Binary Crossover simulates the binary crossover observed in nature as given below.
$c_{1, k}=\frac{1}{2}\left[\left(1-\beta_{k}\right) p_{1, k}+\left(1+\beta_{k}\right) p_{2, k}\right]$
$c_{2, k}=\frac{1}{2}\left[\left(1+\beta_{k}\right) p_{1, k}+\left(1-\beta_{k}\right) p_{2, k}\right]$
where $c_{i, k}$ is the $i$ th child with $k$ th component, $p_{i, k}$ is the selected parent and $\beta_{k}(\geqslant 0)$ is a sample from a random number generated having the density
$p(\beta)=\frac{1}{2}\left(\eta_{c}+1\right) \beta^{\eta_{c}}, \quad$ if $0 \leqslant \beta \leqslant 1$
$p(\beta)=\frac{1}{2}\left(\eta_{c}+1\right) \frac{1}{\beta^{\beta_{c}+2}}, \quad$ if $\beta>1$.
This distribution can be obtained from a uniformly sampled random number $u$ between $(0,1) . \eta_{c}$ is the distribution index for crossover. That is
$\beta(u)=(2 u)^{\left(\frac{1}{2} \gamma_{1}\right)}$
$\beta(u)=\frac{1}{\left[2(1-u)\right]^{\left(\frac{1}{2} \gamma_{1}\right)}}$

![img-3.jpeg](img-3.jpeg)

Fig. 4. EDATDEA flow diagram.
3.1.5.2. Polynomial mutation. The equations for the polynomial mutation are as described in the following equations, here $c_{k}$ is the child and $p_{k}$ is the parent with $p_{k}^{0}$ being the upper bound on the parent component, $p_{k}^{l}$ is the lower bound and $\delta_{k}$ is small variation which is calculated from a polynomial distribution, and in this equation $r_{k}$ is an uniformly sampled random number between $(0,1)$ and $\eta_{m}$ is mutation distribution index.
$c_{k}=p_{k}+\left(p_{k}^{0}-p_{k}^{l}\right) \delta_{k}$
$\delta_{k}=\left(2 r_{k}\right)^{\frac{1}{m_{k}-1}}-1, \quad$ if $r_{k}<0.5$
$\delta_{k}=\left[2\left(1-r_{k}\right)\right]^{\frac{1}{m_{k}-1}}$ if $r_{k} \geqslant 0.5$

### 3.1.6. Recombination and selection

The offspring population is combined with the current generation population and selection is performed to set the individuals of the next generation. Since all the previous and current best individuals are added in the population, elitism is ensured. Population is now sorted based on non-domination. The new generation is filled by each front subsequently until the population size exceeds the current population size. If by adding all the individuals in front $F_{j}$ the population exceeds $N$ then individuals in front $F_{j}$ are selected based on their crowding distance in the descending order until the population size is $N$. And hence the process repeats to generate the subsequent generations.

Table 1
NSGA II algorithm result on various crossover probability, mutation probability.

| SN. | Crossover probability 0.6, mutation probability 0.1 |  | Crossover probability 0.7, mutation probability 0.2 |  | Crossover probability 0.8, mutation probability 0.3 |  | Crossover probability 0.9, mutation probability 0.4 |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Profit | Emission | Profit | Emission | Profit | Emission | Profit | Emission |
| 1 | $-11,002,649$ | 369,651.6 | $-11,030,750$ | 347,059 | $-8,202,076$ | 492,403.5 | $-7,029,602$ | 373,270.3 |
| 2 | $-8,860,357$ | 234,049.7 | $-9,050,277$ | 235,867.1 | $-6,024,154$ | 368,877.5 | $-7,964,599$ | 458,815.2 |
| 3 | $-10,668,657$ | 311,490.1 | 10,643,163 | 298,675.8 | $-7,404,146$ | 415,764 | $-7,771,575$ | 400,278.8 |
| 1 | $-10,675,350$ | 334,315 | $-9,671,396$ | 251,475.4 | $-6,755,924$ | 374,423.1 | $-7,677,124$ | 400,278.8 |
| 5 | $-10,959,319$ | 355,917.3 | $-9,893,197$ | 258,064.7 | $-6,302,444$ | 374,242.3 | $-7,061,695$ | 390,036.1 |
| 6 | $-9,956,717$ | 273,182 | $-9,853,696$ | 252,174.8 | $-7,424,119$ | 439,830.7 | $-7,063,670$ | 373,994.7 |
| 7 | $-10,979,379$ | 367,746.2 | $-10,983,164$ | 329,707.5 | $-7,717,673$ | 450,377.5 | $-7,453,781$ | 381,369.5 |
| 8 | $-10,296,534$ | 294,080.5 | $-10,338,694$ | 278,221.3 | $-6,856,975$ | 394,302 | $-7,191,638$ | 374,220.8 |
| 9 | $-101,722,820$ | 339,332.1 | $-10,060,984$ | 266,999.6 | $-7,871,903$ | 465,922.6 | $-7,777,083$ | 444,114.6 |
| 10 | $-10,722,820$ | 339,332.1 | $-10,258,478$ | 266,999.6 | $-8,066,705$ | 490,364.1 | $-7,879,381$ | 452,249 |

Table 2
EDATDEA result on various crossover probability, PEDA.

| SN. | Crossover probability 0.6, <br> PEDA 0.1 |  | Crossover probability 0.6, <br> PEDA 0.2 |  | Crossover probability 0.6, PEDA 0.3 |  | Crossover probability 0.9, <br> PEDA 0.4 |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Profit | Emission | Profit | Emission | Profit | Emission | Profit | Emission |
| 1 | $-11,249,160$ | 243,530.4 | $-11,222,318$ | 268,069.1 | $-10,213,646.16$ | 227,179.384 | $-11,230,587$ | 235,110.9 |
| 2 | $-11,445,186$ | 275,538.5 | $-11,262,799$ | 272,527.4 | $-10,671,832.5$ | 241,474.36 | $-11,333,162$ | 238,313.1 |
| 3 | $-11,445,186$ | 275,538.5 | $-11,216,652$ | 267,831.7 | $-10,659,991.04$ | 240,459.136 | $-11,232,000$ | 235,180.1 |
| 1 | $-11,445,186$ | 275,538.5 | $-11,216,652$ | 267,831.7 | $-10,659,991.26$ | 227,893.424 | $-11,232,000$ | 235,180.1 |
| 5 | $-11,130,965$ | 225,009.9 | $-11,216,652$ | 267,831.7 | $-10,254,402.03$ | 227,892.862 | $-11,231,137$ | 235,145.6 |
| 6 | $-11,287,739$ | 244,761.3 | $-11,077,434$ | 251,004.4 | $-10,942,106.03$ | 227,097.928 | $-11,222,643$ | 234,288.8 |
| 7 | $-11,044,637$ | 242,225 | $-11,071,434$ | 251,004.4 | $-10,212,692.82$ | 227,097.928 | $-11,332,040$ | 238,290.6 |
| 8 | $-11,229,561$ | 242,225 | $-11,216,599$ | 267,805.4 | $-10,212,692.82$ | 227,097.928 | $-11,304,205$ | 235,925.2 |
| 9 | $-11,044,637$ | 222,512.9 | $-11,246,652$ | 267,831.7 | $-10,685,137.34$ | 242,305.296 | $-11,304,205$ | 235,925.2 |
| 10 | $-11,216,599$ | 260,770.9 | $-11,216,599$ | 260,770.9 | $-10,212,521.28$ | 226,972.792 | $-11,304,105$ | 240,094.4 |

Table 3
NSGA II algorithm result crossover probability 0.6, mutation probability 0.1 .

| Parameter tuning NSGA2, PC:0.6 |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| S.No. | Profit | Emission | S.No. | Profit | Emission |  |
| 1 | $-11,002,649$ | 369,651.6 | 26 | $-1E+07$ | 283,966.2 |  |
| 2 | $-8,860,357$ | 234,049.7 | 27 | $-9,310,236$ | 256,240.6 |  |
| 3 | $-10,668,657$ | 311,490.1 | 28 | 311,490.1 | 256,221.4 |  |
| 4 | $-10,675,350$ | 334,315 | 29 | $-1 E+07$ | 277,336.9 |  |
| 5 | $-10,959,319$ | 355,917.3 | 30 | $-1.1 E+07$ | 304,088.4 |  |
| 6 | $-9,956,717$ | 273,182 | 31 | $-9,412,268$ | 256,379.3 |  |
| 7 | $-10,979,379$ | 367,746.2 | 32 | $-1.1 E+07$ | 342,079.2 |  |
| 8 | $-10,296,534$ | 294,080.5 | 33 | $-1.1 E+07$ | 342,079.2 |  |
| 9 | $-10,174,756$ | 285,622.1 | 34 | $-9,422,368$ | 257,283.9 |  |
| 10 | $-10,722,820$ | 339,332.1 | 35 | $-1 E+07$ | 284,782.7 |  |
| 11 | $-9,840,501$ | 271,787.8 | 36 | $-1 E+07$ | 297,345.5 |  |
| 12 | $-10,443,454$ | 298,298.3 | 37 | $-9,032,687$ | 249,532.7 |  |
| 13 | $-9,233,604$ | 252,711.7 | 38 | $-8,880,889$ | 235,819.4 |  |
| 14 | $-9,674,359$ | 258,662.8 | 39 | $-1 E+07$ | 288,931.8 |  |
| 15 | $-9,501,565$ | 258,617.2 | 40 | $-9,790,413$ | 348,903.6 |  |
| 16 | $-10,370,816$ | 303,473.7 | 41 | $-1.1 E+07$ | 348,903.6 |  |
| 17 | $-9,778,804$ | 263,777.4 | 42 | $-1.1 E+07$ | 309,205.3 |  |
| 18 | $-10,370,816$ | 295,357.9 | 43 | $-1.1 E+07$ | 349,404.8 |  |
| 19 | $-10,923,197$ | 352,383.7 | 44 | $-8,955,402$ | 242,914.4 |  |
| 20 | $-10,817,650$ | 346,755.8 | 45 | $-9,024,393$ | 248,239.4 |  |
| 21 | $-10,229,006$ | 289,458.2 | 46 | $-9,698,006$ | 259,015.1 |  |
| 22 | $-9,093,826$ | 251,255.3 | 47 | $-9,501,493$ | 258,407.8 |  |
| 23 | $-9,735,616$ | 261,903.6 | 48 | $-1.1 E+07$ | 309,484.4 |  |
| 24 | $-10,646,623$ | 309,978.5 | 49 | $-1.1 E+07$ | 252,413.4 |  |
| 25 | $-10,028,136$ | 276,801.4 | 50 | $-8,982,808$ | 246,145 |  |

Table 4
NSGA II algorithm result crossover probability 0.7 mutation probability 0.2 .

| Parameter tuning NSGA2, PC:0.7 |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| S. No. | Profit | Emission | S.No. | Profit | Emission |  |
| 1 | $-11,030,750$ | 347,059 | 26 | $-9,321,177$ | 245,588.8 |  |
| 2 | $-9,050,277$ | 235,867.1 | 27 | $-9,252,024$ | 241,307.3 |  |
| 3 | $-10,643,163$ | 298,675.8 | 28 | $-10,722,710$ | 308,691.1 |  |
| 4 | $-9,671,396$ | 251,475.4 | 29 | $-9,512,751$ | 249,274 |  |
| 5 | $-9,893,197$ | 258,064.7 | 30 | $-9,577,666$ | 250,677.6 |  |
| 6 | $-9,853,696$ | 252,174.8 | 31 | $-10,485,544$ | 280,278.3 |  |
| 7 | $-10,983,164$ | 329,707.5 | 32 | $-10,896,427$ | 320,145.2 |  |
| 8 | $-10,338,694$ | 278,221.3 | 33 | $-9,880,993$ | 253,728.4 |  |
| 9 | $-10,060,984$ | 262,246.7 | 34 | $-10,686,161$ | 302,591.3 |  |
| 10 | $-10,258,478$ | 266,999.6 | 35 | $-9,129,640$ | 237,031.8 |  |
| 11 | $-11,021,451$ | 341,497.5 | 36 | $-10,771,354$ | 312,012.4 |  |
| 12 | $-10,815,117$ | 319,564.5 | 37 | $-10,681,586$ | 302,564.8 |  |
| 13 | $-10,197,881$ | 264,140.1 | 38 | $-10,898,631$ | 321,800.5 |  |
| 14 | $-10,517,909$ | 285,641.5 | 39 | $-10,284,666$ | 269,899.8 |  |
| 15 | $-10,988,922$ | 338,785.4 | 40 | $-9,172,400$ | 238,142.3 |  |
| 16 | $-10,784,906$ | 316,293.5 | 41 | $-9,619,662$ | 250,746.9 |  |
| 17 | $-10,560,847$ | 287,942.2 | 42 | $-9,619,662$ | 250,746.9 |  |
| 18 | $-10,156,063$ | 262,756.5 | 43 | $-10,405,744$ | 278,821.8 |  |
| 19 | $-9,424,456$ | 290,439.4 | 44 | $-10,617,120$ | 289,658.9 |  |
| 20 | $-10,334,420$ | 271,125.4 | 45 | $-9,096,203$ | 235,905.2 |  |
| 21 | $-10,007,710$ | 259,957.6 | 46 | $-9,207,953$ | 238,807.8 |  |
| 22 | $-10,007,710$ | 259,957.6 | 47 | $-9,207,953$ | 238,807.8 |  |
| 23 | $-10,700,860$ | 308,165.2 | 48 | $-10,008,908$ | 260,127.2 |  |
| 24 | $-10,968,930$ | 328,445.5 | 49 | $-10,776,361$ | 312,133.2 |  |
| 25 | $-9,296,967$ | 244,423.2 | 50 | $-9,238,191$ | 239,740.8 |  |

# 3.2. EDATDEA 

In Estimation of Distribution based Territory Defining Evolutionary Algorithm we use the estimation of the distribution of various decision variable using the information from the best of chromosomes in the solution. Larrañaga and Lozano (2002) developed Estimation of distribution algorithms for evolutionary com-
putation. Pan and Ruiz (2012) proposed an estimation of distribution algorithm for lot-streaming flow shop problems with setup times. It is assumed that the decision variables are independent and normally distributed. The parameters of the distribution are estimated by using the information in the top MX of chromosomes in the population. Now these distributions are used to generate a proportion of high quality solutions. After this step

Table 5
SGA II algorithm result crossover probability 0.8 mutation probability 0.3 .

| Parameter tuning NSGA2, PC:0.8 |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| S.No. | Profit | Emission | S.No. | Profit | Emission |
| 1 | $-8,202,076$ | 492,403.5 | 26 | $-7,439,516$ | 440,718.6 |
| 2 | $-6,024,154$ | 368,877.5 | 27 | $-6,837,257$ | 380,805.2 |
| 3 | $-7,404,146$ | 415,764 | 28 | $-7,995,869$ | 480,163.8 |
| 4 | $-6,755,924$ | 374,423.1 | 29 | $-6,888,967$ | 397,010.4 |
| 5 | $-6,302,444$ | 374,242.3 | 30 | $-7,087,305$ | 407,199.7 |
| 6 | $-7,424,119$ | 439,830.7 | 31 | $-7,850,604$ | 463,285.9 |
| 7 | $-7,717,673$ | 450,377.5 | 32 | $-7,732,963$ | 460,081.5 |
| 8 | $-6,856,975$ | 394,302 | 33 | $-7,925,315$ | 478,556.8 |
| 9 | $-7,871,903$ | 465,922.6 | 34 | $-6,051,447$ | 491,483.5 |
| 10 | $-7,919,145$ | 490,364.1 | 35 | $-8,134,429$ | 491,483.5 |
| 11 | $-7,919,145$ | 477,201.5 | 36 | $-7,139,224$ | 409,216.2 |
| 12 | $-6,839,285$ | 381,748.8 | 37 | $-8,142,908$ | 492,001 |
| 13 | $-6,101,887$ | 370,821.1 | 38 | $-7,061,825$ | 406,587.2 |
| 14 | $-6,274,112$ | 371,621.7 | 39 | $-6,883,197$ | 395,566 |
| 15 | $-6,905,685$ | 401,743.4 | 40 | $-7,056,579$ | 404,417.4 |
| 16 | $-8,037,980$ | 482,019.9 | 41 | $-8,002,225$ | 481,738.6 |
| 17 | $-7,330,865$ | 410,354 | 42 | $-6,282,171$ | 374,065.8 |
| 18 | $-7,156,769$ | 410,024.1 | 43 | $-7,588,095$ | 446,935.2 |
| 19 | $-7,596,396$ | 448,830.9 | 44 | $-7,546,340$ | 465,092.4 |
| 20 | $-7,596,396$ | 448,830.9 | 45 | $-7,334,965$ | $-7,334,965$ |
| 21 | $-7,596,396$ | 459,064.4 | 46 | $-7,546,340$ | 445,975.3 |
| 22 | $-7,804,670$ | 461,486.1 | 47 | $-7,502,591$ | 445,468.2 |
| 23 | $-7,031,189$ | 401,923.5 | 48 | $-7,516,863$ | 445,973.3 |
| 24 | $-7,479,648$ | 444,887.3 | 49 | $-7,035,309$ | 403,585.6 |
| 25 | $-7,367,622$ | 412,019.9 | 50 | $-7,035,042$ | 402,974.6 |

Table 6
NSGA II algorithm result crossover probability 0.9 mutation probability 0.4 .

| Parameter tuning NSGA2, PC:0.9 |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| S.No. | Profit | Emission | S.N. | Profit | Emission |
| 1 | $-7,029,602$ | 373,270.3 | 26 | $-7,653,862$ | 400,180.1 |
| 2 | $-7,964,599$ | 458,815.2 | 27 | $-7,911,478$ | 456,192.1 |
| 3 | $-7,771,575$ | 435,389.4 | 28 | $-7,325,056$ | 378,107.8 |
| 4 | $-7,677,124$ | 400,278.8 | 29 | $-7,826,273$ | 449,820.8 |
| 5 | $-7,461,695$ | 390,036.1 | 30 | $-7,950,188$ | 457,266.6 |
| 6 | $-7,063,670$ | 373,994.7 | 31 | $-7,788,570$ | 445,818 |
| 7 | $-7,453,781$ | 381,369.5 | 32 | $-7,221,147$ | 376,523 |
| 8 | $-7,191,638$ | 374,220.8 | 33 | $-7,963,035$ | 458,532.5 |
| 9 | $-7,777,083$ | 444,114.6 | 34 | $-7,601,140$ | 398,181.9 |
| 10 | $-7,879,381$ | 452,249 | 35 | $-7,195,702$ | 396,874.1 |
| 11 | $-7,490,084$ | 394,494.3 | 36 | $-7,576,871$ | 396,874.1 |
| 12 | $-7,311,283$ | 377,574.8 | 37 | $-7,588,603$ | 397,337.9 |
| 13 | $-7,238,307$ | 377,572.3 | 38 | $-7,202,279$ | 376,157.8 |
| 14 | $-7,411,706$ | 378,918.1 | 39 | $-7,821,754$ | 448,592 |
| 15 | $-7,840,450$ | 451,368.9 | 40 | $-7,783,508$ | 444,798.8 |
| 16 | $-7,493,268$ | 395,687.1 | 41 | $-7,571,150$ | 396,593.5 |
| 17 | $-7,416,279$ | 380,717.2 | 42 | $-7,226,901$ | 377,174.1 |
| 18 | $-7,350,823$ | 378,869 | 43 | $-7,191,802$ | 374,390.5 |
| 19 | $-7,551,535$ | 395,745.1 | 44 | $-7,824,959$ | 449,702.1 |
| 20 | $-7,902,243$ | 455,558.6 | 45 | $-7,337,229$ | 378,552.3 |
| 21 | $-7,612,270$ | 399,025.4 | 46 | $-7,344,553$ | 378,833.9 |
| 22 | $-7,803,610$ | 446,594.5 | 47 | $-7,786,126$ | 445,203.5 |
| 23 | $-7,647,514$ | 399,369.5 | 48 | $-7,566,597$ | 396,002 |
| 24 | $-7,943,604$ | 456,552.2 | 49 | $-7,592,318$ | 398,134.4 |
| 25 | $-7,814,922$ | 448,554.6 | 50 | $-7,903,898$ | 455,739.5 |

Territory Defining Evolutionary Algorithm is applied to get the pareto-optimal front. A Territory Defining Multi objective Evolutionary Algorithms and Preference Incorporation was proposed by Karahan and Oksalan (2010). In subsequent section we define each step of the algorithm in detail (see Fig. 4).

## Pseudo Code:

Initialize Population $P(0)$ generated randomly, by selecting a value between upper and lower limit
Non-Dominated Sorting of $P(0)$
Initialize Archive Population A(0) set of initial population $P(0)$ lying in first non-dominated front
Repeat until stopping condition is reached
Generate a random number R1 between 0 and 1
If R1 is less than PEDA (probability of using EDA algorithm)

Generate offspring using EDA Algorithm Else
Generate a random number R2 between 0 and 1
If R2 is less than PC (probability of crossover)
Generate offspring using Simulated Binary crossover algorithm

## Else

Generate offspring using Polynomial Mutation algorithm

## End

End
Mark all chromosomes in $P(t)$ that dominates the generated offspring
If Offspring is dominated by any chromosome in $P(t)$ Reject offspring
Check stopping condition
Else
Mark all chromosomes in $A(t)$ dominated by offspring Remove all marked chromosomes from $A(t)$ Calculate scaled rectilinear distance of Offspring from each chromosome in $A(t)$

Calculate maximum scaled absolute objective difference between offspring and chromosome in $A(t)$ having minimum scaled rectilinear distance

If maximum scaled absolute objective difference is greater than territory size Accept offspring in $A(t)$ Else

## Reject Offspring

Check stopping condition
End

Territory Defining Evolutionary Algorithm is applied to get the pareto-optimal front. A Territory Defining Multi objective Evolutionary Algorithms and Preference Incorporation was proposed by Karahan and Oksalan (2010). In subsequent section we define each step of the algorithm in detail (see Fig. 4).

![img-4.jpeg](img-4.jpeg)

Fig. 5. NSGA II algorithm result crossover probability and mutation probability.
have used EDA, Simulated Binary Crossover and polynomial mutation operator to generate the offspring based on the probability

Table 7
Different cases for closed loop green supply chain problem.

| Case | I | J | K | L | M | P | O | N | Q | T |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 3 | 3 | 1 | 2 | 5 | 5 | 2 | 2 | 1 | 1 |
| 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | 2 | 2 | 5 | 2 | 2 | 1 | 2 | 3 |
| 4 | 3 | 3 | 1 | 2 | 5 | 5 | 2 | 2 | 1 | 1 |
| 5 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 6 | 3 | 3 | 2 | 2 | 5 | 2 | 2 | 1 | 2 | 3 |
| 7 | 3 | 3 | 1 | 2 | 5 | 5 | 2 | 2 | 1 | 1 |
| 8 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 9 | 3 | 3 | 2 | 2 | 5 | 2 | 2 | 1 | 2 | 3 |

and stopping criterion. The selection of offspring is first tested into regular population $(P(t))$ and then it is tested into archive population $(A(t))$. The entire individuals that are dominated by offspring are marked if offspring is dominated by at least one chromosome in $P(t)$, it rejected and a new offspring generated. For offspring to be accepted in archive population should not lie in the territory of any of the existing chromosome in the archive population. The chromosome with the minimum scaled rectilinear distance is selected and maximum scaled absolute objective difference is calculated between offspring and the selected chromosome for all the objectives. The detailed procedure of EDATDEA is as follows.
![img-5.jpeg](img-5.jpeg)

Fig. 6. EDATDEA result crossover probability and mutation probability.

Table 8
Performance comparison of EDATDEA and NSGA II algorithm for different cases.

| Case | NSGA2 |  |  |  | EDATDEA |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Max (profit) | Min emission | Avg. (profit) | Avg. emission | Max (profit) | Min emission | Avg. (profit) | Avg. emission |
| 1 | $-11,030,750$ | 235,867.1 | $-10,196,831$ | 279,880.6 | $-11,407,541$ | 229,637.2 | $-11,073,864$ | 242,639 |
| 2 | $-14,128,846$ | 795,287.9 | $-13,251,519$ | 861,146.4 | $-18,489,022$ | 666,332.1 | $-18,042,766$ | 684,760.5 |
| 3 | $-20,146,346$ | 1,230,858.9 | $-18,928,350$ | 1,276,254.6 | $-22,943,299$ | 1,176,132.7 | $-22,713,983$ | 1,201,568.4 |
| 4 | $-2,942,443$ | 176,806.3 | $-2,279,959$ | 218,223 | $-3,811,854$ | 141,509.9 | $-3,616,255$ | 147,143.8 |
| 5 | $-5,102,644$ | 348,686.3 | $-3,716,486$ | 466,711.7 | $-5,974,262$ | 366,779 | $-5,739,311$ | 382,748.3 |
| 6 | $-4,021,765$ | 797,948 | $-1,795,380$ | 914,766.8 | $-5,811,766$ | 735,316.9 | $-5,492,632$ | 741,708.9 |
| 7 | $-12,159,087$ | 193,004.6 | $-10,820,418$ | 271,970.5 | $-12,405,706$ | 246,644.7 | $-12,095,486$ | 261,959 |
| 8 | $-17,769,736$ | 739,196.3 | $-16,218,400$ | 817,117.8 | $-21,431,596$ | 634,224.9 | $-21,191,869$ | 669,073.7 |
| 9 | $-19,641,946$ | 1,434,987 | $-18,677,938$ | 1,502,127 | $-27,816,817$ | 1,195,558 | $-26,980,104$ | 1,223,446 |

![img-6.jpeg](img-6.jpeg)

Fig. 7. Pareto optimal front comparison for case 1.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Pareto optimal front comparison for case 4.

### 3.2.1. Initialization, non-dominated sorting $\mathcal{E}$ ranking

The steps used are same as that used in NSGA II. The main difference is that here we have two population instead of one. The size of one population is fixed whereas the other population varies depending upon the number of solutions we have in the first front. The first population i.e. $P(0)$ is initialized, sorted and ranked in the same way as NSGA II. The second population also known as archive population, $A(0)$ is the set of non-dominated individuals. They are initialized by selecting the solutions from $P(0)$ that lie in the first front.

### 3.2.2. Offspring generation

Three different procedures are used for offspring generation in the algorithm. With a probability of PEDA offspring is generated
![img-8.jpeg](img-8.jpeg)

Fig. 9. Pareto optimal front comparison for case 5.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Pareto optimal front comparison for case 8.
using Estimation of Distribution. The procedure used for generation is, top $\mathrm{M} \%$ of the chromosomes from population are selected. Since using these values of the decision variable we get solutions of good quality, the mean of these values is used as estimates of the mean of normal distribution. The standard deviation of the normal distribution is assumed to be one tenth of the difference of limits for each decision variable. With probability $(1-P E D A) * P C$ offspring is generated using Simulated Binary Crossover operator as described in the NSGA II. With probability $(1-P E D A) *$ $(1-P C)$ offspring were generated using polynomial mutation operator.

### 3.2.3. Criteria for acceptance in $P(t)$

The offspring is first tested for acceptance into regular population, and then it is tested for acceptance into archive population.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Pareto optimal front comparison for case 9.
The evaluation procedure is as follows, first the offspring is tested for dominance. All the individuals that are dominated by offspring are marked, if offspring is dominated by at least one chromosome in $P(t)$, it is rejected and a new offspring is generated, otherwise
offspring is accepted and a marked individual is randomly selected and removed from $P(t)$. If none of the individual is marked then a chromosome is randomly selected and removed.

### 3.2.4. Criteria for acceptance in $A(t)$

For offspring to be accepted in archive population, it should not lie in the territory of any of the existing chromosomes in the archive population. The procedure is as follows, the offspring is tested for dominance, all the individuals dominated by offspring are marked, if it is dominated by any individual in $A(t)$ then it is rejected. If it is not dominated by any individual then all the marked individuals are removed from $A(t)$ and we calculate the scaled rectilinear distance of offspring from each chromosome. The chromosome with the minimum scaled rectilinear distance is selected and maximum scaled absolute objective difference is calculated between offspring and the selected chromosome for all the objectives. If it is more than the territory size the offspring is accepted in archive population else it is rejected and a new offspring is generated.

Scaled Rectilinear Distance : $d_{i c}=\sum_{j=1}^{m}\left|f_{i j}-f_{i j}\right|$

Table 9
Result comparison for case 1.
Case 1 Results

| NSGA2 |  |  |  |  |  | EDATDEA |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission |
| 1 | $-11,030,750$ | 347,059 | 45 | $-1.1 \mathrm{E}+07$ | 289,658.9 | 1 | $-10,712,997$ | 232,352.4 | 45 | $-11,219,725$ | 242,626.2 |
| 2 | $-9,050,277$ | 235,867.1 | 46 | $-9,096,203$ | 235,905.2 | 2 | $-10,712,997$ | 232,352.4 | 46 | $-11,219,725$ | 242,626.2 |
| 3 | $-10,643,163$ | 298,675.8 | 47 | $-9,207,953$ | 238,807.8 | 3 | $-10,705,530$ | 231,870.4 | 47 | $-11,219,725$ | 242,626.2 |
| 4 | $-9,671,396$ | 251,475.4 | 48 | $-1 \mathrm{E}+07$ | 260,127.2 | 4 | $-10,705,530$ | 231,870.4 | 48 | $-10,755,657$ | 234,872.8 |
| 5 | $-9,893,197$ | 258,064.7 | 49 | $-9,238,191$ | 239,740.8 | 5 | $-11,234,206$ | 245,316.4 | 49 | $-11,238,108$ | 245,558.7 |
| 6 | $-9,853,696$ | 252,174.8 | 50 | $-9,238,191$ | 239,740.8 | 6 | $-11,234,206$ | 245,316.4 | 50 | $-11,238,108$ | 245,558.7 |
| 7 | $-10,983,164$ | 329,707.5 |  |  |  | 7 | $-11,232,414$ | 244,666.4 | 51 | $-10,755,657$ | 234,872.8 |
| 8 | $-10,338,694$ | 278,221.3 |  |  |  | 8 | $-11,331,716$ | 255,973.2 | 52 | $-10,758,946$ | 235,022.9 |
| 9 | $-10,060,984$ | 262,246.7 |  |  |  | 9 | $-11,331,716$ | 255,973.2 | 53 | $-11,052,644$ | 238,178.7 |
| 10 | $-10,258,478$ | 266,999.6 |  |  |  | 10 | $-11,405,757$ | 264,367.6 | 54 | $-10,702,263$ | 231,656 |
| 11 | $-11,021,451$ | 341,497.5 |  |  |  | 11 | $-11,241,306$ | 245,804.3 | 55 | $-11,219,725$ | 242,626.2 |
| 12 | $-10,815,117$ | 319,564.5 |  |  |  | 12 | $-11,052,644$ | 238,178.7 | 56 | $-11,219,725$ | 242,626.2 |
| 13 | $-10,197,881$ | 264,140.1 |  |  |  | 13 | $-11,052,644$ | 238,178.7 | 57 | $-10,709,220$ | 232,103.2 |
| 14 | $-10,517,909$ | 285,641.5 |  |  |  | 14 | $-11,052,644$ | 238,178.7 | 58 | $-11,361,206$ | 260,106.7 |
| 15 | $-10,988,922$ | 338,785.4 |  |  |  | 15 | $-10,689,899$ | 231,010.2 | 59 | $-11,342,554$ | 256,919.9 |
| 16 | $-10,784,906$ | 316,293.5 |  |  |  | 16 | $-10,756,548$ | 234,963.3 | 60 | $-11,340,458$ | 256,120.5 |
| 17 | $-10,560,847$ | 287,942.2 |  |  |  | 17 | $-10,756,548$ | 234,963.3 | 61 | $-10,672,581$ | 229,910.2 |
| 18 | $-10,156,063$ | 262,756.5 |  |  |  | 18 | $-10,766,326$ | 237,075.4 | 62 | $-10,672,581$ | 229,910.2 |
| 19 | $-9,424,456$ | 247,802 |  |  |  | 19 | $-10,766,326$ | 237,075.4 | 63 | $-10,672,581$ | 229,910.2 |
| 20 | $-10,620,877$ | 290,439.4 |  |  |  | 20 | $-11,396,779$ | 263,217.2 | 64 | $-10,709,220$ | 232,103.2 |
| 21 | $-10,334,420$ | 271,125.4 |  |  |  | 21 | $-11,396,779$ | 263,217.2 | 65 | $-11,259,088$ | 245,950.5 |
| 22 | $-10,007,710$ | 259,957.6 |  |  |  | 22 | $-11,259,250$ | 245,950.9 | 66 | $-11,259,088$ | 245,950.5 |
| 23 | $-10,700,860$ | 308,165.2 |  |  |  | 23 | $-11,375,700$ | 260,287.6 | 67 | $-11,201,475$ | 241,357 |
| 24 | $-10,968,930$ | 328,445.5 |  |  |  | 24 | $-11,375,700$ | 260,287.6 | 68 | $-10,668,145$ | 229,637.2 |
| 25 | $-9,296,967$ | 244,423.2 |  |  |  | 25 | $-11,373,293$ | 260,224 | 69 | $-10,691,334$ | 231,015.7 |
| 26 | $-9,321,177$ | 245,588.8 |  |  |  | 26 | $-11,166,740$ | 240,583.8 | 70 | $-11,216,216$ | 241,953.1 |
| 27 | $-9,252,024$ | 241,307.3 |  |  |  | 27 | $-11,166,740$ | 240,583.8 | 71 | $-11,216,216$ | 241,953.1 |
| 28 | $-10,722,710$ | 308,691.1 |  |  |  | 28 | $-10,761,384$ | 235,187.6 | 72 | $-11,216,216$ | 241,953.1 |
| 29 | $-9,512,751$ | 249,274 |  |  |  | 29 | $-10,761,384$ | 235,187.6 | 73 | $-11,216,216$ | 241,953.1 |
| 30 | $-9,577,666$ | 250,677.6 |  |  |  | 30 | $-10,761,384$ | 235,187.6 | 74 | $-11,216,216$ | 241,953.1 |
| 31 | $-10,485,544$ | 280,278.3 |  |  |  | 31 | $-10,761,384$ | 235,187.6 | 75 | $-11,216,216$ | 241,953.1 |
| 32 | $-10,896,427$ | 320,145.2 |  |  |  | 32 | $-11,265,508$ | 246,228.7 | 76 | $-11,216,216$ | 241,953.1 |
| 33 | $-9,880,993$ | 253,728.4 |  |  |  | 33 | $-11,173,612$ | 241,015.1 | 77 | $-11,015,514$ | 237,091.5 |
| 34 | $-10,686,161$ | 302,591.3 |  |  |  | 34 | $-11,344,758$ | 257,455.4 | 78 | $-11,050,839$ | 237,944.2 |
| 35 | $-9,129,640$ | 237,031.8 |  |  |  | 35 | $-11,027,866$ | 237,130.5 | 79 | $-11,355,981$ | 257,871.5 |
| 36 | $-10,771,354$ | 312,012.4 |  |  |  | 36 | $-11,027,866$ | 237,130.5 | 80 | $-10,670,750$ | 229,672.5 |
| 37 | $-10,681,586$ | 302,564.8 |  |  |  | 37 | $-11,376,782$ | 260,755.6 | 81 | $-11,209,739$ | 241,825.1 |
| 38 | $-10,898,631$ | 321,800.5 |  |  |  | 38 | $-11,238,108$ | 245,558.7 | 82 | $-11,015,514$ | 237,091.5 |
| 39 | $-10,284,666$ | 269,899.8 |  |  |  | 39 | $-11,344,758$ | 257,455.4 | 83 | $-11,265,683$ | 246,352.7 |
| 40 | $-9,172,400$ | 238,142.3 |  |  |  | 40 | $-11,344,758$ | 257,455.4 | 84 | $-11,265,683$ | 246,352.7 |
| 41 | $-10,916,238$ | 325,333.7 |  |  |  | 41 | $-11,088,997$ | 238,515.7 | 85 | $-10,698,896$ | 231,294 |
| 42 | $-9,619,662$ | 250,746.9 |  |  |  | 42 | $-11,070,970$ | 238,357.2 | 86 | $-10,734,124$ | 233,676.8 |
| 43 | $-10,405,744$ | 278,821.8 |  |  |  | 43 | $-11,070,970$ | 238,357.2 | 87 | $-11,407,541$ | 264,903.8 |
| 44 | $-10,500,335$ | 281,547.5 |  |  |  | 44 | $-11,224,090$ | 243,041.3 | 88 | $-11,239,224$ | 245,588.4 |

Table 10
Result comparison for case 4.

| Case 4 Results |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| NSGA2 |  |  |  |  |  | EDATDEA |  |  |  |  |  |
| S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission |
| 1 | $-2,942,443$ | 276,131 | 29 | $-1,393,470$ | 179,603.5 | 1 | $-3,557,960$ | 142,943.1 | 29 | $-3,662,372$ | 145,308.7 |
| 2 | $-1,355,944$ | 176,806.3 | 30 | $-2,136,335$ | 203,752.6 | 2 | $-2,683,082$ | 141,763.1 | 30 | $-3,662,372$ | 145,308.7 |
| 3 | $-1,867,569$ | 185,487.7 | 31 | $-1,920,161$ | 188,997.6 | 3 | $-2,676,942$ | 141,509.9 | 31 | $-3,712,549$ | 148,828.5 |
| 4 | $-1,588,644$ | 184,287 | 32 | $-2,458,661$ | 217,452.2 | 4 | $-3,648,335$ | 144,979.5 | 32 | $-3,638,969$ | 144,724.3 |
| 5 | $-2,778,550$ | 251,416.7 | 33 | $-2,784,999$ | 265,544.1 | 5 | $-3,648,335$ | 144,979.5 | 33 | $-3,638,969$ | 144,724.3 |
| 6 | $-2,779,540$ | 264,146.3 | 34 | $-2,300,375$ | 211,164.7 | 6 | $-3,648,335$ | 144,979.5 | 34 | $-3,638,969$ | 144,724.3 |
| 7 | $-2,549,840$ | 227,354 | 35 | $-2,727,687$ | 243,921.3 | 7 | $-3,557,960$ | 142,943.1 | 35 | $-3,638,969$ | 144,724.3 |
| 8 | $-2,490,890$ | 217,481.3 | 36 | $-2,180,149$ | 204,596.2 | 8 | $-3,557,960$ | 142,943.1 | 36 | $-3,638,969$ | 144,724.3 |
| 9 | $-2,292,353$ | 210,990 | 37 | $-2,578,679$ | 231,835.2 | 9 | $-3,662,598$ | 147,783.9 | 37 | $-3,781,851$ | 152,620.2 |
| 10 | $-2,757,879$ | 249,024.1 | 38 | $-2,066,267$ | 199,722.2 | 10 | $-3,662,598$ | 147,783.9 | 38 | $-3,559,755$ | 142,978.5 |
| 11 | $-2,341,494$ | 213,600.3 | 39 | $-2,916,221$ | 275,000.6 | 11 | $-3,662,598$ | 147,783.9 | 39 | $-3,570,173$ | 143,062.4 |
| 12 | $-2,238,522$ | 205,998.7 | 40 | $-2,613,653$ | 234,556 | 12 | $-3,662,598$ | 147,783.9 | 40 | $-3,570,173$ | 143,062.4 |
| 13 | $-2,042,398$ | 196,219.4 | 41 | $-1,534,702$ | 182,953.6 | 13 | $-3,662,598$ | 147,783.9 | 41 | $-3,721,430$ | 150,067.4 |
| 14 | $-2,660,806$ | 239,066.1 | 42 | $-1,361,045$ | 176,919.1 | 14 | $-3,720,481$ | 149,978.7 | 42 | $-3,712,333$ | 148,586.4 |
| 15 | $-2,510,079$ | 223,596.5 | 43 | $-1,456,286$ | 181,671.5 | 15 | $-3,553,125$ | 142,679.9 | 43 | $-3,712,333$ | 148,586.4 |
| 16 | $-2,008,183$ | 194,822.5 | 44 | $-2,668,509$ | 239,597 | 16 | $-3,553,125$ | 142,679.9 | 44 | $-3,581,395$ | 143,227.6 |
| 17 | $-2,827,142$ | 267,203.4 | 45 | $-2,231,408$ | 205,957.2 | 17 | $-3,555,055$ | 142,761.3 | 45 | $-3,581,395$ | 143,227.6 |
| 18 | $-2,617,651$ | 234,707.2 | 46 | $-1,984,829$ | 192,053.9 | 18 | $-3,785,043$ | 154,479.7 | 46 | $-3,723,427$ | 150,090.6 |
| 19 | $-2,431,421$ | 215,214.2 | 47 | $-1,570,292$ | 183,554.9 | 19 | $-3,785,043$ | 154,479.7 | 47 | $-3,723,427$ | 150,090.6 |
| 20 | $-2,382,693$ | 214,948.8 | 48 | $-1,986,293$ | 192,164 | 20 | $-3,785,043$ | 154,479.7 | 48 | $-3,641,909$ | 144,747.4 |
| 21 | $-1,936,295$ | 190,436.5 | 49 | $-2,100,664$ | 202,433.8 | 21 | $-3,713,494$ | 149,179.9 | 49 | $-3,581,395$ | 143,227.6 |
| 22 | $-2,870,556$ | 273,908 | 50 | $-2,695,570$ | 241,951.2 | 22 | $-3,713,494$ | 149,179.9 | 50 | $-2,701,190$ | 141,861 |
| 23 | $-2,738,798$ | 244,896.4 |  |  |  | 23 | $-3,786,651$ | 154,532.4 | 51 | $-3,587,535$ | 143,493.7 |
| 24 | $-1,884,421$ | 187,651 |  |  |  | 24 | $-3,786,651$ | 154,532.4 | 52 | $-3,588,074$ | 143,707.2 |
| 25 | $-2,571,232$ | 231,650.7 |  |  |  | 25 | $-3,786,651$ | 154,532.4 | 53 | $-3,710,132$ | 147,821.1 |
| 26 | $-2,515,186$ | 224,002.3 |  |  |  | 26 | $-3,786,651$ | 154,532.4 | 54 | $-3,747,470$ | 151,279.1 |
| 27 | $-1,506,260$ | 182,274.9 |  |  |  | 27 | $-3,786,651$ | 154,532.4 | 55 | $-3,712,843$ | 149,158.1 |
| 28 | $-2,844,914$ | 272,426.4 |  |  |  | 28 | $-3,811,854$ | 154,588.5 | 56 | $-3,568,971$ | 142,980 |

Table 11
Result comparison for case 5.

| Case 5 Results |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| NSGA2 |  |  |  |  |  | EDATDEA |  |  |  |  |  |
| S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission |
| 1 | $-5,102,644$ | 620,869.7 | 26 | $-2,995,743$ | 408,863.9 | 1 | $-5,346,696$ | 366,779 | 26 | $-5,943,054$ | 393,253 |
| 2 | $-1,981,499$ | 348,686.3 | 27 | $-3,611,723$ | 440,554 | 2 | $-5,346,696$ | 366,779 | 27 | $-5,894,274$ | 387,854.9 |
| 3 | $-4,340,781$ | 468,100.9 | 28 | $-4,859,023$ | 559,050.5 | 3 | $-5,951,108$ | 394,583.6 | 28 | $-5,454,362$ | 367,187.2 |
| 4 | $-3,358,509$ | 425,191.5 | 29 | $-3,856,137$ | 448,306.2 | 4 | $-5,969,096$ | 395,027.3 | 29 | $-5,454,362$ | 367,187.2 |
| 5 | $-4,348,859$ | 502,628.4 | 30 | $-3,892,079$ | 448,953.9 | 5 | $-5,969,096$ | 395,027.3 | 30 | $-5,454,362$ | 367,187.2 |
| 6 | $-2,871,121$ | 401,894.3 | 31 | $-4,984,418$ | 615,537 | 6 | $-5,491,372$ | 369,310.2 | 31 | $-5,974,262$ | 395,570 |
| 7 | $-4,461,301$ | 525,732.3 | 32 | $-2,636,618$ | 391,291.7 | 7 | $-5,926,718$ | 391,252.5 | 32 | $-5,974,262$ | 395,570 |
| 8 | $-4,562,344$ | 537,312.6 | 33 | $-3,074,835$ | 416,787.8 | 8 | $-5,926,718$ | 391,252.5 | 33 | $-5,974,262$ | 395,570 |
| 9 | $-4,891,770$ | 560,318.2 | 34 | $-4,752,770$ | 553,938.5 | 9 | $-5,479,489$ | 368,378.3 | 34 | $-5,487,753$ | 368,802.6 |
| 10 | $-4,906,338$ | 588,928.8 | 35 | $-5,057,072$ | 618,321 | 10 | $-5,479,489$ | 368,378.3 | 35 | $-5,938,210$ | 391,946.3 |
| 11 | $-4,368,002$ | 504,996.3 | 36 | $-2,130,557$ | 355,665.9 | 11 | $-5,913,935$ | 390,625.3 | 36 | $-5,939,985$ | 392,950 |
| 12 | $-4,692,324$ | 545,654.3 | 37 | $-2,301,233$ | 383,119.6 | 12 | $-5,913,935$ | 390,625.3 | 37 | $-5,876,597$ | 387,178.1 |
| 13 | $-3,271,731$ | 421,896.2 | 38 | $-2,221,551$ | 380,772.9 | 13 | $-5,528,216$ | 369,860.1 | 38 |  |  |
| 14 | $-2,178,244$ | 374,582 | 39 | $-2,997,823$ | -2,997,823 | 14 | $-5,528,216$ | 369,860.1 | 39 |  |  |
| 15 | $-2,375,565$ | 387,656 | 40 | $-3,986,339$ | 454,190.6 | 15 | $-5,612,377$ | 378,274.3 | 40 |  |  |
| 16 | $-2,540,412$ | 389,441.3 | 41 | $-3,666,372$ | 443,113.1 | 16 | $-5,491,372$ | 369,310.2 | 41 |  |  |
| 17 | $-3,594,576$ | 429,563.7 | 42 | $-4,012,832$ | 456,890.5 | 17 | $-5,596,572$ | 377,152.4 | 42 |  |  |
| 18 | $-2,788,734$ | 391,981.3 | 43 | $-4,124,734$ | 459,853.7 | 18 | $-5,596,572$ | 377,152.4 | 43 |  |  |
| 19 | $-2,171,458$ | 356,011.5 | 44 | $-2,705,465$ | 391,406.9 | 19 | $-5,943,054$ | 393,253 | 44 |  |  |
| 20 | $-3,089,633$ | 418,388.2 | 45 | $-4,738,558$ | 553,428.2 | 20 | $-5,943,054$ | 393,253 | 45 |  |  |
| 21 | $-4,923,700$ | 600,736 | 46 | $-4,246,350$ | 461,279.3 | 21 | $-5,943,054$ | 393,253 | 46 |  |  |
| 22 | $-3,716,481$ | 445,852.6 | 47 | $-4,921,209$ | 591,067.4 | 22 | $-5,943,054$ | 393,253 | 47 |  |  |
| 23 | $-4,503,128$ | 527,689.8 | 48 | $-4,123,259$ | 457,850.4 | 23 | $-5,943,054$ | 393,253 | 48 |  |  |
| 24 | $-4,941,486$ | 611,241.7 | 49 | $-3,597,500$ | 430,305.4 | 24 | $-5,602,919$ | 377,767.7 | 49 |  |  |
| 25 | $-2,030,431$ | 352,677.9 | 50 | $-4,319,033$ | 466,904.3 | 25 | $-5,602,919$ | 377,767.7 | 50 |  |  |

$m=$ number of objective, $i=$ chromosome number varies from 1 to number of chromosomes in archive population, $f=$ normalized value of the objective function, $c=$ offspring chromosome.

Maximum Scaled Absolute Objective Difference : $\delta$
$=\max \left|f_{i j}-f_{i j}\right|$
$i^{\circ}=$ chromosome with minimum scaled rectilinear distance, $f=$ normalized value of the objective function, $c=$ offspring chromosome.

# 4. Simulation result 

In this paper, we used a hybrid TDEA algorithm to solve the closed loop green supply chain problem. The proposed model

Table 12
Result comparison for case 8 .

| Case 8 Results |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| NSGA2 |  |  |  |  | EDATDEA |  |  |  |  |  |
| S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit |
| 1 | $-17,769,736$ | 934,387.6 | 26 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 788,443 | 1 | $-21,128,923$ | 667,710.3 | 26 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 634,916.2 |
| 2 | $-14,630,244$ | 739,196.3 | 27 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 746,731.7 | 2 | $-20,810,955$ | 634,224.9 | 27 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 639,424 |
| 3 | $-17,675,534$ | 887,663.2 | 28 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 766,053.8 | 3 | $-21,339,313$ | 688,405 | 28 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 639,424 |
| 4 | $-17,753,200$ | 934,139.4 | 29 | $-1.8 \mathrm{E} \cdot \mathrm{O} 7$ | 884,116.9 | 4 | $-21,339,313$ | 688,405 | 29 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 690,535.2 |
| 5 | $-16,378,278$ | 831,608.2 | 30 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 859,305.7 | 5 | $-21,339,313$ | 688,405 | 30 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 690,535.2 |
| 6 | $-16,104,488$ | 787,483.1 | 31 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 756,544.6 | 6 | $-21,339,313$ | 688,405 | 31 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 690,535.2 |
| 7 | $-16,878,681$ | 867,931.4 | 32 | $-1.8 \mathrm{E} \cdot \mathrm{O} 7$ | 881,885.4 | 7 | $-21,339,313$ | 688,405 | 32 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 640,363.7 |
| 8 | $-15,723,647$ | 771,811.6 | 33 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 835,652.2 | 8 | $-20,983,763$ | 639,114.8 | 33 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 640,363.7 |
| 9 | $-16,344,211$ | 806,895.2 | 34 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 750,628.6 | 9 | $-21,228,293$ | 669,107 | 34 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 686,857.1 |
| 10 | $-17,187,145$ | 872,663.4 | 35 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 856,076.9 | 10 | $-21,228,293$ | 669,107 | 35 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 634,526 |
| 11 | $-15,397,218$ | 766,241.3 | 36 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 748,352.5 | 11 | $-21,273,159$ | 682,534.9 | 36 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 634,526 |
| 12 | $-17,468,442$ | 875,165 | 37 | $-1.3 \mathrm{E} \cdot \mathrm{O} 7$ | 755,152.5 | 12 | $-21,309,190$ | 683,298.9 | 37 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 634,526 |
| 13 | $-14,861,116$ | 751,431.8 | 38 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 864,666 | 13 | $-21,249,375$ | 670,070.9 | 38 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 634,526 |
| 14 | $-15,170,317$ | 752,264 | 39 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 754,524.9 | 14 | $-21,249,375$ | 670,070.9 | 39 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 685,886.3 |
| 15 | $-16,330,524$ | 805,973.5 | 40 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 774,295.6 | 15 | $-21,241,728$ | 670,005.5 | 40 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 685,886.3 |
| 16 | $-16,269,077$ | 788,443 | 41 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 834,409.9 | 16 | $-20,984,482$ | 639,198.2 | 41 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 682,534.9 |
| 17 | $-15,921,163$ | 781,086.5 | 42 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 839,510.7 | 17 | $-21,364,334$ | 688,526.6 | 42 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 682,534.9 |
| 18 | $-15,921,163$ | 781,086.5 | 43 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 839,510.7 | 18 | $-21,364,334$ | 690,359.6 | 43 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 682,534.9 |
| 19 | $-16,528,814$ | 852,748.4 | 44 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 852,960.1 | 19 | $-21,273,159$ | 682,534.9 | 44 | $-2.1 \mathrm{E} \cdot \mathrm{O} 7$ | 682,534.9 |
| 20 | $-16,480,470$ | 839,696.8 | 45 | $-1.5 \mathrm{E} \cdot \mathrm{O} 7$ | 742,888.1 | 20 | $-21,273,159$ | 682,534.9 |  |  |  |
| 21 | $-15,301,896$ | 761,594.3 | 46 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 857,941.2 | 21 | $-21,273,159$ | 682,534.9 |  |  |  |
| 22 | $-15,793,036$ | 777,799.4 | 47 | $-1.6 \mathrm{E} \cdot \mathrm{O} 7$ | 772,733 | 22 | $-21,273,159$ | 682,534.9 |  |  |  |
| 23 | $-17,533,063$ | 879,471.8 | 48 | $-1.8 \mathrm{E} \cdot \mathrm{O} 7$ | 887,196.3 | 23 | $-21,289,887$ | 682,930.5 |  |  |  |
| 24 | $-16,799,833$ | 860,011.5 | 49 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 859,299.4 | 24 | $-21,289,887$ | 682,930.5 |  |  |  |
| 25 | $-15,908,330$ | 780,539.5 | 50 | $-1.7 \mathrm{E} \cdot \mathrm{O} 7$ | 863,838.8 | 25 | $-20,854,102$ | 634,916.2 |  |  |  |

was evaluated for robustness on nine test problems. The data were randomly chosen and modification in the design of supply chain was done. To check the performance of the proposed algorithm, comparison was made with NSGA II. First we tune the parameters for both the algorithms by selecting different values of a parameter and selecting the one with the best results. Then results for same problem at optimal parameter setting were compared for both the algorithms to check the performance of both algorithms. Time of run for both the algorithms was kept as 600 s and an initial population of 50 was selected for both the algorithms The performance of hybrid TDEA algorithm is tested on different problem sets. It should be noted that same number of generations and same population sizes are used for both algorithms. For the fare comparison
we test the result of NSGA II on different parameters and select the best parameter. To select the best parameter we have run both algorithms on different parameter and after comparison we select the best parameter. Tables 1 and 2 show the parameter result comparison.

Tables 3-6 show the NSGA II results on different parameters. Fig. 5 shows the Pareto optimal front of NSGA II algorithm for different crossover and mutation probability. From the following table and figure we have selected the best parameter values for NSGA II algorithm.

Fig. 6 shows the Pareto optimal front of EDATDEA for different crossover and mutation probability. From the following table and

Table 13
Result comparison for case 9 .

| Case 9 Results |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| NSGA2 |  |  |  |  |  |  | EDATDEA |  |  |
| S.No. | Profit | Emission | S.No. | Profit | Emission | S.No. | Profit | Emission |  |
| 1 | $-19,479,692$ | 1,563,928 | 21 | $-18,001,959$ | 1,438,370 | 1 | $-26,770,218$ | 1,197,533 |  |
| 2 | $-18,160,180$ | 1,444,788 | 22 | $-19,567,763$ | 1,566,029 | 2 | $-27,091,418$ | 1,242,182 |  |
| 3 | $-18,001,954$ | 1,438,369 | 23 | $-19,097,446$ | 1,557,936 | 3 | $-27,816,817$ | 1,268,617 |  |
| 4 | $-18,085,698$ | 1,441,312 | 24 | $-19,630,053$ | 1,566,159 | 4 | $-26,734,562$ | 1,196,256 |  |
| 5 | $-18,084,392$ | 1,440,933 | 25 | $-18,661,657$ | 1,515,031 | 5 | $-26,797,619$ | 1,227,237 |  |
| 6 | $-18,600,746$ | 1,511,230 | 26 | $-18,601,487$ | 1,511,311 | 6 | $-26,757,695$ | 1,196,703 |  |
| 7 | $-18,274,242$ | 1,448,180 | 27 | $-19,068,646$ | 1,557,194 | 7 | $-27,103,778$ | 1,242,421 |  |
| 8 | $-19,488,781$ | 1,563,974 | 28 | $-18,687,362$ | 1,515,903 | 8 | $-27,103,778$ | 1,242,421 |  |
| 9 | $-18,483,841$ | 1,503,116 | 29 | $-19,641,946$ | 1,568,710 | 9 | $-27,103,778$ | 1,242,421 |  |
| 10 | $-18,663,833$ | 1,515,038 | 30 | $-18,075,253$ | 1,439,440 | 10 | $-26,734,562$ | 1,196,256 |  |
| 11 | $-18,301,749$ | 1,453,177 | 31 | $-19,439,517$ | 1,561,703 | 11 | $-27,131,033$ | 1,242,540 |  |
| 12 | $-18,578,102$ | 1,505,581 | 32 | $-18,600,740$ | 1,511,227 | 12 | $-27,131,033$ | 1,242,540 |  |
| 13 | $-18,584,438$ | 1,507,649 | 33 | $-19,565,573$ | 1,564,274 | 13 | $-26,722,584$ | 1,195,558 |  |
| 14 | $-18,088,401$ | 1,444,468 | 34 | $-18,000,173$ | 1,434,987 | 14 | $-26,722,584$ | 1,195,558 |  |
| 15 | $-18,457,119$ | 1,502,059 | 35 | $-18,866,957$ | 1,555,950 |  |  |  |  |
| 16 | $-19,429,503$ | 1,560,343 | 36 | $-18,225,235$ | 1,444,966 |  |  |  |  |
| 17 | $-18,301,794$ | 1,453,306 | 37 | $-18,483,764$ | 1,503,115 |  |  |  |  |
| 18 | $-18,075,331$ | 1,439,441 | 38 | $-18,640,814$ | 1,514,107 |  |  |  |  |
| 19 | $-18,577,529$ | 1,505,243 | 39 | $-19,569,108$ | 1,566,082 |  |  |  |  |
| 20 | $-18,296,790$ | 1,448,313 |  |  |  |  |  |  |  |

figure we have selected the best parameter values for NSGA II algorithm.

In this paper we have select 9 cases to test our results. Following Table 7 shows the cases under we run both the algorithms. For fare comparison we have run the algorithm for same time. We have run both the algorithms for 600 s and calculate the profit and carbon dioxide emission.

Table 8 shows the performance comparison for different cases. A comparison of maximum profit, minimum carbon dioxide emission, average profit and average emission obtaining from EDATDEA and NSGAII algorithm is as shown in following table. We have used small size, minimum size and large size problem to compare the result of EDATDEA and NSGAII. As shown in table EDATDEA has performed better than NSGAII for all cases.

Following Figs. 7-11 and Tables 9-13 show the Pareto front comparison of EDATDEA and NSHGA II algorithm for different cases. For different cases Figures shows that the EDATDEA has better Pareto front than the NSGA II algorithm. EDATDEA can get the near optimal value in limited number of iteration. From figure we can say that EDATDEA performs better than NSGAII in all cases and has the better results.

## 5. Conclusions

Closed loop green supply chain management in semiconductor industries has received much attention in last few years as it allows reducing the carbon dioxide emission and increasing the profit of total supply chain. We have considered a closed loop supply chain with nine echelons, five are in forward direction and four are in reverse direction for carrying back used products and extracting value from it. To solve our model we proposed a new approach named EDATDEA. In order to verify our proposed approach, we have applied EDATDEA on different cases of supply chain and compare with well know approach NSGA II. From the result we can say that this model can be used for the real life problem. The results clearly show that the EDATDEA approach performs better than NSGA II algorithm. EDATDEA can get the near optimal results in limited number of time. In future we can implement some new techniques and model to solve the Green supply chain problem in semiconductor industries. This model can be useful for any industry. In future we can use the real data set or industry to check the applicability of the proposed model.

## References

Abdolhossein, S., Ismail, N., Ariffin, M. K. A., Zulkifli, N., Mirabi, H., \& Nikbakht, M. (2012). A closed loop supply chain networks: An overview. International Journal of Innovative Ideas, 12(4), 1-6.
Brandenburga, M., Kannan, G., Sarkis, J., \& Seuring, S. (2014). Quantitative models for sustainable supply chain management: Developments and directions. European Journal of Operation Research, 233, 299-312.
Canan, R. S., Bhattacharya, S., Luk, N., \& Wassenhove, Van. (2004). Closed-loop supply chain models with product remanufacturing. Management Science, 50(2), 239-252.
Deh, K., Pratap, A., Agarwal, S., \& Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transaction on Evolutionary Computation, 6(2), 182-197.
Eastern Research Group (1999). Preferred and alternative methods for estimation air emissions from semiconductor manufacturing (Vol. 2). EIIP.

Faccio, M., Persona, A., Sgarbossa, F., \& Zanin, G. (2011). Multi-stage supply network design in case of reverse flows: A closed-loop approach. International Journal of Operation Research, 12(2), 157-191.
Faccio, M., Persona, A., Sgarbossa, F., \& Zanin, G. (2014). Sustainable SC through the complete reprocessing of end-of-life products by manufacturers: A traditional versus social responsibility company perspective. European Journal of Operation Research, 233, 359-373.
Fallah, T., Sahraetan, R., Tavakkoli, M. R., \& Moeinipour, M. (2012). An interactive possibilistic programming approach for a multi-objective closed loop supply chain network under uncertainty. International Journal of System Science, 45(3), 283-299.
Georgiadis, P., \& Vlachos, D. (2004). The effect of environmental parameters on product recovery. European Journal of Operational Research, 157, 449-464.
Giovanni, P. D. (2014). Environmental collaboration in a closed-loop supply chain with a reverse revenue sharing contract. Annals of Operation Research, 220, 135-157.
Guide, V. D. R., Jr., \& Van, W. L. N. (2009). The evolution of closed-loop supply chain research. Operation Research, 57, 10-18.
Gungor, A., \& Gupta, S. (1998). Disassembly sequence planning for products with defective parts in product recovery. Computers and Industrial Engineering, 35(1-2), 161-164.
Gungor, A., \& Gupta, S. (1999). Issues in environmentally conscious manufacturing and product recovery: A survey. Computers and Industrial Engineering, 36, 811-853.
Gupta, S., \& Isaacs, J. (1997). Value analysis of disposal strategies for automobiles. Computers and Industrial Engineering, 33(1-2), 325-328.
Kannan, G., \& Popiuc, M. N. (2014). Reverse supply chain coordination by revenue sharing contract: A case for the personal computers industry. European Journal of Operation Research, 233, 326-336.
Kannan, G., Sasikumar, P., \& Devika, K. (2010). A genetic algorithm approach for solving a closed loop supply chain model: A case study of battery recycling. Journal of Applied Mathematics Modeling, 34, 655-670.
Karabas, I., \& Oksalan, M. K. (2010). A territory defining multiobjective evolutionary algorithms and preference incorporation. IEEE Transaction on Evolutionary Computation, 14(4), 636-664.
Koh, S.-G., Hwang, H., Sohn, K.-I., \& Ko, C.-S. (2002). An optimal ordering and recovery policy for reusable items. Computers and Industrial Engineering, 43, 59-73.
Larrahaga, P., \& Lozano, J. A. (2002). Estimation of distribution algorithms: A new tool for evolutionary computation.Boston: Kluwer Academic Publishers.
Lambert, A. (2002). Determining optimum disassembly sequences in electronic equipment. Computers and Industrial Engineering, 43, 553-575.
Lee, J. E., \& Lee, K. D. (2013). Modeling and optimization of closed-loop supply chain considering order or next arrival of goods. International Journal of Innovative Computing, Information and Control, 9(9), 3539-3654.
Lu, L., Qi, X., \& Liu, Z. (2014). On the cooperation of recycling operation. European Journal of Operation Research, 233, 349-358.
Meade, L., \& Sarkis, J. (2007). The theory and practice of reverse logistics. International Journal of Logistics, 3(1), 56-84.
Mutha, A., \& Pokharel, S. (2009). Strategic network design for reverse logistics and remanufacturing using new and old product modules. Computers $\mathcal{E}$ Industrial Engineering, 56, 334-346.
Nakamura, S., \& Kondo, Y. (2006). A waste input-output life-cycle cost analysis of the recycling of end-of-life electrical home appliances. Ecological Economics, 57, 494-506.
Özkor, V., \& Baslıgil, H. (2013). Multi-objective optimization of closed-loop supply chains in uncertain environment. Journal of Cleaner Production, 41, 114-125.
Pan, Q. K., \& Ruiz, R. (2012). An estimation of distribution algorithm for lotstreaming flow shop problems with setup times. Omega, 40, 166-180.
Pohlen, T., \& Farris, M. (1992). Reverse logistics in plastics recycling. International Journal of Physical Distribution and Logistics Management, 22(7), 35-47.
Sarkis, J. (2003). A strategic decision framework for green supply chain management. Journal of Cleaner Production, 11(4), 397-409.
Shim, V. A., Tan, K. C., \& Chia, J. Y. (2013). Multi-objective optimization with estimation of distribution algorithm in a noisy environment. Evolutionary Computation, 21, 149-177.
Srivastava, S. K. (2007). Green supply-chain management: A state-of-the-art literature review. International Journal of Management Reviews, 9(1), 53-80.
Sun, J. Y., Zhang, Q. F., \& Edward, P. K. (2005). EDA: A new evolutionary algorithm for global optimization. Information Sciences, 169, 249-262.
United States Environmental Protection Agency (2005). Average carbon dioxide emission resulting from gasoline and diesel fuel. EPA420-F-05-001.
Yang, C. S., Lu, C. S., Haider, J. J., \& Marlow, P. B. (2013). The effect of green supply chain management on green performance and firm competitiveness in the context of container shipping in Taiwan. Transportation Research, E, 55, 55-73.