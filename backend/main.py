from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from models import PipelineData
from pipeline import is_graph_dag

app = FastAPI()

# adding cross origins to allow request from our frontend server
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

# adding cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# endpoints
@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(pipeline: PipelineData):
    nodes = pipeline.nodes
    edges = pipeline.edges
    
    num_nodes = len(nodes)
    num_edges = len(edges)
    
    is_dag = is_graph_dag(edges)
    
    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag}

