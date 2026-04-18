from mesa import Agent
import numpy as np

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = agent_type
        ## Get the preference range dependong on which group the agent belongs to
        ## Sample from a uniform distribution in this range to assign the agent
        ## their individual preference
        preferences = self.model.preferences[agent_type]
        self.desired_share_alike = self.truncated_normal(
            preferences["mu"],
            preferences["sigma"],
            preferences["min"],
            preferences["max"]
        )

    ## Helper function to find the normal distribution through rejection sampling
    ## to ensure the values are within the range.
    ## Reference: https://relguzman.blogspot.com/2018/04/rejection-sampling-explained.html
    def truncated_normal(self, mu, sigma, min, max):
        while True:
            val = np.random.normal(mu, sigma)
            if min <= val <= max:
                return val


    ## Define basic decision rule
    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore = True, radius = self.model.radius, include_center = False)
        ## Count neighbors of same type as self
        similar_neighbors = len([n for n in neighbors if n.type == self.type])
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if (valid_neighbors := len(neighbors)) > 0:
            share_alike = similar_neighbors / valid_neighbors
        else:
            share_alike = 0
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        ## Desired share is now an attribute of the individual agent rather than a global model parameter
        ## Note that the desired_share_alike is now an attribute of each agent rather than a global param
        if share_alike < self.desired_share_alike:
            self.model.grid.move_to_empty(self)
        else: 
            self.model.happy +=1   
