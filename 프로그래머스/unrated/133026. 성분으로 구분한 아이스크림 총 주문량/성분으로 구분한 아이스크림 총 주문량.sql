-- 코드를 입력하세요
SELECT A.INGREDIENT_TYPE, SUM(B.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO A, FIRST_HALF B
WHERE A.FLAVOR = B.FLAVOR
GROUP BY A.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC
