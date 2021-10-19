from jinja2 import Template

j2_template = Template("Hello {{ something }}!")

my_output = j2_template.render(something="World")

print()
print(my_output)
print()
