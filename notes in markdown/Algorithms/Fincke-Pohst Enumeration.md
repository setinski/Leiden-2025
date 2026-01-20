>[!info] Main idea
>For every [[Primitive vectors|primitive vector]] $\mathbf{v}$ of a full-rank lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$, the projection $\pi_{\mathbf{v}}^{\perp}$ is an isometry, thus, if $\mathbf{t} \in \mathbb{R}^{n}$,
>$$\pi_{\mathbf{v}}^{\perp}(\mathcal{L} \cap (\mathbf{t} + r \mathcal{B}_{2}^{n})) \subseteq \pi_{\mathbf{v}}^{\perp}(\mathcal{L}) \cap (\pi_{\mathbf{v}}^{\perp}(\mathbf{t}) + r \mathcal{B}_{2}^{n-1}).$$
>This idea is used to implement a recursion: the algorithm enumerates over the [[Gram-Schmidt orthogonalization|lattice]] $\pi_{\mathbf{v}}^{\perp}(\mathcal{L})$ to find the set $S' \coloneq \{ \mathbf{s} \in \pi_{\mathbf{v}}^{\perp}(\mathcal{L}) \mid \|\mathbf{s} - \pi_{\mathbf{v}}^{\perp}(\mathbf{t})\|_{2} \leq r \}$ and, for every $\mathbf{s}' \in S'$, we find all elements of $\pi_{\mathbf{v}}^{\perp}(\mathbf{s}')^{{-1}} \cap \mathcal{L}$ whose distance from $\mathbf{t}$ is not bigger than $r$. Note  that if we fix a preimage $\mathbf{x} \in \pi_{\mathbf{v}}^{\perp}(\mathbf{s}')^{{-1}} \cap \mathcal{L}$, then $\mathbf{x} = \alpha\mathbf{v} + \mathbf{s}'$ and $\mathbf{t} = \mathbf{t}' + \beta \mathbf{v}$, where $\alpha,\beta \in \mathbb{R}$ and $\mathbf{t}' = \pi_{\mathbf{v}}^{\perp}(\mathbf{t})$. This implies: $$\|\mathbf{x} - \mathbf{t}\|_{2}^{2} = \|\underbrace{ (\mathbf{s}' - \mathbf{t}') }_{ \perp \mathbf{v} } + \underbrace{ (\alpha - \beta)\mathbf{v}}_{ \mathbin{\!/\mkern-5mu/\!} \;\mathbf{v} }\|_{2}^{2} = \|\mathbf{s}' - \mathbf{t}'\|_{2}^{2} + \|(\alpha - \beta)\mathbf{v}\|_{2}^{2},$$
>by Pythagoras' theorem. Hence it suffices to check that 
>$$\|(\alpha - \beta)\mathbf{v}\|_{2}^{2} \leq r^{2} - \|\mathbf{s}' - \mathbf{t}'\|_{2}^{2}.$$
>Since all elements of $\pi_{\mathbf{v}}^{\perp}(\mathbf{s}')^{{-1}} \cap \mathcal{L}$ can be written in the form $\mathbf{{x}} + z \mathbf{v}$, we simply need to check the inequality above replacing $(\alpha - \beta)$ with $\frac{\langle \mathbf{x}-\mathbf{t}, \mathbf{v} \rangle}{\|\mathbf{v}\|_{2}^{2}} + z$ for all $z \in \mathbb{Z}$. We also need to calculate an arbitrary preimage $\mathbf{x}$ of $\mathbf{s}'$.


```pseudo
	\begin{algorithm}
	\caption{$\texttt{FinckePohstEnum}(\mathbf{B}, \mathbf{t}, r)$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times d}$ of a lattice $\mathcal{L}$, a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{Q}}(\mathcal{L})$, a radius $r \geq 0$.
	\Output A list of all vectors $\mathbf{v} \in \mathcal{L}$ satisfying $\|\mathbf{v} - \mathbf{t}\|_2^2 \leq r^2$.
	\If{n = 1}\Comment{base case}
	\return $\{ z \cdot \mathbf{b}_1 \mid z \in \mathbb{Z}, \|(\frac{\langle \mathbf{0}-\mathbf{t}, \mathbf{b}_1 \rangle}{\|\mathbf{b}_1\|_{2}^{2}} + z) \mathbf{b}_1\|_2 \leq r\}$\comment{while loop that stops when $z$ and $-z$ don't work}
    \EndIf
    \State $S \gets \{\}$
    \State $\mathbf{B}' \gets (\pi_{\mathbf{b}_1}^\perp(\mathbf{b}_2), \ldots, \pi_{\mathbf{b}_1}^\perp(\mathbf{b}_n))$
    \State $S' = \texttt{FinckePohstEnum}(\mathbf{B}', \pi_{\mathbf{b}_1}^\perp(\mathbf{t}), r)$
    \For{$\mathbf{s}' \in S$}
    \State $\rho \gets r^2 - \|\mathbf{s}' - \pi_{\mathbf{b}_1}^\perp(\mathbf{t})\|_2^2$
    \State $\mathbf{y} \gets \mathbf{w} \in \mathbb{Z}^{n-1} \text{ such that } \mathbf{B}' \cdot \mathbf{w} = \mathbf{s}'$
    \State $\mathbf{x} \gets \mathbf{B} \cdot \begin{pmatrix}\mathbf{y}\\0\end{pmatrix}$ \Comment{arbitrary lift of $\mathbf{s}'$ to $\mathcal{L}$}
    \State $S \gets S \cup \{ z \cdot \mathbf{b}_1 + \mathbf{x} \mid z \in \mathbb{Z}, \|(\frac{\langle \mathbf{x}-\mathbf{t}, \mathbf{b}_1 \rangle}{\|\mathbf{b}_1\|_{2}^{2}} + z) \mathbf{b}_1\|_2^2 \leq \rho\}$
    \EndFor
	\return S
	\end{algorithmic}
	\end{algorithm}
```


>[!lemma] 
>Algorithm $\texttt{FinckePohstEnum}$ is correct. That is, it outputs the set $S = \mathcal{L} \cap (\mathbf{t} + r \mathcal{B}_{2}^{n})$.


```pseudo
	\begin{algorithm}
	\caption{\texttt{FinckePohstCVP}$(\mathbf{B}, \mathbf{t}, r)$}
	\begin{algorithmic}
	\Input A basis $\mathbf{B} \in \mathbb Q^{n \times d}$ of a lattice $\mathcal{L}$, a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{Q}}(\mathcal{L})$, a radius $r \geq d(\mathbf{t},\mathcal{L})$.
	\Output A closest vector in $\mathcal{L}$ to the target $\mathbf{t}$.
	\State $S \gets \texttt{FinckePohstEnum}(\mathbf{B},\mathbf{t},r)$
	\return $\operatorname{argmin}_{\mathbf{v} \in S} \|\mathbf{v} - \mathbf{t}\|_2$
	\end{algorithmic}
	\end{algorithm}
```

### Complexity

We can view $\texttt{FinckePohst}$ as a breadth-first exploration of a tree whose level $i$ nodes are constituted by the set $S_{i} \coloneq \pi_{n - i}(\mathcal{L}) \cap r \mathcal{B}_{2}$, where $\pi_{j} = \pi_{\mathbf{b}_{1},\ldots,\mathbf{b}_{j-1}}^{\perp}$. At the bottom of the lattice stands the zero-dimensional lattice, with a single node $\{ 0 \}$. From level $i$ to level $i+1$, a node $\mathbf{v} \in S_{i}$ has a child $\mathbf{v}'$ if $\pi_{n-i}(\mathbf{v}') = \mathbf{v}$. In that sense every node has a single parent but may have zero or several children. Note that building a child $\mathbf{v}'$ of $\mathbf{v}$ is easy to do (polynomial in the size of the input). Therefore the main factor bounding the complexity of the algorithm is the size of the entire tree $\sum_{i = 1}^{n} S_{i}$.

We can bound $S_{i}$ using [[Determinant of a lattice|the fact that]]

$$\frac{|r \mathcal{B}_{2}^{n} \cap (\mathcal{L} + \mathbf{t})|}{\operatorname{vol}(\mathcal{B}_{2}^{n})} \leq \frac{(r + 2 \mu(\mathcal{L}))^{n}}{\det \mathcal{L}}$$

from which it follows that 

$$|S_{i}| \leq \frac{\operatorname{vol}(\mathcal B_{2}^{i}) \cdot (r + 2 \mu(\pi_{n-i}(\mathcal{L})))^{i}}{\det(\pi_{n-i}(\mathcal{L}))}$$

Using that $\operatorname{vol}(\mathcal{B}_{2}^{i}) = \frac{1}{\sqrt{ \pi i }} \left( \frac{{2\pi e}}{i} \right)^{\frac{i}{2}}(1 + o(1))$ from [Stirling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation), we see that:

>[!theorem] 
>The number of nodes visited by $\texttt{FinckePohstEnum}(\mathbf{B}, \mathbf{t}, \cdot)$ is at most
>$$\sum_{i = 1}^{n} \left\{\frac{(r + 2 \mu(\mathcal{L}))^{i}}{\prod_{j = n-i}^{n} \|\mathbf{b}_{j}^{*}\|_{2}} \cdot \left( \frac{2 \pi e}{i} \right)^{i/2} \cdot \frac{1}{\sqrt{ \pi i }} \cdot (1 + o(1))\right\} = O(n^{3/2}) \cdot \left( \frac{\sqrt{ n } (r + 2 \mu(L))}{\sqrt{ 2\pi e } \min\|\mathbf{b}_{i}^{*}\|_{2} } \right)^{n}.$$