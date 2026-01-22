from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    def __init__(self,model):
        self.llm=model
        
        def process(self,state:State)->dict:
            user_input = state["messages"][-1] if state["messages"] else ""
            llm_response = self.llm.invoke/[{"role":"user","content":user_input}]
            
            ## Stimulate tool-specific logic
            tools_response=f"Tools integration for: '{user_input}'"
            
            return {"messages": [llm_response,tools_response]}
        
        def 