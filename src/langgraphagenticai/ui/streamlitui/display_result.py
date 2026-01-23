import streamlit as st
import json
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage


class DisplayResultsStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message
        
    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        if usecase == "Basic Chatbot":
            for e in graph.stream({'messages':("user",user_message)}):
                print(e.values())
                for value in e.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
        
        elif usecase=="Chatbot with Web":
             # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)