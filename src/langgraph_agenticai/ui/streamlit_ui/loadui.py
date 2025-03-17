import streamlit as st
import os
from datetime import date


from langchain_core.messages import AIMessage, HumanMessage
from src.langgraph_agenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() # config
        self.user_controls = {}