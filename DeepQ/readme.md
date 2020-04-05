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


<img src="https://render.githubusercontent.com/render/math?math=">


## References
1. Modern Reinforcement Learning: Deep Q Learning in PyTorch, Phil Tabor, Udemy
