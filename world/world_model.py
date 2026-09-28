class WorldModel:

    def __init__(self):

        self.objects = {}
        self.relationships = []

    def add_object(self, object_id, data):

        self.objects[object_id] = data

    def add_relationship(
        self,
        source,
        relationship,
        target
    ):

        self.relationships.append({
            "source": source,
            "relationship": relationship,
            "target": target
        })

    def get_object(self, object_id):

        return self.objects.get(object_id)

    def get_relationships(self, object_id):

        return [
            r for r in self.relationships
            if r["source"] == object_id
            or r["target"] == object_id
        ]