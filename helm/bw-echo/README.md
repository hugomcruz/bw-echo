# bw-echo Helm Chart

Helm chart for deploying the bw-echo REST API service on Kubernetes.

## Prerequisites

- Kubernetes 1.19+
- Helm 3.0+

## Installing the Chart

To install the chart with the release name `my-bw-echo`:

```bash
helm install my-bw-echo ./helm/bw-echo
```

## Uninstalling the Chart

```bash
helm uninstall my-bw-echo
```

## Configuration

The following table lists the configurable parameters of the bw-echo chart and their default values.

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of replicas | `2` |
| `image.repository` | Image repository | `bw-echo` |
| `image.tag` | Image tag | `latest` |
| `image.pullPolicy` | Image pull policy | `IfNotPresent` |
| `service.type` | Service type | `ClusterIP` |
| `service.port` | Service port | `8000` |
| `ingress.enabled` | Enable ingress | `false` |
| `cluster.country` | Cluster country code | `XX` |
| `cluster.location` | Cluster location | `Not Provided` |
| `cluster.providedBy` | Cluster provider | `Not Provided` |
| `resources.limits.cpu` | CPU limit | `500m` |
| `resources.limits.memory` | Memory limit | `512Mi` |
| `resources.requests.cpu` | CPU request | `100m` |
| `resources.requests.memory` | Memory request | `128Mi` |
| `autoscaling.enabled` | Enable HPA | `false` |

## Example: Custom Values

Create a `custom-values.yaml` file:

```yaml
replicaCount: 3

image:
  repository: my-registry/bw-echo
  tag: "v1.0.0"

service:
  type: LoadBalancer

cluster:
  country: "PT"
  location: "Lisbon"
  providedBy: "Vodafone"

ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: echo.example.com
      paths:
        - path: /
          pathType: Prefix

resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 200m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

Install with custom values:

```bash
helm install my-bw-echo ./helm/bw-echo -f custom-values.yaml
```

## Upgrading

```bash
helm upgrade my-bw-echo ./helm/bw-echo -f custom-values.yaml
```

## Testing the Deployment

After installation, follow the instructions from the NOTES to access your application:

```bash
# Port forward to access locally
kubectl port-forward svc/my-bw-echo 8000:8000

# Test the endpoint
curl http://localhost:8000/echo
```
