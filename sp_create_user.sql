--this is for api.py

DELIMITER $$
CREATE PROCEDURE `sp_create_user`(
IN p_email varchar(80),
IN p_username varchar(45),
IN p_password varchar(45)
)
BEGIN
IF ( select exists (select 1 from user where username = p_username) ) THEN
    select 'Username Exists !!';
ELSE
insert into user (
    email,
    username,
    password
) values (
    p_email,
    p_username,
    p_password
);
END IF;
END$$
DELIMITER ;

-- and this is for api2.py's mysql procedure

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
IN p_name VARCHAR(20),
N p_username VARCHAR(20),
IN p_password VARCHAR(20)
BEGIN
  if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
  
      select 'Username Exists !!';
   
  ELSE
   
      insert into tbl_user
      (
          user_name,
          user_username,
          user_password
      )
      values
      (
          p_name,
          p_username,
          p_password
      );
   
  END IF;
END$$
DELIMITER ;