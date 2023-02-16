### Protobuf `field_mask` example with Python

---

```
<!-- To create a virtual environment -->
$ python -m venv /path/to/directory

<!-- To activate venv -->
$ source /path/to/venv/bin/activate

<!-- To install requirements -->
$ pip install -r requirements.txt

<!-- To generate python files from proto files -->
$ python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. sample.proto

<!-- To run the server in terminal 1 -->
$ python server.py

<!-- To run the client in terminal 1 -->
$ python client.py
```
