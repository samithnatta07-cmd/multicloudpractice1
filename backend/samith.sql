CREATE DATABASE portfolio;
USE portfolio;

CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE certifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150)
);

INSERT INTO skills (name) VALUES
('CCNA'),
('Linux'),
('AWS'),
('VPC'),
('Route 53'),
('Application Load Balancer (ALB)'),
('S3'),
('Lambda'),
('RDS'),
('SNS'),
('CloudWatch'),
('CloudFront'),
('Grafana'),
('Prometheus');



INSERT INTO certifications (name) VALUES
('Oracle Cloud Associate'),
('Aviatrix Multicloud Network Associate');
