rungunicornserver:
	# Use this for console logs
	gunicorn --worker-class eventlet -w 1 mult-trainer:app -b 0.0.0.0:8000 --log-level=DEBUG --no-sendfile --log-file=- --log-level=info


rungunicornserverDev:
	# Use this for console logs
	gunicorn --reload --worker-class eventlet -w 1 tekvideo-dev:app -b 0.0.0.0:8000 --log-level=DEBUG --no-sendfile --log-file=- --log-level=info


rundevelopmentserver:
	export FLASK_ENV=development && flask run


initialize_test_database:
	python initialize_database.py


python_console:
	python -i console.py


.PHONY:


syncinstallation: .PHONY
	pip install -r requirements.txt
	export FLASK_APP=mult-trainer:app && flask db upgrade
	@echo ""
	@echo "Next step is most likely to run 'make rungunicornserver'"


syncinstallationDev: .PHONY
	pip install -r requirements.txt
	export FLASK_APP=mult-trainer-dev::app && flask db upgrade
	@echo ""
	@echo "Next step is most likely to run 'make rungunicornserverDev'"
