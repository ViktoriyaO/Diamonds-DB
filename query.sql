--Запит 1.Âèâåñòè êàòåãîð³¿ òà çàãàëüíó ê³ëüê³ñòü ä³àìàíò³â, ÿê³ âõîäÿòü äî íèõ.

SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC;

--Çàïèò 2. Âèâåñòè êîë³ð òà % ä³àìàíò³â ç òàêèì êîëüîðîì ñåðåä ä³àìàíò³â óñ³õ êîëüîð³â.

SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count; 
       
--Çàïèò 3. Äèíàì³êà çàëåæíîñò³ ïðîçîðîñò³ ä³àìàíòó â³ä ê³ëüêîñò³ ä³àìàíò³â, ç òàêîþ ïðîçîð³ñòþ.

SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC;

