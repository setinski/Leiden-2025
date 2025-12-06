---
tags: definition
---

Let $T$ be a [[Tiling]] for a [[Lattice]] $\mathcal{L} \subseteq \mathbb{R}^{n}$.

>[!define] #definition
>An algorithm solves $T$-tiling if, when given as input a [[Basis of a lattice|basis]] $\mathbf{B}$ of $\mathcal{L}$ and a target $\mathbf{t} \in \operatorname{Span}_{\mathbb{R}}\mathcal{L}$, it outputs a (unique) [[Closest Vector Problem|CVP]]/[[Bounded Distance Decoding|BDD]] vector $\mathbf{v} \in \mathcal{L}$ such that $\mathbf{e} = \mathbf{t} - \mathbf{v} \in T$.

>[!info] Note
>If an algorithm solves $T$-tiling, then, it solves:
>- AbsCVP up to a radius $\mu(T)$;
>- if $d(\mathbf{t},\mathcal{L}) \leq \nu(T)$, it solves:
>	- AbsBDD up to a radius $\nu(T)$;
>	- $1$-CVP;
>- if $d(\mathbf{t},\mathcal{L}) > \nu(T)$, it solves:
>	- $\alpha$-CVP up to an approximation factor $\alpha = \mu(T)/\nu(T)$.
>
>Indeed, 
>- $\mathbf{t} - \mathbf{v} \in T$ implies $\| \mathbf{t} - \mathbf{v} \| \leq \mu(T)$ by definition of $\mu(T)$;
>- if $d(\mathbf{t},\mathcal{L}) \leq \nu(T)$, there exists $\mathbf{v} \in \mathcal{L}$ such that $\|\mathbf{t} - \mathbf{v}\| \underbrace{ \leq  d(\mathbf{t},\mathcal{L})}_{ 1-\text{CVP} } \overbrace{ \leq \nu(T) }^{ \text{AbsBDD} }$, which implies $\mathbf{t} - \mathbf{v} \in T$: the algorithm outputs said $\mathbf{v}$ because of uniqueness;
>- if $d(\mathbf{t},\mathcal{L}) > \nu(T)$, for any $\mathbf{v} \in \mathcal{L}$ such that $\mathbf{v} - \mathbf{t} \in T$, we have $\|\mathbf{t} - \mathbf{v}\| \leq \mu(T) \leq \mu(T) \cdot \frac{d(\mathbf{t},\mathcal{L})}{\nu(T)}$, since $\frac{d(\mathbf{t},\mathcal{L})}{\nu(T)} > 1$.