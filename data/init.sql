CREATE DATABASE cxdata;
ALTER DATABASE cxdata CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use cxdata;

CREATE TABLE study (
    studyname VARCHAR(128),
    study_id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (study_id)
);

CREATE TABLE file
(   file_name VARCHAR(128),
    file_id int not null auto_increment,
    file_path VARCHAR(128),
    study_id int,
    all_text text(16000000),
    PRIMARY KEY (file_id),
    FOREIGN KEY (study_id) REFERENCES study(study_id)
);

CREATE TABLE dialog (
    file_id int NOT NULL,
    line_number int NOT NULL,
    speaker_name text (128),
    clean_timestamp text (65535),
    output_filename VARCHAR(128),
    FOREIGN KEY (file_id) REFERENCES file(file_id)
);