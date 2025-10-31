PROJECT_NAME=BroAi
install: \n\tpip install -r requirements.txt
test: \n\tpytest tests
lint: \n\tflake8 broai tests
format: \n\tblack broai tests
run: \n\tpython broai/main.py
clean: \n\trm -rf build dist *.egg-info
all: install lint test
