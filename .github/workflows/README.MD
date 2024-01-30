# Research Project Workflow

This workflow is part of my research project; however, it currently encounters issues and is not functioning as expected.

## Plans

1. Create a pull request to the `uat` branch.
Execute the `main.yml` workflow, which comprises the following steps:
2. Build and push Docker images to the UAT cloud folder.
3. 1. Plan and apply Terraform to the UAT cloud folder.
3. 2. Test the infrastructure (clusters) in the UAT cloud folder.
3. 3. Destroy the Terraform resources in the UAT cloud folder.
4. Build and push Docker images to the PROD cloud folder.
5. Plan and apply Terraform to the PROD cloud folder.
6. Create a pull request to the `prod` branch.

![Arch](https://github.com/Tousep/stream_finnhub_YC/blob/main/.github/workflows/workflow-plan.jpg)

## Workflows

### 1. `main.yml`

**Description:** The main thread orchestrates the execution of parallel workflows, considering the environment. For production, it ensures the use of UAT-tested infrastructure.

### 2. `docker-image.yml`

**Description:** Build container images and push them to the cloud container registry.

### 3. `terraform_apply.yml`

**Description:** Apply Terraform files to the specified folder using the environments from the UAT configuration.

### 4. `terraform_destroy.yml`

**Description:** Destroy the infrastructure in the specified cloud folder.

### 5. `test.yml`

**Description:** Run tests located in `./terraform-ydb/test/`.

**Environment Configurations:**
  - UAT
  - PROD

**Secrets:**
  - CLICKHOUSE_DB_FINNHUB_USER
  - CLICKHOUSE_DB_FINNHUB_USER_SECRET
  - CLICKHOUSE_DB_NAME
  - FINNHUB_API_KEY
  - KAFKA_FINNHUB_TOPIC
  - KAFKA_USER_CONSUMER
  - KAFKA_USER_PRODUCER
  - KAFKA_USER_SECRET_CONSUMER
  - KAFKA_USER_SECRET_PRODUCER
  - S3_TERRAFORM
  - TF_S3_ACCESS_KEY
  - TF_S3_SECRET_KEY
  - YC_KEY_ID
  - YC_PRIVATE_KEY
  - YC_SERVICE_ACCOUNT_ID

**Variables:**
  - YC_CLOUD_ID
  - YC_CONTAINER_REGISTRY
  - YC_FOLDER_ID

## Contributing

If you encounter issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This research project is licensed under the [MIT License](LICENSE).
