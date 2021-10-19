from jinja2 import Template


j2_template = Template("""hostname {{ hostname }}
{% if ios_ver >= 12.2 -%}
Detected IOS ver {{ ios_ver }}, using new command syntax.
{% else -%}
Detected IOS ver {{ ios_ver }}, using old command syntax.
{% endif %}""")

data = {
    "ios_ver": 12.2,
    "hostname": "ios-router"
}

my_output = j2_template.render(data)

print()
print(my_output)
print()