from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

uClient = uReq("https://soul-knight.fandom.com/wiki/Weapons_(sorted_by_rarity)")
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "soulknight_weapons.csv"
f = open(filename, "w")

headers = "No., Rarity, Weapon Name\n"
f.write(headers)

all_rarity = page_soup.findAll("tr")
rarity_name = ["Common", "Uncommon", "Rare", "Very Rare", "Epic", "Legendary"]
num = 1

for rarity in range (len(all_rarity)):

	that_rarity = all_rarity[rarity]
	all_unparsed_wpns = that_rarity.findAll("td")[1].findAll("a")

	for unparsed_wpn in range (len(all_unparsed_wpns)):

		f.write("{}, {}, {}\n".format(num, rarity_name[rarity], all_unparsed_wpns[unparsed_wpn].text))
		num+=1

f.close()



# Brute Force Method - Literally Copy/Pasted Text from Site and Formatted using split() function
# Bug Found at Index 112 : "SMG M2 -SMG Helix"
# Code below will not be able to split above string as it doesn't satisfy .split(" - ")
# Hence, resultant CSV file will have one less entry as "SMG M2" and "SMG Helix" take up only one cell
# Variable Names changed in Final Code Above


'''
for rarity in range(len(rarity_name_list)):

	format_wpn = rarity_list[rarity].split(" - ")
	print(format_wpn)

	for formatted in range(len(format_wpn)):
		print(formatted)

		f.write(str(num) + ", " + rarity_name_list[rarity] + ", " + format_wpn[formatted] + "\n")

		num+=1
'''

# common = "Bad Pistol - Jack and Mary - The Code - Blood Blade - Dormant Bubble Machine - H2O - Crimson Wine Glass - Sacred Flail - Ancient Bow - Flaring Claw - Wooden Cross - Crispy Bone - Satellite Floating Gun - Boxing Gloves - P250 Pistol - AK-47 - Shotgun - Shotgun Pro - UZI - Snow Fox L - Snow Fox XL - Desert Eagle - Revolver - Twin-barrel Pistol - Assault Rifle - Shaky Blaster - Blaster - Splitter Gun - Volcanic Blaster - M4 - Improved SMG - MP5 - Sniper Rifle - Fine Machine Gun - Ion Railgun - Guardian Railgun - Shotgun M1 - SMG M1 - Pioneer - Blind Missile Battery - Crossbow - Basketball - Football - Machete - Broadsword - Pirate Saber - Katana - Double Blade Sword - Axe - Battle Axe - Rapier - Pitchfork - Spear - Umbrella - Bow - Strong Bow - Composite Bow - Magic Staff - Staff of Nature - Goblin Spear - TNT - Assault Shotgun - Red Dragon - Bleach - PKP - Old Sniper Rifle - Old Rocket Launcher - M14 - Ninja Stars - Molotov Cocktail - Paper Slip - Butcher's Knife - Mini UZI - Iron Claw - Hammer - Wooden Hammer - Trekking Pole - Javelin - Throwing Axe - Long-handled Axe - Woodstick - Tidal Staff - Sawed-off Shotgun - Groundwater - Candied Hawberries - Fertilizer - Watering Can - Shovel - Rings - Royal Knight's Short Sword - Raw Axe - Headgear Hero's Machine Gun - Mercenary Intern's Shotgun - Legendary Apprentice’s Magic Staff - Monster Cuisine"

# uncommon = "Splitter Cannon - Snow Fox XXL - Alien Eagle - Frost Eagle - Flame Eagle - Plasma Eagle - Twin-barrel Rifle - Shotgun Galaxy - Sidewinder Red - Sidewinder Green - Gas Blaster - Flame Blaster - Bazooka - Next-gen SMG - Guardian Rifle - Shotgun M2 - SMG M2 -SMG Helix - Horn - Arbitrator - The Judge - Mace - Triple Crossbow - Knight Spear - Meat - Green Onions - Hunter Bow - Heavenly Sword - Broom - Staff of Light - Blowpipe - Feathered Crossbow - Bouncing Assault Rifle - Boomerang - Spike Knives - Wrenches - Halberd - Carrot - SMG M3 - Poison Eagle - Grenade Pistol - Sickle - RYB Assault Rifle - Bamboo - Executioner - Vine - Crossbow Air - Reusable Health Pot - Reusable Energy Pot - Bayonet Rifle - Assault Sniper Rifle - Green Basin - Channeling Monkey"

# rare = "Assault Rocket - Assault Rifle Pro - Glacier - Furnace - Knight's Fist - Cluster Missile - Next-next-gen SMG - Shotgun M3 - Prototype Railgun - Nasty Laser - Ice Breaker - Jumper - Webber - Crossbow Plus - Badminton Racket - Trident - Laser Sword Blue - Laser Sword Green - Laser Sword Red - Crystal Bow - Flame Bow - Frost Bow - Jade Bow - Fish - Plunger - Staff of Frost - Staff of Flame - Wizard's Staff - Electric Therapy - Cherry Blossom - Laser - Splash Railgun - Ice Spikes - Eagle of Ice and Fire - Windforce - Bouncing Railgun - Bassball Bat - Ninja Stars Plus - Buckler - Stone Hammer - Void Sword - Bow Plus - Frost Spear - Heavy Hunter Axe - Laser Therapy - Reusable Restoration Potion - EM Sniper Rifle - Firecrackers"

# very_rare = "Aurora - Gatling Gun - Rocket Gun - Black Hole Missile - Fusion Drill - Ion Laser - Cleaner - Laser Shotgun - Flame Axe - Frost Sword - Flame Sword - Hero Bow - Plunger Plus - Staff of Thunder - Bouncing Sniper Rifle - Charged Railgun - Hand Grenade - Rainbow - Assault Rifle Pro+ - Next-next-next gen SMG - Meat Grinder - Explosive Warhammer - Thunder Warhammer - Electric Ninja Stars - Rocket Fireworks"

# epic = "Snow Fox Vintage - Soul Calibre - Implosion - Missile Battery - Illusion - Rocket Gun M1 - Grenade SMG - Magic Bow - Laser Fish - Fine Magic Staff - Staff of Illusion - Explosive Crossbow"

# legendary = "Money Gun - Caliburn - Shield - One Punch - Snow Ape's Longbow - Crystal Crab's Katana - Snowman Eagle - Staff of Shooting Stars - Cannibal Plant - Agitated Trunk - Bomber - Staff of Wizard - Staff of Skeleton - Grand Knight's Sword - Extra Crown - The Emperor's New Gun - Dragon Bros’ Sniper Rifle - Floating Gun - Floating Laser - Varkolyn Assault Rifle - Sandworm"