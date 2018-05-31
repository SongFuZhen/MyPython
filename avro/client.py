import io
import json
import socket
import avro.datafile
import avro.schema
import avro.io
import avro.ipc

SCHEMA = avro.schema.Parse(json.dumps({
    "namespace": "example.avro",
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "favorite_number", "type": ["int", "null"]},
        {"name": "favorite_color", "type": ["string", "null"]}
    ]
}))


def send_message(connection, message):
    buf = io.BytesIO()
    writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), SCHEMA)
    writer.append(message)
    writer.flush()
    buf.seek(0)
    data = buf.read()
    connection.send(data)


def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(('127.0.0.1', 12345))
    send_message(connection, {'name': 'Eli',
                              'favorite_number': 42, 'favorite_color': 'black'})


if __name__ == '__main__':
    main()
