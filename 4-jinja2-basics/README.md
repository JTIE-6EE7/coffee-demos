# Coffee and Network Automation (session 4): Jinja2 Basics

How to render device configs using Jinja2 templates

## Intro

https://ttl255.com/jinja2-tutorial-part-1-introduction-and-variable-substitution/

https://packetlife.net/blog/2019/oct/8/templating-device-configurations/

https://codingpackets.com/blog/jinja2-for-network-engineers/

https://realpython.com/primer-on-jinja-templating/


## 1. Template Syntax and Rendering

{{ stuff }}

j2_template.render(stuff="Things")


## 2. Switch Base Config Template

Switch config using template and data dictionary within the Python script


## 3. Switch Base Config from file

Switch config using external j2 template file and YAML data file


## 4. For-loops

{% for acl in mgmt_acl %}
access-list 10 permit {{ acl }}
{%- endfor %}


## 5. Conditionals

Conditional stuff


## Template testing sites

https://ttl255.com/j2live-online-jinja2-parser/

http://jinja.quantprogramming.com/

