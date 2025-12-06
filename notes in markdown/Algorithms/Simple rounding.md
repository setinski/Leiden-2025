
```pseudo
	\begin{algorithm}
	\caption{\texttt{SimpleRounding}$(\mathbf{B},\mathbf{t})$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$, a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}}(\mathcal{L})$.
	\Output $\mathbf{v} \in \mathcal{L}$ such that $\mathbf{e} = \mathbf{t} - \mathbf{v} \in \mathcal{P}(\mathbf{B})$.
	\State $\mathbf{t} \gets \mathbf{B}^{-1} \cdot \mathbf{t}$
	\State $\mathbf{v}' \gets (\lfloor t_i' \rceil)_{i = 1}^k$
	\State $\mathbf{v} \gets \mathbf{B} \cdot \mathbf{v}'$
	\return $\mathbf{v}$
	\end{algorithmic}
	\end{algorithm}
```

>[!lemma] 
>The algorithm $\texttt{SimpleRounding}$ is correct and runs in polynomial time.

>[!info] Note
> The algorithm $\texttt{SimpleRounding}$ solves the [[Tiling problem]] for the [[Fundamental parallelogram]] $\mathcal{P}(\mathbf{B})$. 

>[!corollary] Corollary 
>For a basis $\mathbf{B}$ of $\mathcal{L}$, the algorithm $\texttt{SimpleRounding}(\mathbf{B},\cdot)$ solves $\mu(\mathcal{P}(\mathbf{B}))$-AbsCVP and $\nu(\mathcal{P}(\mathbf{B}))$-AbsBDD.
