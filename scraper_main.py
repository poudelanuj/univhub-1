import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "univhub.settings")
django.setup()

from scraper.university import University

folder = "./univ_scrap/"

universities = [
    "Adelphi University.json",
    "Alliant International University.json",
    "American University.json",
    "Arkansas State University.json",
    "Auburn University.json",
    "Azusa Pacific University.json",
    "Bentley University.json",
]
for x in universities[:-1]:
    u = University(folder+x)
    u.insertion_sequence()

