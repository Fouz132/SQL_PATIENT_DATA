CREATE TABLE Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    aadhar VARCHAR(20) UNIQUE
);
