from CareTaker.configuration_care_taker import ConfigurationCareTaker
from Momento.configuration_momento import ConfigurationMomento
from Originator.configuration_originator import ConfigurationOriginator

class ConfigurationHandler:

    def manage_configuration(self):
        care_taker: ConfigurationCareTaker = ConfigurationCareTaker()
        originator: ConfigurationOriginator = ConfigurationOriginator(height=10, width=20)
        print(f"Height: {originator.height}, Width: {originator.width}")
        
        # snapshot 1
        snapshot: ConfigurationMomento = originator.create_momento()
        care_taker.add_momento(snapshot)
 
        # changing state of object
        originator.set_height(20)
        originator.set_width(30)
        print(f"Height: {originator.height}, Width: {originator.width}")

        # snapshot 2
        snapshot: ConfigurationMomento = originator.create_momento()
        care_taker.add_momento(snapshot)

        # changing state of object
        originator.set_height(30)
        originator.set_width(40)
        print(f"Height: {originator.height}, Width: {originator.width}")

        # oops, something went wrong
        # restore from histore
        snapshot: ConfigurationMomento = care_taker.undo()
        originator.restore_momento(snapshot)
        print("Restore...")
        print(f"Height: {originator.height}, Width: {originator.width}")


ConfigurationHandler().manage_configuration()




