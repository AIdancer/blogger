### 列出所有pod
```
kubectl get pod -n namespace
```

### 打印pod日志
```
kubectl -n namespace logs -f pod_name -c container_name
```

### 查看pod中所有容器
```
#不包括init容器
kubectl get pods POD_NAME_HERE -o jsonpath={.spec.containers[*].name} -n namespace

#查看所有容器
kubectl get pod POD_NAME_HERE -o jsonpath="{.spec['containers','initContainers'][*].name}" -n namespace
```

