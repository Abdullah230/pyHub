import sys
sys.path.insert(0, 'F:/Commits/Python/Lib_projects/protobuf/')
import test_pb2

message = test_pb2.test_message()
message.user_number = 234
message.user_message = "This is a user message"
message.extra_details.extend(["This is supposed to be a mesage", "This is supposed to be message numner 2"])

