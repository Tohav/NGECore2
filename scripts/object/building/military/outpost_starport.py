import sys

def setup(core, object):
	objSvc = core.objectService
	objSvc.createChildObject(object, 'object/creature/npc/theme_park/shared_player_transport.iff', 0, 7, 0, 0.71, 0.71)
	objSvc.createChildObject(object, 'object/tangible/travel/ticket_collector/shared_ticket_collector.iff', 1, 0, -10, 0, 1)	
	objSvc.createChildObject(object, 'object/tangible/terminal/shared_terminal_travel.iff', float(-3.12), float(0.15), float(-17.57), float(0.71), float(-0.71), 1)
	core.mapService.addLocation(object.getPlanet(), 'Starport', object.getPosition().x, object.getPosition().z, 15, 0, 0)	
	return
	