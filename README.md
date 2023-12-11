# kubeai-manifests

| NAME                    | PROMPT                          | DESCRIPTION                                                         | EXAMPLE                 |
|:------------------------|:--------------------------------|:--------------------------------------------------------------------|:------------------------|
| app.yaml                | Create an nginx app configuration manifest      | YAML to define the basic schema of a Kubernetes application         | app.yaml                |
| app-livenessProbe.yaml  | Create a Liveness Probe manifest for nginx app            | YAML to define a liveness probe for your application                | app-livenessProbe.yaml  |
| app-readinessProbe.yaml | Create a Readiness Probe manifest for nginx app          | YAML to define a readiness probe for your application               | app-readinessProbe.yaml |
| app-volumeMounts.yaml   | Create a Volume Mounts manifest for nginx app       | YAML to define and configure storage volumes for your application   | app-volumeMounts.yaml   |
| app-cronjob.yaml        | Create a Cron Job manifest for nginx app            | YAML to define a cron job within your application                   | app-cronjob.yaml        |
| app-job.yaml            | Create a Job manifest for nginx app                   | YAML to define a job within your application                        | app-job.yaml            |
| app-multicontainer.yaml | Create a Multi-container Pods manifest for nginx app     | YAML to define a pod that runs more than one container              | app-multicontainer.yaml |
| app-resources.yaml      | Create a Resource Usage manifest for nginx app     | YAML to configure resource requests and limits for your application | app-resources.yaml      |
| app-secret-env.yaml     | Create a manifest for setting up Secrets as Env Variables | YAML to define environment variables using secrets                  | app-secret-env.yaml     |