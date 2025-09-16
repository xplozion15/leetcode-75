class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i = 0

        while n != 0 and i < len(flowerbed):
            if i == 0:
                if flowerbed[i] == 0 and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                ):
                    flowerbed[i] = 1
                    n -= 1
                    i += 1
                else:
                    i += 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 1
                else:
                    i += 1

            elif i != 0:
                if (
                    flowerbed[i] == 0
                    and flowerbed[i + 1] == 0
                    and flowerbed[i - 1] == 0
                ):
                    flowerbed[i] = 1
                    n -= 1
                    i += 1
                else:
                    i += 1
        if n == 0:
            return True
        else:
            return False