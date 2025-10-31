from deck import Deck, Info, Entry
from copy import deepcopy
from templates.fields import MAIN_SECTION_FIELDS, EXTRA_SECTION_FIELDS, SIDEBOARD_FIELDS


class DeckConverter:
    def __init__(self, deck: Deck, info: Info):
        self.deck = deck
        self.info = info

        self.main_section = {}
        self.extra_section = {}
        self.sideboard_section = {}

        self.main_section_rows = 0
        self.extra_section_rows = 0
        self.sideboard_section_rows = 0

    def _add_main_section_entry(self, entry: Entry):
        if self.main_section_rows >= 31:
            return False
        else:
            name_field, count_field = MAIN_SECTION_FIELDS[self.main_section_rows]
            self.main_section[name_field] = entry.name
            self.main_section[count_field] = entry.count
            self.main_section_rows += 1
            return True
        
    def _add_extra_section_entry(self, entry: Entry):
        if self.extra_section_rows >= 11:
            return False
        else:
            name_field, count_field = EXTRA_SECTION_FIELDS[self.extra_section_rows]
            self.extra_section[name_field] = entry.name
            self.extra_section[count_field] = entry.count
            self.extra_section_rows += 1
            return True

    def _add_sideboard_entry(self, entry: Entry):
        if self.sideboard_section_rows >= 15:
            return False
        else:
            name_field, count_field = SIDEBOARD_FIELDS[self.sideboard_section_rows]
            self.sideboard_section[name_field] = entry.name
            self.sideboard_section[count_field] = entry.count
            self.sideboard_section_rows += 1
            return True
        
    def _count_main_deck(self) -> int:
        total = 0
        for entry in self.deck.main_deck:
            total += entry.count
        return total
    
    def _count_sideboard(self) -> int:
        total = 0
        for entry in self.deck.sideboard:
            total += entry.count
        return total

    def convert(self):
        # remove basics from main deck
        deck = deepcopy(self.deck)
        main_deck = deck.main_deck
        sideboard = deck.sideboard

        basics = ["plains", "island", "swamp", "mountain", "forest", "wastes"]
    
        for i, entry in enumerate(main_deck):
            if entry.name.lower() in basics:
                e = main_deck.pop(i)
                success = self._add_extra_section_entry(e)
                if not success:
                    raise Exception(f"Failed to add {e.name} to extra section")

        for entry in main_deck:
            success = self._add_main_section_entry(entry)
            if not success:
                success = self._add_extra_section_entry(entry)
                if not success:
                    raise Exception(f"Failed to add {entry.name} to main or extra section")

        for entry in sideboard:
            success = self._add_sideboard_entry(entry)
            if not success:
                raise Exception(f"Failed to add {entry.name} to sideboard section")

        pdf_dict = deepcopy(self.info.to_pdf_dict())
        pdf_dict.update(self.main_section)
        pdf_dict.update(self.extra_section)
        pdf_dict.update(self.sideboard_section)

        pdf_dict["Total Cards in Main Deck"] = self._count_main_deck()
        pdf_dict["Total Cards in Sideboard"] = self._count_sideboard()
        return pdf_dict