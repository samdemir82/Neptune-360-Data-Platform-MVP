
CREATE TABLE IF NOT EXISTS raw_meter_readings (
    meter_id VARCHAR(100),
    usage DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fact_meter_usage (
    meter_id VARCHAR(100),
    year INT,
    month INT,
    total_usage DOUBLE PRECISION
);