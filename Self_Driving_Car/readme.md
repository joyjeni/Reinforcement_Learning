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

<img src="https://render.githubusercontent.com/render/math?math=\gamma"> - Discount factor 
### The Bellman Equation


<img src="https://render.githubusercontent.com/render/math?math=V(s)=max_{a} ( {R(s,a)} %2B {\gamma V(s')})">

V(s) - Current State
R(s,a) - Reward for current state action
s' - New state


max of every four state - Left, Right, Up and Down




### References
1. https://medium.com/code-heroku/building-a-crawling-robot-with-q-learning-251e2550d824
2. https://www.rand.org/content/dam/rand/pubs/papers/2008/P550.pdf
3. Prioritized Experience Replay, https://arxiv.org/abs/1511.05952


