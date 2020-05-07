
This is an enhancement from Self Driving Car implemented using DQN algorithm. https://github.com/joyjeni/Reinforcement_Learning/tree/master/dqn_sdc


### SDC implementation using Twin Delayed Deep Deterministic Model TD3

#### Algorithm

1. Allocate memory for experience replay buffer.
2. Create Actor Model and Actor Target. Actor takes states s as input. Here the states S1 is 60x60 cropped area from the center of car location and S2 is next 60x60 location towards car movement  and S3 is orientation of car with respect to goal.Actor outputs actions go front, left, right, orientation 

3. Build two neural networks for critic model and two neural networks for critic target. Critic outputs Plan. Its also called reward table. 

### Training 

Step 4: sample a batch of transitions (s, s’, a, r) from the memory say 1000 transactions

Step 5: From the next state s’, the Actor target plays the next action a’. It outputs logits of 3 actions 

Step 6: We add Gaussian noise to this next action a’ and we clamp it in a range of values (rewards) supported by the environment

Step 7: The two Critic targets take each the couple (s’, a’) as input and return two Q-values Qt1(s’,a’) and Qt2(s’,a’) as outputs. Use variational auto encoder logic to compute difference in two loss values trying to compete with each other.

Step 8: We keep the minimum of these two Q-values: min(Qt1, Qt2). 

Step 9: We get the final target of the two Critic models, which is: Qt = r + γ * min(Qt1, Qt2), where γ is the discount factor

Step 10: The two Critic models take each the couple (s, a) as input and return two Q-values Q1(s,a) and Q2(s,a) as outputs

Step 11: We compute the loss coming from the two Critic models: Critic Loss = MSE_Loss(Q1(s,a), Qt) + MSE_Loss(Q2(s,a), Qt)

Step 12: We backpropagate this Critic loss and update the parameters of the two Critic models with a SGD optimizer

Step 13: Once every two iterations, we update our Actor model by performing gradient ascent on the output of the first Critic model. Thatsy its called ** Twin Delayed ** Deep Deterministic Model 

Step 14: Still once every two iterations, we update the weights of the Actor target by polyak averaging



Step 15: Still once every two iterations, we update the weights of the Critic target by polyak averaging





## References
1. Addressing Function Approximation Error in Actor-Critic Methods, Addressing Function Approximation Error in Actor-Critic Methods, Scott Fujimoto1Herke, van Hoof, David Meger,https://arxiv.org/pdf/1802.09477.pdf

2. TD3, https://github.com/tie304/td3/blob/master/modules/td3.py

3. Bipedal Walker, https://github.com/nikhilbarhate99/TD3-PyTorch-BipedalWalker-v2/blob/master/train.py
4. https://github.com/MrSyee/pg-is-all-you-need/blob/master/04.TD3.ipynb
5. https://mc.ai/td3-learning-to-run-with-ai/
6.https://github.com/Ullar-Kask/Udacity-DRLND/blob/master/p2/src/ddpg_agent.py
7. https://github.com/ikostrikov/pytorch-ddpg-naf/blob/master/main.py
