### Actions : 
Actions are changes to an agents configuration
### Observations:
Observations are what an agent can measure of its environment
### Rewards:

Rewards are used to infer optimal actions to correspond with observation states.

Concepts:

s-State 

a-Action

R-Reward

<img src="https://render.githubusercontent.com/render/math?math=\documentclass[a4paper,12pt]{article}
\usepackage{amssymb,mathtools}
\begin{document}
\[\underbrace{\text{New}Q(s,a)}_{\scriptstyle\text{New Q-Value}}=Q(s,a)+\mkern-34mu\underset{\text{New Q-Value}}{\underset{\Bigl|}{\alpha}}\mkern-30mu[\underbrace{R(s,a)}_{\scriptstyle\text{Reward}}+\mkern-30mu\underset{\text{Discount rate}}{\underset{\Biggl|}{\gamma}}\mkern-75mu\overbrace{\max Q'(s',a')}^{\scriptstyle\substack{\text{Maximum predicted reward, given} \\ \text{new state and all possible actions}}}\mkern-45mu-Q(s,a)]\]
\end{document}"> - Discount

### The Bellman Equation


<img src="https://render.githubusercontent.com/render/math?math=V(s)=max_{a} ( {R(s,a)} %2B {\gamma V(s')})">



