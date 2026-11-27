import re
from datetime import timezone
from dateutil.parser import parse


def extract_iso_datetimes(text: str) -> list[str]:
    pattern = r"On\s+(?:[A-Za-z]{3},\s+)?(.+?\d{1,2}:\d{2}(?::\d{2})?(?:\s*[aApP][mM])?(?:\s*[+-]\d{4})?)"
    matches = re.findall(pattern, text)
    if not matches:
        raise ValueError("Дату не знайдено")

    results = []
    for raw_dt in matches:
        dt = parse(raw_dt.replace("Sept", "Sep"))
        if dt.tzinfo:
            dt = dt.astimezone(timezone.utc)
        results.append(dt.strftime("%Y-%m-%dT%H:%M:%SZ"))

    return results