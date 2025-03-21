from src.langgraph_agenticai.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot implementation
    
    """
    
    def __init__(self, model):
        self.llm = model
        
    def process(self, state: State) -> dict:
        """
        Process the input state and generates a chatbot response
        """
        
        return{"messages": self.llm.invoke(state["messages"])}