# eCom

An e-commerce platform created using Django.

## Dependencies
- Django (3.0.7)
- Python (>=3.6.9)

## Install components
```bash
sudo apt-get update
sudo apt-get install python-pip 
```

### Setting up Virtual Environment and Install Requirements
```bash
sudo pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### Running the website locally

Update settings.py: make DEBUG = True
  
```bash
cd ~/eCom
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Contributors
- Dhanwin Rao  https://github.com/dhanwin247/
- Varun N R    https://github.com/varun-raghavendra/
