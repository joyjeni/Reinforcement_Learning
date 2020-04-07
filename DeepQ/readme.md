* **Agent** learns and makes decisions and maximizes rewards over time
* **Environment** is what changes and its representation
* **Rewards** almost always part of environment
* Set of all possible states **state space**
* Set of all possible actions **action space**
* **Markov Decision Process** state depends only on previous state and action and governed by probability distribution

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

<img src="https://render.githubusercontent.com/render/math?math=G_t=R_{t%2B 1} %2B \gamma R_{t%2B 2} %2B \gamma^2R_{t %2B 3}=\sum_{k=0}^\infty \gamma ^ k R_{t %2B k %2B 1}">

## The Policy
Mapping of states to actions. It can be proabilistic. Policy tells how agent will act in some state


<img src="https://render.githubusercontent.com/render/math?math=\Pi"> - Policy


<img src="https://render.githubusercontent.com/render/math?math=\Pi(s,a) \to "> Probability of selecting a in s

## Value Function
Markov Property + Policy -> Value Function

## Q Learning Algorithm

1. Initialize Q for all states s and actions a
2. Initialize 
<img src="https://render.githubusercontent.com/render/math?math=\alpha = 0.001, \gamma = 0.9, \epsilon_max = 1.0 , \epsilon_min = 0.01">
3. Repeat for n_episodes
      * Initialize state s
      * For each step of episode
          Choose a with epsilon-greedy
          Perform a, get new state s' and reward r
          
          <img src="https://render.githubusercontent.com/render/math?mathQ(s,a) =Q(s,a) %2B \gamma(r %2B \gamma max Q(s',a_max)-Q(s,a))">
          s=s'
 * Agent should be a class
 * Q is a dictionary
 * Decrement epsilon over time
 * Seperate files
 * Plot average score over 100 games
 * Run for 500,000 total games



<img src="https://render.githubusercontent.com/render/math?math=">

## References
1. Modern Reinforcement Learning: Deep Q Learning in PyTorch, Phil Tabor, Udemy
