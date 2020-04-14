from __future__ import print_function
import grpc
import time_pb2_grpc
import time_pb2

def run():
        channel = grpc.insecure_channel('server:50051')
        stub = time_pb2_grpc.TimeStub(channel)
        response = stub.WhatTime(time_pb2.TimeRequest(requestId = 1))    
        print(response.message)

if __name__ == '__main__':
        run()
