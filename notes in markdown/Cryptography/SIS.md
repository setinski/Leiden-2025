---
tags: definition
---

>[!define] #definition
>##### $q$-ary lattice
>A lattice $\mathcal{L} \subseteq \mathbb{R}^{n}$ is $q$-ary if $q\mathbb{Z}^{n} \subseteq \mathcal{L} \subseteq \mathbb{Z}^{n}$.

>[!example] For ==#example==
>If $\mathbf{A} \in \mathbb{Z}_{q}^{n \times m}$, the lattice
>$$\Lambda_{q}^{\perp}(\mathbf{A}) \coloneq \{ \mathbf{z} \in \mathbb{Z}^{m} \mid \mathbf{A} \mathbf{z} \equiv 0 \mod q \}$$
>is $q$-ary of rank $m$ and $\det(\Lambda_{q}^{\perp}(\mathbf{A})) \leq q^{n}$.
>
>Indeed, $\Lambda_{q}^{\perp}(\mathbf{A}) = \ker(\mathbf{A} \colon \mathbb{Z}^{m} \to \mathbb{Z}_{q}^{n})$ and $$\frac{\mathbb{Z}^{m}}{\Lambda_{q}^{\perp}(\mathbf{A})} \cong \operatorname{im} \mathbf{A} \leq \mathbb{Z}_{q}^{n},$$
>which implies both $\operatorname{rk} \Lambda_{q}^{\perp}(\mathbf{A}) = m$ and $\det(\Lambda_{q}^{\perp}(\mathbf{A})) \leq q^{n}$, since $\left|\frac{\mathbb{Z}^{m}}{\Lambda_{q}^{\perp}(\mathbf{A})}\right| = \frac{\det(\Lambda_{q}^{\perp}(\mathbf{A}))}{\det(\mathbb{Z}^{m})} = \det(\Lambda_{q}^{\perp}(\mathbf{A}))$.

>[!define] #definition
>##### SIS problem
>For $n,m,q \in \mathbb{N}^{+}$ and $\beta \in \mathbb{R}^+$, we define the $\operatorname{SIS}_{n,m,q,\beta}$ as follows:
>- **Input**: $\mathbf{A} \gets \mathcal{U}(\mathbb{Z}_{q}^{n \times m})$ — matrix sampled uniformly;
>- **Output**: $\mathbf{z} \in \mathbb{Z}^{m} \setminus \{ \mathbf{0} \}$ such that $\|\mathbf{z}\| \leq \beta$ and $\mathbf{A} \mathbf{z} \equiv 0 \mod q$. In other words, a vector $\mathbf{0} \neq \mathbf{z} \in \Lambda_{q}^{\perp}(\mathbf{A}) \cap \beta \mathcal{B}$.

>[!info] Note
>$\operatorname{SIS}_{n,m,q,\beta}$  is vacuosly hard if $\beta < \lambda_{1}(\Lambda_{\mathbf{A}}^{\perp})$ and is trivial if $\beta \geq q = |(q,0,0,\ldots,0)|$.

Using the [[Minkowski bound]] we can prove the following:

>[!corollary] Corollary 
>For any $\mathbf{A} \in \mathbb{Z}_{q}^{n \times m}$, $\lambda_{1}^{\infty}(\Lambda_{q}^{\perp}(\mathbf{A})) \leq 2 \frac{\det \Lambda_{q}^{\perp}(\mathbf{A})^{1/m}}{(\operatorname{vol} \mathcal{B}_{\infty})^{1/m}} = 2q^{n/m}$ and $\lambda_{1}^{(2)}(\Lambda_{q}^{\perp}(\mathbf{A})) \leq q^{n/m} \sqrt{ \frac{2n}{\pi e} } + o(\sqrt{ n })$.

>[!lemma] 
>For any $f > 1$ and a random $\mathbf{A} \gets \mathcal{U}(\mathbb{Z}_{q}^{n \times m})$, it holds except with probability at most $f^{-n}$ that $$\lambda^{(\infty)}(\Lambda_{q}^{\perp}(\mathbf{A})) > \frac{\left( q/f \right)^{n/m} - 1}{2}.$$

>##### Proof
>We claim that for any $\mathbf{x} \in \mathbb{Z}_{q}^{m} \setminus \{ 0 \}$, $\mathbb{P}_{\mathbf{A} \gets \mathcal{U}(\mathbb{Z}_{q}^{n \times m})}[\mathbf{A} \mathbf{x} \equiv 0 \mod q] = q^{-n}$. Indeed, since $\mathbb{Z}_{q}$ is a finite field, $\mathbf{A}\mathbf{x}$ is uniform in $\mathbb{Z}_{q}^{n}$ over the uniform choice of $\mathbf{A}$.  Hence $\mathbb{P}_{\mathbf{A} \gets \mathcal{U}(\mathbb{Z}_{q}^{n \times m})}[\mathbf{A} \mathbf{x} \equiv 0 \mod q] = \mathbb{P}_{\mathbf{z} \gets \mathcal{U}(\mathbb{Z}_{q}^{n})}[\mathbf{z} \equiv 0 \mod q] = \prod_{i = 1}^{n}\mathbb{P}[z_{i} \equiv 0 \mod q] = q^{-n}$. Let then $\beta > 0$ and $\mathbf{C}\coloneq (\mathbb{Z}^{m} \setminus \{ \mathbf{0} \}) \cap \beta \mathcal{B}_{\infty} = \{ -\lfloor \beta \rfloor, \ldots,  \lfloor \beta \rfloor\}^{m} \setminus \{ \mathbf{0} \}$. Then $|\mathbf{C}| = (2 \lfloor \beta \rfloor + 1)^{m} - 1 \leq (2 \beta + 1)^{m}$, hence $$
\begin{align*}
\mathbb{P}_{\mathbf{A} \gets \mathcal{U}(\mathbb{Z}_{q}^{n \times m})}[\exists \mathbf{x} \in \mathbf{C} \mid \mathbf{A} \mathbf{x} \equiv 0 \mod q]&=\mathbb{P}_{\mathbf{A}}\left[\bigcup_{\mathbf{x} \in \mathbf{C}} \{\mathbf{A} \mathbf{x} \equiv 0 \mod q\}\right]\\&\leq \sum_{\mathbf{x} \in \mathbf{C}} \mathbb{P}_{\mathbf{A}}[\mathbf{A}\mathbf{x} \equiv 0 \mod q] =|C| q^{-n} \leq \frac{(2 \beta + 1)^{m}}{q^n}.
\end{align*}$$
Choosing $\beta = \frac{(q/f)^{n/m} - 1}{2}$ proves the assertion.

>[!info] Note
>Recall that $\lambda_{1}^{(2)}(\mathcal{L}) \geq \lambda_{1}^{\infty}(\mathcal{L})$. With more effort, one can show that $\lambda_{1}^{(2)}(\Lambda_{q}^{\perp}(\mathbf{A})) \geq q^{n/m} \Theta(\sqrt{ n })$ with probability greater than $1 - 2^{n}$.

### Hardness regimes of SIS

Let $\mathcal{L} = \Lambda_{q}^{\perp}(\mathbf{A})$. Since $\lambda_{1}(\mathcal{L}) \approx q^{n/m}$ with overwhelming probability ($\geq 1 - 2^{\Theta(n)}$), SIS has three clear regimes:
1. if $\beta \geq q$, then $\operatorname{SIS}_{n,m,q,\beta}$ admits the trivial solution $(q,0,0,\ldots,0)$;
2. if $\beta \geq (\gamma_{2} + \varepsilon)^{m} q^{n/m}$ (and in fact whenever $\beta \geq (\gamma_{2} + \varepsilon)^{m'} q^{n/m'}$ for some $m' \leq m$ since a solution to $\operatorname{SIS}_{n,m',q,\beta}$ can be extended to a solution to $\operatorname{SIS}_{n,m,q,\beta}$  by padding it with $m-m'$ zeros), the problem can be solved using LLL in polynomial time;
3.  if $\beta < q^{n/m}$, the the problem is vacuously hard with overwhelming probability.
