BEGIN;
CREATE TABLE `webservice_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `name` varchar(50) NOT NULL
)
;
CREATE TABLE `webservice_account_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `account_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`account_id`, `tag_id`)
)
;
ALTER TABLE `webservice_account_tag` ADD CONSTRAINT `tag_id_refs_id_97305488` FOREIGN KEY (`tag_id`) REFERENCES `webservice_tag` (`id`);
CREATE TABLE `webservice_account` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `code` varchar(50) NOT NULL,
    `description` longtext NOT NULL,
    `is_container` bool NOT NULL,
    `is_root` bool NOT NULL,
    `name` varchar(100) NOT NULL,
    `notes` longtext NOT NULL,
    `parent_id` integer,
    `type` smallint UNSIGNED NOT NULL
)
;
ALTER TABLE `webservice_account_tag` ADD CONSTRAINT `account_id_refs_id_495e90a7` FOREIGN KEY (`account_id`) REFERENCES `webservice_account` (`id`);
ALTER TABLE `webservice_account` ADD CONSTRAINT `parent_id_refs_id_e900f480` FOREIGN KEY (`parent_id`) REFERENCES `webservice_account` (`id`);
CREATE TABLE `webservice_transaction_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `transaction_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`transaction_id`, `tag_id`)
)
;
ALTER TABLE `webservice_transaction_tag` ADD CONSTRAINT `tag_id_refs_id_f813e214` FOREIGN KEY (`tag_id`) REFERENCES `webservice_tag` (`id`);
CREATE TABLE `webservice_transaction` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `date` date NOT NULL,
    `number` varchar(50) NOT NULL,
    `text` varchar(200) NOT NULL,
    `time` time
)
;
ALTER TABLE `webservice_transaction_tag` ADD CONSTRAINT `transaction_id_refs_id_6f78806c` FOREIGN KEY (`transaction_id`) REFERENCES `webservice_transaction` (`id`);
CREATE TABLE `webservice_split` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `account_id` integer NOT NULL,
    `amount` numeric(20, 2) NOT NULL,
    `reconciliation_state` varchar(1) NOT NULL,
    `text` varchar(200) NOT NULL,
    `transaction_id` integer NOT NULL
)
;
ALTER TABLE `webservice_split` ADD CONSTRAINT `transaction_id_refs_id_4684a512` FOREIGN KEY (`transaction_id`) REFERENCES `webservice_transaction` (`id`);
ALTER TABLE `webservice_split` ADD CONSTRAINT `account_id_refs_id_a4017bab` FOREIGN KEY (`account_id`) REFERENCES `webservice_account` (`id`);
CREATE TABLE `webservice_device_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`device_id`, `tag_id`)
)
;
ALTER TABLE `webservice_device_tag` ADD CONSTRAINT `tag_id_refs_id_cde0546d` FOREIGN KEY (`tag_id`) REFERENCES `webservice_tag` (`id`);
CREATE TABLE `webservice_device` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `brand` varchar(100) NOT NULL,
    `build_id` varchar(100) NOT NULL,
    `description` longtext NOT NULL,
    `last_active` datetime NOT NULL,
    `model` varchar(100) NOT NULL,
    `name` varchar(50) NOT NULL,
    `serial` varchar(100) NOT NULL
)
;
ALTER TABLE `webservice_device_tag` ADD CONSTRAINT `device_id_refs_id_d8521032` FOREIGN KEY (`device_id`) REFERENCES `webservice_device` (`id`);
CREATE TABLE `webservice_invoicescan` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `image` varchar(100) NOT NULL
)
;
CREATE TABLE `webservice_location` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `owner_id` integer NOT NULL,
    `accuracy` double precision NOT NULL,
    `altitude` double precision NOT NULL,
    `bearing` double precision NOT NULL,
    `latitude` double precision NOT NULL,
    `longitude` double precision NOT NULL,
    `speed` double precision NOT NULL
)
;
CREATE INDEX `webservice_tag_cb902d83` ON `webservice_tag` (`owner_id`);
CREATE INDEX `webservice_account_tag_93025c2f` ON `webservice_account_tag` (`account_id`);
CREATE INDEX `webservice_account_tag_5659cca2` ON `webservice_account_tag` (`tag_id`);
CREATE INDEX `webservice_account_cb902d83` ON `webservice_account` (`owner_id`);
CREATE INDEX `webservice_account_410d0aac` ON `webservice_account` (`parent_id`);
CREATE INDEX `webservice_transaction_tag_0f45431a` ON `webservice_transaction_tag` (`transaction_id`);
CREATE INDEX `webservice_transaction_tag_5659cca2` ON `webservice_transaction_tag` (`tag_id`);
CREATE INDEX `webservice_transaction_cb902d83` ON `webservice_transaction` (`owner_id`);
CREATE INDEX `webservice_split_cb902d83` ON `webservice_split` (`owner_id`);
CREATE INDEX `webservice_split_93025c2f` ON `webservice_split` (`account_id`);
CREATE INDEX `webservice_split_0f45431a` ON `webservice_split` (`transaction_id`);
CREATE INDEX `webservice_device_tag_b6860804` ON `webservice_device_tag` (`device_id`);
CREATE INDEX `webservice_device_tag_5659cca2` ON `webservice_device_tag` (`tag_id`);
CREATE INDEX `webservice_device_cb902d83` ON `webservice_device` (`owner_id`);
CREATE INDEX `webservice_invoicescan_cb902d83` ON `webservice_invoicescan` (`owner_id`);
CREATE INDEX `webservice_location_cb902d83` ON `webservice_location` (`owner_id`);

COMMIT;
