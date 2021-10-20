from jinja2 import Template

template = """
hostname {{ site_code }}-{{ device_role }}-{{ device_name}}

no ip domain lookup
ip domain name {{ domain_name }}
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}
ip ssh version 2

ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}

logging host {{ splunk_pri }}
logging host {{ splunk_sec }}"""

data = {
    "site_code": "nsh",
    "device_role": "core",
    "device_name": "sw-01",
    "domain_name": "local.lab",
    "name_server_pri": "192.0.2.11",
    "name_server_sec": "192.0.2.12",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
    "splunk_pri": "192.0.2.21",
    "splunk_sec": "192.0.2.22",
}

j2_template = Template(template)

cfg = j2_template.render(data)

print(cfg)
print()