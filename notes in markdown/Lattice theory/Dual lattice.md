---
tags: definition
---

>[!define] #definition
>##### Dual [[Lattice|lattice]]
>The dual of a lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ is defined as the set
>$$\mathcal{L}^{\lor} \coloneq \{  \mathbf{x} \in \operatorname{Span}_{\mathbb{R}}(\mathcal{L}) \mid \langle \mathbf{x}, \mathcal{L} \rangle \subseteq \mathbb{Z} \}.$$

>[!lemma] 
>The dual of a lattice is a lattice.

>##### Proof
>$\mathcal{L}^{\lor}$ is clearly a group by bilinearity. Let $\mathbf{B}$ be a basis of $\mathcal{L}$. Using the [[Diseguaglianze importanti|Cauchy-Schwartz]] inequality, we can prove that any $\mathbf{0} \neq \mathbf{x} = \sum x_{i} \mathbf{b}_{i} \in \operatorname{Span}_{\mathbb{R}}\mathcal{L}$ satisfies $\|\mathbf{b}_{i}\|_{2} \cdot \|\mathbf{x}\|_{2} \geq |\langle \mathbf{x}, \mathbf{b}_{i} \rangle| \in \mathbb{Z}$. Note that there must exist $j$ such that $\langle \mathbf{x}, \mathbf{b}_{j} \rangle \neq 0$ (since otherwise $\mathbf{x} \in \operatorname{Span}_{\mathbb{R}}(\mathcal{L})^{\perp} \cap \operatorname{Span}_{\mathbb{R}}(\mathcal{L}) = \{ \mathbf{0} \}$), hence $|\langle \mathbf{x}, \mathbf{b}_{j} \rangle| \geq 1$   and thus: $\|\mathbf{x}\|_{2} \geq \frac{1}{\|\mathbf{b}_{j}\|_{2}} \geq \frac{1}{\max_{i = 1}^{n}\|\mathbf{b}_{i}\|}$, which means that $\mathcal{L}^{\lor}$ admits a minimal distance.


>[!info] Note
>Replacing $\mathbf{b}_{i}$ above with $\mathbf{y}_{i}$, the vector achieving the $i$-th [[Successive minima]] proves that $\lambda_{1}(\mathcal{L}^{\lor}) \geq \frac{1}{\lambda_{n}(\mathcal{L})}$.

>[!define] #definition
>##### dual basis
>Let $\mathbf{B}\in \mathbb{R}^{n \times k}$ have rank $k \leq n$. The dual basis $\mathbf{B}^{\lor}$ is defined as $\mathbf{B}^{\lor} \coloneq \mathbf{B}(\mathbf{B}^{T}\mathbf{B})^{-1}$. If $k = n$, then $\mathbf{B}^{\lor} = \mathbf{B}^{-T}$.

>[!lemma] 
>$\mathbf{B}^{\lor}$ is a ==pseudo-inverse== of $\mathbf{B}$, that is:
>1. $(\mathbf{B}^{\lor})^{T} \cdot \mathbf{B} = \mathbf{I}_{k} = \mathbf{B}^{T} \cdot \mathbf{B}^{\lor}$;
>2. $\operatorname{Span}_{\mathbb{R}} \mathbf{B} = \operatorname{Span}_{\mathbb{R}} \mathbf{B}^{\lor}$;
>
>Furthermore,
>3. $\mathbf{B}^{\lor} \mathbf{B}^{T} \mathbf{y} = \mathbf{y}$ for all $\mathbf{y} \in \operatorname{Span}_{\mathbb{R}}(\mathbf{B})$, i.e. $\mathbf{B}^{\lor} \mathbf{B}$ acts like the identity on $\operatorname{Span}_{\mathbb{R}} \mathbf{B}$.

>[!The proof is immediate]-
>$1$ follows from explicitly writing $\mathbf{B}^{T} \mathbf{B}^{\lor}$, the second one follows from definitoon of the dual and the fact that $(\mathbf{B}^{\lor})^{\lor} = \mathbf{B}$, for the third one note that $\mathbf{y} = \mathbf{B} \mathbf{x}$ implies $\mathbf{B}^{\lor} \mathbf{B}^{T} \mathbf{B} \mathbf{x} = \mathbf{B}\mathbf{x} = \mathbf{y}$.

>[!lemma] 
>Every matrix $\mathbf{B} \in \mathbb{R}^{n \times k}$ of rank $k$ admits a unique pseudo-inverse $\mathbf{D}$ (i.e. such that $\mathbf{D}^{T} \mathbf{B} = \mathbf{I}_{k}$ and $\operatorname{Span}_{\mathbb{R}} \mathbf{B} = \operatorname{Span}_{\mathbb{R}} \mathbf{D}$).

>[!The proof is immediate]-
>That $\mathbf{D} \coloneq \mathbf{B}^{\lor}$ is a pseudo-inverse of $\mathbf{B}$ is clear by the last lemma. Suppose that $\mathbf{C}$ is a different pseudo-inverse and set $\mathbf{E} \coloneq \mathbf{D} - \mathbf{C}$. Note that $\mathbf{E}^{T}\mathbf{B} = \mathbf{D}^{T}\mathbf{B} - \mathbf{C}^{T}\mathbf{B} = \mathbf{0}$, so that the columns of $\mathbf{E}$ are orthogonal to $\operatorname{Span}_{\mathbb{R}} \mathbf{B}$. However, $\operatorname{Span}_{\mathbb{R}} \mathbf{E} \subseteq \operatorname{Span}_{\mathbb{R}} \mathbb{D} + \operatorname{Span}_{\mathbb{R}} \mathbf{C} = \operatorname{Span}_{\mathbb{R}} \mathbf{B}$, which implies $\operatorname{Span}_{\mathbb{R}} \mathbf{E} = 0$.

>[!lemma] 
>If $\mathbf{B} \in \mathbb{R}^{n \times k}$ is a basis of a lattice $\mathcal{L}$, then $\mathbf{B}^{\lor}$ is a basis of $\mathcal{L}^{\lor}$.

>##### Proof
>Note that $\mathbf{y} \in \mathcal{L}^{\lor} \iff \mathbf{B}^{T} \mathbf{y} \in \mathbb{Z}^{k}$. From $(\mathbf{B}^{\lor})^{T} \cdot \mathbf{B} = \mathbf{I}_{k}$ we obtain that $\mathcal{L}(\mathbf{B}^{\lor})$ is a sublattice of $\mathcal{L}^{\lor}$. Conversely, if $\mathbf{y} \in \mathcal{L}^{\lor} \subseteq \operatorname{Span}_{\mathbb{R}} \mathbf{B}$, we see that $\mathbf{B}^{\lor} \underbrace{ \mathbf{B}^{T} \mathbf{y} }_{ \in \mathbb{Z}^{k} } = \mathbf{y}$.

>[!corollary] Corollary 
>Let $\mathcal{L}$ be a lattice. Then:
>1. $\mathcal{L}$ and $\mathcal{L}^{\lor}$ have the same $\mathbb{R}$-span and in particular the same rank;
>2. $\det \mathcal{L} = \frac{1}{\det \mathcal{L}^{\lor}}$;
>3. $(\mathcal{L}^{\lor})^{\lor} = \mathcal{L}$.

>[!The proof is immediate]-
>The only point that merits a proof is $(2)$ and indeed $|\det({\mathbf{B}^{\lor}}^{T} \mathbf{B}^{\lor})| = |\det((\mathbf{B}^{T}\mathbf{B})^{-1})| = \frac{1}{|\det(\mathbf{B}^{T}\mathbf{B})|}$.

### Reversed dual [[Gram-Schmidt orthogonalization]]

>[!info] Note
>In order to simplify the following paragraph, we assume $n = k$ (which implies that the dual of a basis is its inverse transpose), but all theorems remain true even if $k < n$.

Let $\mathbf{J} \in \operatorname{GL}_{n}(\mathbb{Z})$ be the $n \times n$ matrix with all $0$'s except for $1$'s on the antidiagonal (reversal matrix). In other words $\mathbf{A}\mathbf{J}$ inverts the order of the columns of $\mathbf{A}$ and $\mathbf{J}\mathbf{A}$ inverts the order of the rows. Note that the GSO of $\mathbf{B}$ gives $\mathbf{B} = \mathbf{B}^{*}\mathbf{T} = \mathbf{Q} \mathbf{\Delta} \mathbf{T}$ for some diagonal matrix $\mathbf{\Delta}$, upper triangular matrix $\mathbf{T}$ with unit diagonal, and orthogonal matrix $\mathbf{Q}$. Then $\mathbf{B}^{\lor} = (\mathbf{Q} \mathbf{\Delta} \mathbf{T})^{\lor} = \mathbf{Q}\mathbf{\Delta}^{-1}\mathbf{T}^{-T}$, hence $\mathbf{D} \coloneq \mathbf{B}^{\lor}\mathbf{J} = \mathbf{Q}\mathbf{\Delta}^{-1}\mathbf{T}^{-T}\mathbf{J} = (\mathbf{Q}\mathbf{J})(\mathbf{J}\mathbf{\Delta}^{-1}\mathbf{J})(\mathbf{J}\mathbf{T}^{-T}\mathbf{J})$ and $\mathbf{J}\mathbf{T}^{-T}\mathbf{J}$ is upper triangular with unit diagonal, since $\mathbf{J} \mathbf{A} \mathbf{J}$ is obtained by flipping $\mathbf{A}$ over the diagonal and then over the anti-diagonal, which turns a lower-triangular matrix into an upper triangular one. It follows that $\mathbf{D}^{*} = \mathbf{Q} \mathbf{\Delta}^{-1} \mathbf{J} = \mathbf{B}^{*}\mathbf{\Delta}^{-2} \mathbf{J}$. In what follows let $\mathbf{x}_{-i}$ denote that $(n-i)$-th column vector of $\mathbf{X} \in \mathbb{R}^{n \times n}$, i.e. the $i$-th column vector of $\mathbf{X} \mathbf{J}$.

>[!lemma] 
>Let $\mathbf{B} \in \mathbb{R}^{n \times n}$ be a basis and $\mathbf{D} \coloneq \mathbf{B}^{\lor} \mathbf{J}$. Then:
>$$\mathbf{d}_{i}^{*} = \frac{\mathbf{b}_{-i}^{*}}{\|\mathbf{b}_{-i}^{*}\|^{2}}.$$
>>[!info] Note
>>$\mathbf{d}_{1} = \mathbf{d}_{1}^{*} = \frac{\mathbf{b}_{n}^{*}}{\|\mathbf{b}_{n}^{*}\|^{2}} \in \mathcal{L}^{\lor}$.

>[!lemma] 
>For any basis $\mathbf{B} \in \mathbb{R}^{n \times k}$ and $\mathbf{D} = \mathbf{B}^{\lor} \mathbf{J}$, then $\mathbf{D}_{i:j}^{\lor} = \mathbf{B}_{-j:-i}\mathbf{J}$ and $\mathbf{D}_{i:j}^{*} = \mathbf{B}_{-j:-i}^{*}\mathbf{\Delta}^{-2}\mathbf{J}$.

>##### Proof
>The equality $\mathbf{D}_{i:j}^{*} = \mathbf{B}_{-j:-i}^{*}\mathbf{\Delta}^{-2}\mathbf{J}$ follows from the previous lemma. The other equality requires a bit more work: we show that $\mathbf{B}_{-j:-i}\mathbf{J}$ is a pseudo-inverse of $\mathbf{D}_{i:j}$ by exploiting $\mathbf{D}_{i:j} = \mathbf{D}_{i:j}^{*}(\mathbf{J}\mathbf{T}^{-T}\mathbf{J})$ and ${\mathbf{B}_{-j:-i}^{*}}^{T} \mathbf{B}_{-j:-i}^{*} = \mathbf{\Delta}^{2}$.

>[!lemma] 
>Let $\mathcal{L}$ be a lattice and let $S \subseteq \operatorname{Span}_{\mathbb{R}}\mathcal{L}$ be a real sub-vector space such that $\dim S = \dim (S \cap \mathcal{L})$. Then $(S \cap \mathcal{L})^{\lor} = \pi_{S}(\mathcal{L}^{\lor})$.

>##### Proof
>To see that $\pi_{S}(\mathcal{L}^{\lor}) \subseteq (S \cap \mathcal{L})^{\lor}$ note that if $\mathbf{x} \in \mathcal{L}^{\lor}$, then $\pi_{S}(\mathbf{x}) \in S = \operatorname{Span}_{\mathbb{R}}(S \cap \mathcal{L})$ and $\langle \pi_{S}(\mathbf{x}),S \cap \mathcal{L} \rangle = \langle \mathbf{x}, S \cap \mathcal{L} \rangle \subseteq \mathbb{Z}$, where we have used that $\mathbf{x} = \underbrace{ \mathbf{x}-\pi_{S}(\mathbf{x}) }_{ \perp S } + \pi_{S}(\mathbf{x})$. Conversely, let $\mathbf{y} \in (S \cap \mathcal{L})^{\lor} \subseteq S$. Then $\pi_{S}(\mathbf{y}) = \mathbf{y}$ and $\langle \mathbf{y}, \mathcal{L} \rangle \subseteq \langle \mathbf{y}, \mathcal{L} \cap S \rangle + \underbrace{ \langle \mathbf{y}, \mathcal{L} \cap S^{\perp} \rangle }_{ = 0 } \in \mathbb{Z}$, where we have used that $\operatorname{Span}_{\mathbb{R}} \mathcal{L}$ decomposes as $S \oplus S^{\perp}$.

### Dual reduction

>[!info] Note
>Observe that if $\mathbf{D} = \mathbf{B}^{\lor} \mathbf{J}$, then $\ell_{i}(\mathbf{D}) = - \ell_{n+1-i}(\mathbf{B})$.

>[!lemma] 
>A basis $\mathbf{B}$ of a $2$-dimensional lattice $\mathcal{L}$ is Lagrange-reduced if and only if $\mathbf{D} = \mathbf{B}^{\lor} \mathbf{J}$ is Lagrange-reduced.

>##### Proof
>Since $\|\mathbf{b}_{1}\|_{2} \cdot \|\mathbf{b}_{2}^{*}\|_{2} = \det \mathcal{L}$, minimising $\|\mathbf{b}_{1}\|_{2}$ is equivalent to maximising $\|\mathbf{b}_{2}^{*}\|_{2}$, which is equivalent to minimising $\mathbf{d}_{1} = \frac{\mathbf{b}_{2}^{*}}{\|\mathbf{b}_{2}^{*}\|_{2}^2}$.
>
>To see that the second property of Lagrange-reduceness (i.e. [[Size Reduction]]) holds, we use the fact that it is equivalent to stating that the off-diagonal coefficient $\mathbf{T}_{1,2}$ of $\mathbf{T}$ is less that $\frac{1}{2}$ in absolute value. Since $\mathbf{T}_{D} = \mathbf{J} \mathbf{T}_{\mathbf{B}}^{T} \mathbf{J}$, we note that if $\mathbf{T}_{\mathbf{B}} = \begin{pmatrix}1 & x \\ 0 & 1\end{pmatrix}$, then $\mathbf{T}_{\mathbf{D}} = \begin{pmatrix}1 & -x \\ 0 & 1\end{pmatrix}$, from which the assertion follows.

>[!corollary] Corollary  
>A basis $\mathbf{B}$ of a $2$-dimensional lattice $\mathcal{L}$ is $\varepsilon$-WLLL reduced if and only if $\mathbf{D} = \mathbf{B}^{\lor} \mathbf{J}$ is $\varepsilon$-WLLL reduced.

>[!The proof is immediate]-
>$\mathbf{B}$ being $\varepsilon$-WLLL is equivalent to $\mathbf{B}_{i:i+1}$ being Lagrange-reduced for all $i$, which is equivalent to $\mathbf{D}_{i:i+1}$ being Lagrange-reduced for all $i$, which is equivalent to $\mathbf{D}$ being $\varepsilon$-WLLL.