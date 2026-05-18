## 2 Small Worlds and Large Worlds

### 2.1 Garden of Forking Data

[1, pp. 23]
<img src="./fig-2.2.png" width="500"><br/><br/>

Given a conjecture $A = [1,0,1]$

where
- $1$ is the color blue
- $0$ is the color white

<br/>

##### 2.1.1 Counting Possibilities

|           |   Conjecture    |   Ways to produce  1-0-1  |
|-----------|-------------|-------------------------------|
|   $c_1$   |   0-0-0-0   |   $0 \times 4 \times 0 = 0$   |
|   $c_2$   |   1-0-0-0   |   $1 \times 3 \times 1 = 3$   |
|   $c_3$   |   1-1-0-0   |   $2 \times 2 \times 2 = 8$   |
|   $c_4$   |   1-1-1-0   |   $3 \times 1 \times 3 = 9$   |
|   $c_5$   |   1-1-1-1   |   $4 \times 0 \times 4 = 0$   |


<br/>

##### 2.1.2 Combining Other Information

[1, pp. 25]

- We will first assume all conjectures are equal in probability
- Then, comparing "Ways to produce", we decide $p(c_4) > p(c_3) > p(c_2)$
- Then, we have priors (0,3,8,9,0)
- We update our assumptions
- Multiplication of prior and new counts is to enumerate all the combinatorial "paths"

|| Conjecture | Ways to produce 1  | Prior counts | New count |    
|-|-|-|-|-|
| $c_1$ | 0-0-0-0 | $0$ | $0$ | $0 \times 0 =  0$ |
| $c_2$ | 1-0-0-0 | $1$ | $3$ | $1 \times 3 =  3$ |
| $c_3$ | 1-1-0-0 | $2$ | $8$ | $2 \times 8 = 16$ |
| $c_4$ | 1-1-1-0 | $3$ | $9$ | $3 \times 9 = 27$ |
| $c_5$ | 1-1-1-1 | $4$ | $0$ | $4 \times 0 =  0$ |

<br/><br/>

|| Hypothesis | Likelihood | Prior | Posterior |    
|-|-|-|-|-|
| $c_1$ | 0-0-0-0 | $0$ | $0$ | $0 \times 0 =  0$ |
| $c_2$ | 1-0-0-0 | $1$ | $3$ | $1 \times 3 =  3$ |
| $c_3$ | 1-1-0-0 | $2$ | $8$ | $2 \times 8 = 16$ |
| $c_4$ | 1-1-1-0 | $3$ | $9$ | $3 \times 9 = 27$ |
| $c_5$ | 1-1-1-1 | $4$ | $0$ | $4 \times 0 =  0$ |


<br/><br/>


### 2.2 Building a Model

##### 2.2.2 Bayesian Updating
[1, pp. 29]

<img src="./IMG_5135345A6617-1.jpeg" />

**Reference(s)**
1. R. McElreath, Statistical Rethinking