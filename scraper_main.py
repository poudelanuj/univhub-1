import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "univhub.settings")
django.setup()

from scraper.university import University

u=University("./scraped_universities/James Cook University.json")

u.insertion_sequence()