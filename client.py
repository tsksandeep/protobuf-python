import grpc

import sample_pb2
import sample_pb2_grpc

from google.protobuf import field_mask_pb2

channel = grpc.insecure_channel('127.0.0.1:5005')
stub = sample_pb2_grpc.SampleStub(channel)

sample_req = sample_pb2.Request(
    field_1="sample_1",
    field_2="sample_2",
    field_mask=field_mask_pb2.FieldMask(
        # Allow only the fields mentioned in the paths
        paths=[
            'field_1',
            'field_2',
        ]
    )
)

print(stub.SampleFunction(sample_req))
