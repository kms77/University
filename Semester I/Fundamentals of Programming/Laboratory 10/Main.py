from Repository.Repository import Repo
from Service.Service import Service
from UI.UI import Presentation

repo = Repo()
service = Service(repo)
ui = Presentation(service)
ui.start()
