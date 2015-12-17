**Quickstart:**

```
git clone git@github.com:Isizukuri/dlvpef.git
virtualenv --no-site-packages venv
source venv/bin/activate
pip2.7 install -r requirements.txt
cd src/
python manage.py migrate
python manage.py createsuperuser
python manage.py run
```
