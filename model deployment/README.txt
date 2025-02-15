
install requirements
pip install -r requirements.txt

run the model
uvicorn app:app --reload

build the container
docker build -t regression-api .

run the container
docker run -p 80:80 regression-api

Deploy to Kubernetes

Start Kubernetes Cluster we use minikube
minikube start --memory=1800 --cpus=2 --driver=docker
eval $(minikube docker-env)  #linux
@FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i #windows


Build and Load Docker Image
docker build -t regression-api .

Apply Kubernetes Configuration
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Verify Deployment
kubectl get pods
kubectl get services

Access the Application
minikube service regression-api-service --url #this gives a url for the app

Scaling the Application
kubectl scale deployment regression-api --replicas=5

Updating the Application when changing deployment.yaml
kubectl apply -f deployment.yaml

Clean Up
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

Adding domaine name to the app  minikube addons enable ingress
kubectl apply -f ingress.yaml