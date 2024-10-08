-- 코드를 작성해주세요
SELECT SUM(COALESCE(G.SCORE, 0)) AS "SCORE", G.EMP_NO AS "EMP_NO", E.EMP_NAME AS "EMP_NAME", E.POSITION AS "POSITION", E.EMAIL AS "EMAIL"
FROM HR_EMPLOYEES E
JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
GROUP BY E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
ORDER BY SCORE DESC
LIMIT 1
