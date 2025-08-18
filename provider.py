class Provider:
    def __init__(self, provider_id, name, service, rating):
        self.provider_id = provider_id
        self.name = name
        self.service = service
        self.rating = rating

    def __lt__(self, other):
        return self.provider_id < other.provider_id

    def __eq__(self, other):
        return self.provider_id == other.provider_id

    def __str__(self):
        return f"[{self.provider_id}] {self.name} - {self.service} {self.rating:.1f}★"