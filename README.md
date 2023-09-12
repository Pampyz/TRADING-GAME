# TRADING-GAME
The TRADING-GAME investigates different questions posed in the context of a special multiplayer game. The game can be described as the "game of economics', where actors try to improve their own standing in an economic environment. The game is modelled on an 'austrian' interpretation of value & economics, where every agent have their own valuation of different assets. This valuation is considered subjective and not comparable between agents.

We also attempt to use this framework to model economic time-series using certain emergent features of the inter-agent communication which is enabled in the game. In other words, we are using this framework as an inductive bias on the underlying structure of the time-series. Specifically, we attempt to model exchange rates of different kinds as the result of a multi-player process where each player act on a market based on their own utilities & policies. This model is then trained end-to-end.

Multi-player games of different kinds are generally characterized by imperfect information (meaning that no single player has access to all knowledge) and hence leads to the importance of various forms of communication. Furthermore, in this case all players have a different utility - making communication in various ways important not just to probe the state, but also the utilities of other agents in order to make good decisions.

<h2> Practical setting </h2>

The full game consists of <i> agents</i>, each possessing <i>assets</i>, a <i>utility</i>, and <i>time</i>. There also exist <i> marketplaces </i> where agents can trade assets.  Each actor can at every step take one of several <i>actions</i>, determined by the current state. 

In this brief explanation of the full game, every word in italics corresponds to a class in the implementation of the game. Also, sometimes the words agent & actors are used interchangeably - they mean the same thing. Due to the complexity of the full game, many experiments are run on reduced variants of it.

<h4> Agents </h4>
Every agent possesses a certain quantity of assets, a utility function, and time. Time can be considered a special asset, it reduces every timestep until it reaches zero, then the agent dies. The goal for every agent is to find a policy that maximizes their own specific utility function. Some actors are 'dummys' and always act according to a specific policy (ex. randomly), without learning.

<h4>Assets</h4>
An typical asset has a global <i>stock</i> corresponding to the amount existing, a global <i>supply</i> corresponding to how much more of the asset is created (or destroyed) every time-step. The supply can be dependent on the actions of the actors.

Some special assets are 'knowledge', giving.

In general, there are defined relations between assets, 
Also there are graph relations between them -> relation

<h4>Relations</h4>
A relation defines how assets can be combined. This in turn is a determinant of the state transition function. For example, a relation can...

<h4>Policies</h4>
Every agent has a policy which determines what actions it will take given a history of observations and . Every agent is considered rational - meaning that it will always try to maximize its own utility function in the long run.

<h4>Utilities</h4>
Agents have utilities 
The utilities are assumed to satisfy
U(alternative 1)
This leads naturally to an individual reward function 

<h4>Marketplaces</h4>
In the full game the agents have 
In some experiments they can barter (trade one asset for any other), in others theycan via a special'money', and in some they can also trade labor.

The reduced game where all the utilities are the same and

<h2> Theoretical setting </h2>
<h4>MDP</h4>
The MDP (Markov decision process) is a central object in control theory, game theory and reinforcement learning. In a MDP, there is a single agent acting by selecting actions a in an environment manifested in the state. The state updates and the agent receives a reward. Depending on the There might be  
When policy wants to be found: RL. When state transisions are known: search. Model-based. on-policy & off-policy

<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$
<h5>Policy: </h5>

$p(a_{t}|s_{t}) = \pi(s_{t})$

<h5>Reward:</h5>

$r(s_{t+1}, s_{t})$

<h4>POMDP</h4>
Partially observable MDP:
Identical to a MDP exept that the agent only has access to an observation of the state - not necessarily the full state of the environment.

<h5>State transition function & reward function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$,

$r(s_{t+1}, s_{t})$
<h5>Observation function: </h5>

$p(o_{t}|s_{t}) = \omega(s_{t})$

<h5>Policy: </h5>

$p(a_{t}|o_{t}) = \pi(o_{t})$


<h4>DPOMPD</h4>
In a decentralized POMDP the POMDP is generalized in that there is a multitude of agents, . In an analogous way there is a DMDP (where all agents have full observation of the state)

<h4> TRADING-GAME </h4>
The natural extension to the DPOMDP is the setting where all agents have different rewards functions. This setting is called a POSG - a partially observable stochastic game.  

TRADING GAME is a special kind of POSG - where actors attempt 
The state transition depends


Goal of MDP, ... is to maximize reward. All such processes also have in common that 
<h2> Metrics </h2>

<h2> Experiments / Example games </h2>

Zero-sum trading.
In this game all the assets have fixed 

Subcategory: Fish catching

Emergency of marketplaces
Investigate how marketplaces of barter -> marketplace of money. Especially 
Marketplace of 'weak' money -> marketplace of hard money

Healthy economy scenario?

Fiat blackhole scenario?