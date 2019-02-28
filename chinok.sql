--Use your query to return the email, first name, last name, and Genre of all Rock Music listeners.
SELECT c.Email,c.FirstName,c.LastName, g.Name AS Genre 
FROM customers c, invoices i, invoice_items it, tracks t, genres g
WHERE c.CustomerId = i.CustomerId AND i.InvoiceId = it.InvoiceId
AND it.TrackId = t.TrackId AND t.GenreId = g.GenreId
AND Genre = "Rock"
GROUP BY c.FirstName, c.LastName
ORDER BY c.Email 


--Write a query that returns the Artist name and total track count of the top 10 rock bands.*\
SELECT a.name AS ArtistName, COUNT(t.TrackId) AS TotalTracks
FROM artists a, albums ab, tracks t, genres g
WHERE a.ArtistId = ab.ArtistId AND ab.AlbumId = t.AlbumId
AND t.GenreId = g.GenreId AND g.Name = 'Rock'
GROUP BY ArtistName 
ORDER BY TotalTracks DESC 
LIMIT 10
