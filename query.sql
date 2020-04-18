--Запит 1. Вивести категорії та загальну кількість діамантів, які входять до них.

SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC;

--Запит 2. Вивести колір та % діамантів з таким кольором.

SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count; 
       
--Запит 3. Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість.

SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC;

