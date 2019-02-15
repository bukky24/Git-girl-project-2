/*What is the total spending (revenue) for each country? */

SELECT BillingCountry as Country, SUM(Total) as Revenue
FROM invoices 
GROUP BY BillingCountry
ORDER BY Revenue DESC


/*What is the most prefered Media-type? */

SELECT m.Name as MediaTypeName,m.MediaTypeId,COUNT(t.MediaTypeId) as Num, SUM(it.Quantity*it.UnitPrice) as Sales
FROM media_types m
JOIN Tracks t
ON m.MediaTypeId = t.MediaTypeId
JOIN invoice_items it
ON t.TrackId = it.TrackId
JOIN Invoices i
ON it.InvoiceId = i.InvoiceId
GROUP BY MediaTypeName
ORDER BY Sales DESC
LIMIT 1


