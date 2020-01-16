import openstack
from InfoObtainer import InfoObtainer

# Ottiene l'id del progetto da visualizzare
# project_name = input("Inserisci il nome del progetto:")

conn = openstack.connection.from_config(cloud="devstack", project_name="Project_1")

# Save services status
services_status = {}

services = conn.identity.services()

# fill services_status dictionary
for service in services:
    s = service.to_dict()
    name = s["name"]
    enabled = s["is_enabled"]
    services_status[name] = enabled

print("\nServices status:")
i = 1
for s in services_status:
    if s in ("glance", "cinder", "nova", "placement", "neutron", "keystone"):
        print(f"{i}) {s:10}", "->", "Enabled" if services_status[s] == True else "Disabled")
        i += 1

infoObt = InfoObtainer(conn)
service_number = 6#int(input("\nInsert service number to get specific info:\n"))

if service_number == 1:
    infoObt.print_glance_info()
elif service_number == 2:
    infoObt.print_cinder_info()
elif service_number == 3:
    infoObt.print_placement_info()
elif service_number == 4:
    infoObt.print_neutron_info()
elif service_number == 5:
    infoObt.print_nova_info()
elif service_number == 6:
    infoObt.print_keystone_info()



"""servers = conn.compute.servers()
for server in servers:
    print(server)

servers = conn.compute.images()
for server in servers:
    print(server)

servers = conn.compute.flavors()
for server in servers:
    print(server)

servers = conn.compute.services()
for server in servers:
    print(server)"""