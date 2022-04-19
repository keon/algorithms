#Class Photo problem
#Time O(nlongn) | Space O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    
    redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	shirtColorInFirstRow='RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
	for i in range(len(redShirtHeights)):
		redShirtHeight=redShirtHeights[i]
		blueShirtHeight=blueShirtHeights[i]
		
		if shirtColorInFirstRow=='RED':
			if redShirtHeight>=blueShirtHeight:
				return False
		else:
			if blueShirtHeight>=redShirtHeight:
				return False
	return True		
				
