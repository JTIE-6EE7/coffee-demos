from jinja2 import Template

t = Template("Hello {{ something }}!")

my_output = t.render(something="World")

print(my_output)

