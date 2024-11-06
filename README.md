### A* Pathfinding App

This is a simple pathfinding application that visualizes the A* algorithm in action. You can interact with the grid by selecting start, end, and barrier points, and then find the shortest path between the start and end points, with the option to use diagonal movements.
Features

    Interactive Grid: Draw barriers and set start and end points on a grid.
    Find Path: Use the A* algorithm to calculate the shortest path.
    Clear Grid: Reset the grid to the default state.

Requirements

    Node.js (version 14 or later)
    Vite (for fast development and bundling)
    FastAPI (for the backend)

Setup Instructions
1. Clone the repositories

Clone both the frontend and backend repositories. The backend repository should contain the FastAPI code.

# Clone the frontend (Vite) app
```bash
git clone https://github.com/rdouda/astar-app.git
```
# Clone the backend (FastAPI) app in another directory
```bash
git clone https://github.com/rdouda/astar-api.git
```
2. Set up the FastAPI backend

Go to the `astar-api` directory and install the required dependencies.

Linux
```bash
cd astar-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Windows
```bash
cd astar-api
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

To run the FastAPI server, use the following command:

```bash
fastapi run --port 8088
```

This will start the FastAPI backend on http://localhost:8088.

3. Set up the Vite frontend

Go back to the astar-app directory and install the required dependencies for the frontend:

```bash
cd ../astar-app
npm install
```
4. Create a `.env` file for the frontend

Create a `.env` file in the root of the astar-app project directory and add the following configuration to specify the API URL.
```bash
VITE_API_URL=http://localhost:8088
```
Make sure to replace http://localhost:8088 with the actual URL of your backend API if it's hosted elsewhere.

5. Run the development server for the frontend

Now that the backend is running, you can start the Vite frontend development server:

```bash
npm run dev
```

This will start the Vite app on http://localhost:5173 (by default). You can now open this URL in your browser to interact with the app.
