DROP TABLE IF EXISTS `clinicOpening`;

DROP TABLE IF EXISTS `clinic`;
CREATE TABLE IF NOT EXISTS `clinic` (
  `clinicName` varchar(100) NOT NULL,
  `doctorName` varchar(100) NOT NULL,
  `groupedLocation` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `postalCode` int(6) NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `contactNumber` varchar(15) NOT NULL,
  PRIMARY KEY (`clinicName`, `doctorName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `clinicOpening` (
  `clinicName` varchar(100) NOT NULL,
  `openingDays` varchar(20) NOT NULL,
  `openingHour` varchar(10) NOT NULL,
  `closingHour` varchar(10) NOT NULL,
  PRIMARY KEY (`clinicName`, `openingDays`, `openingHour`),
  FOREIGN KEY (`clinicName`) REFERENCES `clinic`(`clinicName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;