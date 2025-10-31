from decklist_generator import generate_decklist


def main():
    generate_decklist(
        input_file="example_decklists/Eldrazi Tron - moxfield.txt",
        output_fname="etron_decklist.pdf",
        date="2025-10-31",
        event="RCQ",
        location="My LGS",
        deck_name="Eldrazi Tron",
        deck_designer="Alice Smith",
        first_name="Joe",
        last_name="Bloggs"
    )

    generate_decklist(
        input_file="example_decklists/Deck - Mono-Green Amulet Titan - mtggoldfish.txt",
        output_fname="amulet_decklist.pdf",
        date="2025-10-31",
        event="RCQ",
        location="My LGS",
        deck_name="Amulet Titan",
        deck_designer="John Smith",
        first_name="Sarah",
        last_name="Roberts"
    )


if __name__ == "__main__":
    main()