import subprocess
import sys

# Function to install a package if it's not found
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install jinja2 and pyyaml (os is built-in)
install_package('jinja2')
install_package('pyyaml')

# Now proceed with the rest of the script
from jinja2 import Environment, FileSystemLoader
import yaml
import os

# Define the data to populate the template
data = {
    "devices": [
        {"name": "leaf1", "ip": "192.168.1.1", "role": "leaf", "location": "rack1"},
        {"name": "leaf2", "ip": "192.168.1.2", "role": "leaf", "location": "rack2"},
        {"name": "spine1", "ip": "192.168.2.1", "role": "spine", "location": "rack3"},
        {"name": "spine2", "ip": "192.168.2.2", "role": "spine", "location": "rack4"},
    ]
}

# File paths
base_dir = os.path.dirname(__file__)
template_file = "test0.j2"
output_file = "test1.yml"

# Render the Jinja2 template and save as YAML
env = Environment(loader=FileSystemLoader(base_dir))
template = env.get_template(template_file)
rendered_yaml = template.render(data)

with open(os.path.join(base_dir, output_file), "w") as yaml_file:
    yaml_file.write(rendered_yaml)


print('\n')
print(f"YAML file '{output_file}' generated successfully.")
print('\n')

# Load and display the YAML content
with open(output_file, "r") as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)

print("Contents of the YAML file:")
print(yaml.dump(yaml_content, default_flow_style=False))
print('\n')
print('\n')
print('\n')
