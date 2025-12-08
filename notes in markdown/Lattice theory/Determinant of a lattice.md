---
tags: definition
aliases: volume
---

>[!define] #definition
>##### Determinant of a lattice
>If $\mathcal{L}$ is a [[Lattice]], its determinant is defined as $\sqrt{ |\det(\mathbf{B}^{T}\mathbf{B})| }$ for any [[Basis of a lattice|basis]] $\mathbf{B}$ of $\mathcal{L}$.

>[!info] Note
>The value of $\sqrt{ |\det(\mathbf{B}^{T}\mathbf{B})| }$ is independent on the choice of basis, since, for all $\mathbf{U} \in \operatorname{GL}_{k}(\mathbb{Z})$, $\det((\mathbf{B}\mathbf{U})^{T}\mathbf{B}\mathbf{U}) = \det(\mathbf{U}^{T}\mathbf{B}^{T}\mathbf{B}\mathbf{U}) = \det(\mathbf{B}^{T}\mathbf{B})$ by the multiplicativity of the determinant. Another way to see this is to use the fact that [[Tiling|any two tilings have the same volume]] and note that $\det \mathcal{L} = \operatorname{vol} \mathcal{P}(\mathbf{B})$: This follows from the [[Gram-Schmidt orthogonalization]] of $\mathbf{B}$: indeed, if $\mathbf{B} = \mathbf{Q}\mathbf{R}$, then $\operatorname{vol}(\mathcal{P}((\mathbf{B}))) = \operatorname{vol}\left( \mathbf{Q}\mathbf{R}\left[ -\frac{1}{2}, \frac{1}{2}\right)^{k} \right) = \operatorname{vol}\left( \mathbf{R}\left[ -\frac{1}{2}, \frac{1}{2}\right)^{k} \right) = \det \mathbf{R}$, where we have used that $\mathbf{Q}$ is an isometry and thus preserves volumes. To conclude note that $\det(\mathbf{B}^{T}\mathbf{B}) = \det(\mathbf{R}^{T}\mathbf{Q}^{T}\mathbf{Q}\mathbf{R}) = \det(\mathbf{R}^{T}\mathbf{R}) = \det(\mathbf{R})^{2}$.

>[!note] Remark
>If $\mathcal{L}$ is full rank and $\mathbf{B}$ is a basis of $\mathcal{L}$, then $\det L = |\det \mathbf{B}|$.

Let $\mathcal B$ be the closure of the unit ball in $\mathbb{R}^{n}$.

>[!proposition] 
>Let $T$ be a bounded tiling for a lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ of full rank, with covering radius $\mu = \sup\limits_{x \in T} \|x\|$. Then, for any $r > \mu$, $$\frac{(r - \mu)^{n}}{\det \mathcal{L}} \leq \frac{|\mathcal{L} \cap r \mathcal B|}{\operatorname{vol}(\mathcal B)} \leq \frac{(r+\mu)^{n}}{\det \mathcal{L}}$$

>##### Proof
>We have $T \subseteq \mu \mathcal{B}$ by definition of covering radius, which implies $(\mathcal{L} \cap r \mathcal B) + T \subseteq r \mathcal{B} + \mu \mathcal{B} = (r + \mu)\mathcal{B}$, therefore $\operatorname{vol}((\mathcal{L} \cap r \mathcal B) + T) \leq (r + \mu)^{n} \operatorname{vol} \mathcal B$. Since $T$ is a tiling, $$\operatorname{vol}((\mathcal{L} \cap r \mathcal B) + T) = \operatorname{vol}\left(\bigsqcup_{x \in \mathcal{L} \cap r \mathcal B} x + T\right) = \sum_{x \in \mathcal{L} \cap r \mathcal B} \operatorname{vol}(x + T) = |\mathcal{L} \cap r \mathcal B|\operatorname{vol}(T) = |\mathcal{L} \cap r \mathcal B|\det \mathcal{L},$$ from which the second inequality follows easily. For the first, note that since $T$ is a covering, $\mathbb{R}^{n} = \mathcal{L} + T$ and hence $(r - \mu) \mathcal B \subseteq (\mathcal{L} \cap r \mathcal B) + T$: indeed if $\mathbf{x} \in (r - \mu) \mathcal B$, then $\mathbf{x} = \mathbf{t} + \mathbf{e}$ for some $\mathbf{t} \in \mathcal{L}$ and $\mathbf{e} \in T$, and $\|\mathbf{t}\| = \|\mathbf{x} - \mathbf{e}\| \leq \|\mathbf{x}\| + \|\mathbf{e}\| \leq r - \mu + \mu = r$. Therefore, $$\operatorname{vol}((r-\mu)\mathcal B) = (r - \mu)^{n} \operatorname{vol}\mathcal B \leq \operatorname{vol} (\mathcal{L} \cap r \mathcal B) + T \leq |\mathcal{L} \cap r \mathcal B| \det \mathcal{L},$$ which concludes the proof.

>[!theorem] 
>Let $\| \cdot \|$ be any norm on $\mathbb{R}^{n}$, let $\mathcal{L} \subseteq \mathbb{R}^{n}$ be a full-rank lattice. Then:
>$$\lim_{ r \to \infty } \frac{{|\mathcal{L} \cap r \mathcal B|}}{r^{n} \operatorname{vol}(\mathcal B)} = \frac{1}{\det \mathcal{L}}.$$

>##### Proof
>The theorem follows from the proposition above, together with the squeeze theorem, if we set $T = \mathcal{P}(\mathbf{B})$ for a basis $\mathbf{B}$ of $\mathcal{L}$. Indeed, $\mathcal{P}(\mathbf{B})$ is bounded since we have $\mu(\mathcal{P}(\mathbf{B})) \leq \sum_{i = 1}^{k}\| b_{i} \|$ by the triangular inequality.