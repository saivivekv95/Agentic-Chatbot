from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder = StateGraph(State)
        
        
    def basic_chatbot_build_graph(self):
        
        self.basic_chatbot_node =BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
    
    def chatbot_with_tools_build_graph(self):
        """
        :param self: Builda advanced chatbot graph with tool integration.
        """
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)
        
        ### Define he LLM
        llm=self.llm
        ##Define the chatbot node
        
        
        ## Add the nodes
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_node("tools",tool_node)
        ## Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
        
        
    def setup_graph(self,usecase:str):
        if usecase == 'Basic Chatbot':
            self.basic_chatbot_build_graph()
        if usecase == 'Chatbot with Web':
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()