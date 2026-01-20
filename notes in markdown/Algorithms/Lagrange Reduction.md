---
tags: definition
alises: Lagrange-reduced
---


>[!define] #definition
>##### Lagrange reduced basis
>Let $\mathcal{L}$ be a $2$-dimensional lattice. A basis $\mathbf{B}$ of $\mathcal{L}$ is ==Lagragnge Reduced== if:
>- $\mathbf{b}_{1}$ is a shortest vector of $\mathcal{L}$;
>- $|\langle \mathbf{b}_{1},\mathbf{b}_{2} \rangle| \leq \frac{1}{2} \|\mathbf{b}_{1}\|_{2}^{2}$.

>[!info] Note
>If $\mathbf{B}$ is Lagrange-reduced, then $\|\mathbf{b}_{i}\|_{2} = \lambda_{i}(\mathcal{L})$ for $i \in \{ 1,2 \}$. Also, $$\|\mathbf{b}_{1}^{*}\|_{2}^{2} = \|\mathbf{b}_{1}\|_{2}^{2} \leq \|\mathbf{b}_{2}\|_{2}^{2} = \left\|\mathbf{b}_{2}^{*} + \frac{\langle \mathbf{b}_{2}, \mathbf{b}_{1}\rangle}{\| \mathbf{b}_{1} \|_{2}^{2} } \mathbf{b}_{1}\right\|_{2}^{2} = \|\mathbf{b}_{2}^{*}\|_{2}^{2} + \frac{|\langle \mathbf{b}_{2}, \mathbf{b}_{1}\rangle|^{2}}{\| \mathbf{b}_{1}^{*}\|_{2}^{4}} \|\mathbf{b}_{1}^{*}\|_{2}^{2} \leq \|\mathbf{b}_{2}^{*}\|_{2}^{2} + \frac{1}{4}\|\mathbf{b}_{1}^{*}\|_{2}^{2},$$
>so that $\|\mathbf{b}_{2}^{*}\|_{2}^{2} \geq \frac{3}{4} \|\mathbf{b}_{1}^{*}\|_{2}^{2}$, i.e. $\|\mathbf{b}_{1}^{*}\|_{2} \leq \gamma_{2} \|\mathbf{b}_{2}^{*}\|_{2}$ , or $\ell_{2} \geq \ell_{1} - \log \sqrt{ \frac{4}{3} }$ and the [[Basis of a lattice|profile]] of the basis does not decrease too sharply.

>[!theorem] Wristwatch lemma
>Every $2$-dimensional lattice admits a Lagrange-reduced basis

The proof of the Wristwatch lemma amount to proving correctedness and termination of the following algorithm:

```pseudo
	\begin{algorithm}
	\caption{\texttt{LagrangeReduce}$(\mathbf{B})$}
	\begin{algorithmic}
	\Input A basis $(\mathbf{b}_1,\mathbf{b}_2) \in \mathbb Q^{2 \times 2}$ of a full-rank lattice $\mathcal{L}$.
	\Output A Lagrange-reduced basis $(\mathbf{b}_1,\mathbf{b}_2) \in \mathbb Q^{2 \times 2}$ of $\mathcal{L}$.
	\Repeat
	\State swap $\mathbf{b}_1\leftrightarrow \mathbf{b}_2$
	\State $k \gets \lceil \frac{\langle \mathbf{b}_1, \mathbf{b}_2\rangle}{\|\mathbf{b}_1\|_2^2} \rfloor$
	\State $\mathbf{b}_2 \gets \mathbf{b}_2 - k \mathbf{b}_1$
    \Until{$\|\mathbf{b}_1\|_2 \leq \|\mathbf{b}_2\|_2$}
	\return $(\mathbf{b}_1, \mathbf{b}_2)$
	\end{algorithmic}
	\end{algorithm}
```

Termination of the algorithm follows from the fact that, if $k = 0$ then the algorithm merely swaps $\mathbf{b}_{1}$ and $\mathbf{b}_{2}$ (and concludes after at most two swaps), otherwise $k \neq 0$ and (assuming WLOG $\mathbf{b}_{1} = (0,1)^{T}$ and $\mathbf{b}_{2} = (\alpha,\beta)^{T}$), $\|\mathbf{b}_{1}^{\text{new}}\|_{2} = \|\mathbf{b}_{2} - k \mathbf{b}_{1}\|_{2} = \|(\alpha, \beta - \lfloor \beta \rceil)\|_{2} \leq \|(\alpha, \beta)\|_{2} = \| \mathbf{b}_{2} \|_{2} < \|\mathbf{b}_{1}^{\text{old}}\|$ , which means that $\|\mathbf{b}_{1}\|_{2}$ *strictly* diminishes at each iteration. If $r$ is the initial value of $\|\mathbf{b}_{1}\|_{2}$, then since after each iteration $\mathbf{b}_{1}$ becomes a different vector of the set $r \mathcal{B} \cap \mathcal{L}$, the number of total iterations is bounded by $|r \mathcal{B} \cap \mathcal{L}|$, which is finite.

Since the only operations in the loop are swaps and row-additions, which are represented by multiplication by a unimodular matrix in $\operatorname{GL}_{2}(\mathbb{Z})$, we conclude that the final pair of vectors do indeed form a basis of $\mathcal{L}$.

Assuming WLOG $\mathbf{b}_{1} = (0,1)^{T}$ and $\mathbf{b}_{2} = (\alpha,\beta)^{T}$ after the last swap, then at the end of the iteration we have $|\langle \mathbf{b}_{1}, \mathbf{b}_{2} \rangle| = |\beta - \lceil \beta \rfloor| \leq \frac{1}{2} = \frac{1}{2} \|\mathbf{b}_{1}\|_{2}^{2}$.

To conclude, we observe that $\mathbf{b}_{1}$ is indeed a shortest vector of $\mathcal{L}$.  WLOG, suppose that at the end of the loop we have $\mathbf{b}_{1} = (0,1)^{T}$ and $\mathbf{b}_{2} = (\alpha,\beta)^{T}$, with $|\beta| \leq \frac{1}{2}$. Then if $\mathbf{v} \in \mathcal{L}$, we have $\mathbf{v} = m \mathbf{b}_{1} + n \mathbf{b}_{2}$, and it is obvious that if $m = 0$ or $n = 0$ then $\|\mathbf{v}\|_{2} \geq \|  \mathbf{b}_{1} \|$. If $n,m \neq 0$ then
$$
\begin{align*}
\|\mathbf{v}\|_{2}^{2} = \|(n \alpha, m + n \beta)\|_{2}^{2} = n^{2} \alpha^{2} + n^{2} \beta^{2} + m^{2} + 2 m n \beta \geq n^{2} + m^{2} - |mn| \geq \min(n^{2},m^2) \geq 1 = \|\mathbf{b}_{1}\|_{2}^{2},
\end{align*}
$$
where the first inequality comes from the fact that $\alpha^{2} + \beta^{2} = \|\mathbf{b}_{2}\|_{2}^{2} \geq \|\mathbf{b}_{1}\|_{2}^{2} = 1$ and $|\beta| \leq \frac{1}{2}$ 

### Complexity

>[!lemma] 
>The Lagrange reduction algorithm terminates after $25 + \max\left\{ 0, \log_{2} \frac{\|\mathbf{b}_{1}\|_{2}}{\sqrt{ \det \mathcal{L} }} \right\}$ iterations. 

>##### Proof
>Assume, modulo rescaling the lattice, that $1 = \|\mathbf{b}_{1}^{*}\|_{2} \cdot \|\mathbf{b}_{2}^{*}\|_{2} = \det \mathcal{L}$. We divide the algorithm in two phases:
>- ($\|\mathbf{b}_{1}\|_{2}^{2} \geq 2$): in this phase $1 = \|\mathbf{b}_{1}^{*}\|_{2} \cdot \|\mathbf{b}_{2}^{*}\|_{2} \geq 2 \|\mathbf{b}_{2}^{*}\|_{2}$, hence $\|\mathbf{b}_{2}^{*}\|_{2}^{2} \leq \frac{1}{2} \leq \frac{1}{4} \|\mathbf{b}_{1}\|_{2}^{2}$. Let $\mathbf{c}_{1} \coloneq \mathbf{b}_{1}^{\text{new}} = \mathbf{b}_{2} - k \mathbf{b}_{1}$. Then, by bilinearity, setting $\alpha = \frac{\langle \mathbf{b}_{2}, \mathbf{b}_{1}\rangle}{\|\mathbf{b}_{1}\|_{2}^{2}}$, $$|\langle \mathbf{c}_{1}, \mathbf{b}_{1} \rangle| \leq |\langle \mathbf{b}_{2} - k \mathbf{b}_{1}, \mathbf{b}_{1} \rangle| = \left|\left\langle \alpha \cdot \|\mathbf{b}_{1}\|_{2}^{2} - \left \lceil \alpha \right \rfloor \cdot \|\mathbf{b}_{1}\|_{2}^{2} \right\rangle\right| \leq \frac{1}{2} \|\mathbf{b}_{1}\|_{2}^{2}.$$
>Also, $\langle \mathbf{c}_{1},\mathbf{b}_{2}^{*} \rangle = \langle \mathbf{b}_{2},\mathbf{b}_{2}^{*} \rangle = \|\mathbf{b}_{2}^{*}\|_{2}^{2}$, which implies $\mathbf{b}_{2}^{*} \perp (\mathbf{c}_{1} - \mathbf{b}_{2}^{*})$ and hence, noting also that $\mathbf{c}_{1} - \mathbf{b}_{2}^{*} = (\alpha - \lceil \alpha \rfloor) \mathbf{b}_{1}$, by Pythagoras' theorem,
>$$\|\mathbf{c}_{1}\|_{2}^{2} = \|\mathbf{b}_{2}^{*} + (\mathbf{c}_{1} - \mathbf{b}_{2}^{*})\|_{2}^{2} = \|\mathbf{b}_{2}^{*}\|_{2}^{2} + \|\mathbf{c}_{1} - \mathbf{b}_{2}^{*}\|_{2}^{2} \leq \frac{1}{4} \|\mathbf{b}_{1}\|_{2}^{2} + \frac{1}{4} \|\mathbf{b}_{2}^{*}\|_{2}^{2} = \frac{1}{2} \|\mathbf{b}_{1}\|_{2}^{2}.$$ 
>Thus $\|\mathbf{b}_{1}\|_{2}^{2}$ decreases by $\frac{1}{2}$ every iteration. Hence the number of iterations in this first phase is at most $\log_{2}(\|\mathbf{b}_{1}\|_{2}^{2})$
>- ($\|\mathbf{b}_{1}\|_{2}^{2} < 2$): we distinguish two subcases:
>	- if $\lambda_{2}^{(2)}(\mathcal{L})^{2} \geq 2$, then $\|\mathbf{b}_{1}\|_{2}^{2} < 2 \leq \lambda_{2}^{(2)}(\mathcal{L})^{2}$ implies that $\|\mathbf{b}_{1}\|_{2} = \lambda_{1}^{(2)}(\mathcal{L})$ and the algorithm is done.
>	- if $\lambda_{2}^{(2)}(\mathcal{L})^{2} < 2$, then a property of [[Successive minima]] implies $\lambda_{1}^{(2)}(\mathcal{L}) \sqrt{ 2 }\geq \lambda_{1}^{(2)}(\mathcal{L}) \cdot \lambda_{2}^{(2)}(\mathcal{L}) \geq \det \mathcal{L} = 1$, hence $\lambda_{1}^{(2)}(\mathcal{L}) \geq \frac{1}{\sqrt{ 2 }}$. The points visited in this phase (i.e. the possible different value that $\mathbf{b}_{1}$ can assume) belong to $\|\mathbf{b}_{1}\|_{2}\mathcal{B} \subseteq \sqrt{ 2 } \mathcal B$ and are at least $\frac{1}{\sqrt{ 2 }}$: if $P$ is the set of those points then for all $p \in P$ we have $\mathcal B_{\frac{1}{2 \sqrt{ 2 }}}(p) \subseteq \left( \sqrt{ 2 } + \frac{1}{2 \sqrt{ 2 }} \right) \mathcal{B}$ and hence $$|P| \leq \frac{\left( \sqrt{ 2 } + \frac{1}{2 \sqrt{ 2 }} \right)^{2}\operatorname{vol} \mathcal{B}}{\left( \frac{1}{2 \sqrt{ 2 }} \right)^{2}\operatorname{vol} \mathcal{B}} = 8 \cdot \left(2 + 1 + \frac{1}{8}\right) = 25.$$ 