class Locator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = (self.height // 16, self.height // 16)
        self.n_vertical = 16
        self.n_horizontal = self.width // self.block_size[0]
        self.shift_horizontal = (self.width - self.n_horizontal * self.block_size[0]) // 2
        self.shift_vertical = (self.height - self.n_vertical * self.block_size[1]) // 2
