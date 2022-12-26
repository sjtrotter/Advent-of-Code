#!/usr/bin/env python

inputfile = open("input2.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())


class Robot():
    def __init__(self, parent, botType="ore"):
        if botType == "ore":
            parent.spendOre(parent.ore_cost)
        if botType == "clay":
            parent.spendOre(parent.clay_cost)
        if botType == "obsidian":
            parent.spendOre(parent.obsidian_ore_cost)
            parent.spendClay(parent.obsidian_clay_cost)
        if botType == "geode":
            parent.spendOre(parent.geode_ore_cost)
            parent.spendObsidian(parent.geode_obsidian_cost)

        self.botType = botType
        self.parent = parent

    def operate(self):
        self.parent.mine(self.botType)


class Blueprint():
    def __init__(self, id, ore_cost, clay_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost):
        self.id = id
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_ore_cost = obsidian_ore_cost
        self.obsidian_clay_cost = obsidian_clay_cost
        self.geode_ore_cost = geode_ore_cost
        self.geode_obsidian_cost = geode_obsidian_cost
        self.ore = self.ore_cost
        self.clay = 0
        self.obsidian = 0
        self.geodes = 0
        self.geodeBots = []
        self.clayBots = []
        self.obsidianBots = []
        self.oreBots = []
        self.oreBots.append(Robot(self,botType="ore"))
        self.bots = self.oreBots
        self.botQueue = []
        self.botType = "clay"


    def shouldBuildOre(self):
        if self.ore > int(max([self.clay_cost,self.obsidian_ore_cost,self.geode_ore_cost]) * 0.64):
            return False
        else:
            return True

    def shouldBuildClay(self):
        if self.clay > int(self.obsidian_clay_cost * 0.64):
            return False
        else:
            return True

    def shouldBuildObsidian(self):
        if self.obsidian > int(self.geode_obsidian_cost * 0.5):
            return False
        else:
            return True

    def shouldBuildGeode(self):
        return True

    def makeBot(self):
        if self.obsidian >= self.geode_obsidian_cost and self.ore >= self.geode_ore_cost \
            and self.shouldBuildGeode():
            self.geodeBots.append(Robot(self,botType="geode"))
            return self.geodeBots[-1]
        if self.clay >= self.obsidian_clay_cost and self.ore >= self.obsidian_ore_cost \
            and self.shouldBuildObsidian():
            self.obsidianBots.append(Robot(self,botType="obsidian"))
            return self.obsidianBots[-1]
        if self.ore >= self.clay_cost and self.shouldBuildClay():
            self.clayBots.append(Robot(self,botType="clay"))
            return self.clayBots[-1]
        if self.ore >= self.ore_cost and self.shouldBuildOre():
            self.oreBots.append(Robot(self,botType="ore"))
            return self.oreBots[-1]

        # if self.ore >= self.ore_cost:
        #     self.botQueue.append(Robot(self,botType="ore"))

    def mine(self, botType):
        if botType == "ore":
            self.ore += 1
        if botType == "clay":
            self.clay += 1
        if botType == "obsidian":
            self.obsidian += 1
        if botType == "geode":
            self.geodes += 1

    def operate(self):
        
        newBot = self.makeBot()

        for bot in self.bots:
            bot.operate()

        if newBot != None:
                self.bots.append(bot)


    def spendOre(self, ores):
        self.ore -= ores

    def spendClay(self, clays):
        self.clay -= clays

    def spendObsidian(self, obsidians):
        self.obsidian -= obsidians

    def getQualityLevel(self):
        return self.geodes * self.id


blueprints = {}
for line in data_list:
    bp,dt = line.split(":")
    ore,clay,obsidian,geode = dt.split(".")[0:4]
    id = int(bp.split(" ")[-1])
    oreCost = int(ore.split(" ")[-2])
    clayCost = int(clay.split(" ")[-2])
    obsOreCost = int(obsidian.split(" ")[-5])
    obsClayCost = int(obsidian.split(" ")[-2])
    geoOreCost = int(geode.split(" ")[-5])
    geoObsCost = int(geode.split(" ")[-2])

    blueprints[id] = Blueprint(id,oreCost,clayCost,obsOreCost,obsClayCost,geoOreCost,geoObsCost)

# blueprints[blueprint] = Blueprint(1,4,2,3,14,2,7)

for blueprint in blueprints.keys():

    for i in range(1,25):
        # print("Minute:", i)
        blueprints[blueprint].operate()

    print("id:",blueprints[blueprint].id,", ores:",blueprints[blueprint].ore,", clay:",blueprints[blueprint].clay,", obsidian:",blueprints[blueprint].obsidian,", geodes:",blueprints[blueprint].geodes,", Quality:",blueprints[blueprint].getQualityLevel())
    string = "bots: "

    for bot in blueprints[blueprint].bots:
        string += str(bot.botType) + " "

    print(string)