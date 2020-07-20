build:
	docker-compose build --pull --parallel

down:
	docker-compose down

clean: down
	docker rmi -f nimble-test_web
	docker rmi -f nimble-test_backend
	docker rmi -f nimble-test_worker

reset: down build
	docker-compose up -d

restart:
	docker-compose restart

tests:
	docker-compose run --rm backend bash -c "/usr/src/scripts/init_test_db.sh"
	docker-compose run --rm -e POSTGRES_DB=nimble_test backend pytest -v