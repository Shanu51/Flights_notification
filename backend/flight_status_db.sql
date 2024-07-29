-- Create the database
CREATE DATABASE flight_status;

-- Connect to the database
\c flight_status;

-- Create the flight_status table
CREATE TABLE flight_status (
    flight_id VARCHAR(10) PRIMARY KEY,
    airline VARCHAR(50),
    status VARCHAR(20),
    departure_gate VARCHAR(10),
    arrival_gate VARCHAR(10),
    scheduled_departure TIMESTAMP,
    scheduled_arrival TIMESTAMP,
    actual_departure TIMESTAMP,
    actual_arrival TIMESTAMP
);

-- Create the notifications table
CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    flight_id VARCHAR(10) REFERENCES flights(flight_id),
    message TEXT,
    timestamp TIMESTAMP,
    method VARCHAR(10),
    recipient VARCHAR(50)
);

-- Create a log table
CREATE TABLE change_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(255),
    operation VARCHAR(10),
    old_data TEXT,
    new_data TEXT,
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger on your target table (e.g., 'your_table')
DELIMITER //

CREATE TRIGGER flight_status
AFTER UPDATE ON flight_status
FOR EACH ROW
BEGIN
    INSERT INTO change_log (table_name, operation, old_data, new_data)
    VALUES ('your_table', 'UPDATE', OLD.data, NEW.data);
END //

DELIMITER ;
