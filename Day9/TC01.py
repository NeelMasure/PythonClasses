from Day9.BaseClass import Base

class TestCase01(Base):

    def tc001(self):
        print("tc001")
        self.click(self,"Search")
        self.scroll(self,"End")


t=TestCase01
t.tc001()




