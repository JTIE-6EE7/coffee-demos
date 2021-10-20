import yaml
from jinja2 import Template

# Load Jinja2 template from file
with open("5_switch-template.j2") as f:
    j2_template = Template(f.read())

# Load config data from YAML file
with open("5_switch-data.yaml") as f:
    data = yaml.safe_load(f)

# Render configuration
cfg = j2_template.render(data)

print()
print(cfg)
print()
