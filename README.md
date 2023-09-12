# TRADING-GAME
The TRADING-GAME investigates different questions posed in the context of a special multiplayer game. The game can be described as the "game of economics', where actors try to improve their own standing in an economic environment. The game is modelled on an austrian interpretation of value & economics, where every actor is assumed to possess their own specific valuation of assets. This valuation is considered subjective and not comparable between actors.

We also attempt to use this framework to model economic time-series using certain emergent features of the inter-agent communication which is enabled in the game. Another way of formulating this is that we are using this framework as an inductive bias on the underlying structure of the time-series. Specifically, we attempt to model exchange rates of different kinds as the result of a multi-player process where each player acts on a market based on their own utilities & policies. This model is then trained end-to-end.

Multi-player games of different kinds are generally characterized by imperfect information (meaning that no single player has access to all knowledge) and hence leads to the importance of various forms of communication. Furthermore, in this case all players have a different utility - making communication in various ways important not just to probe the state, but also the utilities of other agents in order to make good decisions.

<h1> Practical setting </h1>

The full game consists of <i> agents</i>, each possessing <i>assets</i>, a <i>utility function</i>, and <i>time</i>. There also exist <i> marketplaces </i> where agents can trade assets.  Each actor can at every step take one of several <i>actions</i>, determined by the current state and the specifics of the game at hand.

In this brief explanation of the full game, every word in italics corresponds to a class in the implementation of the game. Also, the words actor & agent mean the same thing. Due to the complexity of the full game, many experiments are run on reduced variants of it.

<h3> Agents </h3>
Every agent possesses a certain quantity of assets, a utility function, and time. Time can be considered a special asset, it reduces every timestep until it reaches zero, then the agent dies. The goal for every agent is to find a policy that maximizes their own specific utility function. Some actors are 'dummys' and always act according to a specific policy (ex. randomly), without learning.

<h3>Assets</h3>
An typical asset has a global <i>stock</i> corresponding to the amount existing, a global <i>supply</i> corresponding to how much more of the asset is created (or destroyed) every time-step. The supply can be dependent on the actions of the actors.

Some special assets are 'knowledge', giving.

In general, there are defined relations between assets, 
Also there are graph relations between them -> relation

<h3>Relations</h3>
A relation defines how assets can be combined. This in turn is a determinant of the state transition function. For example, a relation can...

<h3>Policies</h3>
Every agent has a policy which determines what actions it will take given a history of observations and . Every agent is considered rational - meaning that it will always try to maximize its own utility function in the long run.

<h3>Utilities</h3>
Agents have utilities 
The utilities are assumed to satisfy
U(alternative 1)
This leads naturally to an individual reward function 

<h3>Marketplaces</h3>
In the full game the agents have 
In some experiments they can barter (trade one asset for any other), in others theycan via a special'money', and in some they can also trade labor.

The reduced game where all the utilities are the same and

<h1> Theoretical background </h1>
<h2>MDP</h2>
The MDP (Markov decision process) is a general model of a process that develops over time based on input. It is central in control theory, game theory and reinforcement learning, amongst others. In an MDP, there is a single agent acting by selecting actions a in an environment manifested by the state s. The state updates after every time-step based on the previous state and action, after which the agent receives a reward. In general, the dynamics of a MDP are probabilistic and defined by the following equations:
<br>

<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$

<h5>Reward:</h5>

$r(s_{t+1}, s_{t})$

<h5>Policy: </h5>

$p(a_{t}|s_{t}) = \pi(s_{t})$
<br><br>

The specific usage of an MDP depends on the specifics of these equations. For instance, in control theory the reward is often defined as the difference between a target value and a measured value, and is almost always non-zero. The state transition function is typically not known exactly, but a close physical model can often be approximated. In some games the rewards are only given at the end, based on win or loss (for instance in chess). 

The duration of an MDP can be both fixed-length or infinite-length. 

Another example of how an MDP is used is when the reward function & dynamics are fully known. In that case, the goal of finding the policy that maximizes reward is equivalent to the problem of search. 

In reinforcement learning, the state & reward dynamics are assumed to be fully unknown and to be inferred from continus experiment. This gives rise to a trade-off between exploration & exploitation. This will in general be of high importance in analyzing the TRADING-GAME. In general, the goal of reinforcement learning is to find a policy that maximized the expected cumulative discounted reward - meaning that it seeks to find 

$max_{\pi \in \Pi} \mathbf{E}_{s_{i}, a_{i} \forall i}\sum_{t=0}^{t=\infty}r(s_{t+1}, s_{t})\gamma^{t}$

where expectations are taken over the given

<h2>POMDP</h2>
Partially observable MDP - identical to an MDP exept that the agent only has access to an observation of the state. This observation is not necessarily the full state of the environment, and could be a partial observation or even a function of the state.
<br>
<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$,

<h5>Reward: </h5>

$r(s_{t+1}, s_{t})$

<h5>Observation function: </h5>

$p(o_{t}|s_{t}) = \omega(s_{t})$

<h5>Policy: </h5>

$p(a_{t}|o_{t}) = \pi(o_{t})$
<br>

<h2>DPOMPD</h2>
In a decentralized POMDP the POMDP is generalized in that there is a multitude of agents, each taking a separate decision based on their own observations. In an analogous way there is a DMDP (where all agents have full observation of the state). The state is updated on the joint decisions made by all actors, and the reward is 
<br>

<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a^{0}_{t},...,a^{n}_{t})$

<h5>Reward: </h5>

$r^{i}(s_{t+1}, s_{t})$

<h5>Observation function: </h5>

$p(o_{t}|s_{t}) = \omega(s_{t})$

<h5>Policy: </h5>

$p(a_{t}|o_{t}) = \pi(o_{t})$
<br><br>


<h2> TRADING-GAME </h2>
The natural extension to the DPOMDP is the setting where all agents have different rewards functions. This setting is called a POSG - a partially observable stochastic game.  

TRADING GAME is a special kind of POSG - where actors attempt 
The state transition depends


Goal of MDP, ... is to maximize reward. All such processes also have in common that 
<h1> Metrics </h1>
One difference between for instance reinforcement learning & the trading game is that TG has no clear global metric on which to measure success. We make use of several different tricks to follow up on what's happening .

<h1> Experiments / Example games </h1>

Zero-sum trading.
In this game all the assets have fixed 

Subcategory: Fish catching

Emergency of marketplaces
Investigate how marketplaces of barter -> marketplace of money. Especially 
Marketplace of 'weak' money -> marketplace of hard money

Healthy economy scenario?

Fiat blackhole scenario?

Economy with some asymptotic actors (only utility of money is interesting) and some 'normal actors' (which would like different assets all the time)

Final disclaimer & outro (essentially a model of capitalism, what happens with )