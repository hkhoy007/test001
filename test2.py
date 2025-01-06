"""
# from jinja2 import Environment, FileSystemLoader
# import yaml
# import os

# # Define the data to populate the template
# data = {
#     "devices": [
#         {"name": "leaf1", "ip": "192.168.1.1", "role": "leaf", "location": "rack1"},
#         {"name": "leaf2", "ip": "192.168.1.2", "role": "leaf", "location": "rack2"},
#         {"name": "spine1", "ip": "192.168.2.1", "role": "spine", "location": "rack3"},
#         {"name": "spine2", "ip": "192.168.2.2", "role": "spine", "location": "rack4"},
#     ]
# }

# # Define file paths
# base_dir = os.path.dirname(__file__)
# template_file = "test0.j2"
# output_file = "test1.yml"

# # Load the Jinja2 template
# env = Environment(loader=FileSystemLoader(base_dir))
# template = env.get_template(template_file)

# # Render the template with data
# rendered_yaml = template.render(data)

# # Write the output to the YAML file
# with open(os.path.join(base_dir, output_file), "w") as yaml_file:
#     yaml_file.write(rendered_yaml)

# print(f"YAML file '{output_file}' has been generated in the 'Main' directory.")
# print('\n')
# print('\n')
# print('\n')


# # Define the path to the YAML file
# file_path = "test1.yml"

# # Read and parse the YAML file
# with open(file_path, "r") as yaml_file:
#     yaml_content = yaml.safe_load(yaml_file)

# # Print the contents of the YAML file to the screen
# print("Contents of the YAML file:")
# print('\n')
# print(yaml.dump(yaml_content, default_flow_style=False))
# print('\n')
# print('\n')
# print('\n')
"""

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

print(f"YAML file '{output_file}' generated successfully.")

# Load and display the YAML content
with open(output_file, "r") as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)

print("Contents of the YAML file:")
print(yaml.dump(yaml_content, default_flow_style=False))
