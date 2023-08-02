import docker
from docker.errors import DockerException
from utils import handle_error

def deploy_code(repo_name, target_env, deployment_script=None, resources=None):
    """
    Function to deploy the codebase to a specified environment.
    """
    try:
        client = docker.from_env()

        # Build Docker image
        image, build_logs = client.images.build(path="GitBotAI/GitBotAI/Dockerfile", tag=f"{repo_name}:latest", dockerfile="Dockerfile")

        # Log build output
        for log in build_logs:
            print(log)

        # Define container settings based on user input
        container_settings = {
            "image": image.id,
            "detach": True,
            "name": f"{repo_name}_container",
            "environment": [f"TARGET_ENV={target_env}"],
            "cpu_shares": resources.get("cpu_shares", None),
            "mem_limit": resources.get("mem_limit", None),
        }

        # Run deployment script if provided
        if deployment_script:
            container_settings["command"] = deployment_script

        # Create and start the container
        container = client.containers.create(**container_settings)
        container.start()

        print(f"Successfully deployed {repo_name} to {target_env}.")

    except DockerException as e:
        handle_error(e)