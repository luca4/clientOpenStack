import openstack
import sys

#Ottiene l'id del progetto da visualizzare
#project_name = input("Inserisci il nome del progetto:")

conn = openstack.connection.from_config(cloud="devstack", project_name="Project_1")

#Print logged user info

services = conn.identity.services()
        print(service)

user = conn.get_user("Watcher")
print(user)
print("Logged user info:"
      "\nName: ", user.get("name"),
      "\nEmail: ", user.get("email"),
      "\nDescription: ", user.get("description"))


