create database Airport_Company_Database
go
use Airport_Company_Database
go

CREATE TABLE Country(
Country_Id INT PRIMARY KEY IDENTITY,
Name VARCHAR(50))

CREATE TABLE Airport(
Airport_Id INT PRIMARY KEY IDENTITY,
Country_Id INT FOREIGN KEY REFERENCES Country(Country_Id),
City VARCHAR(50),
Name VARCHAR(50))

CREATE TABLE Gate(
Gate_Id INT PRIMARY KEY IDENTITY,
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Status VARCHAR(50))

CREATE TABLE Runway(
Runway_Id INT PRIMARY KEY IDENTITY,
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Track INT)

CREATE TABLE Airline_Company(
Airline_Company_Id INT PRIMARY KEY IDENTITY,
Number_of_Aircrafts INT,
Name VARCHAR(50))

CREATE TABLE Airport_Companies(
Airport_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Airline_Company_Id INT FOREIGN KEY REFERENCES Airline_Company(Airline_Company_Id),
CONSTRAINT pk_Airport_Companies PRIMARY KEY (Airport_Id, Airline_Company_Id))

CREATE TABLE Aircraft(
Aircraft_Id INT PRIMARY KEY IDENTITY,
Country_Id INT FOREIGN KEY REFERENCES Airport(Airport_Id),
Airline_Company_Id INT FOREIGN KEY REFERENCES Airline_Company(Airline_Company_Id),
Model VARCHAR(50),
Capacity INT)

CREATE TABLE Flight(
Flight_Id INT PRIMARY KEY IDENTITY,
Aircraft_Id INT FOREIGN KEY REFERENCES Aircraft(Aircraft_Id))

CREATE TABLE Crew(
Crew_Id INT FOREIGN KEY REFERENCES Flight(Flight_Id),
Number_of_People INT,
CONSTRAINT pk_FlightCrew PRIMARY KEY(Crew_Id))

CREATE TABLE Pilot(
Pilot_Id INT PRIMARY KEY IDENTITY,
Crew_Id INT FOREIGN KEY REFERENCES Crew(Crew_Id),
Name VARCHAR(50),
Phone VARCHAR(50))

CREATE TABLE Stewardess(
Stewardess_Id INT PRIMARY KEY IDENTITY,
Crew_Id INT FOREIGN KEY REFERENCES Crew(Crew_Id),
Name VARCHAR(50))

CREATE TABLE Booking(
Booking_Id INT PRIMARY KEY IDENTITY,
Flight_Id INT FOREIGN KEY REFERENCES Flight(Flight_Id),
Price INT)

CREATE TABLE Passager(
Passager_Id INT PRIMARY KEY IDENTITY,
Name VARCHAR(50),
Phone VARCHAR(50),
Email VARCHAR(50))

CREATE TABLE Payment(
Booking_Id INT FOREIGN KEY REFERENCES Booking(Booking_id),
Passager_Id INT FOREIGN KEY REFERENCES Passager(Passager_Id),
Payment_Status VARCHAR(50),
constraint pk_Payment PRIMARY KEY (Booking_Id,Passager_Id))
