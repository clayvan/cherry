from flask import Flask, send_file, request, Response
from kubernetes import client, config
from prometheus_client import start_http_server, Counter, generate_latest, Gauge

app = Flask(__name__)

count_of_metrics_requests = Counter(
    'count_of_metrics_requests',
    'Number of requests sent to the metrics endpoint.'
)

num_of_pods = Gauge(
    'num_of_pods',
    'Number of pods running in k8s cluster.'
)

def get_pod_count():
    print('Loading kubeconfig from local kubeconfig')
    config.load_kube_config()
    api_instance = client.CoreV1Api()
    pods = api_instance.list_pod_for_all_namespaces(watch=False)

    return len(pods.items)

@app.route('/metrics', methods=['GET'])
def get_data():
    count_of_metrics_requests.inc()
    num_of_pods.set(get_pod_count())

    return Response(generate_latest())
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')