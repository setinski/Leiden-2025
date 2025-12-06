---
tags: definition
aliases: ["covering", "packing", "tiling"]
---

>[!define] #definition
>##### Covering, packing, tiling
>Let $\mathcal{L}$ be a [[Lattice]] and let $S \subseteq \operatorname{Span}_{\mathbb{R}}\mathcal{L}$. Then $S$ is
>- an ==$\mathcal{L}$-covering==, if $\mathcal{L} + S = \operatorname{Span}_{\mathbb{R}} \mathcal{L}$;
>- an ==$\mathcal{L}$-packing== if for any pair $\mathbf{t},\mathbf{u} \in \mathcal{L}$, $t + S \cap u + S = \varnothing$;
>- an ==$\mathcal{L}$-tiling== (or a *fundamental domain*)  if it both the above hold, i.e. for each $\mathbf{x} \in \operatorname{Span}_{\mathbb{R}} \mathcal{L}$, there exist *unique* $\mathbf{v} \in \mathcal{L}$ and $\mathbf{e} \in S$ such that $\mathbf{x} = \mathbf{v} + \mathbf{e}$.

>[!proposition] 
>Let $\mathcal{L} \subseteq \mathbb{R}^{n}$ be a lattice of rank $k$. Let $S \subseteq \operatorname{Span}_{\mathbb{R}}\mathcal{L}$ be a measurable set. If $S$ is an $\mathcal{L}$-(covering,packing,tiling) then $\operatorname{vol}(S)\mathrel{(\geq, \leq, =)} \operatorname{vol}(\mathcal{P}(\mathbf{B}))$, where $\mathbf{B}$ is a [[Basis of a lattice|basis]] of $\mathcal{L}$. In particular, every tiling has the same volume.

>##### Proof
>Note that since the [[Fundamental parallelogram]] $P \coloneq \mathcal{P}(\mathbf{B})$ is an $\mathcal{L}$-tiling, we may write $S = \operatorname{Span}_{\mathbb{R}}\mathcal{L} \cap S = \bigsqcup\limits_{\mathbf{x} \in \mathcal{L}} (\mathbf{x} + P) \cap S$. Let $T \coloneq \bigcup\limits_{\mathbf{x} \in \mathcal{L}} P \cap (S - \mathbf{x}) \subseteq P$. Then $\operatorname{vol} T \leq \operatorname{vol} P$ and  $\operatorname{vol} T \leq \operatorname{vol} S$ by the properties of the Lebesgue measure (and the fact that $P \cap (S - \mathbf{x}) = ((P+\mathbf{x}) \cap S) - \mathbf{x}$). If $S$ is a covering, then $\operatorname{vol} P = \operatorname{vol} T \leq \operatorname{vol} S$. If $S$ is a packing, then the union in $T$ is disjoint and $\operatorname{vol} S = \operatorname{vol} T \leq \operatorname{vol} P$.

>[!define] #definition
>##### Inner radius and covering radius
>If $T$ is a tiling for a lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$, its ==inner radius== is by definition $\nu(T) = \inf\limits_{x \in \mathbb{R}^{n} \setminus T}\|x\| = \sup \{r \in \mathbb{R}^{+} \mid r \mathcal B \subseteq T\}$ and its ==covering radius== is defined as $\mu(T) = \sup\limits_{x \in T}\|x\| = \inf\{r \in \mathbb{R}^{+} \mid T \subseteq r \mathcal B\}$.

>[!info] Note
>For any tiling $T$ of a lattice $\mathcal{L}$, we have:
>- $\mu(T) \geq \mu(\mathcal{L}) \coloneq \sup_{x \in \operatorname{Span}_{\mathbb{R}}\mathcal{L}} d(x,\mathcal{L})$, since for every $\mathbf{x} \in \operatorname{Span}_{\mathbb{R}}\mathcal{L}$, $\mathbf{x} = \mathbf{v} + \mathbf{e}$, for some $\mathbf{e} \in T$ and $\mathbf{v} \in \mathcal{L}$, hence $\mu(T) > \|\mathbf{e}\| = \|\mathbf{x} - \mathbf{v}\| \geq d(\mathbf{x},\mathcal{L})$.
>- $\nu(T) \leq \frac{\lambda_{1}(\mathcal{L})}{2}$, as $\frac{\lambda_{1}(\mathcal{L})}{2}\mathcal B$ contains at least two points of $\mathcal{L}$, whereas $T \cap \mathcal{L} = (0 + T) \cap \mathcal{L} = \{0\}$: hence $\frac{\lambda_{1}(\mathcal{L})}{2}\mathcal B \not \subseteq T$.