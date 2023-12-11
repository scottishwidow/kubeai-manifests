## Kubectl OpenAI plugin


github.com/sozercan/kubectl-ai?tab=readme-ov-file#kubectl-openai-plugin-

## Installation


```bash

wget https://github.com/sozercan/kubectl-ai/releases/download/v0.0.11/kubectl-ai_linux_amd64.tar.gz | tar zxf kubectl-ai_linux_amd64.tar.gz

mv kubectl-ai /usr/local/bin/

chmod +x /usr/local/bin/kubectl-ai

```

```bash

read -s OPENAI_API_KEY

export OPENAI_API_KEY

export OPENAI_VERSION=gpt-3.5-turbo

```

## Prompts testing 

```bash

kubectl ai 'create an nginx deployment with 3 replicas' --require-confirmation=false > test.yaml


```


| NAME                    | PROMPT                          | DESCRIPTION                                                         | EXAMPLE                 |
|:------------------------|:--------------------------------|:--------------------------------------------------------------------|:------------------------|
| app.yaml                | Create an nginx app configuration manifest      | Kubernetes manifest for a basic application schema         | app.yaml                |
| app-livenessProbe.yaml  | Create a Liveness Probe manifest for nginx app            | Kubernetes manifest for a Pod resource, includes a configuration for a readiness probe                | app-livenessProbe.yaml  |
| app-readinessProbe.yaml | Create a Readiness Probe manifest for nginx app          | Kubernetes manifest for a Pod resource, includes a configuration for a liveness probe               | app-readinessProbe.yaml |
| app-volumeMounts.yaml   | Create a Volume Mounts manifest for nginx app       | Kubernetes manifest for a Pod resource that includes a volume   | app-volumeMounts.yaml   |
| app-cronjob.yaml        | Create a Cron Job manifest for nginx app            | Kubernetes manifest for a CronJob resource                   | app-cronjob.yaml        |
| app-job.yaml            | Create a Job manifest for nginx app                   | Kubernetes manifest for a Job resource                        | app-job.yaml            |
| app-multicontainer.yaml | Create a Multi-container Pods manifest for nginx app     | Kubernetes manifest for a Pod resource that contains multiple containers              | app-multicontainer.yaml |
| app-resources.yaml      | Create a Resource Usage manifest for nginx app     | Kubernetes manifest for a Deployment and a corresponding Service | app-resources.yaml      |
| app-secret-env.yaml     | Create a manifest for setting up Secrets as Env Variables | Kubernetes manifest for a Secret resource                 | app-secret-env.yaml     |
