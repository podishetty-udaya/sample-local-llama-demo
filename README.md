<h2> # Kubernetes YAML Generator with Ollama </h2>

Generate Kubernetes Deployment and Service YAML for a Python Flask app using **Ollama**, a local LLM that runs on your machine. Perfect for DevOps engineers who want fast, private, and cost-effective AI automation.

---

<h2> ## 🚀 Features </h2>

- Generate **Deployment** and **Service** YAML for Flask apps.
- Supports:
  - Replicas
  - Container ports
  - Resource requests & limits
  - Liveness & readiness probes
  - Labels
  - ClusterIP Service
- **Fully offline**: No cloud or internet required.
- **Secure**: All data stays local.
- **Easy integration**: Can be used in Python scripts, CI/CD pipelines, or automation tools.

---

<h2> 🖥️ Getting Started on Windows </h2>

1.	Download the Installer: Get the latest .exe from the official site: https://ollama.com/download
2.	Run the Installer: Follow the setup wizard to complete the installation.
3.	Open a terminal: Launch Command Prompt or PowerShell.
4.	Verify installation:
ollama --version
5.	Download a model: Pull a model to get started. For general use, a smaller model like Llama  2 .






<h2>📝 Demo Execution</h2>

<div style="border:2px solid #4CAF50; padding:10px; border-radius:8px; background-color:#f0fff0;">
<h2>🚀 Run Locally</h2>

1️⃣ **Create Virtual Environment**  
<pre>
python3 -m venv venv
source venv/bin/activate   # On Linux/MacOS
# or
.\venv\Scripts\activate    # On Windows
</pre>

2️⃣ **Install Dependencies**  
<pre>
pip3 install -r requirements.txt
</pre>

3️⃣ **Run the Application**  
<pre>
python3 generate_dockerfile.py
</pre>

The script will generate a Dockerfile for your project and print it to the console.
</div>


<div style="border:2px solid #2196F3; padding:10px; border-radius:8px; background-color:#e8f4ff;">
<h2>🛠️ How It Functions</h2>

1️⃣ Sends a prompt to the Ollama Llama3 model specifying your desired Kubernetes configuration.  
2️⃣ Receives valid Kubernetes YAML in response.  
3️⃣ Prints the YAML to the terminal or allows saving it to a file.
</div>

<div style="border:2px solid #FF9800; padding:10px; border-radius:8px; background-color:#fff8e1;">

