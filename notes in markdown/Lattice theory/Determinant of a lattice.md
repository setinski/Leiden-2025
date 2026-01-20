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
>If $\mathcal{L}$ is full rank and $\mathbf{B}$ is a basis of $\mathcal{L}$, then $\det \mathcal{L} = |\det \mathbf{B}|$.

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

>[!proposition] 
>If $\mathcal{L}'$ is a sublattice of a lattice $\mathcal{L}$ and they have the same rank, then $|\mathcal{L}/\mathcal{L}'| = \det \mathcal{L}' / \det \mathcal{L} = |\mathcal{L} \cap T'|$, where $T'$ is any tiling of $\mathcal{L}'$.

>##### Proof
>The first equality be proven either using the [aligned basis theorem](https://kconrad.math.uconn.edu/blurbs/linmultialg/alignedbases.pdf) or by induction on $\dim \mathcal{L}$, using in the inductive step that if $\mathbf{b}_{1}$ is a primitive vector in $\mathcal{L}$, then $\det \mathcal{L} = \prod_{i = 1}^{n}\|\mathbf{b}_{i}^{*}\| = \|\mathbf{b}_{1}\| \cdot \det(\pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}))$, the latter being [[Gram-Schmidt orthogonalization|a lattice of lower rank]]. By the rank-nullity theorem for abelian groups, if $\mathbf{b}_{1}$ is a primitive vector in $\mathcal{L}'$ and $\frac{\mathbf{b}_{1}}{r}$ is a primitive vector in $\mathcal{L}$:
>$$\left| \frac{\mathcal{L}}{\mathcal{L}'} \right| = \left| \frac{\pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}) \oplus \frac{\mathbf{b}_{1}}{r} \mathbb{Z}}{\pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}') \oplus \mathbf{b}_{1} \mathbb{Z}} \right| = \left| \frac{\pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L})}{\pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}')} \right| \cdot \left| \frac{\frac{\mathbf{b}_{1}}{r} \mathbb{Z}}{ \mathbf{b}_{1} \mathbb{Z}} \right| = \frac{\det \pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}')}{r \det \pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L})} = \frac{\|\mathbf{b}_{1}\|\det \pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L}')}{r\|\mathbf{b}_{1}\| \det \pi_{\mathbf{b}_{1}}^{\perp}(\mathcal{L})} = \frac{\det \mathcal{L}'}{ \det \mathcal{L}},$$
>where we have used the isomorphism
>$$\frac{A \oplus B}{C \oplus D} \cong \frac{A}{C} \oplus \frac{B}{D}$$
>where $A,B,C,D$ are abelian groups and the isomorphism is obtained from the natural map $\varphi \colon (a,b) \in A \oplus B \colon \twoheadrightarrow (a + C,b + D) \in \frac{A}{C} \oplus \frac{B}{D}$ after quotienting by $\ker \varphi = C \oplus D$
>The second equality follows from the bijectivity of the map
>$$\begin{align*} \mathcal{L}/\mathcal{L}' &\to \mathcal{L} \cap T'\\\mathbf{x} + \mathcal{L}' &\mapsto \mathbf{t}' \end{align*}$$
>where $\mathbf{t}'$ is the unique element of $T'$ such that $\mathbf{x} = \mathbf{t}' + \mathbf{x}'$ for some $\mathbf{x}' \in \mathcal{L}'$.

>[!proposition] 
>For any full-rank lattice $\mathcal{L}$ of rank $n$, any radius $r > 2 \pi(\mathcal{L})$, and any shift $\mathbf{t} \in \mathbb{R}^{n}$, it holds that:
>$$\frac{(r - 2 \mu(\mathcal{L}))^{n}}{\det \mathcal{L}} \leq \frac{|\mathcal{L} \cap (\mathbf{t} + r \mathcal{B})|}{\operatorname{vol} \mathcal B} \leq \frac{(r + 2 \mu(\mathcal{L}))^{n}}{\det \mathcal{L}} .$$
>Furthermore, if $\mathbf{t} = \mathbf{0}$, the quantity $2 \mu(\mathcal{L})$ can be replaced by $\mu(\mathcal{L})$.

>##### Proof
>