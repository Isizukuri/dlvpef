**Quickstart:**

```
git clone git@github.com:Isizukuri/simpleLandingPage.git
cd simpleLandingPage/
virtualenv --no-site-packages .env
source .env/bin/activate
pip2.7 install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py run
```
