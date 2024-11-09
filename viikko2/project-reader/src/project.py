class Project:
    def __init__(self, name, license, description, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_authors(self, authors):
        return "\n- ".join(authors) if self.authors else "-"

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if dependencies else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}"
            f"\n\nAuthors: \n- {self._stringify_authors(self.authors)}"
            f"\n\nDependencies: \n- {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
