>[!define] #definition
>##### Size-reduced [[Basis of a lattice|basis]]
>A basis $\mathbf{B} \in \mathbb{R}^{n \times n}$ of a lattice is ==size-reduced== if for all $i \in \{ 1,\ldots,n-1 \}$,
>$$|\langle \mathbf{b}_{i}^{*},\mathbf{b}_{j} \rangle| \leq \frac{1}{2} \|\mathbf{b}_{i}^{*}\|_{2}^{2} \quad \forall j > i.$$
>
>Equivalently, each entry of the off-diagonal of the matrix $R$ appearing in the [[Gram-Schmidt orthogonalization|QR decomposition]] of $\mathbf{B}$ is bounded by $\frac{1}{2}$.

```pseudo
	\begin{algorithm}
	\caption{\texttt{SizeReduce}$(\mathbf{B})$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times d}$ of a lattice $\mathcal{L}$.
	\Output A size-reduced basis $\mathbf{B}$ of $\mathcal{L}$.
	\If{d = 1}
	\Return $\mathbf{B}$
    \EndIf
    \State $\mathbf{B}' \gets (\mathbf{b}_1,\ldots,\mathbf{b}_{d-1})$
    \State $\mathbf{C}' \gets \texttt{SizeRed}(\mathbf{B}')$
    \State $\mathbf{v} \gets \texttt{NearestPlane}(\mathbf{C}',\pi_{\mathbf{C}'}(\mathbf{b}_d))$
	\return $(\mathbf{C}|\mathbf{b}_d - \mathbf{v})$
	\end{algorithmic}
	\end{algorithm}
```

>[!lemma] 
>Algorithm $\texttt{SizeReduce}$ is correct and runs in polynomial time

>##### Proof
>Polynomial time is obvious. We prove correctness by induction on $d$. If $d = 1$ it is clear. Set $\mathbf{C} \gets \texttt{SizeReduce}(\mathbf{B})$. Let us first prove that $\mathbf{C}$ is a basis of $\mathcal{L}(\mathbf{B})$. Since $\mathbf{v} \in \mathcal{L}(\mathbf{C}')$, $\mathbf{v} = \mathbf{C} \cdot \mathbf{x}$ for some $\mathbf{x} \in \mathbb{Z}^{d-1}$, and we have:
>$$\mathbf{B} \cdot \begin{pmatrix}\mathbf{U} & \mathbf{0} \\ \mathbf{0} & 1\end{pmatrix} \cdot \begin{pmatrix}\mathbf{I} & \mathbf{0} \\ -\mathbf{x} & 1\end{pmatrix} = \mathbf{C},$$
>for some unimodular matrix $\mathbf{U}$ representing size-reduction of $\mathbf{B}'$.
>
>To see that $\mathbf{C}$ is size-reduced, recall that by definition $\pi_{\mathbf{C}'}(\mathbf{x}) = \sum_{i = 0}^{d-1} \frac{\langle \mathbf{x},\mathbf{c}_{i} \rangle}{\|\mathbf{c}_{i}^{*}\|^{2}} \mathbf{c}_{i}^{*}$, so that $$\langle \pi_{\mathbf{C}'}(x),\mathbf{c}_{j}^{*} \rangle = \left\langle\sum_{i = 0}^{d-1} \frac{\langle \mathbf{x},\mathbf{c}_{i} \rangle}{\|\mathbf{c}_{i}^{*}\|^{2}} \mathbf{c}_{i}^{*}, \mathbf{c}_{j}^{*} \right\rangle = \langle \mathbf{x},\mathbf{c}_{j}^{*}\rangle.$$
>Hence, for all $i < n$, $$|\langle \mathbf{c}_{i}^{*}, \mathbf{b}_{d} - \mathbf{v}\rangle| = |\langle \mathbf{c}_{i}^{*}, \pi_{\mathbf{C}'}(\mathbf{b}_{d}) - \mathbf{v}\rangle| \leq \frac{1}{2} \|\mathbf{c}_{i}^{*}\|,$$
>since $\pi_{\mathbf{C}'}(\mathbf{b}_{d}) - \mathbf{v} \in (\mathbf{C}')^{*} \cdot [\frac{1}{2}, \frac{1}{2})^{d-1}$.

>[!lemma] 
>Let $\mathbf{B} \in \mathbb{Q}^{n \times d}$ be a matrix of rank $d$ and let $\mathbf{C} \gets \texttt{SizeReduce}(\mathbf{B})$. Then $\mathbf{C}^{*} = \mathbf{B}^{*}$ and consequently $P(\mathbf{B}) = P(\mathbf{C})$.

>##### Proof
>We prove the statement by induction on $d$. It is clear for $d = 1$. Suppose $(\mathbf{C}')^{*} = (\mathbf{B}')^{*}$. Then we only need to prove that $\mathbf{c}_{d}^{*} = \mathbf{b}_{d}^{*}$, which follows from the fact that $\pi_{\mathbf{C}'}^{\perp}(\mathbf{v}) = \mathbf{0}$ since $\mathbf{v} \in \mathcal{L}(\mathbf{C}') = \mathbf{C}' \cdot \mathbb{Z}^{d-1}$ by correctness of $\texttt{NearestPlane}$.

>[!lemma] 
>Let $\mathbf{B} \in \mathbb{Q}^{n \times d}$ be a size-reduced matrix of a lattice $\mathcal{L} \subseteq \mathbb{Z}^{n}$. Then $$\log(\|\mathbf{b}_{i}\|),\log(\|\mathbf{b}_{i}^{*}\|_{2}) \leq \operatorname{poly}(n) \cdot \log(P(\mathbf{B})).$$

>##### Proof
>Note that if $1 \leq i \leq d$, then since $(\mathbf{b}_{1},\ldots,\mathbf{b}_{i}) \in \mathbb{Z}^{n \times i}$, we have $\det(\mathcal{L}_{1:i}) \geq 1$ and thus $\det(\mathcal{L}_{1:i}) \leq P(\mathbf{B})$. Therefore, $\|\mathbf{b}_{i}^{*}\| = \det(\mathcal{L}_{1:i+1})/\det(\mathcal{L}_{1:i}) \leq \det(\mathcal{L}_{1:i+1}) \leq P(\mathbf{B})$. By size-reduceness of $\mathbf{B}$, for all $1 \leq j \leq d$, $\mathbf{b}_{j} = \mathbf{b}_{j}^{*} + \sum_{i = 1}^{j-1} c_{i}\mathbf{b}_{i}^{*}$ with $|c_{i}| \leq \frac{1}{2}$ for all $i$. Hence: $$\|\mathbf{b}_{j}\| = \|\mathbf{b}_{j}^{*}\| + \sum_{i = 1}^{j-1} c_{i}\|\mathbf{b}_{i}^{*}\| \leq \left( 1 + \frac{j-1}{2} \right)P(\mathbf{B}) \leq  \left( 1 + \frac{n-1}{2} \right)P(\mathbf{B}).$$

By virtue of this lemma, we see that interlocking size-reduction with $\varepsilon$-W[[LLL]] reduction leads to complete control over the size of the coefficients of $\mathbf{B}$ as well as those of $\mathbf{B}^{*}$.

