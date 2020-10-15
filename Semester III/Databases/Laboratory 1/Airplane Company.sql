create database Airport_Company
go
use Airport_Company
go

CREATE TABLE Country(
Country_Id INT PRIMARY KEY IDENTITY,
Name varchar(50) NOT NULL)

CREATE TABLE Airport(
Airport_Id INT FOREIGN KEY REFERENCES Country(Country_Id),
City varchar(50),
Name varchar(50),
CONSTRAINT pk_CountryAirport PRIMARY KEY(Airport_Id))

CREATE TABLE Gate(
Gate_Id INT PRIMARY KEY IDENTITY,
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Status varchar(50))

CREATE TABLE Runway(
Runway_Id INT PRIMARY KEY IDENTITY,
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Track INT)

CREATE TABLE Aircraft_Company(
Aircraft_Company_Id INT PRIMARY KEY IDENTITY,
Number_of_Aircrafts INT)


CREATE TABLE Aircraft(
Aircraft_Id INT PRIMARY KEY IDENTITY,
Country_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Aircraft_Company_Id INT FOREIGN KEY REFERENCES Aircraft_Company(Aircraft_Company_Id),
Model varchar(50),
Capacity INT)


CREATE TABLE Airport_Companies(
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Aircraft_Company_Id INT FOREIGN KEY REFERENCES Aircraft_Company(Aircraft_Company_Id),
CONSTRAINT pk_Airport_Companies PRIMARY KEY (Airport_Id, Aircraft_Company_Id))

CREATE TABLE Pilot(
Pilot_Id INT PRIMARY KEY IDENTITY,
Name varchar(50),
Phone varchar(50))

CREATE TABLE Crew(
Crew_Id INT PRIMARY KEY IDENTITY)

CREATE TABLE Passager(
Passager_Id INT PRIMARY KEY IDENTITY,
Name varchar(50),
Phone varchar(50),
Email varchar(50))

CREATE TABLE Flight(
Flight_Id INT FOREIGN KEY REFERENCES Pilot(Pilot_Id),
Crew_Id INT FOREIGN KEY REFERENCES Crew(Crew_Id),
CONSTRAINT pk_FlightPilot PRIMARY KEY(Flight_Id),
Aircraft_Id INT FOREIGN KEY REFERENCES Aircraft(Aircraft_Id))

CREATE TABLE Booking(
Booking_Id INT PRIMARY KEY IDENTITY,
Flight INT FOREIGN KEY REFERENCES Flight(Flight_Id),
Price INT)

CREATE TABLE Payment(
Booking_Id INT FOREIGN KEY REFERENCES Booking(Booking_id),
Passager_Id INT FOREIGN KEY REFERENCES Passager(Passager_Id),
constraint pk_Payment PRIMARY KEY (Booking_Id,Passager_Id),
Amount INT,
Payment_Status varchar(50))