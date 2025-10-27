COPY raw_data.gap
FROM 's3://gap-dashboard-data/raw-data/gap.csv'                      -- s3 주소
IAM_ROLE 'arn:aws:iam::956403430996:role/redshift-s3-access-role'    -- IAM ROLE arn
CSV
IGNOREHEADER 1
DELIMITER ','
DATEFORMAT 'auto';
