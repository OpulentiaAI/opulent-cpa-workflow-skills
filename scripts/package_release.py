#!/usr/bin/env python3
import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def add_tree(archive, source, prefix):
    for file_path in sorted(source.rglob("*")):
        if file_path.is_file() and file_path.name not in {".DS_Store"} and "__pycache__" not in file_path.parts:
            archive.write(file_path, Path(prefix) / file_path.relative_to(source))


def digest(file_path):
    value = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def main():
    DIST.mkdir(exist_ok=True)
    for old in DIST.glob("*.skill"):
        old.unlink()
    for old in DIST.glob("*.harbor.zip"):
        old.unlink()
    outputs = []
    for skill in sorted((ROOT / "skills").iterdir()):
        if not skill.is_dir():
            continue
        archive_path = DIST / f"{skill.name}.skill"
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            add_tree(archive, skill, skill.name)
        outputs.append(archive_path)
        environment = ROOT / "environments" / skill.name
        environment_archive = DIST / f"{skill.name}.harbor.zip"
        with zipfile.ZipFile(environment_archive, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            add_tree(archive, environment, skill.name)
        outputs.append(environment_archive)
    checksums = [f"{digest(file_path)}  {file_path.name}" for file_path in sorted(outputs)]
    (DIST / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    print(f"PACKAGED: {len(outputs) // 2} skills and {len(outputs) // 2} Harbor environment archives")


if __name__ == "__main__":
    main()

