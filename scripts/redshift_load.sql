COPY customer_transactions
FROM 's3://your-bucket/output/'
IAM_ROLE 'arn:aws:iam::your-account-id:role/RedshiftCopyRole'
FORMAT AS CSV
IGNOREHEADER 1;
