-- 코드를 입력하세요
SELECT * 
    FROM FOOD_PRODUCT
    WHERE PRICE = (
                    SELECT MAX(PRICE) AS PRICE
                        FROM FOOD_PRODUCT
                )