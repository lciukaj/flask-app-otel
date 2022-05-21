<H2>This is a simple Flask App that allows you test Open Telemetry capabilites. </H2>

<B>This projects consits of following components:</b>
  
- Frontend service (Flask)
- Backend service (Flask)
- MySQL database
- OpenTelemetry collector
- Jaeger
- Zipkin
- Optionally any commercial backend of your choice (e.g. AppDynamics)<BR>

<H2>Please see below steps to quickly run this test setup on Minikube on your local machine:</H2>

<BR>
<B>1. Building Docker images.</B>

`docker build -t flask-app-otel-frontend ./frontend`

`docker build -t flask-app-otel-backend ./backend`

<BR>
<B>2. Loading images to Minikube.</B>

`minikube image load flask-app-otel-frontend:latest`

`minikube image load flask-app-otel-backend:latest`

<BR>
<B>3. Deploying containers to Kubernetes and exposing frontend service.</B>

`kubectl create -f ./k8s/flask-app-otel.yaml`

`kubectl create -f ./k8s/mysql.yaml`

`minikube service flask-app-otel-frontend-svc --url`

<BR>
<B>4. Deploying OTel collector.</B>

`kubectl create -f ./k8s/otel-collector.yaml`

<BR>
<B>5. Deploying Jaeger and exposing service.</B>

`kubectl create -f ./k8s/cert-manager.yaml`

`kubectl create namespace observability`

`kubectl create -f ./k8s/jaeger-operator.yaml -n observability`

`kubectl create -f ./k8s/jaeger.yaml`

`minikube service jaeger-query --url`

<BR>
<B>6. Deploying Zipkin and exposing service.</B>

`kubectl create -f ./k8s/zipkin.yaml`
`minikube service zipkin-svc --url`
