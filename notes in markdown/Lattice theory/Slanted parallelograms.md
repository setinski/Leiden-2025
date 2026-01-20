---
aliases: "orthogonal parallelogram"
---

>[!theorem] 
>For any basis $\mathbf{B} \in \mathbb{R}^{n \times n}$ of a full-rank lattice $L$ and any upper triangular matrix $\mathbf{T} \in \mathbb{R}^{n \times n}$ with unit diagonal, $\mathcal{P}(\mathbf{B} \cdot \mathbf{T})$ is a [[Tiling|tiling]] for $L$.

>##### Proof
>Note that $\mathcal{P}(\mathbf{B} \cdot \mathbf{T})$ is a tiling for $L = \mathbf{B} \cdot \mathbb{Z}^{n}$ if and only if $\mathcal{P}(\mathbf{T})$ is a tiling for $\mathbb{Z}^{n}$. Thus we may assume $\mathbf{B} = \mathbf{I}_{n}$. 
>
>Suppose $\mathbf{v} + \mathbf{e} = \mathbf{v}' + \mathbf{e}'$ for some $\mathbf{v}, \mathbf{v}' \in \mathbb{Z}^{n}$ and $\mathbf{e},\mathbf{e}' \in \mathcal{P}(\mathbf{T}) = \mathbf{T} \cdot [-\frac{1}{2}, \frac{1}{2})^{n}$. Since $T_{n,n} = 1$, $(\mathbf{e}-\mathbf{e}')_{n} = T_{n,n}(u-u') \in (-1,1)$ — where $u,u' \in [-\frac{1}{2}, \frac{1}{2})$. From $(\mathbf{e}-\mathbf{e}')_{n} = (\mathbf{v} - \mathbf{v}')_{n} \in \mathbb{Z}$ we obtain $(\mathbf{e}-\mathbf{e}')_{n} = 0$. This is enough to prove by induction that $\mathcal{P}(\mathbf{T})$ is packing for $\mathbb{Z}^{n}$: indeed, the base case $n = 1$ follows immediately, and if $n \geq 1$, then by the above argument from $\mathbf{v} + \mathbf{e} = \mathbf{v}' + \mathbf{e}'$ we deduce $e_{n} = e_{n}'$, $v_{n} = v_{n}'$, which implies $$\begin{pmatrix}
v_{1} \\
\vdots  \\
v_{n-1}
\end{pmatrix} + \begin{pmatrix}
e_{1} \\
\vdots  \\
e_{n-1}
\end{pmatrix} = \begin{pmatrix}
v_{1}' \\
\vdots  \\
v_{n-1}'
\end{pmatrix} + \begin{pmatrix}
e_{1}' \\
\vdots  \\
e_{n-1}'
\end{pmatrix},$$
>from which we conclude $e_{i} = e_{i}'$, $v_{i} = v_{i}'$ for all $i \in \{ 1,\ldots,n - 1 \}$ by induction.
>
>To conclude the statement we need to check that $\mathcal{P}(\mathbf{T})$ is a covering for $L$. We do so by induction. If $n = 1$ the statement is obvious since $\mathbf{T} = (1)$. Suppose $n \geq 1$ and $\mathbf{x} \in \mathbb{R}^{n}$. Let $\tilde{\mathbf{T}}$ be the matrix obtained by removing the last column and last row of $\mathbf{T}$. The inductive hypothesis thus proves that we may write $$\begin{pmatrix}
x_{1} \\
\vdots \\
x_{n-1}
\end{pmatrix} - (x_{n} - \lfloor x_{n} \rceil) \begin{pmatrix}
T_{1,n} \\
\vdots \\
T_{n-1,n}
\end{pmatrix} = \begin{pmatrix}
v_{1} \\
\vdots  \\
v_{n-1}
\end{pmatrix} + \tilde{\mathbf{T}} \begin{pmatrix}
u_{1} \\
\vdots \\
u_{n-1}
\end{pmatrix}$$
>where $v_{i} \in \mathbb{Z}$ and $u_{i} \in [\frac{1}{2}, \frac{1}{2})$ for all $i \in \{ 1,\ldots,n-1 \}$. Hence:
>$$\begin{pmatrix}
v_{1} \\
\vdots  \\
v_{n-1}  \\
\lfloor x_{n} \rceil
\end{pmatrix} + \mathbf{T} \begin{pmatrix}
u_{1} \\
\vdots \\
u_{n-1} \\
(x_{n} - \lfloor x_{n} \rceil) \\
\end{pmatrix} = \mathbf{x},$$
>as desired. 

>[!corollary] Corollary 
>If $\mathbf{B} \in \mathbb{R}^{n \times n}$ is a basis of a full-rank lattice $L$, then the ==orthogonal parallelogram== $\mathcal{P}(\mathbf{B}^{*})$ is tiling for $L$.

>##### Proof
>This follows since the [[Gram-Schmidt orthogonalization]] gives $\mathbf{B} = \mathbf{B}^{*} \cdot \mathbf{T}$, i.e. $\mathbf{B}^{*} = \mathbf{B} \cdot \mathbf{T}^{-1}$, where $\mathbf{T}$, and thus $\mathbf{T}^{-1}$, is upper triangular with unit diagonal.

>[!note] Inner and outer radii of $\mathcal{P}(\mathbf{B}^{*})$
>If $\mathbf{B} = \mathbf{B}^{*} \mathbf{T} = \mathbf{Q} \mathbf{D} \mathbf{T}$, then $\mathbf{C} \coloneq (\mathbf{B}^{*})^{-T} = (\mathbf{D}^{-1}\mathbf{Q}^{T})^{T} = \mathbf{Q}\mathbf{D}^{{-1}} = \mathbf{B}^{*} \mathbf{D}^{-2}$, and $\mathbf{D}^{-2} = \operatorname{diag}(\frac{1}{\|\mathbf{b}_{i}^{*}\|_{2}^{2}})$ so that $$\mathcal{P}(\mathbf{B}^{*}) = \left\{  \mathbf{x} \in \operatorname{Span}_{\mathbb{R}} \mathcal{L} \;\left|\; \mathbf{c}_{i}^{T} \cdot \mathbf{x} \in \left[ -\frac{1}{2}, \frac{1}{2} \right), \, \forall i \right\}\right. = \left\{  \mathbf{x} \in \operatorname{Span}_{\mathbb{R}} \mathcal{L}  \;\left|\;  \frac{\mathbf{b}_{i}^{*} \cdot \mathbf{x}}{\| \mathbf{b}_{i}^{*} \|_{2}^{2} } \in \left[ -\frac{1}{2}, \frac{1}{2} \right) \, \forall i \right\}\right.$$
>It follows then by the [[Diseguaglianze importanti|Cauchy-Schwartz]] inequality that:
>$$\nu^{(2)}(\mathcal{P}(\mathbf{B}^{*})) = \frac{1}{2} \min_{i \in \{ 1,\ldots,k \}} \| \mathbf{b}_{i}^{*} \|_{2}.$$
>Conversely, by the orthogonality of the $\mathbf{b}_{i}^{*}$'s, $\|\mathbf{B}^* \cdot \mathbf{x}\|_{2}^{2} = \sum_{i = 1}^{k} x_{i}^{2} \|\mathbf{b}_{i}^{*}\|_{2}^{2}$, hence:
>$$\mu^{(2)}(\mathcal{P}(\mathbf{B}^{*})) = \frac{1}{2} \sqrt{ \sum_{i = 1}^{k} \| \mathbf{b}_{i}^{*} \|_{2}  },$$