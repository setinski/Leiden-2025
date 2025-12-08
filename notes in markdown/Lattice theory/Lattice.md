---
tags: definition
---

Fix any norm $\|\cdot\|$ on $\mathbb{R}^{n}$.

>[!define] #definition
>##### Lattice
>A lattice $\mathcal{L}$ is a discrete^[In the sense that, endowed with the subspace topology of $\mathbb{R}^{n}$, it is discrete, i.e. every point is open. Concretely, for every $x \in \mathcal{L}$, there exists $\delta > 0$ such that $B_{\delta}(x) \cap \mathcal{L} = \{x\}$. ] additive subgroup of $\mathbb{R}^{n}$ for some $n \in \mathbb{N}$. We set $\dim(\mathcal{L}) \coloneq \dim(\operatorname{span} \mathcal{L})$.

>[!info] Note
>Every lattice $\mathcal{L}$ is *uniformly discrete*, in the sense that there exists $\delta > 0$ such that for every $x \in \mathcal{L}$, $B_\delta(x) \cap \mathcal{L} = \{ x \}$.
>>[!The proof is immediate]-
>>Assume, by way of contradiction, that for all $\delta > 0$ there exists some $x_{\delta} \in \mathcal{L}$ such that $B_{\delta}(x_{\delta}) \cap \mathcal{L} \neq \{ x_{\delta} \}$. If $y_{\delta} \in B_{\delta}(x_{\delta}) \setminus \{ x_{\delta} \}$, then $y_{\delta} - x_{\delta} \in \mathcal{L}$ and $0 < \| y_{\delta} - x_{\delta} \| < \delta$. Hence for all $\delta > 0$, we have $B_{\delta}(0) \cap \mathcal{L} \setminus \{ 0 \} \ni y_{\delta} - x_{\delta}$, which contradicts the discreteness of $\mathcal{L}$.

>[!proposition] 
>$0 \neq \mathcal{L} \leq (\mathbb{R}^{n},+)$ is discrete if and only if it admits a non-zero minimal distance, i.e. $\lambda_{1}(\mathcal{L}) \coloneq\min_{x\neq y \in \mathcal{L}}\|y - x\| > 0$.

>##### Proof
>If $\mathcal{L}$ admits a minimal distance $\delta$, then it is clearly discrete: for every $x \in \mathcal{L}$, $B_{\frac{\delta}{2}}(x) \cap \mathcal{L} = \{x\}$.
>
>Let now  $\mathcal{L}$ be a lattice, hence uniformly discrete.  Notice that $$\lambda_{1}(\mathcal{L}) = \min_{x\neq y \in \mathcal{L}}\|y - x\| = \min_{x \in L} \min_{y \in \mathcal{L} \setminus \{ x \}}\|y - x\| = \min_{y \in \mathcal{L} \setminus \{ 0 \}}\|y\|,$$
>where the latter equality holds because if $\tilde{y}$ is a minimum for $y \in \mathcal{L} \setminus \{ x \} \mapsto \|y-x\|$, then $\tilde{y} - x \in \mathcal{L}$. By uniform discreteness, $a \coloneq\inf_{y \in \mathcal{L} \setminus \{ 0 \}}\|y\|$ is strictly positive. By definition of infimum, there exists a sequence $\{ y_{n} \} \in \mathcal{L}^{\mathbb{N}}$ such that $0 < \|y_{n}\| < a + \frac{1}{n}$. By the squeeze theorem, the limit $y \coloneq \lim_{ n} y_{n}$ exists and by continuity of the norm, $\|y\| = a$. Since every convergent sequence in $\mathbb{R}^{n}$ is Cauchy, eventually $\|y_{n} - y_{m}\| < a$. However, since $y_{n} - y_{m} \in \mathcal{L}$, we decuce that $\{ y_{n} \}_{n \in \mathbb{N}}$ is eventually constant, hence $y \in \mathcal{L}$ and $\|y\| = a = \lambda_{1}(\mathcal{L})$.

>[!example] As an ==#exercise==
>Give an example of:
>- a finitely generated subgroup of $\mathbb{R}$ which does not admit a minimal distance (which therefore is not discrete);
>- a discrete subset (but not uniformly) of $\mathbb{R}$ which is not a group and does not admit a minimal distance.

>[!Solution]-
>An example of the latter is the set $\left\{ \frac{1}{n} \mid n \in \mathbb{N} \right\}$ (this is obvious). An example of the former is the group $G \coloneq \mathbb{Z} + \pi \mathbb{Z}$ (this is less obvious). The reason why $G$ does not admit a minimal distance is that the set $A \coloneq \{ \{m \pi\} \mid m \in \mathbb{Z}\} \subseteq G$ is dense in $[0,1]$. Let us prove that $A$ does not admit an element of minimal distance. For all $n \in \mathbb{N}$, dividing $[0,1]$ in $n$ subintervals of length $\frac{1}{n}$, we see that by the pidgeonhole principle (given $n+1$ elements of $A$, at least two of them lie in the same exact subinterval) we can find $m \neq k \in \mathbb{N}$ and $h,j \in \mathbb{N}$ such that $|m\pi - k - h\pi + j| = |(m-h)\pi - (k-j)| = \{(m-h)\pi\} < \frac{1}{n}$.