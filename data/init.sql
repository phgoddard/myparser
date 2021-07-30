CREATE DATABASE cxdata;
ALTER DATABASE cxdata CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use cxdata;

CREATE TABLE dialog (
    id INT NOT NULL AUTO_INCREMENT,
    form NVARCHAR(30), /* citation form in the vocab list, sans root symbol for verbs */
    pos VARCHAR(30), /* part of speech */
    definition NVARCHAR(255),
    verb_class VARCHAR(10),
    verb_surface NVARCHAR(30),
    preverb NVARCHAR(30), /* for verbs where additional preverb has unpredictable meaning, e.g. ava-gam */
    noun_gender VARCHAR(30),
    noun_declension NVARCHAR(10),
    chapter INT,
    PRIMARY KEY (id)
);

INSERT INTO lexicon
    (form, pos, definition, verb_class, verb_surface, preverb, noun_gender, noun_declension, chapter)
VALUES
/* Chapter 3 */
    (N'ca', 'indeclinable', N'and (postposed)', NULL, NULL, NULL, NULL, NULL, 3),
    (N'vā', 'indeclinable', N'or (postposed)', NULL, NULL, NULL, NULL, NULL, 3),
    (N'tu', 'indeclinable', N'but (postposed)', NULL, NULL, NULL, NULL, NULL, 3),
