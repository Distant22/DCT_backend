GRANT ALL PRIVILEGES ON DCT.* TO 'dct_user'@'%' IDENTIFIED BY 'dct_secret';

CREATE TABLE `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `imageType` INT NOT NULL
);