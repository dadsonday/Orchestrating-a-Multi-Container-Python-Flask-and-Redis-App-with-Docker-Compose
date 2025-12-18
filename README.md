# Orchestrating-a-Multi-Container-Python-Flask-and-Redis-App-with-Docker-Compose
In modern DevOps, managing multiple interconnected services is a fundamental skill. In this project, I built a scalable web application using Python Flask and Redis, orchestrated entirely through Docker Compose.

<img width="800" height="533" alt="image" src="https://github.com/user-attachments/assets/25b7deb1-8c7e-43b5-9b5f-f2afb070a9f2" />

🛠️ Step 1: Initializing the Environment
I began by setting up the project directory and authenticating with Docker Hub.
docker login
mkdir -p redis-docker-project/{app,docker-compose.yml}

<img width="732" height="268" alt="image" src="https://github.com/user-attachments/assets/d3f40885-b916-454d-870a-98570be67955" />

⚠️ The "Directory vs. File" Gotcha
If you look closely at the command above, using {app,docker-compose.yml} inside mkdir actually created docker-compose.yml as a directory. I noticed this when trying to edit it later.
To fix this, I had to:
Identify that it was a directory when the rm command failed.
Use the recursive remove command: rm -r docker-compose.yml.
Later, properly touch the file or create it via an editor.

<img width="769" height="172" alt="image" src="https://github.com/user-attachments/assets/61b79191-6052-4054-9e65-66986e95e7bd" />
<img width="600" height="160" alt="image" src="https://github.com/user-attachments/assets/7f166bb0-5182-4cb9-bef9-6fc7b2187906" />

📂 Step 2: Project Structure & File Creation
A clean project structure is vital for Docker orchestration. I organized the application logic inside an app/ folder, with the orchestration file at the root.
<img width="389" height="177" alt="image" src="https://github.com/user-attachments/assets/f68d24b9-0066-4375-a01e-29a19cca5271" />

I navigated into the app directory to initialize the core component files:
app.py
requirement.txt
Dockerfile

<img width="800" height="370" alt="image" src="https://github.com/user-attachments/assets/e8ebec86-beb9-4ac2-835d-c8ceff64a5d5" />

💻 Step 3: Developing the Application Logic
Using the vi editor, I populated the files with the necessary code and dependencies.
The Flask Application (app.py)
The application connects to Redis via a host defined in our environment variables. Every time the root page is refreshed, it increments a counter in the Redis datastore.
/////////////////////////////////////////////////////////////////////////////
from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("visits")
    return f"Hello! This page has been visited {count} times. Like and follow CloudDaemon"
////////////////////////////////////////////////////////////////////////////
    
<img width="800" height="595" alt="image" src="https://github.com/user-attachments/assets/fc96d139-9346-49f1-b752-dcd670248983" />

Dependencies (requirement.txt)
I listed the lightweight requirements needed: flask and redis.

<img width="669" height="697" alt="image" src="https://github.com/user-attachments/assets/a7e956f3-d2dc-48ee-acb1-b0876c045244" />


🐋 Step 4: Dockerization & Orchestration
With the code ready, I defined how the containers should be built and how they should interact.
The Dockerfile
The Dockerfile uses python:3.11-slim as a base. It sets the working directory, installs dependencies, and exposes port 5000.
<img width="535" height="689" alt="image" src="https://github.com/user-attachments/assets/2cc483fd-8cf4-4bbd-9f9c-c029b35d4117" />

The Docker Compose File
The docker-compose.yml file acts as the orchestrator. It defines:
web service: Builds from the /app directory and maps port 5000.
redis service: Pulls the official Redis 7 image.
networking: Sets REDIS_HOST=redis so the containers can talk to each other.

<img width="569" height="708" alt="image" src="https://github.com/user-attachments/assets/93816931-ab8c-47ac-83bf-d981fe3c384c" />

🚀 Step 5: Deployment & Verification
To bring the entire stack to life, I ran the build and up command from the project root:
docker-compose up --build

<img width="800" height="373" alt="image" src="https://github.com/user-attachments/assets/a40834bd-ddb8-48cf-bb6e-b67078ac9ce3" />

Validating the Containers
I used docker ps to verify that both the web service and the Redis datastore were active and mapped to their respective ports.

<img width="800" height="318" alt="image" src="https://github.com/user-attachments/assets/85402816-4fb8-4e74-96b7-f60c04deb1ad" />


Testing the Web Service
Navigating to 127.0.0.1:5000 confirmed the application was working and communicating with Redis.

<img width="800" height="395" alt="image" src="https://github.com/user-attachments/assets/5b3192a2-15f1-45b8-bb1f-b508d3e9f434" />

Inspecting the Redis Datastore
Finally, I accessed the running Redis container using docker exec to verify the data persisted. Running GET visits via the redis-cli confirmed the visit count.
<img width="800" height="414" alt="image" src="https://github.com/user-attachments/assets/7b4baf79-571f-41cf-ba90-362a0bbe6217" />

🏁 Conclusion
By leveraging Docker Compose, we've created a reproducible, isolated environment where a Python backend and a Redis database work in perfect sync. This setup handles the complexities of networking and dependency management, allowing us to focus on the code.
Would you like me to help you write a "Cleanup" section explaining how to stop and remove these containers and networks safely?
Do subscribe to my Youtube channel, i'll be posting a video on this project soon: https://www.youtube.com/@Cloud_Daemon
Happy Learning!

