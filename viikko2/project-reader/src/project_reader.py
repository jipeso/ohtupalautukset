import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        p = toml.loads(content)

        self.name = p["tool"]["poetry"]["name"]
        self.description = p["tool"]["poetry"]["description"]
        self.license = p["tool"]["poetry"]["license"]
        self.authors = p["tool"]["poetry"]["authors"]
        self.dependencies = p["tool"]["poetry"]["dependencies"]
        self.dev_dependencies = p["tool"]["poetry"]["group"]["dev"]["dependencies"]


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(self.name, self.description, self.license, self.authors, self.dependencies, self.dev_dependencies)
