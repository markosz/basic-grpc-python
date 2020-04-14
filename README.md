# basic-grpc-python

Time server and client written in python and communicating via grpc

Different setups:
1. standalone python apps via localhost communication
2. apps running in docker containers, comm. by IP address
3. apps running in k8s pods, comm. by IP address (pod) or service name (service)

A microk8s specific task:
import a local docker image to microk8s:  

https://microk8s.io/docs/registry-images

For testing the client interactively:

https://gc-taylor.com/blog/2016/10/31/fire-up-an-interactive-bash-pod-within-a-kubernetes-cluster

Use sed to replace server name/IP in time_client.py
