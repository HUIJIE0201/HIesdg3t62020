DROP DATABASE IF EXISTS Insurance_Claim;
CREATE DATABASE Insurance_Claim;

USE Insurance_Claim;

DROP TABLE IF EXISTS  insurance_claim;
CREATE TABLE insurance_claim(

    PatientID int,
    ClinicID int,
    ClaimID int PRIMARY KEY,
    ClaimDate DATE,
    Medicine text,
    BillAmount FLOAT,
    ClaimedAmount FLOAT,
    ClaimStatus VARCHAR(255),
    RefundStatus VARCHAR(255)
);



