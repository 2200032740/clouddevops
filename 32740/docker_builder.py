import os

def build_docker_image(image_name="todo-app"):
    print(f"Building Docker image: {image_name}...")
    os.system(f"docker build -t {image_name} .")

if __name__ == "__main__":
    build_docker_image()
