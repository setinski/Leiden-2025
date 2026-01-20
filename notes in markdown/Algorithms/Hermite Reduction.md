---
aliases: Hermite's bound
---

>[!define] #definition
>Let $\mathcal{L} \subseteq \mathbb{R}^{n}$ be a full rank lattice. We set
>$$\gamma(\mathcal{L}) \coloneq \frac{\lambda_{1}(\mathcal{L})^{2}}{\det(\mathcal{L})^{2/n}}$$

>[!define] #definition
>##### Hermite's constant
>$$\gamma_{n} \coloneq \sup_{\mathcal{L} \in \Gamma_{n}} \gamma(\mathcal{L}),$$
>where $\Gamma_{n}$ is defined as the set of all full rank lattices in $\mathbb{R}^{n}$.

![[Tensored hexagonal lattices#^654bc6]]

>[!theorem] Hermite's bound
>$$\gamma_{n} \leq \gamma_{2}^{n-1}.$$

The proof of Hermite's bound amounts to the proof of the correctedness of the following algorithm:

```pseudo
	\begin{algorithm}
	\caption{\texttt{HermiteReduce}$(\mathbf{B})$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$.
	\Output A basis $\mathbf{B}$ of $\mathcal{L}$ such that $\|\mathbf{b}_1\|_2^2 \leq \gamma_2^{n-1} \cdot \det(\mathcal{L})^{2/n}$.
	\While{$\exists i$ such that $\mathbf{B}_{i:i+1}$ is not Lagrange reduced}
    \State Find a matrix $\mathbf{U} \in \operatorname{GL}_2(\mathbb Z)$ such that $\mathbf{B}_{i:i+1} \mathbf{U}$ is Lagrange reduced
    \State $(\mathbf{b}_i',\mathbf{b}_{i+1}') \gets (\mathbf{b}_i,\mathbf{b}_{i+1})\mathbf{U}$
    \State $\mathbf{B} \gets (\mathbf{b}_1,\mathbf{b}_2,\ldots,\mathbf{b}_{i-2},\mathbf{b}_i',\mathbf{b}_{i+1}',\mathbf{b}_{i+2},\ldots,\mathbf{b}_n)$
    \EndWhile
	\return $\mathbf{B}$
	\end{algorithmic}
	\end{algorithm}
```

Let us first observe that the algorithm is correct, assuming it terminates. If it does terminate, then for all $i \in \{ 1,\ldots,n-1 \}$, $\mathbf{B}_{i:i+1}$ is [[Lagrange Reduction|Lagrange-reduced]], which implies that $\|\mathbf{b}_{i}^{*}\|_{2} \leq \gamma_{2} \|\mathbf{b}_{i+1}^{*}\|$. In particular, $\lambda_{1}(\mathcal{L})^{n} = \|\mathbf{b}_{1}^{*}\|_{2}^{n} \leq \prod_{i = 1}^{n} \gamma_{2}^{i-1} \|\mathbf{b}_{i}^{*}\|_{2} = \gamma_{2}^{(n-1)n/2} \det \mathcal{L}$, hence on one hand $\|\mathbf{b}_{1}\|_{2}^{2} \leq \gamma_{2}^{n-1} \cdot \det(\mathcal{L})^{2/n}$ (and the algorithm is correct), but also $\gamma(\mathcal{L}) \leq \gamma_{2}^{n-1}$, which implies Hermite's bound follows after after taking the supremum over all $\mathcal{L} \in \Gamma_{n}$.

We prove that the algorithm terminates by induction on $n = \dim \mathcal{L}$.  Termination in dimension $2$ amounts to termination of the Lagrange algorithm. Let now $n \geq 2$. Note that Lagrange-reducing $\mathbf{B}_{1:2}$, if it is not already Lagrange-reduced, replaces $\mathbf{b}_{1}$ by a vector of *strictly* smaller norm. Indeed, if $\mathbf{B}_{1:2}$ is *not* Lagrange reduced, since the condition $|\langle \mathbf{b}_{1},\pi_{1}(\mathbf{b}_{2}) \rangle| = |\langle \mathbf{b}_{1},\mathbf{b}_{2} \rangle| = 0 \leq \frac{1}{2} \|\mathbf{b}_{1}\|_{2}$ is always trivially satisfied, the obstruction to Lagrange-reduceness must be that $\mathbf{b}_{1}$ is not a shortest vector of $\mathcal{L}_{1:2}$, which it is after the basis is reduced. Since $\|\mathbf{b}_{1}\| \in r \mathcal{B} \cap \mathcal{L}$ for some $r \in \mathbb{R}^{+}$, it follows that $\mathbf{B}_{1:2}$ can be Lagrange-reduced by Hermite reduction only a finite number of times. Excluding those, the algorithm only touches vectors of $\mathbf{B}_{2:n}$ and thus terminates by induction since $\dim \mathcal{L}_{2:n} = n-1$.