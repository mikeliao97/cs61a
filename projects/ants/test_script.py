from ant import ant
colony.food = 0
bodyguard0 = BodyguardAnt()
harvester0 = HarvesterAnt()
place0 = colony.place["tunnel_0_0"]
place0.add_insect(bodyguard0)
place0.add_insect(harvester0)
place0.ant is bodyguard0
