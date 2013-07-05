pda
===

Personal Data Assistant app which includes a planner (calendar), task, and notepad. Written in Python + Django.

Required Packages
-----------------

  - Database
    *   psycopg2 (http://initd.org/psycopg/)
        Installation:
          $ [sudo] pip install psycopg2
  - Template
    *   django-crispy-forms (http://django-crispy-forms.readthedocs.org/en/latest/install.html#installing-django-crispy-forms)
        $ [sudo] pip install django-crispy-forms
  - Optimization
    *   compressor (https://github.com/jezdez/django_compressor)
        $ [sudo] pip install django_compressor
  - Localization
    *   gettext
        $ brew install gettext
        $ brew link gettext [--force]
