-- V1_queens.sql
CREATE TABLE queens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    number_queens INT NOT NULL,
    solutions TEXT[] NOT NULL,
    created_by VARCHAR(150) NOT NULL,
    updated_by VARCHAR(150),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);