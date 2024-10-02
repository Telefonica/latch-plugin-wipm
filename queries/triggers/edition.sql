CREATE DEFINER=`$wordpress_user`@`%` TRIGGER IF NOT EXISTS $trigger_name
BEFORE $action ON $wordpress_db.wp_posts
FOR EACH ROW
BEGIN
    DECLARE latch_readonly ENUM('on', 'off');
    DECLARE latch_edition ENUM('on', 'off');

    SELECT latch INTO latch_readonly FROM latch.latch WHERE operation_name = 'ReadOnly';
    SELECT latch INTO latch_edition FROM latch.latch WHERE operation_name = 'Edition';
    
    IF latch_readonly = 'off' OR latch_edition = 'off' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'latch';
    END IF;
END;