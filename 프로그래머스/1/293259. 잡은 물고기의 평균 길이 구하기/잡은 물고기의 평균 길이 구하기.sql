-- 코드를 작성해주세요
SELECT ROUND(AVG(COALESCE(LENGTH, 10)), 2) AS "AVERAGE_LENGTH"
FROM FISH_INFO

