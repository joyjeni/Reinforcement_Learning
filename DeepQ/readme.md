* **Agent** learns and makes decisions
* **Environment** is what changes and its representation
* **Rewards** almost always part of environment
* Set of all possible states **state space**
* Set of all possible actions **action space**
* **Markov Decision Process** state depends only on previous state and action

## Probabilistic Transitions
Actions cause state transitions

<img src="https://render.githubusercontent.com/render/math?math=p(s',r|a,s) \neq 1">

<img src="https://render.githubusercontent.com/render/math?math=\sum_{(s',r)} p(s',r|a,s)=1">
Probabilities define our dynamics

## Episodic Game Play
Terminal state is unique. Ensures sum over rewards finite. <img src="https://render.githubusercontent.com/render/math?math=G_T=0">

## Reward Discounting

Not all tasks are episodic!


<img src="https://render.githubusercontent.com/render/math?math=\sum_{t=0}^\infty R_t \to \infty">
Fix by discounting factor <img src="https://render.githubusercontent.com/render/math?math=\gamma">


<img src="https://render.githubusercontent.com/render/math?math=0 \leq \gamma \leq 1">
if ,<img src="https://render.githubusercontent.com/render/math?math=\gamma \to 1 ">Far sighted ,

<img src="https://render.githubusercontent.com/render/math?math=\gamma \to 0"> Myopic

<img src="https://render.githubusercontent.com/render/math?math=0.95 \leq \gamma \leq 0.99">

<img src="https://render.githubusercontent.com/render/math?math=G_t=R_{t+1} %2B \gamma R_{t+2} %2B \gamma^2R_{t %2B 3}=\sum_{k=0}^\infty \gamma ^ k R_{t %2B k %2B 1}">



<img src="https://render.githubusercontent.com/render/math?math=">

## References
1. Modern Reinforcement Learning: Deep Q Learning in PyTorch, Phil Tabor, Udemy
