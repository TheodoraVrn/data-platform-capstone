SELECT
    GROUPING(c.country) grouping_country,
    GROUPING(cat.category) grouping_category,
    c.country,
    cat.category,
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimCountry" c ON f.countryid = c.countryid
JOIN "DimCategory" cat ON f.categoryid = cat.categoryid
GROUP BY GROUPING SETS (
    (c.country, cat.category),
    (c.country),
    (cat.category),
    ()
);


SELECT
    d."Year",
    c.country,
    AVG(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY ROLLUP (d."Year", c.country)
ORDER BY d."Year", c.country;


SELECT
    d."Year",
    c.country,
    AVG(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY CUBE (d."Year", c.country)
ORDER BY d."Year", c.country;


CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT
    c.country,
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimCountry" c ON f.countryid = c.countryid
GROUP BY c.country;
