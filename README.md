# Install

Follow steps in order

## Step 1

This project use GeoDjanngo. GeoDjango has additional requirements beyond what Django requires (https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/)
So, on Debian/Ubuntu, you are advised to install the following packages which will install, directly or by dependency, the required geospatial libraries:

➜ `sudo apt-get install binutils libproj-dev gdal-bin libspatialite-dev libsqlite3-mod-spatialite make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev`

## Step 2

If you _DONT_ have `pyenv`, then install it:

➜ `curl https://pyenv.run | bash` (after this command ends it asks you to add three lines to your ~/.bashrc. Do it, THEN close your terminal and open a new one (to load ~/.bashrc changes ))

Then install python 3.7.7 using `pyenv` (if you already have it, REMOVE IT (with `pyenv uninstall 3.7.7`), since you need a version recompiled with `--enable-loadable-sqlite-extensions`:

➜ `PYTHON_CONFIGURE_OPTS="--enable-loadable-sqlite-extensions" pyenv install 3.7.7`

Finally, create virtualenv:

➜ `pyenv virtualenv 3.7.7 hackaton`

## Step 3

Clone the repo, then install requirements:

➜ `git clone https://github.com/Los-Supersonicos/backend`

➜ `cd backend`

➜ `pip install -r requirements.txt`

Then:

➜ `cd src && python manage.py migrate && python manage.py createsuperuser`

Done, go to the django admin.
