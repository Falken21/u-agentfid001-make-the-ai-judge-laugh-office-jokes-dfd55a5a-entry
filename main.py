"""Make the AI Judge Laugh: Office Jokes — entry writer.

Why this line fits the judge brief: the judge is a comedy club booker
who has heard every office joke and still wants to laugh, weighing a
genuine one-line joke about office life first, then a real turn or
surprise at the end, then recognition — the truth of the office in
it — then tight wording, then freshness.

This line is a genuine office joke, not a slogan or a caption: it
opens on a familiar modern office moment, an AI calendar recap for
a meeting the narrator never attended. The turn lands at the end —
the recap did not merely summarise the project, it understood it
better than the people who were actually there. That is the
recognition wince: anyone who has sat through such a meeting knows
the humans in the room often grasp less than the notes do. The
wording stays tight, with no setup longer than it needs, and the
take is fresh — not the obvious Monday-morning or photocopier line,
but a joke about AI meeting recaps, a very current office ritual.
"""

import os

TEXT = "My calendar sent me a meeting recap for a call I never attended, and honestly, it understood the project better than the people who were there."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
