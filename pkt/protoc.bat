
protoc.exe --python_out=..\src msg_type_data.proto
protoc.exe --python_out=..\src msg_type_play.proto
protoc.exe --python_out=..\src msg_enum.proto
protoc.exe --python_out=..\src msg_struct.proto
protoc.exe --python_out=..\src msg_error.proto
protoc.exe --python_out=..\src msg_packet_data.proto
protoc.exe --python_out=..\src msg_packet_play.proto

ProtoGen.exe --include_imports msg_type_data.proto
ProtoGen.exe --include_imports msg_type_play.proto
ProtoGen.exe --include_imports msg_enum.proto
ProtoGen.exe --include_imports msg_struct.proto
ProtoGen.exe --include_imports msg_error.proto
ProtoGen.exe --include_imports msg_packet_data.proto
ProtoGen.exe --include_imports msg_packet_play.proto

pause
