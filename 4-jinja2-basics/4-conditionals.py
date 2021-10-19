from jinja2 import Template


t = Template("""hostname {{ hostname }}
{% if ios_ver >= 12.2 -%}
Detected IOS ver {{ ios_ver }}, using new command syntax.
{% else -%}
Detected IOS ver {{ ios_ver }}, using old command syntax.
{% endif %}""")

data = {
    "ios_ver": 12.2,
    "hostname": "ios-router"
}

my_output = t.render(data)

print()
print(my_output)
print()