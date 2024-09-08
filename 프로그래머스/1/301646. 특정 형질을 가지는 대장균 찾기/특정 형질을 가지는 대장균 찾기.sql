-- 코드를 작성해주세요
SELECT COUNT(*) AS "COUNT"
FROM ECOLI_DATA
-- 비트 연산
-- GENOTYPE & 4 = 4는 GENOTYPE를 2진수로 바꿨을 때 3번째 자리(4)가 1인지 확인하는 연산이라 할 수 있음
WHERE GENOTYPE & 2 = 0 AND
(GENOTYPE & 1 = 1 OR GENOTYPE & 4 = 4)