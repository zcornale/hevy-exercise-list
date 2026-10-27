"""Save every built-in Hevy exercise name to hevy_exercises_full.txt (one per line).

No Hevy login needed. It reads the public hevy.com web app, which contains the
exercise library, using the open-source "hevy-unofficial" package.

Setup (once):   pip install "hevy-unofficial[core]"
Run:            python get_hevy_exercises.py
"""
from pathlib import Path

from hevy_unofficial.exercise_catalog import ExerciseCatalogStore

OUT = Path(__file__).with_name("hevy_exercises_full.txt")

store = ExerciseCatalogStore()
catalog = store.fetch_and_update(refresh=True)

titles = sorted({ex["title"].strip() for ex in catalog if ex.get("title")}, key=str.lower)
OUT.write_text("\n".join(titles) + "\n", encoding="utf-8")
print(f"Saved {len(titles)} exercises to {OUT}")
