-- Encryption
UPDATE Patient SET
    name = AES_ENCRYPT(name, 'secret_key'),
    age = AES_ENCRYPT(CAST(age AS CHAR), 'secret_key'),
    gender = AES_ENCRYPT(gender, 'secret_key'),
    phone = AES_ENCRYPT(phone, 'secret_key'),
    diagnosis = AES_ENCRYPT(diagnosis, 'secret_key');

-- Decryption
SELECT
    patient_id,
    CAST(AES_DECRYPT(name, 'secret_key') AS CHAR(255) CHARACTER SET utf8) AS name,
    CAST(AES_DECRYPT(age, 'secret_key') AS CHAR) AS age,
    CAST(AES_DECRYPT(gender, 'secret_key') AS CHAR(10) CHARACTER SET utf8) AS gender,
    CAST(AES_DECRYPT(phone, 'secret_key') AS CHAR(15)) AS phone,
    CAST(AES_DECRYPT(diagnosis, 'secret_key') AS CHAR(255) CHARACTER SET utf8) AS diagnosis
FROM Patient;
