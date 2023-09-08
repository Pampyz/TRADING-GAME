# TRADING-GAME
The TRADING-GAME investigates different questions posed in the context of a special multiplayer game. The game can be described as the "game of economics', where actors try to improve their own standing. The game is modelled on an 'austrian' interpretation of value & economics, where every agent have their own valuation of different assets which is not comparable between agents.

We also attempt to use this framework to model economic time-series using certain emergent features of the inter-agent communication. In other words, we are using this framework as an inductive bias on the underlying structure of the time-series. Specifically, we attempt to model exchange rates of different kinds as the result of a multi-player process where each player act on a market based on their own utilities & policies. This model is trained end-to-end.

Multi-player games of different kinds are generally characterized by imperfect information (meaning that no single player has access to all knowledge) and hence leads to the importance of communication. Furthermore, in this case all players have a different utility - making communication in various ways important not just to probe the state, but also the utilities of other agents in order to make good decisions.

<h2> Practical setting </h2>

The full game consists of <i> actors</i>, each possessing <i>assets</i>, a <i>utility</i>, <i>capacity</i>, and <i>time</i>. There also exist <i> marketplaces </i> where actors can trade assets.  Each actor can at every step take one of several <i>actions</i>, determined by the current state. 

For every word in italics, there is a corresponding class in the repo.

<h4>Assets</h4>
Assets have 

<h4>Policies</h4>
Every 

<h4>Utilities</h4>
Actors have 

<h4>Marketplaces</h4>
In some experiments they can barter (trade one asset for any other), in others theycan via a special'money', and in some they can also trade labor.



The reduced game where all the utilities are the same and

<h2> Theoretical setting </h2>
<h4>MDP</h4>
The MDP (Markov decision process) is a central object in game theory, control theory and reinforcement learning. In a MDP, there is a single agent acting by selecting actions a in an environment manifested in the state. The state updates and the agent receives a reward.

State transition function:
$p(s_{t+1}|s_{t}, a{t})$



Policy:
$p(a_{t}|s_{t} = \pi(a_{t})$

<h4>POMDP<h5>
Partially observable MDP:
Agent gets an observation which is not necessarily the full state of the environment. Otherwise the same - the state is updated based 

<h4>Dec-POMPD</h4>
Decentralized POMDP:
Multitude of agents!

<h4> TRADING-GAME </h4>
When they have different rewards function - Partially observable stochastic game.
TRADING GAME is a kind of POSG - where actors attempt 

*Experiments