from datetime import datetime   # //a pontos idohoz
from concurrent import futures
import time_pb2_grpc
import time_pb2
import grpc

class TimeServicer(time_pb2_grpc.TimeServicer):
    def WhatTime(self, request, context):
        currentTime = datetime.now().strftime("%H:%M:%S")
        return time_pb2.TimeResponse(message = "id: {},".format(request.requestId) + " " + currentTime)
    # //visszaadja az kliens altal atadott azonositot es a pontos idot

def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        time_pb2_grpc.add_TimeServicer_to_server(
            TimeServicer(), server)
        server.add_insecure_port('[::]:50051')    #//50051-es porton kommunikalnak
        server.start()
        server.wait_for_termination()

if __name__ == '__main__':
    serve()

