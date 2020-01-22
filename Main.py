import openstack
from openstack.exceptions import SDKException

from InfoObtainer import InfoObtainer
import os
import sys


# Ottiene l'id del progetto da visualizzare
# project_name = input("Inserisci il nome del progetto:")

try:
    conn = openstack.connection.from_config(cloud="devstack", project_name="Project_2")
except SDKException:
    print("Error: a problem occurred while connecting to OpenStack!")
    sys.exit(1)

print("Successfully connected to OpenStack\n")

infoObt = InfoObtainer(conn)
while True:
    services = None
    try:
        services = conn.identity.services()
    except:  # InternalServerError:
        print("Error: a problem occurred while connecting to keystone!")
        sys.exit(1)

    # Print services status
    print("\n\nServices status:")
    i = 1
    for service in services:
        service = service.to_dict()
        name = service["name"]
        if name in ("glance", "cinder", "nova", "placement", "neutron", "keystone"):
            print(f"{i}) {name:10}", "->", "Enabled" if service["is_enabled"] is True else "Disabled")
            i += 1

    # Get chosen value and check it
    try:
        service_number = 5  # int(input("\nInsert service number to get specific info (0 to exit program):\n"))
    except ValueError:
        print("Error: Insert integer value!\n")
        continue
    if service_number < 0 or service_number > 6:
        print("Error: Number must be between 0 and 6\n")
        continue

    # Clear the screen
    os.system('clear')

    if service_number == 0:
        break
    elif service_number == 1:
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

    break;  # TODO only for development

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
