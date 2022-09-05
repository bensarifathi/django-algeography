<p align="center"><img src="https://i.imgur.com/05tgtP5.png"></p>
<h1 align="center">Django-Algereography</h1>

**Django-Algereography** allows you to add Models of Algerian Wilayas and Dairas to your existing or new cool Django project .

**- 58 Wilayas.**  
**- 548 Dairas.**  
**- Support both Arabic and French languages.**  
**- Built in models relationships, so you can for example do: `Daira.objects.get(pk=1).wilaya` to get the Wilaya of Daira with the id=1.**   


## Installation
#### Step 1 - Install the package
    pip install algereography
    # or 
    pip install django-algerography

#### Step 2 - Add the package to the installed app
    INSTALLED_APPS = [
    # ... other django app,
    'algerography',
    # or
    'django_algerography'
]

#### Step 3 - Load data fixtures into your db
    python manage.py load_algerography

## Contributing
Thank you for considering contributing to Laravel-Algereography project! Feel free to contribute in any way, we welcome every contribution.

## License
Django-Algereography project is an open-sourced software licensed under the [MIT license](https://github.com/bensarifathi/django-algeography/blob/master/LICENCE)

## Credit
This project was inspied by [Laravel-algerography](https://github.com/theHocineSaad/laravel-algereography).
