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
        """ Print nova service info """

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
            print(f"ID:{f.id:3}  Name:{f.name:9}   RAM:{f.ram:5} MB   Disk:{f.disk:3} GB   Virtual CPUs:{f.vcpus}  Is public:{f.to_dict().get('os-flavor-access')}")
            has_elements = True
        if not has_elements:
            print("No flavors found!")


    def print_glance_info(self):
        """ Print glance service info """
        # image
        pass

    def print_cinder_info(self):
        """ Print cinder service info """
        # block storage
        pass

    def print_placement_info(self):
        """ Print placement service info """
        pass

    def print_neutron_info(self):
        """ Print neutron service info """
        # networking
        pass

