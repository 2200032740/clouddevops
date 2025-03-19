import os

def apply_terraform():
    print("Applying Terraform changes...")
    os.system("terraform apply -auto-approve")

if __name__ == "__main__":
    apply_terraform()
