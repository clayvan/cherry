# cherry

This is the project for the below challenge [listed here](https://gist.github.com/stmpy/ea13965c5f3263f2b03cb26c44d5b8df)

## Usage

To build:
```sh
docker build -t clayvan.com/cherry:v0.1.0 -f cherry.Dockerfile .
```

To run, first ensure you've loaded your kube context to the cluster you'd like to scrape metrics for:
```sh
docker run \
    -p 5000:5000 \
    -v ${HOME}/.kube/config:/root/.kube/config \
    clayvan.com/cherry:v0.1.0
```

Exposing a local prometheus instance:
```sh
docker run \
    -v ${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml \
    -p 9090:9090 \
    prom/prometheus:v2.1.0 \
    --config.file=/etc/prometheus/prometheus.yml
```