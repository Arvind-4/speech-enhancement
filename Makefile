frontend: 
	npm run dev --prefix=apps/frontend

backend:
	bash commands/run.dev.sh

activate:
	source bin/activate

run: 
	bash commands/run.dev.sh  & npm run dev --prefix=apps/frontend

install: 
	npm install --prefix=apps/frontend
	pip install -r requirements.txt

clean:
	rm -rf ./**/__pycache__
	rm -rf ./**/static
	rm -rf ./**/node_modules
	rm -rf ./**/build

format:
	black ./apps/**/*.py
	npm run format --prefix=apps/frontend

format-watch:
	npm run format:watch --prefix=apps/frontend

.PHONY: install clean reinstall format