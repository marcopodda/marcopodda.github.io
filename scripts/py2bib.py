#! /usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "pybtex",
#     "PyYAML",
#     "setuptools<81",
# ]
# ///

import re
from pathlib import Path

import yaml
from pybtex.database import parse_file



def infer_type(presort):
    if presort == "aa":
        return "Book Chapter"
    elif presort == "bb":
        return "Journal"
    elif presort == "cc":
        return "Conference"
    elif presort == "dd":
        return "Abstract"
    elif presort == "ee":
        return "Thesis"
    raise ValueError(f"Unknown presort {presort}")




def _clean_latex_string(text):
    if not isinstance(text, str):
        return text

    # Step 1: Convert pybtex's internal representation of special characters to LaTeX
    # (e.g., for characters like '---' for em-dash, which pybtex might store differently)
    # This step is largely handled by pybtex's default field access.

    # Step 2: Handle common LaTeX commands for accents and special characters
    # Source: Adapted from various latex-to-unicode converters
    replacements = {
        r"\"{a}": "ä",
        r"\"{A}": "Ä",
        r"\"{o}": "ö",
        r"\"{O}": "Ö",
        r"\"{u}": "ü",
        r"\"{U}": "Ü",
        r"\"{e}": "ë",
        r"\"{E}": "Ë",
        r"\'{a}": "á",
        r"\'{A}": "Á",
        r"\'{e}": "é",
        r"\'{E}": "É",
        r"\'{i}": "í",
        r"\'{I}": "Í",
        r"\'{o}": "ó",
        r"\'{O}": "Ó",
        r"\'{u}": "ú",
        r"\'{U}": "Ú",
        r"\'{y}": "ý",
        r"\'{Y}": "Ý",
        r"\`{a}": "à",
        r"\`{A}": "À",
        r"\`{e}": "è",
        r"\`{E}": "È",
        r"\`{i}": "ì",
        r"\`{I}": "Ì",
        r"\`{o}": "ò",
        r"\`{O}": "Ò",
        r"\`{u}": "ù",
        r"\`{U}": "Ù",
        r"\^{a}": "â",
        r"\^{A}": "Â",
        r"\^{e}": "ê",
        r"\^{E}": "Ê",
        r"\^{i}": "î",
        r"\^{I}": "Î",
        r"\^{o}": "ô",
        r"\^{O}": "Ô",
        r"\^{u}": "û",
        r"\^{U}": "Û",
        r"\~{n}": "ñ",
        r"\~{N}": "Ñ",
        r"\~{o}": "õ",
        r"\~{O}": "Õ",
        r"\c{c}": "ç",
        r"\c{C}": "Ç",
        r"\oe{}": "œ",
        r"\OE{}": "Œ",
        r"\ae{}": "æ",
        r"\AE{}": "Æ",
        r"\aa{}": "å",
        r"\AA{}": "Å",
        r"\o{}": "ø",
        r"\O{}": "Ø",
        r"\ss{}": "ß",
        r"--": "–",  # en-dash
        r"---": "—",  # em-dash
        r"\\": "\\",  # Backslash
        r"\$": "$",
        r"\%": "%",
        r"\&": "&",
        r"\#": "#",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        # Greek letters (basic)
        r"\\alpha": "α",
        r"\\beta": "β",
        r"\\gamma": "γ",
        # Add more as needed
    }

    # Apply replacements
    for latex_char, unicode_char in replacements.items():
        text = text.replace(latex_char, unicode_char)

    # Step 3: Remove remaining unescaped braces that are not part of commands
    # This is tricky as BibTeX uses braces for protection.
    # A simple removal might break valid LaTeX math or structures.
    # However, for plain text fields, often outer braces are just for parsing.
    # Let's target only single *outer* braces that pybtex might leave.
    # More complex cases might need regex that balances braces.
    # For now, let's remove common outer braces if they encompass the whole string.
    if text.startswith("{") and text.endswith("}"):
        # Only remove if it's not a common LaTeX command structure inside
        # This is a heuristic and might need refinement for complex cases
        if not re.search(r"\\.", text[1:-1]):  # Check for \command inside
            text = text[1:-1]  # Remove outer braces

    # Remove any remaining simple curly braces that might have been part of commands
    text = text.replace("{", "").replace("}", "")

    return text.strip()  # Remove any leading/trailing whitespace


def bib_to_yaml_converter(bib_file_path, yaml_file_path):
    try:
        bib_data = parse_file(bib_file_path)
    except FileNotFoundError:
        print(f"Error: BibTeX file not found at '{bib_file_path}'")
        return
    except Exception as e:
        print(f"Error parsing BibTeX file '{bib_file_path}': {e}")
        return

    publications = []

    for entry_key in bib_data.entries:
        entry = bib_data.entries[entry_key]

        pub_dict = {}

        pub_dict["id"] = entry_key

        pub_dict["type"] = infer_type(entry.fields["presort"])  # Clean type too

        common_fields = [
            "title",
            "journal",
            "booktitle",
            "publisher",
            "volume",
            "number",
            "pages",
            "url",
            "DOI",
            "isnb",
            "issn",
            "pdf",
            "code",
        ]
        for field in common_fields:
            if field in entry.fields:
                pub_dict[field] = _clean_latex_string(entry.fields[field])  # Apply cleaning

        if "year" in entry.fields:
            try:
                pub_dict["year"] = int(entry.fields["year"])
            except ValueError:
                pub_dict["year"] = _clean_latex_string(entry.fields["year"])
                print(
                    f"Warning: Year '{entry.fields['year']}' for entry '{
                        entry_key
                    }' is not an integer. Stored as string."
                )

        if "author" in entry.persons:
            formatted_authors = []
            for person in entry.persons["author"]:
                parts, name_parts = [], []
                if person.first_names:
                    name_parts.extend(person.first_names)
                if person.middle_names:
                    name_parts.extend(person.middle_names)

                for n in name_parts:
                    parts.append(f"{n[0].upper()}.")

                if person.last_names:
                    parts.extend(person.last_names)

                formatted_authors.append(" ".join(parts))
            pub_dict["authors"] = _clean_latex_string(", ".join(formatted_authors))
        elif "editor" in entry.persons:
            formatted_editors = []
            for person in entry.persons["editor"]:
                name_parts = []
                if person.first_names:
                    name_parts.extend(person.first_names)
                if person.middle_names:
                    name_parts.extend(person.middle_names)
                if person.last_names:
                    name_parts.extend(person.last_names)
                formatted_editors.append(" ".join(name_parts))
            pub_dict["authors"] = _clean_latex_string(", ".join(formatted_editors) + " (Ed.)")

        if "note" in entry.fields:
            notes_field = entry.fields["note"]
            tags = []
            for part in notes_field.split(";"):
                cleaned_part = _clean_latex_string(part).strip()  # Clean tags too
                if cleaned_part.startswith("tag:"):
                    tag_parts = cleaned_part.split(":")
                    if len(tag_parts) == 2:
                        tags.append(tag_parts[1])
            if tags:
                pub_dict["tags"] = tags

        publications.append(pub_dict)

    try:
        with open(yaml_file_path, "w", encoding="utf-8") as f:
            yaml.dump(
                publications,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
            )
        print(
            f"Successfully converted {len(publications)} entries from '{bib_file_path}' to '{
                yaml_file_path
            }'"
        )
    except IOError as e:
        print(f"Error writing YAML file: {e}")


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    input_bib_file = root / "_bibliography/references.bib"
    output_yaml_file = root / "_data/publications.yaml"

    print("Starting BibTeX to YAML conversion...")
    bib_to_yaml_converter(input_bib_file, output_yaml_file)
    print("Conversion process finished.")
