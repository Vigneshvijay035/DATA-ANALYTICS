create database Customer_Anayytics_DB
use Customer_Anayytics_DB

CREATE TABLE Customer_Transactions (
	Transaction_ID INT PRIMARY KEY,
	Customer_ID INT,
	Product_Category VARCHAR(2555),
	Purchase_Amount DECIMAL(10,2),
	Transaction_Date DATE,
	Payment_Method VARCHAR(50)
);

INSERT INTO Customer_Transactions VALUES
(1, 101, 'Electronics', 15000.00, '2024-03-01', 'Credit Card'),
(2, 102, 'Clothing', 2500.00, '2024-03-02', 'UPI'),
(3, 103, 'Groceries', 1500.00, '2024-03-05', 'Cash'),
(4, 101, 'Home Appliances', 5500.00, '2024-03-07', 'Debit Card'),
(5, 104, 'Electronics', 22000.00, '2024-03-10', 'Credit Card');

select * from Customer_Transactions