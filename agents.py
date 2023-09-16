import numpy as np

class Agent:
    def __init__(self):
        pass

class RandomAgent(Agent):
    def __init__(self):
        super().__init__()
    
    def act(self, observation, actions):
        return np.random.choice()

class LinearAgent(Agent):
    def __init__(self):
        super().__init__()
        #self.linear vector

    def act(self, observation, actions):
        return np.random.choice()

class QAgent(Agent):
    def __init__(self, config):
        super().__init__()
        self.parse_config(config)
    
    def parse_config(self):
        pass

AgentFactory = {
    'random': RandomAgent
}