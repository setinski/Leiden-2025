---
tags: definition
aliases: SVP
---

>[!define] #definition
>##### SVPs
>The approximate Shortest Vector Problem with approximation factor $\alpha \geq 1$, denoted ==$\alpha$-SVP==, is defined as follows:
>- Given as input the basis $\mathbf{B}$ of a lattice $\mathcal{L}$
>- Output $\mathbf{v} \in L \setminus \{ \mathbf{0} \}$ such that $\| \mathbf{v} \| \leq \alpha \lambda_{1}(L)$.
>
>==ExactSVP== is by definition $1$-SVP. ==$\alpha$-HSVP== is defined as follows:
>- Given as input the basis $\mathbf{B}$ of a lattice $\mathcal{L}$
>- Output $\mathbf{v} \in L \setminus \{ \mathbf{0} \}$ such that $\| \mathbf{v} \| \leq \alpha \lambda_{1}(L)$.
>
>==AbsSVP== is defined as follows:
>- Given as input the basis $\mathbf{B}$ of a lattice $\mathcal{L}$ and some $C \in \mathbb{R}^{+}$
>- Output $\mathbf{v} \in L \setminus \{ \mathbf{0} \}$ such that $\| \mathbf{v} \| \leq C$.

>[!info] Note
>A shortest vector is never unique, for example because $\mathbf{v}$ and $-\mathbf{v}$ have the same norm.
