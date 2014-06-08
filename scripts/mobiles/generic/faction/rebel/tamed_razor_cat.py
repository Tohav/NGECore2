import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('rebel_tamed_razor_cat')
	mobileTemplate.setLevel(10)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(65)
	mobileTemplate.setHideType("Bristly Hide")
	mobileTemplate.setHideAmount(35)
	mobileTemplate.setBoneType("Animal Bones")
	mobileTemplate.setBoneAmount(30)
	mobileTemplate.setSocialGroup("razor cat")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(True)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(1)
	
	templates = Vector()
	templates.add('object/mobile/shared_corellian_sand_panther.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('tamed_razor_cat', mobileTemplate)
	return