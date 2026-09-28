import json
from pathlib import Path


class Memory:

    def __init__(self, path="cosmos_memory.json"):

        self.path = Path(path)

        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {
                "investigations": [],
                "objects": [],
                "knowledge": []
            }

    def remember_investigation(self, investigation):

        self.data["investigations"].append(investigation)

        self.save()

    def remember_object(self, obj):

        self.data["objects"].append(obj)

        self.save()

    def remember_knowledge(self, knowledge):

        self.data["knowledge"].append(knowledge)

        self.save()

    def search(self, keyword):

        results = []

        for section in self.data.values():

            for item in section:

                if keyword.lower() in str(item).lower():
                    results.append(item)

        return results

    def save(self):

        self.path.write_text(
            json.dumps(
                self.data,
                indent=2
            )
        )