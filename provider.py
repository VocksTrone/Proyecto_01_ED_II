from mensajes import YELLOW, RESET

def rating_to_stars(rating: float) -> str:
    rounded = int(rating) if rating % 1 < 0.7 else int(rating) + 1
    return YELLOW + "★" * rounded + RESET

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
        stars = rating_to_stars(self.rating)
        return f"[{self.provider_id}] {self.name} - {self.service} {self.rating:.1f} {stars}"
