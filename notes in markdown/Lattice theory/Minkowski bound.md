>[!lemma] Blichfeldt's Lemma
>For any [[Lattice]] $\mathcal{L}$ of rank $k$ and any measurable set $S \subseteq \operatorname{Span}_{\mathbb{R}}\mathcal{L}$ such that $\operatorname{vol}_{k}(S) > \det \mathcal{L}$, there exists distinct $\mathbf{x},\mathbf{y} \in S$ such that $\mathbf{x}-\mathbf{y} \in \mathcal{L}$.

>##### Proof
>The Lemma follows from [[Tiling|a characterisation of packings]].

>[!theorem] Minkowski's Convex Body Theorem
>For any lattice $\mathcal{L}$ of rank $K$ and any symmetric ($S = - S$) convex set $S \subseteq \operatorname{Span}_{\mathbb{R}}\mathcal{L}$ such that $\operatorname{vol}(S) > 2^{n} \det \mathcal{L}$, the set $S \cap \mathcal{L}$ contains a non-zero vector, i.e. $|S \cap \mathcal{L}| > 1$.

>##### Proof
>Since $S$ is symmetric and convex, $\frac{1}{2} S \subseteq S$. Since $\operatorname{vol}\left( \frac{1}{2} S \right) > \det \mathcal{L}$, by Blichfeldt's Lemma, there exist $\mathbf{x},\mathbf{y} \in S$ such that $\mathbf{x}-\mathbf{y} \in \mathcal{L} \setminus \{ 0 \}$, but $\mathbf{x} - \mathbf{y} \in \frac{1}{2} S + \frac{1}{2} S = S$.

>[!theorem] Minkowski's bound
>The minimal distance of any lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ of full rank is bounded above:$$\lambda_{1}(\mathcal{L}) \leq 2 \left(\frac{\det \mathcal{L}}{\operatorname{vol} \mathcal B}\right)^{\frac{1}{n}},$$
>where $\mathcal B$ is the closed ball of radius one.

>##### Proof
>The set $\frac{(2 + r)(\det \mathcal{L})^{\frac{1}{n}}}{(\operatorname{vol} \mathcal B)^{\frac{1}{n}}} \mathcal B$ is convex and symmetric and has volume $(2 + r)^{n} \det \mathcal L$: by Minkowski's Convex Body Theorem, $\mathcal{L}$ contains an element of norm less than $\frac{(2 + r)(\det \mathcal{L})^{\frac{1}{n}}}{(\operatorname{vol} \mathcal B)^{\frac{1}{n}}}$. In the limit $r \to 0$ we obtain the desired bound.

>[!note] Remark
>In the $\ell_{2}$ norm, $\mathcal B$ has volume $\frac{\pi^{n/2}}{\Gamma\left( \frac{n}{2} + 1 \right)}$ and $\Gamma(x+1) \sim \sqrt{ 2 \pi x }\left( \frac{x}{e} \right)^{x}$ by [Stirling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation). Therefore we have:$$\lambda_{1}^{(2)}(\mathcal{L}) \leq \det(\mathcal{L})^{\frac{1}{n}}\left(\sqrt{ \frac{2n}{\pi e} } + o(\sqrt{ n })\right).$$
>Note also that the restriction of an $\ell_{2}$-ball to any subspace of $\mathbb{R}^{n}$ is still an $\ell_{2}$-ball, which proves that the bound above is not limited to full rank lattices.