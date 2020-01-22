class InfoObtainer:

    def __init__(self, connection):
        self.connection = connection

    def print_keystone_info(self):
        """ Print keystone service info """

        user = self.connection.get_user("Watcher")
        print("\nLogged user info:"
              "\nName: ", user["name"],
              "\nEmail: ", user["email"],
              "\nDescription: ", user["description"])

        print("\nAll projects list:")
        projects = self.connection.identity.projects()
        for project in projects:
            project = project.to_dict()
            name = project["name"]
            description = project["description"]
            enabled = "True" if project["is_enabled"] == 1 else "False"
            identifier = project["id"]
            print(f"Name: {name:20} Description: {description:30} Enabled: {enabled:7} ID: {identifier}")

    def print_nova_info(self):
        """ Print nova service info (Compute) """

        print("\nServer list:")
        has_elements = False
        for s in self.connection.compute.servers():
            print(f"Name:{s.name}  Status:{s.status}  Description:{s.description}  Image id:{s.image.id}  Flavor name:{s.flavor.get('original_name')}")
            has_elements = True
        if not has_elements:
            print("No servers found!")

        print("\nAvailable flavors:")
        has_elements = False
        for f in self.connection.compute.flavors():
            print(f"ID:{f.id:3}  Name:{f.name:9}   RAM:{f.ram:5} MB   Disk:{f.disk:3} GB   Virtual CPUs:{f.vcpus}")
            has_elements = True
        if not has_elements:
            print("No flavors found!")

    def print_glance_info(self):
        """ Print glance service info (Images) """

        print("\nAvailable images:")
        has_elements = False
        for i in self.connection.image.images():
            print(f"Name:{i.name}  Disk format:{i.disk_format}  Visible:{i.visibility}  Size:{round(i.size/1024/1024, 2)} MB  Status:{i.status}  Created at:{i.created_at}")
            has_elements = True
        if not has_elements:
            print("No images found!")

    def print_cinder_info(self):
        """ Print cinder service info (Block storage)"""

        print("\nAvailable volumes:")
        has_elements = False
        for v in self.connection.block_storage.volumes():
            print(f"ID:{v.id}  Name:{v.name:7}  Size:{v.size} GB  Status:{v.status:6}  Created at:{v.created_at}  Encrypted:{v.is_encrypted}")
            has_elements = True
        if not has_elements:
            print("No volumes found!")

    def print_neutron_info(self):
        """ Print neutron service info """

        print("\nAvailable networks:")
        has_elements = False
        for n in self.connection.network.networks():
            print(f"ID:{n.id}  Name:{n.name:7}  Description:{n.description}  MTU:{n.mtu}  Status:{n.status}  Shared:{n.is_shared}  "
                  f"Network type:{n.provider_network_type}")
            has_elements = True
        if not has_elements:
            print("No networks found!")

        print("\nAvailable routers:")
        has_elements = False
        for r in self.connection.network.routers():
            print(f"ID:{r.id}  Name:{r.name}  Status:{r.status}  Description:{r.description}  Distributed:{r.is_distributed}  "
                  f"Created at:{r.created_at}")
            has_elements = True
        if not has_elements:
            print("No routers found!")

