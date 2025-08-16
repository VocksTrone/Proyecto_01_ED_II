class Provider:
    def __init__(self, provider_id, name, service, rating):
        self.provider_id = provider_id
        self.name = name
        self.service = service
        self.rating = rating

    def __lt__(self, other):
        if self.service == other.service:
            return self.name < other.name
        return self.service < other.service

    def __eq__(self, other):
        return self.service == other.service and self.name == other.name

    def __str__(self):
        return f"[{self.provider_id}] {self.name} - {self.service} {self.rating}★"