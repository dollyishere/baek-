-- 코드를 입력하세요
SELECT COUNT (*) AS USERS FROM USER_INFO
WHERE 20 <= AGE && AGE <= 29 && DATE_FORMAT(JOINED, '%Y') = '2021'