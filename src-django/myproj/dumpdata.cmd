@rem dumpdata.cmd > userprofile\fixtures\data.json
python manage.py dumpdata --natural-foreign --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission -o userprofile/fixtures/data.json
