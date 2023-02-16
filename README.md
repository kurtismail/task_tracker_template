   94  python -m venv env
   95  source env/Scripts/activate
   96  pip install -r requirements.txt
   97  python manage.py migrate
   98  python manage.py createsuperuser
   99  python manage.py runserver
  100  python manage.py startapp todo
  101  history

  # integer db'de daha az yer tutar, onun için 1,2,3 olarak tanımladık

  title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    from django import forms
    from .models import Todo

# todo içinde templete folder oluştur
base.html

bootstrap kullanmak için: getbootstrap.com adresinden cdn linklerini base.html'e kopyalamanız yeterli.