# Animal Crossing Villager Database

## A database to reference the villagers I've invited to my Animal Crossing: New Horizons island

### API Reference

WIP: endpoint paths, methods, parameters

endpoints example:

**Villagers**

- index: GET /villagers
- show: GET /villagers/:id
- create: POST /villagers
- delete: DELETE /villagers

### Project Evolution

I first created this database completely in Postgres and manually inputted 
the data. Then I switched to Flask/SQLAlchemy to follow along with what I was 
learning in the Nucamp SQL course. Now, I’ve decided to switch to Django to have use a framework that already has everything I’ll need built-in (including user accounts easier front-end development). I'm still implementing the basic functions and endpoints, but in the future hope to create a complete web app with a frontend for user access.

### ORM Implementation

While using SQL would've been simpler to get started with, I wanted to build my experience with Django. I found that it also helped when inputting the initial values for some tables, since I could automate some repetitive values with Python and Django’s [custom management commands](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/).

```python
from django.core.management.base import BaseCommand
from app.models import Coffee
import itertools

class Command(BaseCommand):

    def handle(self, *args, **options):
        combo = [['Blue Mtn', 'Kilimanjaro', 'Mocha', 'Blend'],
                 ['None', 'Little', 'Regular', 'A Lot'],
                 [0, 1, 2, 3]]
        blends = list(itertools.product(*combo))
        coffees = []
        for b in blends:
            c = Coffee(beans=b[0], milk=b[1], sugar=b[2])
            coffees.append(c)

        for c in coffees:
            c.save()
```

Using itertools, I created a list of all possible coffee combinations, then passed each of those values to be added to the coffees table.

### Roadmap

I've created a kanban board of my progress and new features I want to implement in this project, which I will keep adding to: [Link](https://ticiadev.notion.site/DevOps-Django-portfolio-project-roadmap-3a4af7320d0844809f80b86f43a6994b)

### Issues

TBD
