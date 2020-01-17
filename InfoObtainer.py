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
        # compute
        pass

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

