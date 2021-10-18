from jinja2 import Template

t = Template("My favorite numbers: {% for n in numbers %}{{n}} {% endfor %}")

my_output = t.render(numbers=range(1,11))

print(f"\n{my_output}\n")
