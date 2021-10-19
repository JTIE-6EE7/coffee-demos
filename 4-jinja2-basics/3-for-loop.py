from jinja2 import Template

j2_template = Template("My favorite numbers: {% for n in numbers %}{{n}} {% endfor %}")

my_output = j2_template.render(numbers=range(1,11))

print()
print(my_output)
print()