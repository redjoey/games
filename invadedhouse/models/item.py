class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.get_name()

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def look(self):
        print(self.get_description())
