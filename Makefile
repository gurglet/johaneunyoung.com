all: languages runserver

languages:
	@cd wedding && django-admin.py makemessages -l sv
	@cd wedding && django-admin.py makemessages -l en
	@cd wedding && django-admin.py compilemessages
	@echo "Remember to restart any running servers to see changes"

runserver:
	python manage.py runserver
