---
tags: definition
aliases: primitive
---

>[!define] #definition
>##### Primitive vector 
>A non-zero vector $\mathbf{v}$ of a [[Lattice]] $\mathcal{L}$ is primitive if and only if $(\mathbf{v} \cdot \mathbb{R}) \cap \mathcal{L} = \mathbf{v} \cdot \mathbb{Z}$, i.e. if and only if $\frac{1}{j} \mathbf{v} \notin \mathcal{L}$ for all $j \in \mathbb{Z}_{>1}$.

>[!lemma]
>A vector $\mathbf{v} \in \mathcal{L}$ is primitive if and only if it is part of some [[Basis of a lattice|basis]] of $\mathcal{L}$.

>##### Proof
>If $\mathbf{B}$ is a basis of $\mathcal{L}$ with $\mathbf{b}_{1} = \mathbf{v}$ and $j \in \mathbb{Z}_{>1}$, then $\frac{1}{j}\mathbf{v} \in \mathcal{L}$ implies $\frac{1}{j} \mathbf{v} = \mathbf{B} \cdot \mathbf{x}$ for some $\mathbf{x} \in \mathbb{Z}^{k}$; but since $\frac{1}{j}\mathbf{v} = \mathbf{B} \cdot \left( \frac{1}{j},0,\ldots,0 \right)$, we have $\mathbf{B} \cdot \left[\mathbf{x} - \left( \frac{1}{j},0,\ldots,0 \right)\right] = 0$, which implies $\mathbf{x} = \left( \frac{1}{j},0,\ldots,0 \right)$ since $\mathbf{B}$ is non singular, contradicting $\mathbf{x} \in \mathbb{Z}^{k}$.
>
>Suppose now that $\mathbf{v}$ is primitive and let $\mathbf{B}'$ be a basis of $\mathcal{L}' = \pi_{\mathbf{v}}^{\perp}(\mathcal{L})$.  Let $\mathbf{b}_{i} \in \mathcal{L}$ be a preimage of $\mathbf{b}_{i}'$ for all $i$. Set $\mathbf{B} = (\mathbf{b}_{1}|\cdots|\mathbf{b}_{k-1}|\mathbf{v})$. Notice that $\mathbf{v} \notin \operatorname{Span}_{\mathbb{R}} \mathcal{L}'$, as well as the non-singularity of $\mathbf{B}'$, imply the non-singularity of $\mathbf{B}$. Since $\operatorname{rk} \mathcal{L}'$ equals [[Gram-Schmidt orthogonalization|one minus the rank of]] $\mathcal{L}$, $\operatorname{Span}_{\mathbb{R}}\mathbf{B} = \operatorname{Span}_{\mathbb{R}} \mathcal{L}$. Any $\mathbf{w} \in \mathcal{L}$ can thus be written as $\mathbf{B} \cdot \mathbf{x}$ for some $\mathbf{x} \in \mathbb{R}^{k}$. Notice that $\pi_{\mathbf{v}}^{\perp}(\mathbf{w}) = \mathbf{B}' \cdot \begin{pmatrix}x_{1} \\ \vdots \\ x_{k-1}\end{pmatrix} \in \mathcal{L}'$, hence $x_{i} \in \mathbb{Z}$ for all $i \leq k-1$. Furthermore, from $x_{k} \mathbf{v} = \mathbf{w} - \sum_{i = 1}^{k-1} x_{i} \mathbf{b}_{i} \in \mathcal{L}$ we deduce that $x_{k}$ is an integer as well, thus proving that $\mathbf{B} \cdot \mathbb{Z}^{k} = \mathcal{L}$.