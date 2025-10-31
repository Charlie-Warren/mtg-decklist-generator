from dataclasses import dataclass

@dataclass
class Entry:
    name: str
    count: int

@dataclass
class Deck:
    main_deck: list[Entry]
    sideboard: list[Entry]


@dataclass
class Info:
    date: str
    event: str
    location: str
    deck_name: str
    deck_designer: str
    first_name: str
    last_name: str

    def to_pdf_dict(self) -> dict[str, str]:
        ret = {
            "Date": self.date,
            "Event": self.event,
            "Location": self.location,
            "Deck Name": self.deck_name,
            "Deck Designer": self.deck_designer,
            "First Name": self.first_name,
            "Last Name": self.last_name,
        }
        try:
            ret["Last Initial"] = self.last_name[0]
        except:
            ret["Last Initial"] = "-"
        return ret