import os

os.system("git bisect start $BAD_COMMIT $GOOD_COMMIT")
os.system("git bisect run python manage.py test")
