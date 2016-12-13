###This program will extract data from the Illustris simulation
## and calculate the radial distribution of mass,etc
## using concentric radii  

from scipy.stats import gaussian_kde
import pylab
import matplotlib.pyplot as plt
import h5py
import numpy as np
import requests
def get(path, params=None):
    # make HTTP GET request to path
    headers = {"api-key":"452a77edd4324ec835da440fc3fdc50b "}
    r = requests.get(path, params=params, headers=headers)

    # raise exception if response code is not HTTP SUCCESS (200)
    r.raise_for_status()

    if r.headers['content-type'] == 'application/json':
        return r.json() # parse json responses automatically

    if 'content-disposition' in r.headers:
        filename = r.headers['content-disposition'].split("filename=")[1]
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename # return the filename string

    return r



import requests
baseUrl = 'http://www.illustris-project.org/api/'
headers = {"api-key":"452a77edd4324ec835da440fc3fdc50b"}



##############################################
####MAIN PROGRAM STARTS HERE


############### This program will track the evolution of the contents of galaxies
########starting at snap number 20 #######
########It contains loops which keep track of the url associated with each galaxy
##### it then takes this url and accesses all the data on it
###### in order to calculate the gas, dm, bh, and star radial density profiles
##### The program then finds power laws associated with these densities. 



id = 13

url = "http://www.illustris-project.org/api/Illustris-2/snapshots/130/subhalos/" + str(id)
sub = get(url) # get json response of subhalo properties
print url
# prepare dict to hold result arrays

fields = ['snap','id','mass_gas','mass_stars','mass_dm','mass_bhs','len_stars','related']
r = {}
for field in fields:
	r[field] = []
n = 0	
while sub['desc_sfid'] != -1:
	for field in fields:
		r[field].append(sub[field])
		

		
	#print r['mass_stars']
# request the full subhalo details of the descendant by following the sublink URL
	s = r['id'][n]
	sub = get(sub['related']['sublink_descendant'])
	#print len(r['id'])
	
	p = r['mass_stars']
	q = r['len_stars']
	#print p
	#print q
	t = r['snap'][n]
	url1 = "http://www.illustris-project.org/api/Illustris-2/snapshots/" + str(t) + "/subhalos/" + str(s)
	print url1
	
	
	###### all the initialized code here
	id1 = s
	print id1
	if t == 19 :
		redshift = 18.789189562448097
		print redshift
	elif t == 20:
	
		redshift = 17.9630246045828
		print redshift
	elif t == 21:
		redshift = 17.0854527855627
		print redshift
	elif t ==  22:
		redshift = 16.248493279904903
	elif t ==  23 :
		redshift = 	15.450266628902101
	elif t ==  24 :
		redshift = 14.7634960164193
	elif t ==  25 :
		redshift = 14.0339921444525
	elif t ==  26 :
		redshift = 13.338248289848599
	elif t ==  27 :
		redshift = 12.6747021048037
	elif t ==  28 :
		redshift = 12.0418635439251
	elif t ==  29 :
		redshift = 11.49738795480349
	elif t ==  30 :
		redshift = 10.919033198155402
	elif t ==  31 :
		redshift = 10.367443572408702
	elif t ==  32 :
		redshift = 9.996590466186328
	elif t ==  33 :
		redshift = 9.84138043947183
	elif t ==  34 :
		redshift = 9.38877127194055
	elif t ==  35 :
		redshift = 9.00233985416247
	elif t ==  36 :
		redshift = 8.907999185598529
	elif t ==  37 :
		redshift = 8.44947629436874
	elif t ==  38 :
		redshift = 8.01217294886593
	elif t == 39 :
		redshift = 7.595107149871599
	elif t ==  40 :
		redshift = 7.23627606616736
	elif t ==  41 :
		redshift = 7.0054170455445295
	elif t == 42 :
		redshift = 6.855117262650801
	elif t ==  43 :
		redshift =  6.491597745667499
	elif t ==  44 :
		redshift = 6.14490120341637
	elif t ==  45 :
		redshift =  6.0107573988449
	elif t ==  46 :
		redshift = 5.846613747881871
	elif t ==  47 :
		redshift = 5.5297658079491
	
	elif t ==  48 :
		redshift = 5.227580973127339
	elif t == 49 :
		redshift =  4.99593346816462
	elif t ==  50 :
		redshift = 4.9393806634910105
	elif t ==  51 :
		redshift = 4.66451770247093
	elif t ==  52 :
		redshift = 4.42803373660555 
	elif t ==  53 :
		redshift =  4.17683491472647
	elif t ==  54 :
		redshift =  4.007945111465269
	elif t ==  55 :
		redshift =  3.93726108472758
	elif t == 56 :
		redshift =  3.70877426464224
	elif t ==  57 :
		redshift =  3.49086136926065
	elif t ==  58 :
		redshift =  3.28303305795652
	elif t ==  59 :
		redshift =  3.0848226358340103
	elif t ==  60 :
		redshift =  3.00813107163038
	elif t ==  61 :
		redshift =  2.89578500572743
	elif t ==  62 :
		redshift =  2.73314261731872
	elif t ==  63 :
		redshift =  2.57729027160189
	elif t ==  64 :
		redshift = 2.44422570455415
	elif t ==  65 :
		redshift = 2.31611074395689
	elif t ==  66 :
		redshift = 2.2079254723837
	elif t ==  67 :
		redshift = 2.10326965259577
	elif t ==  68 :
		redshift = 2.00202813925285
	elif t ==  69 :
		redshift = 	1.90408954353277	
	elif t ==  70 :
		redshift = 	1.82268925262035
	elif t ==  71:
		redshift = 	1.74357057433086
	elif t == 72:
		redshift = 	1.66666955611447
	elif t ==  73 :
		redshift = 	1.60423452207311
	elif t ==  74 :
		redshift = 	1.53123902915761
	elif t ==  75:
		redshift = 	 1.4719748452658
	elif t ==  76 :
		redshift = 	1.4140982203725199
	elif t == 77 :
		redshift = 	1.357576667403
	elif t ==  78 :
		redshift = 	1.30237845990597
	elif t ==  79 :
		redshift = 	1.2484726142451399
	elif t ==  80 :
		redshift = 	1.206258080781
	elif t ==  81 :
		redshift = 	1.1546027123602198
	elif t ==  82 :
		redshift = 	1.11415056376538
	elif t ==  83 :
		redshift = 	1.07445789454767
	elif t ==  84 :
		redshift = 	1.03551044566414
	elif t ==  85 :
		redshift = 	0.9972942257819399
	elif t ==  86 :
		redshift = 	0.987852810815766
	elif t ==  87 :
		redshift = 	0.950531351585033
	elif t ==  88 :
		redshift = 	0.923000816177909
	elif t ==  89 :
		redshift = 	0.886896937575248
	elif t ==  90 :
		redshift = 	0.8514709006246489
	elif t ==  91 :
		redshift = 	0.816709979011851
	elif t ==  92 :
		redshift = 	0.791068248946339
	elif t ==  93 :
		redshift = 	0.7574413726158531
	elif t ==  94 :
		redshift = 	0.732636182022312
	elif t ==  95 :
		redshift =  0.700106353718523	
	elif t ==  96 :
		redshift =  0.676110411213478
	elif t ==  97 :
		redshift = 	0.644641840684537
	elif t ==  98 :
		redshift = 	0.621428745242514
	elif t ==  99 :
		redshift = 	0.598543288187567
	elif t ==  100 :
		redshift = 	0.5759808451078869
	elif t ==  101 :
		redshift = 	0.546392183141022
	elif t ==  102 :
		redshift = 	 0.524565820433923
	elif t ==  103 :
		redshift = 	0.503047523244883
	elif t ==  104 :
		redshift = 	 0.48183294342095095	
	elif t == 105 :
		redshift = 	0.460917794180647	
	elif t ==  106 :
		redshift = 	 0.44029784924774296	
	elif t ==  107 :
		redshift = 	0.41996894199726703			
	elif t ==  108 :
		redshift = 	0.39992696461356303	
	elif t ==  109:
		redshift = 	0.380167867260239
	elif t ==  110:
		redshift = 	0.360687657261817
	elif t ==  111:
		redshift = 	0.34785384185817797	
	elif t ==  112:
		redshift = 	0.32882972420595397	
	elif t == 113:
		redshift = 	0.310074120127834	
	elif t ==  114:
		redshift = 	0.29158323972192396	
	elif t ==  115:
		redshift = 	 0.27335334657844	
	elif t ==  116:
		redshift = 	 0.261343256161012	
	elif t ==  117:
		redshift = 	0.24354018155467003	
	elif t ==  118:
		redshift = 	0.22598838626019802
	elif t == 119 :
		redshift = 	0.21442503551449502	
	elif t ==  120:
		redshift = 	0.19728418237600998	
	elif t ==  121:
		redshift = 	0.18038526170574898	
	elif t ==  122:
		redshift = 	0.16925203324361102	
	elif t ==  123:
		redshift = 	0.15274876890238098	
	elif t ==  124:
		redshift = 	0.141876203969562	
	elif t ==  125:
		redshift = 	0.125759332411261	
	elif t ==  126:
		redshift = 	0.10986994045882499	
	elif t ==  127:
		redshift = 	0.0994018026302219	
	elif t ==  128:
		redshift = 	0.0838844307974793	
	elif t ==  129:
		redshift = 	0.0736613846564387	
	elif t ==  130:
		redshift = 	0.058507322794513	
	elif t ==  131:
		redshift = 	0.048523629981805906	
	elif t ==  132:
		redshift = 	0.0337243718735154	
	elif t ==  133:
		redshift = 	0.0239744283827625
	elif t ==  134:
		redshift = 	0.00952166696794476	
	elif t ==  135:
		redshift = 	2.2204460492503099e-16	
				
	
	
	import pylab
	import matplotlib.pyplot as plt
	id1 = s
	
	params = {'stars':'Coordinates,GFM_Metallicity,Masses'}
	scale_factor = 1.0 / (1+redshift)          #IMPORTANT NEEDED FOR EACH REDSHIFT
	little_h = 0.704        #IMPORTANT NEEDED FOR EACH REDSHIFT
	
	starnorm = 10e10 / (little_h)
	sub1 = get(url1) # get json response of subhalo properties
	saved_filename = get(url1 + "/cutout.hdf5",params) # get and save HDF5 cutout file
	
	little_r = 0    
	big_r = .5   #units are kpc
	count = 0 
	radialstarmass_density =([])
	radialstarmass = ([])
	radial_distance = ([])
	final_total_mass = ([])
	while (count < 2):
	
		 try:
		 	with h5py.File(saved_filename) as f:
		 
		     		dx2 = f['PartType4']['Coordinates'][:,0] - sub1['pos_x']
        	 		dy2 = f['PartType4']['Coordinates'][:,1] - sub1['pos_y']
        	 		dz2 = f['PartType4']['Coordinates'][:,2] - sub1['pos_z']
        	 		dens = np.log10(f['PartType4']['Masses'][:])
        	 		masses = f['PartType4']['Masses'][:]
    				metals = f['PartType4']['GFM_Metallicity'][:]
        	 		rr2 = np.sqrt(dx2**2 + dy2**2 + dz2**2)
        			rr2 *= (scale_factor/little_h)# ckpc/h -> physical kpc  IMPORTANT
        	 		
        	 		rrr2 = sorted(rr2)
        	 		
        	 		print "printing rrr2"
        	 		print rrr2
        	 		print len (rrr2)
        	 		
        	 			
        			volume2 = ([])
        			coun = 0
        			iter = len(rrr2) / (50) 
        			remainder = len(rrr2) % (50)
        			
        			outer_radius2 = ([])
        			while coun < iter:
        				#print "now printing rr2"
        				#print rrr2
        				top5 = rrr2[:50]
        				#print "printing first 5"
        				#print top5
        				
        				totalmass2 = len(top5) * 0.000340371179
        				
        				#print top50[0]
        				outer_radius2.insert(coun,top5[49])
        				del rrr2[:50]
        				coun = coun + 1		
        	 		
        			# need to insert the outer most remainder and the 0,0 rad
        			
        				
        			outer_radius2.insert(iter,rrr2[remainder - 1]) # warning this will give error if remainder is 0
        			
        			
        			outer_radius2.insert(0,0)
        			
        			
        			
        			print "now printing radiii"
        			print outer_radius2
        			
        			m = 0
        			starmass_density = ([])
        			starmetal = ([])
        			radial_distance2 = ([])      	 		
        	 		average_star_mass = ([])
        	 		while m <= iter:
        				print "raddii for volume"
        				
        				print outer_radius2[m + 1]
        				print outer_radius2[m]
        				
        				#   now w is an array of random particle id's not ordered by number precisely
        				
        				w = np.where( (rr2 >= outer_radius2[m]) & (rr2 < outer_radius2[m + 1]) ) 
        				
        				
        				print "printing w masses"
        				MASS = masses[w] 
        				
        				
        				METAL = metals[w]
        				
        				
        				MASSESS = MASS.tolist()
    					METALSS = METAL.tolist()
    					
    					
    					
    					METALS =   [( x / 0.0127) for x in METALSS]
    					
    					MASSES = [(x * 0.3814381382231999) for x in MASSESS]
    					print MASSES
    					
    					
    					TOTMass = sum(MASSES)
    					
    					print TOTMass
    					print "now printing metals"
    					
    				
    					
    					print METALSS
    					print METALS
    					print "printing w"
    					print len(MASSES)
    					print w
    					
    					totalmass = sum(MASSES)
    					
    					totalmetals = sum(METALS)
    					
    					average_mass = totalmass / (len(MASSES))
    					
    					
    					print "now printing totalstarmass, len of stars, average starmass"
    					#print totalstarmass
        				
        				print len(w)
        				#average_starmass = totalstarmass / len(w)
        				#print average_starmass
        				
        				volume2 = (4.0/3.0)*3.14*((outer_radius2[m + 1])**3) - (4.0/3.0)*3.14*((outer_radius2[m])**3)
						
						
        				density2 = totalmass / (volume2)
        				averagem = totalmetals / (len(MASSES))
						

						
        				
        				starmass_density.insert(m,density2)
						
						
						
						#averagemetal = totalmetals / len(MASSES)
					
					average_star_mass.insert(m,average_mass)
					starmetal.insert(m,averagem)
					radial_distance2.insert(m,outer_radius2[m + 1])	
					final_total_mass.insert(m, totalmass)	
        				
        				m = m + 1
        		
        		
        	 	#	radialstarmass.insert(count,totalmass2)
        	 	#	radial_distance.insert(count,big_r)
        	 	#	density = radialstarmass[count] / volume2
        #print density
        	 	#	radialstarmass_density.insert(count,density2)
        
        	 		little_r = little_r + .5    
        	 		big_r = big_r + .5   #units are kpc
    		 		count = count + 1
		 except KeyError:
			 break
	
	print average_star_mass
	print starmetal
	print radial_distance2
	print starmass_density
	print sum(final_total_mass)
	
	
	axes = plt.gca()
	axes.set_xlim([0,200])
	plt.plot(radial_distance2,starmass_density)
	plt.xlabel('Radius kpc')
	plt.ylabel('Star Matter Density 10^10 Msolar /kpc^3')
	plt.title('Star Matter Density  at Redshift %s'%(redshift))
	
	plt.show()
	
		
	axes = plt.gca()
	axes.set_xlim([0,200])
	plt.plot(radial_distance2,starmetal)
	plt.xlabel('Radius kpc')
	plt.ylabel('Metallicity Msolar')
	plt.title('Star Metallicity  at Redshift %s'%(redshift))
	
	plt.show()
	
	
			
	axes = plt.gca()
	axes.set_xlim([0,200])
	plt.plot(radial_distance2,average_star_mass)
	plt.xlabel('Radius kpc')
	plt.ylabel('Average_star_mass 10^4 Msolar')
	plt.title('Average Star mass at Redshift %s'%(redshift))
	
	
	
	plt.show()
	
		
	plt.hist2d(dx2,dy2,bins=[1350,900])
	plt.xlabel('$\Delta x$ [ckpc/h]')
	plt.ylabel('$\Delta y$ [ckpc/h]')
	pylab.show()    
    
				
######   n = n + 1 iterates over all subhalo numbers #######	
	
	n = n + 1
	#print s
	#print t
	
	
	
