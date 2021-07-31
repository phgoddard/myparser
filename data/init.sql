CREATE DATABASE cxdata;
ALTER DATABASE cxdata CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use cxdata;

CREATE TABLE fileMetaData (
    study_name VARCHAR(128),
    study_id INT,
    file_name VARCHAR(128),
    file_id INT,
    file_path VARCHAR(128),
    output_filename VARCHAR(128),
    all_text VARCHAR(16000000),
    PRIMARY KEY (file_id)
);

CREATE TABLE dialog (
    file_id INT,
    line_number INT,
    line_text text (65535),
    clean_nlnum text (65535),
    clean_timestamp text (65535),
    speaker_name text (128),
    PRIMARY KEY (file_id)
);

