# TRADING-GAME
The TRADING-GAME investigates different questions posed in the context of a special multiplayer game. The game can be described as the "game of economics', where actors try to improve their own standing in an economic environment. The game is modelled on an austrian interpretation of value & economics, where every actor is assumed to possess their own specific valuation of assets. This valuation is considered subjective and not comparable between actors.

We also attempt to use this framework to model economic time-series using certain emergent features of the inter-agent communication which is enabled in the game. Another way of formulating this is that we are using this framework as an inductive bias on the underlying structure of the time-series. Specifically, we attempt to model exchange rates of different kinds as the result of a multi-player process where each player acts on a market in a way that attempts to maximize their own utilities. This model is then trained end-to-end.

Multi-player games of different kinds are generally characterized by imperfect information (meaning that no single player has access to all knowledge) and hence leads to the importance of various forms of communication. Furthermore, in this case all players have a different utility - making communication in various ways important not just to probe the state, but also the utilities of other agents in order to make good decisions.

<h1> Practical setting </h1>

The full game consists of <i> agents</i>, each possessing <i>assets</i> and a <i>utility function</i>. There also exist <i> marketplaces </i> where agents can trade assets.  Each actor can at every step take one of several <i>actions</i>, determined by the current state and the specifics of the game at hand. Between the assets there exist <i>relations</i>, signifying how they can be converted into each other.

In this brief explanation of the full game, every word in italics corresponds to a class in the implementation of the game. Also, the words actor & agent mean the same thing. Due to the complexity of the full game, many experiments are run on reduced variants of it.

<h3> Agents </h3>
Every agent possesses a certain quantity of assets and a utility function. The utility function evaluates how satisfied the agent is with its assets. Time can be considered a special asset, it reduces every timestep until it reaches zero, then the agent dies. Some actors are 'dummys' and always act according to a specific policy (ex. randomly), without learning. Most agents however, are driven to change and improve their policy to act in a way that maximizes their own specific utility function.

<h3>Assets</h3>
An typical asset has a global stock corresponding to the amount existing, and a global supply corresponding to how much more of the asset is created (or destroyed) every time-step. In general, this stock & supply is not something which is pre-defined, but is defined via the potential actions & relations that are available to the actors. Only in simplified versions of the game are they fixed. The types of assets are varied and in general exist in a few classes of particular significance.

<h5>Time </h5>
A very important asset is 'time' - given to each agent at the start of their entry in the game. It usually starts at a fixed value and decreases with some amount every time-step. When it reaches zero the agent typically "dies" and leaves the game. 

<h5>Consumption assets </h5>
Another common asset class can be described as the class of consumption assets. These typically decay every time-step, but do not lead to agent death when the agent possesses a zero quantity of them.

<h5>Capital assets</h5> An important special class of assets can be called capital, giving the possibility to combine assets to produce new ones. This capital can be in the form of knowledge or 'tangible' assets. The difference is that tangible assets can be traded on a marketplace while knowledge assets has to be 'taught'. In the trading of a tangible asset, the one selling it loses the asset, whereas a knowledge asset is not consumed during the teaching. Knowledge & capital assets typically lack utility of their own (although they possess market value), however they inherit this from the potential of their usage. The exact way in which consumptions assets can be combined in order to create new ones, either together with or without capital assets, are determined by the relations on them.

<h5>Investment assets </h5>
Other assets include investment assets that very rarely are consumed. A special such asset is called 'money'. They typically have little to no utility except as a medium of exchange.

<h5>Financial assets</h5>
The assets in the class of 'economic contracts' can also be formed, including loans, promises of labor (employment), options & other derivatives. 

<h5>Other assets</h5>
There are many other types of assets conceivable. One special class of capital assets are weapons, possessing special relations that does not only affect the assets of the actor possessing it, but also other actors. However, the focus of this investigation is not to attempt to model the entire world, rather just the particular setting where agents trade. In order to do this it is to a certain extent necessary to introduce a context where the agents can independently act in a simulated world (as manifested in the assets, relations between them, and actions that can be taken). What is special in general about a trade is that although both parties have their own  
<br>

In general, it's important to note that assets have no value except for that which is defined by the utilities of every agent. This is the main evaluation of success that every agent uses, and it's important to separate this from other emergent & implicit notions of value. The relations define an implicit 'valuation' of every asset for instance in terms of the amount of time it would require to produce it. Also, the marketplaces define another evaluation of assets in terms of the market price of them (which introduces a 'global & virtual' evaluation of all assets).

<h3>Relations</h3>
A relation defines how assets can be combined. For instance there might be an asset which can be made by combining five units of wood with ten units of time (a table). Assume there to be n assets and the quantity of each asset determined by a tuple where the amount at index i is equal to the amount in possession. In that case, a relation can be written as 

$ R: (s_{r_{1}}, s_{r_{2}}, ..., s_{r_{n}}) \to (a_{r_{1}}, a_{r_{2}}, ..., a_{r_{n}}) $ 

where the left hand side contains the quantities to be subtracted by the relation and the right hand side the quantities to be added. The set of assets and relations between them defines a graph - which can be loosely be interpreted as the part of the state transition which pertains to the 'natural world'. The other part is the one dependent on the trades made between the agents on the available marketplaces. What is also special about relations is that they are not always fully known - a part of the activities of any agent can be to 

Implicitly define all assets via relations?

<h3>Policies</h3>
Every agent has a policy which determines what actions it will take given a history of observations and actions. Every agent is considered rational - meaning that it will always try to maximize its own utility function in the long run. Several types of 'stupid' policies are considered, for instance the random actor and the non-trading actor (will never trade). These are mainly used for reference, 

<h3>Utilities</h3>
Difficult. 
Agents have utilities 
The utilities are assumed to satisfy
U(alternative 1)
This leads naturally to an individual reward function 

Utility of a relation: U(..., )

<h3>Marketplaces</h3>
In the full game the agents have access to a range of marketplaces. In each marketplace they are
In some experiments they can barter (trade one asset for any other), in others theycan via a special'money', and in some they can also trade labor.

The marketplace typically defines things such as net-worth, virtual opportunity, etc... -> the basis of inter-agent complexity in this game.

The reduced game where all the utilities are the same and

<h1> Theoretical background </h1>
<h2>MDP</h2>
The MDP (Markov decision process) is a general model of a process that develops over time based on input. It is central in control theory, game theory, time series analysis and reinforcement learning, amongst other fields. In an MDP, there is a single agent acting by selecting actions a in an environment manifested by the state s. The state updates after every time-step based on the previous state and action, after which the agent receives a reward. This reward is dependent only on the state and not the eventual path taken.In general, the dynamics of a MDP are probabilistic and defined by the following equations:
<br>

<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$

<h5>Reward:</h5>

$r(s_{t})$

<h5>Policy: </h5>

$p(a_{t}|s_{t}) = \pi(s_{t})$
<br><br>

How an MDP is used in practice depends on the specifics of these equations. For instance, in control theory the reward is often defined dependent on the difference between a target value and a measured value, meaning that it is almost always non-zero. The state transition function is typically not known exactly, but a close physical model can often be approximated. The goal in this setting is to find a policy which keeps the target value as close to the measured value as possible. This means that the reward is often negative.

In some games the rewards are only given at the end, based on win or loss, for instance in chess. In this case case, the policy needs to take into consideration that the time between an action and its positive or negative consequence might be large.

Another example of how an MDP is used is when the reward function & dynamics are fully known. In that case, the goal of finding the policy that maximizes reward is equivalent to the problem of search. 

In reinforcement learning, the state & reward dynamics are assumed to be fully unknown and to be inferred from continus experiment. This gives rise to a trade-off between exploration & exploitation. This will in general be of high importance in analyzing the TRADING-GAME. In general, the goal of reinforcement learning is to find a policy that maximized the expected cumulative discounted reward - meaning that it seeks to find 

$max_{\pi \in \Pi} \mathbf{E}_{s_{i}, a_{i} \forall i}\sum_{t=0}^{t=\infty}r(s_{t+1}, s_{t})\gamma^{t}$

over some space of potential policies $\Pi$, where expectations are taken over the distributions of the random variables $s_{t}$, $a_{t}$.

Lastly, it's important to note that the duration of an MDP can be both fixed-length or infinite-length. We will mainly be considering finite-length scenarios, however, in some cases these will be considered to start <i> in medias res </i> in the context of an infinite-length game.


<h2>POMDP</h2>
A partially observable MDP is identical to an MDP exept that the agent only has access to an observation of the state. This observation is not necessarily the full state of the environment, and could be a partial observation or an arbitrary function of the state. The extension is straightforward and given below:
<br>
<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a_{t})$,

<h5>Reward: </h5>

$r(s_{t})$

<h5>Observation function: </h5>

$p(o_{t}|s_{t}) = \omega(s_{t})$

<h5>Policy: </h5>

$p(a_{t}|o_{t}) = \pi(o_{t})$
<br>

<h2>DPOMPD</h2>
In a decentralized POMDP the POMDP is generalized in that there is a multitude of agents, each taking a separate decision based on their own observations. In an analogous way there is a decentralized MDP (where all agents have full observation of the state). The state is updated on the joint decisions made by all actors, and the reward is also joint. This means that this is a cooperative model, suitable for swarm behaviour & distributed computation. With n actors, the corresponding definitions follow:
<br>

<h5>State transition function:</h5>

$p(s_{t+1}|s_{t}, a^{0}_{t},...,a^{n}_{t})$

<h5>Reward: </h5>

$r(s_{t})$

<h5>Observation functions: </h5>

$p(o^{i}_{t}|s_{t}) = \omega^{i}(s_{t})$

<h5>Policies:</h5>

$p(a^{i}_{t}|o^{i}_{t}) = \pi^{i}(o_{t})$

where superscript i means "pertaining to agent i".

<h2> TRADING-GAME </h2>
The natural extension to the DPOMDP is the setting where all agents have different rewards functions. This setting is called a POSG - a partially observable stochastic game. The different rewards mean that the agents can now work against & together with each other, meaning that a POSG represents a model of a general multi-player game.

TRADING GAME is a special kind of POSG - where state dynamics, policies and rewards are motivated on the 'practical' discussions above. The specific setting enables a market order which brins a venu for cooperative actions. There is a need to communicate abilities &. However, it is also interesting to note what hostile activities it can also enable - ...

The TRADING-GAME setting differs from ordinary reinforcement learning in a few ways. The goal of an ordinary MDP is typically to maximize the reward for a single actor. This is a global measure of success for the entire process. However, in the trading game, there is no such global measure. Each actor tries to maximize their own utility, but these are assumed not to be comparable between agents.

Nash equilibria

The trading game is also specific in that the game is assumes to possess a 'natural' reward function, being derived from a utility function defined on the possession of a collection of assets.

The trading game is immensely complex and can be varied in many ways. The sources of complexity is mainly the number & complexity (in terms of the policies) of the agents, the complexity of their utilities, and the complexity & number of relations and assets. As mentioned before, the game can be extended with violent assets, financial assets, new channels for communication extending beyond marketplaces, etc.

<h1> Metrics & visualization</h1>
Coming soon!

<h1> Experiments / Example games </h1>

Zero-sum trading. In this game all the assets are fixed and there exist no relations. Only trading can be used. 
<br>
Infinite v.s. finite lifetimes.
<br>
Barter marketplace v.s. money marketplace

Subcategory - Fish catching
<br>
Subcategory - Emergent modelling


Emergence of marketplaces
<br>
Investigate how marketplaces of barter leads to marketplace of money. 
Investigate how marketplace of 'weak' money leads to marketplace of hard money
<br>
Healthy economy scenario?

Other ideas:
Fiat blackhole scenario? (privileged actors)
<br>
Violence & assets with inter-actor relations?
<br>
Economy with some asymptotic actors (only utility of money is interesting) and some 'normal actors' (which would like different assets all the time)

Final disclaimer & outro (essentially a model of capitalism, what happens with life & children etc, note that utility is social and depends on communication, wealth accumulates & is finite etc.) Real life is infinite-horizon, inheritance, etc. Also relations are dependent on other actors - making no decisions truly independent. 