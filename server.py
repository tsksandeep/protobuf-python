import grpc
import time
from concurrent import futures

import sample_pb2
import sample_pb2_grpc


class SampleServicer(sample_pb2_grpc.SampleServicer):

    def SampleFunction(self, request, context):
        response = sample_pb2.Response()
        response.field_1 = "sample123"
        response.field_2 = "sample123"
        response.field_3 = "sample123"

        if len(request.field_mask.ListFields()) > 0:
            masked_response = sample_pb2.Response()
            request.field_mask.MergeMessage(response, masked_response)
            return masked_response

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=12))

sample_pb2_grpc.add_SampleServicer_to_server(
    SampleServicer(), server)

print('Starting server. Listening on port 5005.')
server.add_insecure_port('[::]:5005')
server.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    server.stop(0)
