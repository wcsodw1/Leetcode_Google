# Write your MySQL query statement below
SELECT tb1.Score AS Score, (SELECT count(distinct tb2.Score)
                            FROM Scores AS tb2
                            WHERE tb2.Score >= tb1.Score ) AS "Rank"
FROM Scores AS tb1
ORDER BY tb1.Score DESC; 



'''
# DESC 是descend 降序意思, asc 是ascend 升序的意思

Expected
| score | rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.5   | 4    |
'''

-- SELECT class, count (class) AS number 
-- FROM Courses 
-- GROUP BY class
-- HAVING count (class) > 5;





