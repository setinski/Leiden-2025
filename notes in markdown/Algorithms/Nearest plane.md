
```pseudo
	\begin{algorithm}
	\caption{\texttt{NearestPlane}$(\mathbf{B},\mathbf{t})$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$, a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}}(\mathcal{L})$.
	\Output $\mathbf{v} \in \mathcal{L}$ such that $\mathbf{e} = \mathbf{t} - \mathbf{v} \in \mathcal{P}(\mathbf{B}^*)$.
	\State Compute the GSO $\mathbf{B}^*$ of $\mathbf{B}$
	\State $\mathbf{v} \gets \mathbf{0}$
	\State $\mathbf{e} \gets \mathbf{t}$
	\For{ $i = n$ down to $1$}
    \State $k\gets \lfloor \frac{\langle \mathbf{e},\mathbf{b}_i^* \rangle}{\|\mathbf{b}_i^*\|^2} \rceil$
    \State $\mathbf{e} \gets \mathbf{e} - k \mathbf{b}_i$
    \State $\mathbf{v} \gets \mathbf{v} + k \mathbf{b}_i$
    \EndFor
	\return $\mathbf{v}$
	\end{algorithmic}
	\end{algorithm}
```


>[!lemma] 
>The algorithm $\texttt{NearestPlane}$ is correct and runs in polynomial time.

>##### Proof of correctness
>Note that at each iteration $\mathbf{e} + \mathbf{v} = \mathbf{t}$ and $\mathbf{v} \in \mathcal{L}$, hence  this remains true also at the end. The algorithm does finitely many iteration by construction, so it necessarily terminates. Since $|\langle \mathbf{b}_{i},\mathbf{b}_{i}^{*} \rangle| = \|\mathbf{b}_{i}^{*}\|^{2}$, at the end of iteration $i$ we have $$\frac{\langle \mathbf{e}^\text{new},\mathbf{b}_i^* \rangle}{\|\mathbf{b}_i^*\|^2} = \frac{\langle \mathbf{e} - k \mathbf{b}_{i},\mathbf{b}_i^* \rangle}{\|\mathbf{b}_i^*\|^2} = \frac{\langle \mathbf{e},\mathbf{b}_i^* \rangle}{\|\mathbf{b}_i^*\|^2} - k \in \left[ -\frac{1}{2}, \frac{1}{2} \right)$$
>by construction. Also, in later iteration this quantity does not change, since $\langle\mathbf{b}_{i}, \mathbf{b}_{i-p}^{*}\rangle = 0$ for all $p \geq  0$.

>[!info] Note
> The algorithm $\texttt{NearestPlane}$ solves the [[Tiling problem]] for the [[Slanted parallelograms|orthogonal parallelogram]] $\mathcal{P}(\mathbf{B}^{*})$. 

>[!corollary] Corollary 
>For a basis $\mathbf{B}$ of $\mathcal{L}$, the algorithm $\texttt{NearestPlane}(\mathbf{B},\cdot)$ solves $\mu(\mathcal{P}(\mathbf{B}^{*}))$-Abs[[Closest Vector Problem|CVP]], $\nu(\mathcal{P}(\mathbf{B}^{*}))$-Abs[[Bounded Distance Decoding|BDD]] and $\frac{\mu(\mathcal{P}(\mathbf{B}^{*}))}{\nu(\mathcal{P}(\mathbf{B}^{*}))}$-CVP.
