## Zadanie: Uruchomienie aplikacji w Kubernetes

Celem zadania jest wdrożenie komponentów aplikacji (API, worker, Redis) w klastrze Kubernetes przy użyciu plików konfiguracyjnych YAML.

### Kroki
0. Uruchom komende 
```bash
minikube start
```

1. Wdróż deployment API:

```bash
kubectl apply -f api-deployment.yml
```
Utwórz service dla API:
```bash
kubectl apply -f api-service.yml
```
Wdróż worker:
```bash
kubectl apply -f worker-deployment.yml
```
Uruchom Redis:

```bash
kubectl apply -f redis-pod.yml
```
Utwórz service dla Redis:

```bash
kubectl apply -f redis-service.yml
```
Sprawdź status zasobów:

```bash
kubectl get pods
kubectl get services
```

### Sprawdzenie działania API w Minikube

Po wdrożeniu wszystkich komponentów sprawdź, czy serwis API jest dostępny:

```bash
minikube service api
Polecenie powinno zwrócić adres URL podobny do:
```

http://192.168.49.2:30080

Następnie sprawdź działanie API w przeglądarce lub przez curl:
```bash
curl http://192.168.49.2:30080
```