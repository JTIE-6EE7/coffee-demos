from jinja2 import Template

template = """hostname {{ hostname }}

no ip domain lookup
ip domain name local.lab
ip ssh version 2
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}

logging host {{ splunk_pri }}
logging host {{ splunk_sec }}"""

data = {
    "hostname": "core-sw-nsh-01",
    "name_server_pri": "192.0.2.11",
    "name_server_sec": "192.0.2.12",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
    "splunk_pri": "192.0.2.21",
    "splunk_sec": "192.0.2.22",
}

j2_template = Template(template)

cfg = j2_template.render(data)

print()
print(cfg)
print()