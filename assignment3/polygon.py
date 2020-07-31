class Polygon:
    def __init__(self,noOfSides):
        self.n=noOfSides
        self.sides=[0 for i in range(noOfSides)]
    def setSides(self):
        self.sides=[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def displaySides(self):
        for i in range(self.n):
            print("Side "+str(i+1)+" is : "+self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def getArea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of triangle is %0.2f" %area)
    
t=Triangle()
t.setSides()
t.getArea()