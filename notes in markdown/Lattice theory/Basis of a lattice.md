---
tags: definition
aliases: basis
---

>[!define] #definition
>##### Basis of a [[Lattice]]
>A matrix $\mathbf{B} = [\mathbf{b}_{1}, \ldots, \mathbf{b}_{k}] \in \mathbb{R}^{n \times k}$ is a ==basis== of a lattice $\mathcal{L}$ if $\mathcal{L}(\mathbf{B}) \coloneq \mathbf{B} \cdot  \mathbb{Z}^k = \mathcal{L}$ and $\operatorname{rk}(\mathbf{B}) = k$.

>[!lemma] 
>Let $L'$ be a lattice admitting a basis $\mathbf{B}$ and let $L$ be a superlattice of $L'$ of the same dimension. The quotient group $L/L'$ is finite.

>##### Proof
>Since $L$ and $L'$ have the same dimension, we have $\operatorname{Span}_{\mathbb{R}}L' = \mathbf{B} \cdot \mathbb{Z}^{k} = \operatorname{Span}_{\mathbb{R}}L$. Since [[Fundamental parallelogram|the fundamental parallelepiped is a tiling]] for $L'$, any $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}} L$ can be written uniquely as $\mathbf{x} + \mathbf{e}$, for $\mathbf{x} \in L'$ and $\mathbf{e} \in \mathcal{P}(\mathbf{B})$. Note that since $L' \subseteq L$, $\mathbf{e} \in L$. Consider the map
>$$\begin{align*}
>\varphi \colon L &\to \mathcal{P}(\mathbf{B}) \cap L\\
>\mathbf{t} &\mapsto \mathbf{e}
>\end{align*}$$
>Note that $L' \subseteq \ker \varphi$, which implies $|L/L'| \leq |L/\ker \varphi| = |\operatorname{im} \varphi| \leq |\mathcal{P}(\mathbf{B}) \cap L|$. To conclude we note that $|\mathcal{P}(\mathbf{B}) \cap L|$ is finite. Indeed, the set $\mathcal{P}(\mathbf{B}) \cap L$ is uniformly discrete (since so is $L$) and is bounded (since so is $\mathcal{P}(\mathbf{B})$). By uniform discreteness, there exists $\varepsilon > 0$ such that $B_{\varepsilon}(x) \cap B_{\varepsilon}(y) = \varnothing$ for all $x\neq y \in \mathcal{P}(\mathbf{B}) \cap L$. The set $S \coloneq \bigsqcup\limits_{x \in \mathcal{P}(\mathbf{B}) \cap L} B_{\varepsilon}(x)$ is bounded (and in particular has finite volume) by boundedness of $\mathcal{P}(\mathbf{B}) \cap L$. By additivity of the Lebesgue measure, $\operatorname{vol}(S) = \varepsilon \operatorname{vol} \mathcal B \cdot |\mathcal{P}(\mathbf{B}) \cap \mathcal{L}| < \infty$, where $\mathcal B$ is the ball of radius one. Hence $|\mathcal{P}(\mathbf{B}) \cap \mathcal{L}| < \infty$.


>[!theorem] Every lattice admits a basis

>##### Proof
>Let $\mathcal{L} \subseteq \mathbb{R}^{n}$ be a lattice and let $k = \operatorname{rk}(\mathcal{L})$. Let $\mathbf{B}$ be a matrix whose column vectors are linearly independent vectors of $\mathcal{L}$. The last proposition implies that the quotient $\mathcal{L}/\mathcal{L}(\mathbf{B})$ is finite. If $\mathcal{L} = \mathcal{L}(\mathbf{B})$, $\mathbf{B}$ is a basis for $\mathcal{L}$. Suppose that $\mathcal{L}(\mathbf{B}) \neq \mathcal{L}$. [[(rivedi) Lemmi preparatori al primo teorema di Sylow#Lemma di Cauchy-Galois|Cauchy-Galois]]'s Lemma implies the existence of $\mathbf{x} + \mathcal{L}(\mathbf{B}) \in \mathcal{L}/\mathcal{L}(\mathbf{B})$ of order a prime $p$. $p\mathbf{x} \in \mathcal{L}(B) = \mathbf{B}\cdot \mathbb{Z}^{k}$ implies that $\mathbf{x} \in \mathbf{B}\mathbf{y}$ for some $\mathbf{y} \in \frac{1}{p} \mathbb{Z}^{k}$. Up to reordering the vectors in $\mathbf{B}$, we may assume that the first entry of $\mathbf{y}$ is not integral, i.e. $\mathbf{y} = \left( \frac{a}{p}, \mathbf{y}' \right)$ for some $\mathbf{y}' \in \frac{1}{p}\mathbb{Z}^{k-1}$ and $a \equiv 1 \mod p$. Note that we may further assume $a = 1$, up to replacing $\mathbf{x}$ with $c\mathbf{x} - \left( \frac{ac - 1}{p} \right)\mathbf{b}_{1}$, where $ac \equiv 1 \mod p$. Set $\mathbf{B}' \coloneq [\mathbf{x},\mathbf{b}_{2},\ldots,\mathbf{b}_{k}]$. We have $\mathcal{L}(B) \subsetneq \mathcal{L}(\mathbf{B}') \subseteq \mathcal{L}$: the latter inclusion is clear, plus $\mathbf{b}_{1} = \mathbf{B}' \cdot \begin{pmatrix}p \\ \mathbf{y}'\end{pmatrix} \in \mathbf{B}' \cdot \mathbb{Z}^{k}$ and $\mathbf{x} \notin \mathcal{L}(B)$ justify the first proper inclusion. Hence replacing $\mathbf{B}$ with $\mathbf{B}'$ decreases the size of the quotient $\mathcal{L}/\mathcal{L}(\mathbf{B})$. We can repeat this process until we reach $|\mathcal{L}/\mathcal{L}(\mathbf{B})| = 1$.

>[!proposition] 
>If $\mathbf{B}$ is a basis of $\mathcal{L}$, then any and all bases of $\mathcal{L}$ belong to the set
>$$\{\mathbf{B} \mathbf{U} \mid \mathbf{U} \in \operatorname{GL}_k(\mathbb{Z})\}.$$

>##### Proof
>Let $\mathbf{B}'$ be another basis of $\mathcal{L}$. Then $\mathbf{B}' = \mathbf{B}\mathbf{M}$ for some $\mathbf{M} \in \mathbb{Z}^{k \times k}$. Conversely, $\mathbf{B} = \mathbf{B}' \mathbf{M}'$ for some $\mathbf{M}' \in \mathbb{Z}^{k \times k}$. Therefore $\mathbf{B} = \mathbf{B} \mathbf{M} \mathbf{M}'$, i.e. $\mathbf{B}(\mathbf{M} \mathbf{M}' - \mathbf{I}_{k}) = 0$, which, by non-singularity of $\mathbf{B}$, implies $\mathbf{M}\mathbf{M}' = \mathbf{I}_{k}$. Let now $\mathbf{U} \in \operatorname{GL}_{k}(\mathbb{Z})$. Then we have $\mathcal{L}(\mathbf{B}\mathbf{U}) \subseteq \mathcal{L}(\mathbf{B})$ since $\mathbf{B}\mathbf{U} \subseteq \mathcal{L}^{k} = \mathbf{B} \mathbb{Z}^{k \times k}$ and $\mathcal{L}(\mathbf{B}\mathbf{U}) \subseteq \mathcal{L}(\mathbf{B}\mathbf{U}\mathbf{U}^{-1}) = \mathbf{L}(\mathbf{B})$ for the same reason.