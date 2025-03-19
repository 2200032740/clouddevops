import os

def deploy_to_kubernetes():
    print("Deploying application to Kubernetes...")
    os.system("kubectl apply -f deployment.yaml")

if __name__ == "__main__":
    deploy_to_kubernetes()
