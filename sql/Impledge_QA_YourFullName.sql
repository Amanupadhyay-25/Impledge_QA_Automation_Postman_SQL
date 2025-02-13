-- Update queries before running SELECT queries
UPDATE Admissions SET attending_doctor_id = 29 WHERE attending_doctor_id = 3;
UPDATE Admissions SET patient_id = 4 WHERE patient_id = 35;

-- 1. Get doctors with admissions
SELECT DISTINCT d.* FROM Doctors d
JOIN Admissions a ON d.doctor_id = a.attending_doctor_id;

-- 2. Get doctors without admissions
SELECT * FROM Doctors
WHERE doctor_id NOT IN (SELECT attending_doctor_id FROM Admissions);

-- 3. Get patients with incomplete admissions due to missing doctor details
SELECT * FROM Patients
WHERE patient_id IN (SELECT patient_id FROM Admissions WHERE attending_doctor_id IS NULL);
