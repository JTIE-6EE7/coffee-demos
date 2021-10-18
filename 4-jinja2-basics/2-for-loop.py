from jinja2 import Template

t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")

my_output = t.render()

print(my_output)
