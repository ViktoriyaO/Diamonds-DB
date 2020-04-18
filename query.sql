--����� 1.������� ������� �� �������� ������� �������, �� ������� �� ���.

SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC;

--����� 2. ������� ���� �� % ������� � ����� �������� ����� ������� ��� �������.

SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count; 
       
--����� 3. ������� ��������� ��������� ������� �� ������� �������, � ����� ���������.

SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC;

