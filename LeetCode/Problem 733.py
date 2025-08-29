from copy import deepcopy

class Solution:

    def solve(self, image, color, intial_color, r, c):
        if r == len(image) or r < 0 or c == len(image[0]) or c < 0:
            return 
        if image[r][c] != intial_color:
            return
        image[r][c] = color
        self.solve(image, color, intial_color, r+1, c)
        self.solve(image, color, intial_color, r-1, c)
        self.solve(image, color, intial_color, r, c+1)
        self.solve(image, color, intial_color, r, c-1)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        intial_color = image[sr][sc]
        image_cpy = deepcopy(image)
        self.solve(image_cpy, color, intial_color, sr, sc)
        return image_cpy

        