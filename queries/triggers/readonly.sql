CREATE DEFINER=`$wordpress_user`@`%` TRIGGER IF NOT EXISTS $trigger_name
BEFORE $action ON $wordpress_db.wp_comments
FOR EACH ROW
BEGIN
    DECLARE latch_readonly ENUM('on', 'off');
    
    SELECT latch INTO latch_readonly FROM latch.latch WHERE operation_name = 'ReadOnly';
    
    IF latch_readonly = 'off' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'latch';
    END IF;
END;