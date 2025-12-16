from langgraph.graph import StateGraph,END,START
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_core.messages import HumanMessage,BaseMessage,ToolMessage,SystemMessage
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Sequence
import os,sys,json
from operator import add as addMessage

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import *

load_dotenv()

Groq_api_key=os.getenv("GROQ_API_KEY")
# model initialization
llm=ChatGroq(model_name="llama-3.1-8b-instant",temperature=0,api_key=Groq_api_key)
# embedding of the huggingface
embeddingtask=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
# vector database creation
vectorstore=Chroma(
    embedding_function=embeddingtask,
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION_NAME
)



# ===retrivate of the data from the documant===

retrivervector=vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={'k': 3}
)

#==tool retirver==
@tool
def retriever_tool(query:str)->str:
    """ Retriver tool for retriving the csv data from the retriver"""
    docs=retrivervector.invoke(query)
    if not docs:
        print("No relavent infromation is found")
    result=[]
    for i,doc in enumerate(docs):
        result.append(f"document {i+1}:\n {doc.page_content[:800]}")
    return "\n\n".join(result)
    
    
tools=[retriever_tool]



tool_dict={t.name: t for t in tools}

# creating the state
class Agent_state(TypedDict):
    messages:Annotated[Sequence[BaseMessage],addMessage]
system_prompt = """
You are a climate information assistant.

Answer ONLY in the following format:
display the user aksed climate loacation and the deatils follows:
Temperature:
Humidity:
Rainfall:
and also the changes from it from previous to now like increase or decrease of it
Do not add anything else.
"""


def Agent_rag(state:Agent_state):
    message_data=list(state["messages"])
    system_prompt=SystemMessage(content=system_prompt)
    fullMessage=[system_prompt]+message_data
    response=llm.invoke(fullMessage)
    return {"messages":[response]}
# dising node of the graph
def disiding(state:Agent_state):
    message=state["messages"][-1]
    if getattr(message,"tool_calls",None):
        return "continue"
    return "exit"

def tool_action(state:Agent_state):
  """tool_action tool """
  ai_message=state["messages"][-1]
  tool_calls=ai_message.tool_calls
  tool_messages=[]
  for t in tool_calls:
      tool_name=t['name']
      tool_args=t['args']
      tool_id=t.get("id",t.get("tool_call_id"))
      query= tool_args.get("query", "")
      
      print(f"\nExecuting tool '{tool_name}' with query: {query}")
      
      if tool_name not in tool_dict:
          tool_output="Invalid tool name."
      else:
          tool_output= tool_dict[tool_name].invoke(query)
      
      tool_messages.append(
          ToolMessage(
              tool_calls_id=tool_id,
              name=tool_name,
              content=str(tool_output)       )
      )
  return {"messages":tool_messages}

graph=StateGraph(Agent_state)
graph.add_node("agent_rag",Agent_rag)
graph.add_node("tool_action",tool_action)
graph.add_edge(START,"agent_rag")
graph.add_edge("tool_action","agent_rag")
graph.add_conditional_edges(
    "agent_rag",
    disiding,{

        "continue":"tool_action",
        "exit":END
    }
)
app=graph.compile()

for line in sys.stdin:
    data=json.loads(line)
    userinput=data["input"]
    try:
        result=app.invoke({"messages":[HumanMessage(content=userinput)]})
        print(json.dumps({"output":result["messages"][-1].content}),flush=True)
    except  Exception as e:
        print(json.dumps({"error":str(e)}))


