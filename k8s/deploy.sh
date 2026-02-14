kubectl apply -f api-deployment.yml
kubectl apply -f worker-deployment.yml
kubectl apply -f redis-pod.yml
kubectl apply -f api-service.yml
kubectl apply -f redis-service.yml

# nowe confi 
kubectl apply -f api-config.yml
kubectl apply -f api-hpa.yml
kubectl apply -f worker-pvc.yaml
kubectl apply -f ingress.yml