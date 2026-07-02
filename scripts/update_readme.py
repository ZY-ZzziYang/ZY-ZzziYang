from pathlib import Path
import random

from jinja2 import Template


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "README_TEMPLATE.md"
README_PATH = ROOT / "README.md"

GREETINGS = [
    "Keep coding and make the workflow smoother.",
    "Build one reliable tool, then let it save time every day.",
    "Small automations compound into big wins.",
    "Turn repetitive work into a button.",
    "Make the lab workflow cleaner than yesterday.",
]


def main() -> None:
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    rendered = template.render(greeting=random.choice(GREETINGS))
    README_PATH.write_text(rendered, encoding="utf-8")
    print("README.md updated from README_TEMPLATE.md.")


if __name__ == "__main__":
    main()
