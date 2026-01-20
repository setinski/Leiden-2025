>[!tip] Idea
>[[Hermite Reduction|Hermite's algorithm]] is too slow: to speed it up it suffices to slightly relax its termination condition.

>[!define] #definition
>##### $\varepsilon$-weakly LLL-reduced basis
>A basis $\mathbf{B}$ of a full rank lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ is $\varepsilon$-WLLL reduced if
>$$\|\mathbf{b}_{i}^{*}\|_{2} \leq (\gamma_{2} + \varepsilon) \|\mathbf{b}_{i+1}^{*}\|,$$
>for all $i \in \{ 1,\ldots,n-1 \}$. The inequality above is known as the Lovàsz condition on $(\mathbf{b}_{i}^{*},\mathbf{b}_{i+1}^{*})$.

```pseudo
	\begin{algorithm}
	\caption{$\varepsilon$-\texttt{WLLL-reduce}$(\mathbf{B}, \varepsilon)$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$, a positive real $\varepsilon > 0$.
	\Output An $\varepsilon$-WLLL reduced basis $\mathbf{B}$ of $\mathcal{L}$.
	\While{$\exists i$ such that $\|\mathbf{b}_{i}^{*}\|_{2} > (\gamma_{2} + \varepsilon) \|\mathbf{b}_{i+1}^{*}\|$}
    \State Find a matrix $\mathbf{U} \in \operatorname{GL}_2(\mathbb Z)$ such that $\mathbf{B}_{i:i+1} \mathbf{U}$ is Lagrange reduced
    \State $(\mathbf{b}_i',\mathbf{b}_{i+1}') \gets (\mathbf{b}_i,\mathbf{b}_{i+1})\mathbf{U}$
    \State $\mathbf{B} \gets (\mathbf{b}_1,\mathbf{b}_2,\ldots,\mathbf{b}_{i-2},\mathbf{b}_i',\mathbf{b}_{i+1}',\mathbf{b}_{i+2},\ldots,\mathbf{b}_n)$
    \EndWhile
	\return $\mathbf{B}$
	\end{algorithmic}
	\end{algorithm}
```

>[!theorem] 
>If $\mathbf{B} \in \mathbb{Z}^{n \times n}$, $\varepsilon$-WLLL reduction terminates after $\operatorname{poly}\left( n,\log\|\mathbf{B}\|_{\infty}, \frac{1}{\varepsilon} \right)$ iterations.

>##### Proof
>To show termination of the algorithm, we prove that the [[Basis of a lattice|potential]] $P(\mathbf{B})$ is decreased by a constant amount at each iteration, which is enough to conclude termination since $P(\mathbf{B}) \geq 1$, which follows from the fact that, for all $i$, $\det \mathcal{L}_{1:i} \in \mathbb{Z} \setminus \{ 0 \}$, as $(\mathbf{b}_{1}|\cdots|\mathbf{b}_{i}) \in \mathbb{Z}^{i \times n}$ and the [[Gram-Schmidt orthogonalization]] does not change the determinant. After one iteration, only one $\det \mathcal{L}_{i:i+1}$ is modified (for other $i$'s that determinant is not touched) and after an instance of Lagrange reduction, we go from $\| \mathbf{b}_{i}^{*} \|^{2}_{2} > (\gamma_{2} + \varepsilon) \det L_{i:i+1}$ to $\|\mathbf{b}_{i}^{*} \|^{2}_{2} \leq \gamma_{2} \det L_{i:i+1}$, so that $P(\mathbf{B})$ is diminished by a factor of at least $f = \sqrt{ \frac{\gamma_{2}}{\gamma_{2} + \varepsilon} }$. Since the initial potential is bounded by $\|\mathbf{B}\|_{\infty}^{n(n+1)/2}$ (where $\|\mathbf{B}\|_{\infty} = \max_{i = 1}^{n}\|\mathbf{b}_{i}\|_{2}$), after $N$ iterations we have $$1 \leq P(\mathbf{B}) \leq f^{N} P(\mathbf{B})_{\text{init}} \leq f^{N} \cdot \|\mathbf{B}\|_{\infty}^{n(n+1)/2}.$$
>Hence the algorithm is terminated whenever $f^{N} \cdot \|\mathbf{B}\|_{\infty}^{n(n+1)/2} \leq 1$, i.e.
>$$N \geq \frac{n(n+1)\log(\|\mathbf{B}\|_{\infty})}{-2 \log f},$$
>Note that $- \log f = \frac{1}{2} \log\left( 1 + \frac{\varepsilon}{\gamma_{2}} \right) =\frac{\varepsilon}{2\gamma_{2}} + O(\varepsilon^{2})$, hence the number of iterations is at most
>$$\frac{n(n+1)\log(\|\mathbf{B}\|_{\infty})}{\frac{\varepsilon}{\gamma_{2}} + O(\varepsilon^{2})} = \operatorname{poly}\left( n,\log\|\mathbf{B}\|_{\infty}, \frac{1}{\varepsilon} \right).$$

>[!info] Note
>The calculations above only show boundedness of the number of iterations. This is not enough to prove that the algorithm runs in polynomial time, as time complexity in principle cannot be lower than space complexity, and for the latter we have not estabilished any bounds. In other words, we should show that, at each step of the algorithm, the rational numbers occurring in $\mathbf{B}^{*}$ do not have very large numerators/denominators and show that the size of the integers coefficients of $\mathbf{B}$ can be bounded in some way. To achieve this we actually need to modify the algorithm. The only thing we can easily establish so far is that the denominators of the entries in $\mathbf{B}^{*}$ are bounded by $\det \mathcal{L}(\mathbf{B})^{2}$, as the following lemma shows.

>[!lemma] 
>If $\mathbf{B} \in \mathbb{Z}^{n \times m}$ has rank $m$, then $\mathbf{B}^{*} \in \frac{1}{\|\mathbf{b}_{1}\|^{4(n-2)}\det(\mathbf{B}^{T}\mathbf{B})} \mathbb{Z}^{n \times m}$.

>##### Proof
>We prove it by induction on $m$. If $m = 1$ then $\mathbf{B}^{*} = \mathbf{B}$ and hence has integer coefficients. Otherwise suppose $m \geq 1$ and let $d \coloneq \|\mathbf{b}_{1}\|_{2}^{2}$, $\mathbf{C} \coloneq \mathbf{B}_{2:m} \in \frac{1}{d}\mathbb{Z}^{(m-1) \times n}$. Then, by induction, $d\mathbf{C}^{*} = (d\mathbf{C})^{*} \in \frac{1}{\det (d\mathbf{C})^{T} (d\mathbf{C})} \mathbb{Z}^{n \times (m-1)} = \frac{1}{d^{2(n-1)}\det (\mathbf{C}^{T}\mathbf{C})} \mathbb{Z}^{n \times (m-1)}$, i.e. $\mathbf{C}^{*} \in \frac{1}{d^{2n-1}\det (\mathbf{C}^{T}\mathbf{C})} \mathbb{Z}^{n \times (m-1)}$ and, since $\det(\mathbf{B}^{T}\mathbf{B}) = \prod_{i = 1}^{m} \|\mathbf{b}_{i}^{*}\|_{2}^{2} = d\det(\mathbf{C}^{T}\mathbf{C})$, we have $\mathbf{B}^{*} = (\mathbf{b}_{1}|\mathbf{C}^{*}) \in \frac{1}{d^{2n-2}\det(\mathbf{B}^{T}\mathbf{B})} \mathbb{Z}^{n \times m}$.

To achieve control over the size of the integer coefficients of $\mathbf{B}$ we apply [[Size Reduction]] at each step of the algorithm above. We obtain the following:

```pseudo
	\begin{algorithm}
	\caption{$\varepsilon$-\texttt{LLL-reduce}$(\mathbf{B}, \varepsilon)$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$, a positive real $\varepsilon > 0$.
	\Output An $\varepsilon$-LLL reduced basis $\mathbf{B}$ of $\mathcal{L}$.
	\State $\mathbf{B} \gets \texttt{SizeReduce}(\mathbf{B})$
	\While{$\exists i$ such that $\|\mathbf{b}_{i}^{*}\|_{2} > (\gamma_{2} + \varepsilon) \|\mathbf{b}_{i+1}^{*}\|$}
    \State Find a matrix $\mathbf{U} \in \operatorname{GL}_2(\mathbb Z)$ such that $\mathbf{B}_{i:i+1} \mathbf{U}$ is Lagrange reduced
    \State $(\mathbf{b}_i',\mathbf{b}_{i+1}') \gets (\mathbf{b}_i,\mathbf{b}_{i+1})\mathbf{U}$
    \State $\mathbf{B} \gets (\mathbf{b}_1,\mathbf{b}_2,\ldots,\mathbf{b}_{i-2},\mathbf{b}_i',\mathbf{b}_{i+1}',\mathbf{b}_{i+2},\ldots,\mathbf{b}_n)$
    \State $\mathbf{B} \gets \texttt{SizeReduce}(\mathbf{B})$
    \EndWhile
	\return $\mathbf{B}$
	\end{algorithmic}
	\end{algorithm}
```

>[!define] #definition
>##### $\varepsilon$-LLL-reduced basis
>A basis $\mathbf{B}$ of a full rank lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ is $\varepsilon$-LLL reduced if it is both size-reduced and $\varepsilon$-WLLL reduced.

>[!info] Note
>The extra size reduction at each step does not affect $\mathbf{B}^{*}$, hence carrying it out does not affect the total number of iterations needed to complete the algorithm.

>[!theorem] 
>LLL-reduction algorithm with input a basis $\mathbf{B} \in \mathbb{Z}^{n \times n}$ runs in polynomial time.


### Properties of LLL-reduce bases
>[!lemma] 
>For any basis $\mathbf{B} \in \mathbb{R}^{n \times k}$ of a lattice $\mathcal{L}$, $\lambda_{1}(\mathcal{L}) \geq \min_{i = 1}^{d} \|\mathbf{b}_{i}^{*}\|_{2}$.

>##### Proof
>Since the [[Slanted parallelograms|orthogonal parallelogram]] $\mathcal{P}(\mathbf{B}^{*})$ is tiling, it contains a unique lattice point, i.e. $\mathbf{0}$. hence $\mathbf{B}^{*}\cdot(-1,1)^{k} \cap \mathcal{L} =\{ \mathbf{0} \}$, which implies that $\lambda_{1}(\mathcal{L}) \geq \sup\{r > 0 \mid r \mathcal{B}_{2} \subseteq \mathbf{B}^{*}\cdot (-1,1)^{d}\} = \min_{i = 1}^{d} \|\mathbf{b}_{i}^{*}\|_{2}$, where the equality follows from [[Diseguaglianze importanti|Cauchy-Schwartz]].

>[!lemma] 
>For any lattice $\mathcal{L}$, $\lambda_{i}(\mathcal{L}_{k:n}) \leq \lambda_{i+k-1}(\mathcal{L})$.

>##### Proof
>Assume, without loss of generality, that $k = 2$. Let $\mathbf{v}_{i} \in \mathcal{L}$ be a vector achieving the $i$-th [[Successive minima]] $\lambda_{i}(\mathcal{L})$. Let $j$ be the smallest index such that $\pi_{2}(\mathbf{v}_{j}) \in \operatorname{Span}(\pi_{2}(\mathbf{v}_{1}),\ldots,\pi_{2}(\mathbf{v}_{j-1}))$, which is well-defined since $\operatorname{rk}\pi_{2}(\mathcal{L}) = \operatorname{rk} \mathcal{L} - 1$. Set $$\boldsymbol{\omega}_{i} \coloneq \begin{cases}\pi_{2}(\mathbf{v}_{i}) & i < j;\\ \pi_{2}(\mathbf{v}_{i+1})& i \geq j.\end{cases}$$
>By construction, $\boldsymbol{\omega}_{1},\ldots,\boldsymbol{\omega}_{d-1}$ are independent vectors of $\mathcal{L}_{2:n} = \pi_{2}(\mathcal{L})$ and furthermore $\lambda_{i}(\mathcal{L}_{2:k}) = \|\boldsymbol{\omega}_{i}\| \leq \max(\|\pi_{2}(\mathbf{v}_{i})\|, \|\pi_{2}(\mathbf{v}_{i+1})\|) \leq \max(\|\mathbf{v}_{i}\|, \|\mathbf{v}_{i+1}\|) = \max(\lambda_{i}(\mathcal{L}),\lambda_{i+1}(\mathcal{L})) = \lambda_{i+1}(\mathcal{L}),$
>where in the last inequality we have implicitly used Pythagoras' theorem.

>[!theorem] 
>Let $\mathbf{B}$ be an $\varepsilon$-WLLL reduced basis of a lattice $\mathcal{L}$ and let $\alpha = \gamma_{2} + \varepsilon$. Then:
>1. $\|\mathbf{b}_{1}\|_{2} \leq \alpha^{(n-1)/2} \cdot \det(\mathcal{L})^{1/n}$ (Root Hermite-factor bound);
>2. $\|\mathbf{b}_{1}\|_{2} \leq \alpha^{n-1} \cdot \lambda_{1}(\mathcal{L})$ (Approximation factor bound);
>3. $\|\mathbf{b}_{i}^{*}\|_{2} \leq \alpha^{n-i} \lambda_{i}(\mathcal{L})$.
>
>If, further, $\mathbf{B}$ is size-reduced, then we have the following:
>4. $\|\mathbf{b}_{i}\|_{2} \leq \alpha^{i-1} \cdot \|\mathbf{b}_{i}^{*}\|_{2} \leq \alpha^{n-1} \cdot \lambda_{i}(\mathcal{L})$ (Approximation factor-alike bound);
>5. $\prod_{i = 1}^{n}\|\mathbf{b}_{i}\|_{2} \leq \alpha^{\frac{n(n-1)}{2}} \cdot \det \mathcal{L}$.

>##### Proof
>We deduce the first one with reasoning similar to the proof of correctness of the [[Hermite Reduction]] algorithm. $(2)$ and $(3)$ follow from $\varepsilon$-WLLL reduceness of $\mathbf{B}$ combined with the two lemmas above. $(4)$ is a matter of performing computations and using that $\mathbf{b}_{i} = \mathbf{b}_{i}^{*} + \sum_{j = 1}^{i-1} c_{j} \mathbf{b}_{j}^{*}$ with $|c_{j}| \leq \frac{1}{2}$ (size-reduceness), as well as $\| \mathbf{b}_{j}^{*} \| \leq \alpha^{i-j} \| \mathbf{b}_{i}^{*} \|$ ($\varepsilon$-WLLL reduceness) to calculate $\| \mathbf{b}_{i}^{*} \|$. For $(5)$, note that:
>$$\prod_{i = 1}^{n}\|\mathbf{b}_{i}\|_{2} \overset{(4)}\leq \prod_{i = 1}^{n} \alpha^{i-1} \cdot \|\mathbf{b}_{i}^{*}\|_{2} =\alpha^{\frac{n(n-1)}{2}} \det \mathcal{L}.$$

>[!lemma] 
>If $\mathbf{B}$ is $\varepsilon$-LLL reduced basis of $\mathcal{L}$, then $\|\mathbf{b}_{i}^{*}\| \geq \alpha^{-i} \cdot \lambda_{i}(\mathcal{L})$.

By pre-processing a basis with LLL before running [[Nearest plane]] we obtain the following:

>[!theorem] 
>For any $\alpha > \gamma_{2}$, there exists a polynomial time algorithm solving $(\alpha^{-n}/2)$-[[Bounded Distance Decoding|BDD]] in lattices of dimension $n$.

By pre-processing a basis with LLL before running [[Fincke-Pohst Enumeration]] we obtain the following:

>[!theorem] 
>There exists an algorithm solving Exact-[[Shortest Vector Problem|SVP]]  in time $2^{O(n^{2})}$ for lattices of dimension $n$.