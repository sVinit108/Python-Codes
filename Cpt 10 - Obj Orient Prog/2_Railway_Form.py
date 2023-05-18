class RailwayForm:
    formType='Railway Form'
    def printData(self):
        print(f'Name: {self.name}')
        print(f'Train: {self.train}')
vinitApplication = RailwayForm()
vinitApplication.name=' Vinit'
vinitApplication.train='Rajdhani Express'
vinitApplication.printData()

vivaanApplication = RailwayForm()
vivaanApplication.name=' Vivaan'
vivaanApplication.train='Rajdhani Express'
vivaanApplication.printData()