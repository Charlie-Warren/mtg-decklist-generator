from pypdf import PdfReader, PdfWriter
from pathlib import Path
from deck import Entry, Deck, Info
from deck_converter import DeckConverter


def read_moxfield_text(file_path) -> Deck:
    with open(file_path, "r") as f:
        raw = f.readlines()

    raw = [line for line in raw if "SIDEBOARD:\n"!=line]
    split_index = raw.index("\n")
    
    main = raw[:split_index]
    sideboard = raw[split_index + 1:]

    main_lines = [line.strip() for line in main if line != "\n"]
    sideboard_lines = [line.strip() for line in sideboard if line != "\n"]

    main_deck = []
    for line in main_lines:
        count, name = line.split(" ", maxsplit=1)
        main_deck.append(Entry(name, int(count)))

    sideboard = []
    for line in sideboard_lines:
        count, name = line.split(" ", maxsplit=1)
        sideboard.append(Entry(name, int(count)))

    return Deck(main_deck, sideboard)


def save_pdf(writer: PdfWriter, fname: str = "decklist.pdf") -> None:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / fname

    with open(output_path, "wb") as f:
        writer.write(f)


def get_writer() -> PdfWriter:
    script_dir = Path(__file__).parent.absolute()
    template_path = script_dir / "templates" / "constructed_decklist_blank.pdf"
    reader = PdfReader(template_path)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    return writer


def generate_decklist(
        input_file,
        output_fname: str,
        date: str,
        event: str,
        location: str,
        deck_name: str,
        deck_designer: str,
        first_name: str,
        last_name: str
    ) -> None:
    deck = read_moxfield_text(input_file)
    info = Info(date, event, location, deck_name, deck_designer, first_name, last_name)
    deckconverter = DeckConverter(deck, info)

    writer = get_writer()
    print(f"Fields = {writer.get_fields()}")
    pdf_dict = deckconverter.convert()
    writer.update_page_form_field_values(writer.pages[0], pdf_dict)
    save_pdf(writer, output_fname)