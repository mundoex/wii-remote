class WiiAcc():
    def __init__(self, start_v3):
        self.prev_v3=start_v3
        self.cur_v3=start_v3

    def update(self, new_v3):
        self.prev_v3=self.cur_v3
        self.cur_v3=new_v3

    def difference(self):
        return self.cur_v3-self.prev_v3