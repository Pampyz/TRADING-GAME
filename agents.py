class Agent:
    def __init__(self, policy):
        pass

class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

AgentFactory = {
    'random': RandomAgent
}