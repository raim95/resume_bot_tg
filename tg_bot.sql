BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `tg_bot` (
	`id`	INTEGER,
	`file_id`	TEXT,
	`right_answer`	TEXT,
	`wrong_answer`	TEXT
);
INSERT INTO `tg_bot` VALUES (2,'AgADAgADM6oxGzKuOEqIliBpcrhxEmTotw4ABMz1bUytvqsjxBIGAAEC','2_pic','1_pic, 3_pic, 4_pic');
INSERT INTO `tg_bot` VALUES (3,'AgADAgADNKoxGzKuOEoM-P_qhDHSnYR5Xw8ABIMybRi96M09hBYBAAEC','3_pic','1_pic, 2_pic, 4_pic');
INSERT INTO `tg_bot` VALUES (4,'AgADAgADgasxG_-xQEoUWQn0UKKw4p36tw4ABNukZewAAdvcc64KBgABAg','4_pic','1_pic, 2_pic, 3_pic');
INSERT INTO `tg_bot` VALUES (1,'AgADAgADQ6oxGzMeOUpJm5BEf3GTX0FFXw8ABOS27OpWmS0jWxUBAAEC','1_pic','2_pix, 3_pic, 4_pic');
COMMIT;
