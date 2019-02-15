/*What is the total spending (revenue) for each country? */

select BillingCountry as Country, sum(Total) as Revenue
from invoices 
group by BillingCountry
order by Revenue desc


/*What is the most prefered Media-type? */

SELECT m.Name as MediaTypeName,m.MediaTypeId, SUM(it.Quantity*it.UnitPrice) as Sales
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
