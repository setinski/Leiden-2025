---
tags: definition
---

>[!define] #definition
>##### Fundamental parallelogram of a [[Basis of a lattice|basis]] $B$
>If $\mathbf{B} = [\mathbf{b}_{1},\ldots,\mathbf{b}_{k}] \in \mathbb{R}^{n \times k}$ is a basis of a lattice $\mathcal{L}$, we define its fundamental parallelepiped to be the set $\mathcal{P}(\mathbf{B}) \coloneq \mathbf{B} \cdot \left[ - \frac{1}{2}, \frac{1}{2} \right)^{k}$, consisting of elements of the form $\sum_{i = 1}^{k} a_{i} \mathbf{b}_{i}$, where $a_{i} \in \left[ - \frac{1}{2}, \frac{1}{2} \right)$.

>[!proposition] 
>$\mathcal{P}(B)$ is a [[Tiling|tiling]] for $\mathcal{L}$.

>##### Proof
>Every $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}} \mathcal{L}$ can be written as $\mathbf{t} = \sum_{i = 1}^{k} a_{i} \mathbf{b}_{i}$, where $a_{i} \in \mathbb{R}$. Then $$t = \underbrace{ \sum_{i = 1}^{k} \lfloor a_{i} \rceil \mathbf{b}_{i} }_{ \eqcolon \mathbf{x}\in \mathbb{Z}^{k} \cdot \mathbf{B} = \mathcal{L} } + \underbrace{ \sum_{i = 1}^{k} (a_{i} - \lfloor a_{i} \rceil) \mathbf{b}_{i} }_{ \mathbf{e}\in \mathcal{P}(B) }.$$
>Suppose we have $\mathbf{t} = \mathbf{x} + \mathbf{e} = \mathbf{x}' + \mathbf{e}'$ for some $\mathbf{e} \neq \mathbf{e}' \in \mathcal{P}(\mathbf{B})$ and (consequently) $\mathbf{x} \neq \mathbf{x}' \in \mathcal{L}$. Then, we have
>$$0 = (\mathbf{e} - \mathbf{e}') + (\mathbf{x} - \mathbf{x}'),$$
>which implies $\mathbf{e} - \mathbf{e}' \in \mathcal{L}$, contradicting the fact that $\mathbf{e} - \mathbf{e}' \in \mathbf{B} \cdot (-1,1)^{k} \subseteq \mathbb{R}^{n} \setminus \mathcal{L}$.

>[!info] Note
>- The volume of $\mathcal{P}(\mathbf{B})$ equals the [[Determinant of a lattice|determinant]] $\det \mathcal{L}$.
>- $\mathcal{P}(\mathbf{B})$ is bounded since we have $\mu(\mathcal{P}(\mathbf{B})) \leq \frac{1}{2}\sum_{i = 1}^{k}\| b_{i} \|$ by the triangular inequality. In particular, for the $\ell_{2}$-norm, we have $\mu^{(2)}(\mathcal{P}(\mathbf{B})) < \frac{1}{2}\sum_{i = 1}^{k}\| \mathbf{b}_{i} \|_{2}$ as the equality $\|\sum_{i = 1}^{k} a_{i} \mathbf{b}_{i}\|_{2} = \sum_{i = 1}^{k} a_{i}\|\mathbf{b}_{i}\|_{2}$ holds if and only if the $\mathbf{b}_{i}$'s are collinear.  However, $\mu^{(2)}(\mathcal{P}(\mathbf{B}))$ can be arbitrarily close to $\frac{1}{2}\sum_{i = 1}^{k}\| \mathbf{b}_{i} \|_{2}$ for appropriate choices of $\mathbf{B}$.

Finding a bound for the inner radius $\nu(\mathcal{P}(\mathbf{B}))$ is hard for general norms but easier for the euclidean norm if we assume that $\mathbf{B}$ is invertible.

>[!lemma] 
>Let $\mathbf{B} \in \operatorname{GL}_{n}(\mathbb{R})$ and let $\mathbf{C} = (\mathbf{B}^{-1})^{T}$ be its inverse-transpose. Then, $$\mathcal{P}(\mathbf{B}) = \left\{  x \in \mathbb{R}^{n} \; \left| \; \mathbf{c}_{i}^{T} \cdot \mathbf{x} \in \left[ -\frac{1}{2}, \frac{1}{2} \right) \text{ for all } i \in \{ 1,\ldots,n \}  \right\}\right.$$

>##### Proof
>The condition $\mathbf{x} \in \mathcal{P}(\mathbf{B})$ can be rewritten as $\mathbf{B}^{-1} \cdot x \in \left[ - \frac{1}{2}, \frac{1}{2} \right)^{n}$, which is equivalent to $\mathbf{c}_{i}^{T} \cdot \mathbf{x} \in \left[ -\frac{1}{2}, \frac{1}{2} \right)$ for all $i$.

>[!lemma] 
>Let $\mathbf{B} \in \operatorname{GL}_{n}(\mathbb{R})$ and let $\mathbf{C} = (\mathbf{B}^{-1})^{T}$ be its inverse-transpose. Then, $$\nu^{(2)}(\mathcal{P}(\mathbf{B})) = \min_{i \in \{ 1,\ldots, n \}} \frac{1}{2 \| \mathbf{c}_{i} \|_{2} } .$$

>##### Proof
>Recall that $\nu^{(2)}(\mathcal{P}(\mathbf{B})) = \inf\limits_{\mathbf{x} \in \mathbb{R}^{n} \setminus \mathcal{P}(\mathbf{B})} \|\mathbf{x}\|$. By the [[Diseguaglianze importanti|Cauchy-Schwarz inequality]], if $\|\mathbf{x}\|_{2}\|\mathbf{c}_{i}\|_{2} \leq \frac{1}{2}$ for all $i \in \{ 1,\ldots, n \}$, that is if $\| \mathbf{x} \|_{2} \leq \min\limits_{i \in \{ 1,\ldots,n \}} \frac{1}{2 \|\mathbf{c}_{i}\|_{2}}$, then $\mathbf{x} \in \mathcal{P}(\mathbf{B})$ by the lemma above. Therefore, any $\mathbf{x} \in \mathbb{R}^{n} \setminus \mathcal{P}(\mathbf{B})$ satisfies $\|\mathbf{x}\|_{2} > \min\limits_{i \in \{ 1,\ldots,n \}} \frac{1}{2 \|\mathbf{c}_{i}\|_{2}}$ and the vector $\frac{\mathbf{c}_{i}}{2 \|\mathbf{c}_{i}\|_{2}^{2}}$ has norm exactly $\frac{1}{2 \|\mathbf{c}_{i}\|_{2}}$: minimising over $i$ yields the result.

