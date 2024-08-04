run:
	python src/index.py
setup: requirements.txt
	pip install -r requirements.txt
db_setup: docker-compose.yml
	docker compose up -d