import re
from pathlib import Path

GUIDES = sorted((Path(__file__).resolve().parents[2] / "corpus" / "guides").glob("*.md"))
REQUIRED = {"id", "titulo", "idioma", "tipo", "origen", "estado"}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, f"{path.name}: falta el encabezado YAML"
    pairs = (line.split(":", 1) for line in match.group(1).splitlines())
    return {key.strip(): value.strip() for key, value in pairs}


def test_there_are_guides():
    assert len(GUIDES) >= 17


def test_every_guide_has_valid_front_matter():
    for path in GUIDES:
        meta = front_matter(path)
        assert REQUIRED <= meta.keys(), path.name
        assert meta["idioma"] in {"es", "en"}, path.name
        assert path.name.startswith(meta["id"]), path.name


def test_guide_ids_are_unique():
    ids = [front_matter(path)["id"] for path in GUIDES]
    assert len(ids) == len(set(ids))


def test_guides_reference_only_existing_guides():
    known = {front_matter(path)["id"] for path in GUIDES}
    for path in GUIDES:
        text = path.read_text(encoding="utf-8")
        for ref in re.findall(r"\bG-\d{2}\b", text):
            assert ref in known, f"{path.name} cita {ref}, que no existe"


def test_no_obvious_secrets():
    for path in GUIDES:
        text = path.read_text(encoding="utf-8").lower()
        assert "password:" not in text and "contraseña:" not in text, path.name
