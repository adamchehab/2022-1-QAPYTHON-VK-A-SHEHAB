LOG_FILE = "access.log"

all: clean
	@src/script.sh $(LOG_FILE)
	@echo "Generating CSV result files : Running script.sh on $(LOG_FILE) file"

	@python3 src/script.py
	@echo "Converting CSV result files to JSON result files : Running script.py"

	@echo "Done! Check /results folder."

clean:
	@rm -rf results
	@echo "Removing results drectory ..."