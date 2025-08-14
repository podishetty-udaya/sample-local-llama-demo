import ollama

# Prompt for the Dockerfile
PROMPT = """
Generate a complete Kubernetes Deployment and Service YAML for a Python Flask app.

Requirements:
- Deployment name: flask-app
- Image: myapp:latest
- Replicas: 3
- Container port: 5000
- Include resource requests & limits (modest values)
- Add liveness & readiness HTTP probes on /health at port 5000
- Add basic labels for app and tier=backend
- Include a ClusterIP Service named flask-app-svc exposing port 80 -> targetPort 5000
- Output ONLY valid YAML (multi-document if needed), with no explanations.
"""

def generate_dockerfile() -> str:
    """
    Generates a Dockerfile for a Java application using Ollama's LLM.
    """
    # Call the Ollama chat model

    response = ollama.chat(
        model='llama2:7b',
        messages=[{'role': 'user', 'content': PROMPT}]
    )
    
    # Safely extract the assistant's message content
    dockerfile_content = response.get('message', {}).get('content', '')
    return dockerfile_content

if __name__ == '__main__':
    dockerfile = generate_dockerfile()
    print("\nKubernetes YAML generated :\n")
    print(dockerfile)
