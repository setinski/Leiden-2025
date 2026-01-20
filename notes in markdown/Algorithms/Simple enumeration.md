
```pseudo
	\begin{algorithm}
	\caption{\texttt{SimpleEnum}$(\mathbf{B}, \ell, \mathbf{t})$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times n}$ of a full-rank lattice $\mathcal{L}$, a side length $\ell \geq 1$, a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}}(\mathcal{L})$.
	\Output A vector $\mathbf{c} \in \mathcal{L} \cap (\mathbf{t} + \ell \mathcal{P}(\mathbf{B}))$ that is minimal in distance from $\mathbf{t}$.
	\State $\mathbf{c} \gets (\infty, \infty, \ldots, \infty)$
	\State $\mathbf{t}' \gets \mathbf{B}^{-1} \cdot \mathbf{t}$ \Comment{Translate the problem to $\mathbb{Z}^n$}
	\For{$\mathbf{v}' \in \mathbb{Z}^n \cap (\mathbf{t}' + \ell \left[-\frac{1}{2}, \frac{1}{2}\right)^n)$}
	\State $\mathbf{v} \gets \mathbf{B} \cdot \mathbf{v}'$
	\If{$\|\mathbf{v} - \mathbf{t}\| < \|\mathbf{c} - \mathbf{t}\|$}
	\State $\mathbf{c} \gets \mathbf{v}$
    \EndIf
    \EndFor
	\return $\mathbf{c}$
	\end{algorithmic}
	\end{algorithm}
```


>[!lemma] 
>The algorithm $\texttt{SimpleEnum}(\mathbf{B},\ell,\mathbf{t})$ is correct, that is $\mathbf{c} \gets \texttt{SimpleEnum}(\mathbf{B},\ell,\mathbf{t})$ satisfies
>$$\mathbf{c} \in \underset{\mathbf{v} \in \mathcal{L} \cap (\mathbf{t} + \ell\mathcal{P}(\mathbf{B}))}{\operatorname{argmin}}\|\mathbf{v} - \mathbf{t}\|$$

>##### Proof
>This follows from the finiteness of the discrete and bounded set  $\mathbb{Z}^n \cap (\mathbf{t}' + \ell \left[-\frac{1}{2}, \frac{1}{2}\right)^n)$, as well as the fact that $\mathbf{B} \cdot \{\mathbb{Z}^{n} \cap \left( \mathbf{t}' + \ell [-\frac{1}{2}, \frac{1}{2}\right)) \} = \mathcal{L} \cap (\mathbf{t} + \ell\mathcal{P}(\mathbf{B}))$ and the fact that $\ell \geq 1$ ensures that the loop is executed at least once.

>[!corollary] Corollary 
>The algorithm $\texttt{SimpleEnum}(\mathbf{B},\ell,\cdot)$ solves $\alpha$-[[Bounded Distance Decoding|BDD]] up to a radius $\alpha = \min\left\{ \frac{1}{2}, \ell \cdot \frac{\nu(\mathcal{P}(\mathbf{B}))}{\lambda_{1}(\mathcal{L})} \right\}$.

>##### Proof
>This follows from the fact that $d(\mathbf{t},\mathcal{L}) \leq \lambda_{1}(\mathcal{L}) \alpha \leq \ell \cdot \nu(\mathcal{P}(\mathbf{B}))$ implies the existence of $\mathbf{v} \in \mathcal{L}$ such that $\mathbf{v} - \mathbf{t} \in \lambda_{1}(\mathcal{L}) \alpha \mathcal{B} \subseteq \ell \cdot \nu(\mathcal{P}(\mathbf{B})) \mathcal{B} \subseteq \ell \mathcal{P}(\mathbf{B})$, hence a closest vector $\mathbf{v}$ in $\mathcal{L} \cap (\mathbf{t} + \ell \mathcal{P}(\mathbf{B}))$ must necessarily satisfy $\|\mathbf{v} - \mathbf{t}\| \leq \lambda_{1}(\mathcal{L}) \alpha$.

>[!corollary] Corollary 
>If $\ell \cdot \nu(\mathcal{P}(\mathbf{B})) \geq \mu(\mathcal{L})$, then $\texttt{SimpleEnum}(\mathbf{B},\ell,\cdot)$ solves Exact-[[Closest Vector Problem|CVP]] in $\mathcal{L}$.

>##### Proof
>From $d(\mathbf{t}, \mathcal{L}) \leq \sup_{\mathbf{x} \in \mathbb{R}^{n}} d(\mathbf{x},\mathcal{L}) = \mu(\mathcal{L}) \leq \ell \cdot \nu(\mathcal{P}(\mathbf{B}))$ we deduce the existence of $\mathbf{v} \in \mathcal{L}$ such that $\|\mathbf{v} - \mathbf{t}\| \leq \ell \cdot \nu(\mathcal{P}(\mathbf{B}))$, which in particular implies $\mathbf{v} \in \mathbf{t} + \ell \mathcal{P}(\mathbf{B})$. It follows that a closest vector to $\mathbf{t}$ in $\mathbf{t} + \ell \mathcal{P}(\mathbf{B})$ minimises $d(\mathbf{t},\mathcal{L})$.

Choosing $\mathbf{t} = \mathbf{0}$ above gives the following:

>[!corollary] Corollary 
>If $\ell \cdot \nu(\mathcal{P}(\mathbf{B})) \geq \lambda_{1}(\mathcal{L})$, then $\texttt{SimpleEnum}(\mathbf{B},\ell,\mathbf{0})$ solves Exact-[[Shortest Vector Problem|SVP]] in $\mathcal{L}$.

### Complexity

>[!lemma] 
>$\texttt{SimpleEnum}(\cdot,\ell,\cdot)$ requires $O(n^{3} + n^{2} \lceil \ell \rceil^{n})$ arithmetic operations.

>[!corollary] Corollary 
>Up to a polynomial factor in the size of the input,
>- $\texttt{SimpleEnum}\left( \mathbf{B}, \frac{\mu(\mathcal{L})}{\nu(\mathcal{P}(\mathbf{B}))},\cdot \right)$ solves Exact-CVP in time $\lceil \frac{\mu(\mathcal{L})}{\nu(\mathcal{P}(\mathbf{B}))} \rceil^{n}$;
>- $\texttt{SimpleEnum}(\mathbf{B}, \frac{\lambda_{1}(L)}{\nu(\mathcal{P}(\mathbf{B}))},\mathbf{0})$ solves Exact-SVP in time  $\lceil \frac{\lambda_{1}(\mathcal{L})}{\nu(\mathcal{P}(\mathbf{B}))} \rceil^{n}$.

>[!note] Remark
>Calculating the quantities $\mu(\mathcal{L})$ and $\lambda_{1}(\mathcal{L})$ may not be immediately obvious, but one can use the crude upper bounds: $\lambda_{1}(\mathcal{L}) \leq \min \|\mathbf{b}_{i}\|$ and $\mu(\mathcal{L}) \leq \mu(\mathcal{P}(\mathbf{B})) \frac{1}{2} \sum_{i = 1}^{k} \|\mathbf{b}_i\|$.

