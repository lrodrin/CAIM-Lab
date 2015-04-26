import pylab
import numpy
import sys
import argparse
import time

def timeit(method):
	def timed(*args, **kw):
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()

		print '%r (%r, %r) %2.2f sec' % \
			(method.__name__, args, kw, te-ts)
		return result
	return timed


@timeit
def main(argv=None):
	data = numpy.load('images.npy')
	parser = argparse.ArgumentParser()
	parser.add_argument('-img', default=1501, type=int)
	args = parser.parse_args()    

	img_to_compare = data[args.img]

	print "Running Brute-force to find the similituded for img number =", args.img

    # show candidate neighbors for first 10 test images
	dist = 1000000000;
	dist_aux = 0;
	img_fin = 0;
	for i in range(0,1500):
		img_aux = data[i];	
		for y, x in enumerate(img_aux):
			for j,value in enumerate(x):
				dist_aux += abs(img_to_compare[y][j]- value);
		if (dist_aux < dist):
			dist = dist_aux;
			img_fin = i;

		#print "Dist parcial = ", dist, " Ultim dist_aux= ", dist_aux, " Imatge: ", i;
		dist_aux = 0;

	print "La imagen con mas similitud difieren en: ", dist, " y es la numero: ", img_fin    
	return

if __name__ == "__main__":
	sys.exit(main())