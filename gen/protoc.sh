#!/bin/sh

protoc --python_out=../bin msg_type_data.proto
protoc --python_out=../bin msg_type_play.proto
protoc --python_out=../bin msg_enum.proto
protoc --python_out=../bin msg_struct.proto
protoc --python_out=../bin msg_error.proto
protoc --python_out=../bin msg_packet_data.proto
protoc --python_out=../bin msg_packet_play.proto

