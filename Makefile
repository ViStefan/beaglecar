
install:
	[ -d venv ] || python3 -m venv ./venv
	. ./venv/bin/activate; pip3 install -r requirements.txt

clean:
	rm -rf ./venv
