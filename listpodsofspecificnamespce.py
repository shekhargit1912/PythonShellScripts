#Python scripts to list all pods in a specific namespace in a Kubernetes cluster

from kubernetes import client, config

def list_pods_in_namespace(namespace):

    #load kubernetes configuration
    config.load_kube_config() 
    l1=[] 

    v1 = client.CoreV1Api()

    #list all the pods in the specified namespace
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        l1.append(pod.metadata.name)
    return l1

# Specify the namespace you want to list pods from

namespace = "default"
pods = list_pods_in_namespace(namespace)
print(f"Pods in namespace '{namespace}':")
for pod_name in pods:
    print(pod_name)


