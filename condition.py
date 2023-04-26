class Condition:
    def __init__(self, name = "", clear = "", description = ""):
        self.name = name
        self.clear = clear
        self.description = description
        self.size_x = 1
        self.size_y = 1
        self.type = "condition"

    def set_name(self, name):
        self.name = name
    
    def set_clear(self, clear):
        self.clear = clear
    
    def set_description(self, description):
        self.description = description
    
    def get_name(self):
        return self.name

    def get_clear(self):
        return self.clear

    def get_description(self):
        return self.description

    def save_json(self):
        json = {}
        json["type"] = "condition"
        json["name"] = self.name
        json["clear"] = self.clear
        json["description"] = self.description
        json["size_x"] = self.size_x
        json["size_y"] = self.size_y
        return json

    def load_json(self, json):
        self.name = json["name"]
        self.clear = json["clear"]
        self.description = json["description"]
        self.size_x = json["size_x"]
        self.size_y = json["size_y"]
        return self