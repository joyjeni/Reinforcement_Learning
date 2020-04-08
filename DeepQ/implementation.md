1. Split code into two classes. Network class and Agent class.
## Network Class

2. 2 linear layers, hidden layers is 128 x n_actions
3. Use Adam optimizer with learning rate 0.001
4. Mean Squared error loss # nn.MSELoss()
5. Do device selection
6. Add relu activation function

## Agent Class
7. Init keeps track of gamma, epsilon and action space.
8. Epsilon greedy action selection use tensor.item()
9. Decrement epsilon
10. Do zero grad
<img src="https://render.githubusercontent.com/render/math?math=Q(s,a)=Q(s,a) %2B \alpha (r %2B \gamma max Q(s',a_max) -Q(s,a))">
