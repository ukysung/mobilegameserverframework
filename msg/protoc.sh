#!/bin/sh

protoc --python_out=../src msg_type_data.proto
protoc --python_out=../src msg_type_play.proto
protoc --python_out=../src msg_enum.proto
protoc --python_out=../src msg_struct.proto
protoc --python_out=../src msg_error.proto
protoc --python_out=../src msg_packet_data.proto
protoc --python_out=../src msg_packet_play.proto

