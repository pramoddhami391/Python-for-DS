#revision
#we have list in our value
import matplotlib.pyplot as plt
class DataSample:
    def __init__(self,name,value):
        self.name=name
        self.value=value

    def display(self):
        print(f"Sample name:{self.name}")
        print(f"DataSample:{self.value}")

    def summary(self):
        max_value=max(self.value)
        mean_value=sum(self.value)/len(self.value)
        variance=sum((x-mean_value)**2 for x in self.value)/(len(self.value)-1)
        print("Summary:")
        return {
            "mean":sum(self.value)/len(self.value),
            "max":max_value,
            "min":min(self.value),
            "range":max(self.value)-min(self.value),
            "variance":variance,#sample variance (bessel's correction)
            "SD":variance**0.5
        }
    def normalize(self):#in the range of 0-1
        max_value=max(self.value)

        self.value=[x/max_value for x in self.value]
        return self.value
    
    def ploting(self):
        plt.plot(self.value,marker='o')
        plt.title(self.name)
        plt.show()

ds=DataSample("Sample1",[1,2,3,4,5])
ds.display()
ds.summary()
ds.normalize()
ds.ploting()
    