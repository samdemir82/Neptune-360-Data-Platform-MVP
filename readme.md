
## README.md

# IoT Telemetry Data Platform 

---

## 📈 Architecture Overview

This project outlines a scalable, AWS-native data platform architecture designed for IoT telemetry ingestion, storage, processing, and real-time analytics.
It ensures efficient handling of high-frequency meter or sensor data, enabling robust data-driven decision-making and scalable growth for future analytics needs.
![chrome_U7RORlr9Br](https://github.com/user-attachments/assets/ecfaaa94-3eb9-437e-8746-384935a1da2a)


---

## 🏛️ Layers and Technologies Used

| Layer | AWS Service | Purpose / Benefit |
|------|--------------|-------------------|
| **Ingestion** | **Kinesis Firehose** | Streaming massive real-time telemetry |
| | **AWS Lambda** | API calls, pushing batch JSON data |
| | **S3 Landing Zone** | Durable, cheap storage for raw ingestion |
| **ETL** | **Glue Crawlers** | Schema discovery for raw and cleaned zones |
| | **Glue Jobs** | Transform JSON → clean partitioned Parquet |
| | **Glue Workflows** | Manage & orchestrate ETL job dependencies |
| | **Redshift (RAW)** | Store raw copied records from cleaned S3 |
| | **Amazon CloudWatch** | Monitor Glue job executions, Lambda errors, timeout alerts, centralized logs |
| | **Redshift Fact Tables** | Aggregated reporting layer for visualization | 
| | **DynamoDB** | Fast lookup for live meter alerts/status |
| | **Aurora** | Store device metadata, onboarding, customer records |
| **Analytics / Visualization** | **Athena** | Serverless, ad-hoc querying over S3 |
| | **QuickSight** | Business Intelligence and KPI dashboards |
| | **Custom Full-Stack App** | Customer-facing live dashboards and API integration |

---

## 🚀 ETL Pipeline Flow (Step-by-Step)

1. **IoT Meters** send JSON data
2. **AWS Lambda** (or Firehose) ingests into **S3 Landing Zone**
3. **Glue Crawler 1** detects raw files → creates metadata tables
4. **Glue Jobs** clean & enrich → write **Parquet** files into S3 Clean Zone
5. **Glue Crawler 2** detects Clean Zone
6. **Redshift** `COPY` command ingests clean data into Raw Tables
7. **Redshift ETL Jobs** transform Raw → Fact Tables
8. **Athena** queries S3 directly if needed
9. **QuickSight** / **Custom App** visualize analytics from Redshift Fact Tables
10. **DynamoDB** stores live device alerts
11. **Aurora** stores device metadata and customer management

---

## 🧱 Why This Stack?

- **Serverless-first:** (Athena, Firehose, Glue, DynamoDB) → No need to manage servers, auto-scaling, pay-as-you-go
- **Scalable storage:** S3 grows endlessly and cheaply → raw, clean, historical data without capacity issues
- **Query Optimization:** Storing data in Parquet format (columnar) drastically reduces read costs and improves performance for both Athena and Redshift Spectrum.
- **Separate OLTP (Aurora/DynamoDB) from OLAP (Redshift/Athena):** 
  - **Aurora/DynamoDB (OLTP):** Handles real-time operations, metadata, transactions (fast reads/writes)
  - **Redshift/Athena (OLAP):** Handles complex analytical queries and aggregations
- **CloudWatch Monitoring:**  Enables proactive alerting → fix failures fast → better SLA for the business.
   - Lambda errors/timeouts (Alert when job fails)
   - Glue job duration, failure alerts (Glue job duration (longer = more expensive), Glue job DPU usage (more DPUs = higher cost), Number of Glue job runs (batch frequency = cost scale))
   - Redshift query performance alarms (Query duration, WLM queue wait time, Query success vs. timeout/failure rate)
- **Custom Full-Stack App for Dashboards:** Faster, dynamic, real-time dashboards customized to business needs.
   - Custom metrics and layouts based on user role, device, customer
   - Live event tracking (like leaks, outages) updating instantly
   - Custom security: Tight control over data access by tenant/customer
   - No licensing cost growth (QuickSight, PowerBI, Tableau per-user licenses can become expensive as users grow)
   - More flexible UX/UI than QuickSight’s limited dashboarding options

---

## 📈 Next Steps (Roadmap)

| Phase | Upgrade Idea | Benefit |
|-------|--------------|---------|
| 1 | Integrate **DBT (Data Build Tool)** into Redshift | Declarative, version-controlled SQL transformations, better modular ETL management |
| 2 | Add dbt Data Quality Tests (e.g., non-null, uniqueness, foreign key integrity) | Ensure trust in Redshift Fact Tables with live validation |
| 3 | Create DBT Docs and auto-generate lineage graphs | Increase transparency of transformations for data engineers and analysts |
| 4 | Integrate CloudWatch dashboards | Real-time Glue job health, Lambda error rates, Redshift query performance monitoring |
| 5 | Build a live health dashboard (via QuickSight or Custom App) | Share live data pipeline health metrics (data lag, errors, missing partitions) with stakeholders |
| 6 | (Future) Evaluate Snowflake or Redshift RA3 scaling | Handle petabyte-scale growth beyond Redshift if needed |

---

