import os
import sys
import yaml
from agents import AgentFactory
from assets import AssetFactory

def log(message):
    print(message)
    return

class Experiment:
    def __init__(self, conf):
        log('Initiating experiment...')
        self.conf = conf
        self.parse_conf()
    
    def parse_conf(self):
        self.parse_name()
        self.parse_assets()
        self.parse_agents()
        self.parse_marketplaces()

    def parse_name(self):
        self.name = self.conf['name']

    def parse_assets(self):
        assets = []
        entries = [a.split(' ') for a in self.conf['assets']]
        for entry in entries:
            n_assets, type_asset = entry
            assets.extend([AssetFactory[type_asset] for i in range(int(n_assets))])
        self.assets = assets

    def parse_agents(self):
        agents = []
        entries = [a.split(' ') for a in self.conf['agents']]
        for entry in entries:
            n_agents, type_agent = entry
            agents.extend([AgentFactory[type_agent] for i in range(int(n_agents))])
        self.agents = agents

    def log_status_message(self):
        log(f'Experiment name: {self.name}')
        log(f'Number of assets: {len(self.assets)}')
        log(f'Number of agents: {len(self.agents)}')
        log(f'Number of marketplaces: {len(self.marketplaces)}')

def main():
    with open('./experiments/conf.yaml', 'r') as file:
        conf = yaml.safe_load(file)

    experiment = Experiment(conf['experiment'])
    experiment.log_status_message()


if __name__=='__main__':
    main()