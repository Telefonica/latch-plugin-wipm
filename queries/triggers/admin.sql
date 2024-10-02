CREATE DEFINER=`$wordpress_user`@`%` TRIGGER IF NOT EXISTS $trigger_name
BEFORE $action ON $wordpress_db.wp_usermeta
FOR EACH ROW
BEGIN
    DECLARE latch_readonly ENUM('on', 'off');
    DECLARE latch_admin ENUM('on', 'off');
    
    SELECT latch INTO latch_readonly FROM latch.latch WHERE operation_name = 'ReadOnly';
    SELECT latch INTO latch_admin FROM latch.latch WHERE operation_name = 'Administration';
    
    IF latch_readonly = 'off' OR ($variable.meta_key = 'session_tokens' AND latch_admin = 'off') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'latch';
    END IF;
END;