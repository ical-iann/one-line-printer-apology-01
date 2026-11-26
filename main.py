"""The Printer Apology (u-eager-stork-81-9647-the-printer-apology-60229153).

Program/v1 entry: writes the single approved line to entry.txt inside
the directory named by MAKEFUN_OUTPUT_DIR (the harness maps it to
/output/entry.txt). Deterministic, no network, no randomness, no I/O
besides the one output file.

Gate (from the kit RULES): entry.txt must be UTF-8 text of 1-120
characters, a single line, not only whitespace.
"""

import os

LINE = "Maaf, saya tidak sengaja macet — cuma printer yang diberi kertas murahan, ditendang tiap error, dan tetap disalahkan."


def validate_line(line: str) -> None:
    """Raise AssertionError unless `line` passes the competition gate.

    The gate mirrors RULES exactly (1-120 UTF-8 chars, one line, no leading
    or trailing whitespace), so a failure here means the entry would score 0.
    """
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, gate is 1-120"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not start or end with whitespace"
    assert line.strip(), "line must not be only whitespace"
    # The scorer reads UTF-8: prove the exact bytes round-trip cleanly.
    assert line.encode("utf-8").decode("utf-8") == line, "line is not valid UTF-8"


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
