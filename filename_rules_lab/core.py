"""Preview extension-based folder rules. Never moves or reads named files."""
from pathlib import Path

GROUPS = {
    "documents": {".pdf", ".txt", ".md", ".doc", ".docx", ".csv"},
    "images": {".png", ".jpg", ".jpeg", ".gif", ".svg"},
    "audio": {".mp3", ".wav", ".ogg"},
    "video": {".mp4", ".mov", ".avi"},
    "archives": {".zip", ".gz", ".tar", ".7z"},
    "code": {".py", ".js", ".html", ".css", ".sql"},
}


def plan(names):
    if not isinstance(names, list) or not names:
        raise ValueError("Supply at least one filename")
    seen, result = set(), []
    for name in names:
        if not isinstance(name, str) or not name.strip() or name in (".", ".."):
            raise ValueError("Filename is empty or special")
        if any(char in name for char in '/\\:') or any(ord(char) < 32 or ord(char) == 127 for char in name):
            raise ValueError("Use plain filenames without paths or control characters")
        if name.casefold() in seen:
            raise ValueError("Duplicate filenames, ignoring case, are ambiguous")
        seen.add(name.casefold())
        folder = "hidden" if name.startswith(".") else next(
            (group for group, extensions in GROUPS.items() if Path(name).suffix.lower() in extensions), "other")
        result.append({"name": name, "folder": folder, "destination": folder + "/" + name})
    return result
