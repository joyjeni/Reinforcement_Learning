Step 1: We initialize the Experience Replay memory

* Initialize the Experience Replay memory. This will store the past transitions from which it learns the Q-values.
![step1](https://i.imgur.com/oap1vFv.png)

** create memory object 
** Add any transition into memory object
** 


Step 2: We build one neural network for the Actor model and one neural network for the Actor target
![step2](https://i.imgur.com/tGZkP5v.png)

Step 3: We build two neural networks for the two Critic models and two neural networks for the two Critic targets
## Training 

Step 4: We sample a batch of transitions (s, s’, a, r) from the memory

Step 5: From the next state s’, the Actor target plays the next action a’

Step 6: We add Gaussian noise to this next action a’ and we clamp it in a range of values supported by the environment

Step 7: The two Critic targets take each the couple (s’, a’) as input and return two Q-values Qt1(s’,a’) and Qt2(s’,a’) as outputs

Step 8: We keep the minimum of these two Q-values: min(Qt1, Qt2)

Step 9: We get the final target of the two Critic models, which is: Qt = r + γ * min(Qt1, Qt2), where γ is the discount factor

Step 10: The two Critic models take each the couple (s, a) as input and return two Q-values Q1(s,a) and Q2(s,a) as outputs

Step 11: We compute the loss coming from the two Critic models: Critic Loss = MSE_Loss(Q1(s,a), Qt) + MSE_Loss(Q2(s,a), Qt)

Step 12: We backpropagate this Critic loss and update the parameters of the two Critic models with a SGD optimizer

Step 13: Once every two iterations, we update our Actor model by performing gradient ascent on the output of the first Critic model

Step 14: Still once every two iterations, we update the weights of the Actor target by polyak averaging

Step 15: Still once every two iterations, we update the weights of the Critic target by polyak averaging

 
## Reference
1. Deep Reinforcement Learning: Twin Delayed DDPG Algorithm,https://www.mlq.ai/deep-reinforcement-learning-twin-delayed-ddpg-algorithm/

2. https://github.com/safal-singh/TD3PG-Reinforcement-Learning
3. DDPG, https://www.mlq.ai/deep-reinforcement-learning-twin-delayed-ddpg-algorithm/
4. TD3, https://arxiv.org/pdf/1802.09477.pdf
5. TD3 Bipedel walker, https://github.com/PacktPublishing/Reinforcement-Learning-Algorithms-with-Python/blob/master/Chapter08/TD3.py
6. All policy gradients, https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html
7. DPG, http://proceedings.mlr.press/v32/silver14.pdf.

