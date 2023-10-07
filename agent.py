# coding=utf-8
import torch

"""
using LLM model to play card game like poker, go, mahjong, etc.
"""

class LLMAgent:
    def __init__(self, model):
        self.model = model
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
