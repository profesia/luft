-- Delete all records before loading to prevent duplicities
DELETE FROM {{ STAGE_SCHEMA }}.{{ TABLE_NAME }} WHERE {{ TIMESTAMP_COLUMN }}BETWEEN timestamp('{{ DATE_VALID }} 00:00:00') AND timestamp('{{ DATE_VALID }} 23:59:59');
