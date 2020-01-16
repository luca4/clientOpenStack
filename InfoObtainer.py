class InfoObtainer:

    def __init__(self, connection):
        self.connection = connection

    def print_keystone_info(self):
        """ Print keystone service info """

        user = self.connection.get_user("Watcher")
        print("\n[keystone]\nLogged user info:"
              "\nName: ", user["name"],
              "\nEmail: ", user["email"],
              "\nDescription: ", user["description"])

    def print_nova_info(self):
        pass

    def print_glance_info(self):
        pass

    def print_cinder_info(self):
        pass

    def print_placement_info(self):
        pass

    def print_neutron_info(self):
        pass

