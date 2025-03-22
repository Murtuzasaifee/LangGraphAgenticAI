from src.langgraph_agenticai.state.state import State
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_openai_tools_agent, AgentExecutor

class ChatbotAINewsNode:
    
    def __init__(self, model):
        self.llm = model
        
        
    def create_ai_new_chatbot(self, tools):
        
       # AI expert system prompt
        system_prompt = """You are a professional AI news analyst with expertise in:
        - Breaking technology news
        - Emerging AI research trends
        - Industry developments in artificial intelligence
        - Analysis of AI ethics and policy

        Guidelines:
        1. Provide up-to-date, accurate information
        2. Always verify facts using Tavily search
        3. Include relevant sources from search results
        4. Explain technical terms when needed
        5. Maintain neutral, objective tone
        6. Provide a summary of key points and future trends
        
        Provide only information about the AI News and Trends. For other queries, please respond with the reson that you are only the AI News Expert.
        """


        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke([system_prompt] + state["messages"])]}
        
        return chatbot_node