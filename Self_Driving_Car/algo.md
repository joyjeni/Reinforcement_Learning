### Self Driving Car Implementation

1. When car goes to sand penelize and slow down.
2. 5 env 

3. 3 actions - Go left, right, front
4. action to rotation - 0,20,-20 . go straight, go right, go left
5. last_reward - if goes to sand negative reward, if not positive reward

6. scores[] - Array of last_reward. To plot Mean square reward wrt time

7. global sand [] - Its map size.  Initialise 1 if sand and 0 otherwise
8. pos - position of car w.r.to last position and velocity
9. signal - 1 full sand or full density and receives heavy penalty
10. #### Orientation 
* Towards goal : 0<sup>0
* Left  : - 45 <sup>0
* Right : %20 45 <sup>0

