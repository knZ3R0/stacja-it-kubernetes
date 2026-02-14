##  Zadanie — uruchomienie aplikacji z manifestów i test działania
Cel

Uczestnik:
* 
```bash
kubectl delete -f redis-pod.yml
kubectl apply -f redis-pod.yml
```

* uruchomi aplikację z manifestów Kubernetes
```bash
kubectl apply -f api-config.yml
kubectl apply -f api-hpa.yml
kubectl apply -f worker-pvc.yaml
kubectl apply -f ingress.yml
```
Uwaga:
```bash
minikube addons enable ingress
```

```bash
echo "$(minikube ip) api.local" | sudo tee -a /etc/hosts
curl http://api.local
```


* sprawdzi działanie Deployment

* przetestuje Service

* zweryfikuje, czy aplikacja odpowiada z nową konfiguracją. 

* nowy deploy dla nowego obrazu z env dla workera
