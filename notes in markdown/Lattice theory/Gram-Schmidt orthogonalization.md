---
aliases: ["orthogonalization","GSO"]
---

>[!define] #definition
>##### Gram-Schmidt Orthogonalization (GSO)
>The ==GSO== $\mathbf{B}^{*}$ of a non-singular matrix $\mathbf{B}$ is defined recursively by $\mathbf{b}_{i}^{*} = \pi_{i}(\mathbf{b}_{i})$, where $\pi_{i}$ is the function
>$$\pi_{i}\colon \mathbf{x} \mapsto \pi^{\perp}_{\operatorname{Span}(\mathbf{b}_{1}^{*},\ldots,\mathbf{b}_{i-1}^{*})}(\mathbf{x}) = \mathbf{x} - \sum_{j = 1}^{i-1} \frac{\mathbf{x} \cdot \mathbf{b}_{j}^{*}}{\|\mathbf{b}_{j}^{*}\|^{2}_{2}} \mathbf{b}_{j}^{*}.$$

>[!info] Note
>The GSO can also be written as a matrix decomposition: $\mathbf{B} = \mathbf{B}^{*} \cdot \mathbf{T}$, where $\mathbf{T}$ is an upper triangular matrix with unit diagonal and $\mathbf{B}^{*}$ is a matrix with orthogonal columns. This decomposition is intimately related with the [QR decomposition](https://en.wikipedia.org/wiki/QR_decomposition): if $\mathbf{B} = \mathbf{Q} \cdot \mathbf{R}$ where $\mathbf{Q}$ is orthogonal and $\mathbf{R}$ is upper triangular, then one has $\mathbf{B} = \mathbf{Q} \mathbf{D} \mathbf{T}$, where $\mathbf{Q} \mathbf{D} = \mathbf{B}^{*}$ and $\mathbf{D} \coloneq \operatorname{diag}(r_{ii})$.
>
>Note also that $\prod_{i = 1}^{n} \|b_{i}^{*}\|_{2} = \sqrt{|\det \mathbf{{B}^{*}}^{T} \mathbf{B}^{*}|} = \sqrt{|\det \mathbf{B}^{T} \mathbf{B}|} = \det \mathcal{L}(\mathbf{B})$.

>[!theorem] 
>Let $\mathcal{L}$ be a [[Lattice]] of rank $k$ and let $\mathbf{v} \in \mathcal{L}$. Then $\pi_{\mathbf{v}}^{\perp}(\mathcal{L})$ is a lattice of rank $k-1$.

>##### Proof
>Since $\pi_{\mathbf{v}}^{\perp}$ is a linear map, $\mathcal{L}' \coloneq \pi_{\mathbf{v}}^{\perp}(\mathcal{L})$ is a group. To show that $\mathcal{L}'$ is discrete, we make the following claim: every $\mathbf{x} \in \pi_{\mathbf{v}}^{\perp}(\mathcal{L})$ has a preimage $\mathbf{y}$ such that $|\mathbf{y} \cdot \mathbf{v}| \leq \frac{1}{2} \| \mathbf{v} \|^{2}$ i.e. such that $\mathbf{y} \in \mathbf{x} + [-\frac{1}{2}, \frac{1}{2}) \cdot \mathbf{v}$. Note that this implies the discreteness of $\mathcal{L}'$: if $\mathcal{L}'$ were not discrete, $\mathcal B \cap \mathcal{L}$ would contain infinitely many points, each of which would admit a distinct preimage in the set $( \mathcal B + [-\frac{1}{2}, \frac{1}{2} ) \cdot \mathbf{v}) \cap \mathcal{L}$. However, by uniform discreteness of $\mathcal{L}$, the set  the set $( \mathcal B + [-\frac{1}{2}, \frac{1}{2} ) \cdot \mathbf{v}) \cap \mathcal{L}$ cannot be infinite, since $\mathcal B + \left[-\frac{1}{2}, \frac{1}{2} \right) \cdot \mathbf{v}$ is bounded.
>
>To prove the claim, take any preimage $\mathbf{y}'$ of $\mathbf{x}$, set $k \coloneq \left\lfloor \frac{|\mathbf{y}'\cdot \mathbf{v}|}{\| \mathbf{v} \|^{2}} \right\rceil \in \mathbb{Z}$ and set $\mathbf{y} \coloneq \mathbf{y}' - k\mathbf{v}$. Indeed $\mathbf{y} \cdot \mathbf{v} = \left( \frac{|\mathbf{y}'\cdot \mathbf{v}|}{\| \mathbf{v} \|^{2}} - k \right)\|v\|^{2} \leq \frac{1}{2} \|v\|^{2}$.
>
>Note that $\operatorname{Span}_{\mathbb{R}} \mathcal{L}' = \pi_{\mathbf{v}}^{\perp}(\operatorname{Span}_{\mathbb{R}} \mathcal{L})$ since $\pi_{\mathbf{v}}^{\perp}$ is linear and $\pi_{\mathbf{v}}^{\perp}(\operatorname{Span}_{\mathbb{R}} \mathcal{L}) \lneq \operatorname{Span}_{\mathbb{R}} \mathcal{L}$ since $\mathbf{v} \notin \pi_{\mathbf{v}}^{\perp}(\operatorname{Span}_{\mathbb{R}} \mathcal{L})$. Hence $\operatorname{\dim}_{\mathbb{R}}(\pi_{\mathbf{v}}^{\perp}(\operatorname{Span}_{\mathbb{R}} \mathcal{L})) = \operatorname{rk}(\mathcal{L}') \leq k-1$. Furthermore, $\operatorname{Span}_{\mathbb{R}} \mathcal{L} \subseteq \mathbf{v} \cdot\mathbb{R} + \operatorname{Span}_{\mathbb{R}} \mathcal{L}'$, hence $\operatorname{rk}(\mathcal{L}') \geq k-1$.