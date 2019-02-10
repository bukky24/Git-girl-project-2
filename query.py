/* query to determine the countries that have the most invoices*/

SELECT BillingCountry, count(*) as Invoices
FROM invoices
GROUP BY BillingCountry
ORDER BY Invoices DESC


/*query that shows the city with the best customer*/

SELECT BillingCity as City, sum(Total) as InvoiceTotals
FROM Invoices
GROUP BY BillingCity
ORDER BY InvoiceTotals desc
LIMIT 1



/*query that shows the best customer*/
SELECT  upper(LastName) || ' ' || FirstName as FullName, sum(i.Total) as TotalSpent
FROM Customers c, Invoices i
WHERE c.CustomerId=i.CustomerId
GROUP BY (i.CustomerId)
ORDER BY TotalSpent desc
LIMIT 1
