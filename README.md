# VectorShift - Kartik

The assessment is divided into four parts:

## Part-1: Frontend
For this part, I have created an abstraction for the nodes **BaseNode** through which we can simplify the process of new node creation. It takes in basic information about the nodes that is common to all the nodes, like **id**, **data**, **type**, **handles**, and *
*info** and builds the node using this info and appending the **children** elements that are wrapped inside the BaseNode component in the child component.

## Part-2: Design/Styling
For this part I have used **TailwindCSS** because it provides easy way to style the HTML elements using simple inline styling rather than having to manage multiple CSS files.

## Part-3: Text Node Logic
1. For implementing the dynamic height/width of the text node, I simply used a **textarea** element with an **onChange** event listener which calls the adjustHeight() function that simply scrolls though the current height and increases the height of the textarea as the user goes to every next line.
2. For allowing the users to define **variables** in the test using simple {{}} expression structure, I used **regex** to extract all the variable names from the text and simple state management to append the new variables to a list, and every time this list gets updated, we simultaneously update the UI with variable name and it's corresponding handle.

## Part-4: Backend Integration
The **Deploy** button is being used to send the node and edge data to our FastAPI server where we have our backend code to identify if the given nodes and edges form a Directed Acyclic Graph or not. The function **is_graph_dag()** uses simple algorithm based on Kahn's Algorithm of topological sorting to identify if the given graph is DAG or not.

The response object {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag} is sent back to the frontend where we generate an alert to display this response on out UI.

## Installation

Make sure to install all the dependencies of the frontend and backend directories before running both the servers.

Simply go to the frontend directory and run:

```bash
npm install
```

## Usage

Start the frontend react server:
```bash
npm start
```

Start the backend server:
```bash
uvicorn main:app --reload
```

Now you can visit the project on http://localhost:3000/.

Happy Coding.✌🏼✌🏼