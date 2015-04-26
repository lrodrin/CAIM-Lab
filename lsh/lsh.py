#!/usr/bin/env python

"""
Simple module implementing LSH
"""

__version__ = '0.2'
__author__  = 'marias@cs.upc.edu'

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


class lsh(object):
    """
    implements lsh for digits database in file 'images.npy'
    """  
    
    def __init__(self, k, m):
        """ k is nr. of bits to hash and m is reapeats """
        # data is numpy ndarray with images
        self.data = numpy.load('images.npy')
        self.k = k
        self.m = m

        # determine length of bit representation of images
        # use conversion from natural numbers to unary code for each pixel,
        # so length of each image is imlen = pixels * maxval
        self.pixels = 64
        self.maxval = 16
        self.imlen = self.pixels * self.maxval

        # need to select k random hash functions for each repeat
        # will place these into an m x k numpy array
        numpy.random.seed(12345)
        self.hashbits = numpy.random.randint(self.imlen, size=(m, k))

        # the following stores the hashed images
        # in a python list of m dictionaries (one for each repeat)
        self.hashes = [dict()] * self.m

        # now, fill it out
        self.hash_all_images()

        return
    

    def hash_all_images(self):
        """ go through all images and store them in hash table(s) """
        # Achtung!
        # Only hashing the first 1500 images, the rest are used for testing
        for idx, im in enumerate(self.data[:1500]):
            for i in range(self.m):
                str = self.hashcode(im, i)

                # store it into the dictionary.. 
                # (well, the index not the whole array!)
                if str not in self.hashes[i]:
                    self.hashes[i][str] = []
                self.hashes[i][str].append(idx)
        return


    def hashcode(self, im, i):
        """ get the i'th hash code of image im (0 <= i < m)"""
        pixels = im.flatten()
        row = self.hashbits[i]
        str = ""
        for x in row:
            # get bit corresponding to x from image..
            pix = int(x) / int(self.maxval)
            num = x % self.maxval
            if (num <= pixels[pix]):
                str += '1'
            else:
                str += '0'
        return str


    def candidates(self, im):
        """ given image im, return matching candidates (well, the indices) """
        res = set()
        for i in range(self.m):
            code = self.hashcode(im, i)
            if code in self.hashes[i]:
                res.update(self.hashes[i][code])
        return res

    def distance(self, im, candidats):
        dist = 1000000000;
        dist_aux = 0;
        img_fin = 0;
        for i,x in enumerate(candidats):
            img_aux = self.data[x];  
            for j, x2 in enumerate(img_aux):
                for k,value in enumerate(x2):
                    dist_aux += abs(im[j][k]- value);
            if (dist_aux < dist):
                dist = dist_aux;
                img_fin = x;

            #print "Dist parcial = ", dist, " Ultim dist_aux= ", dist_aux, " Imatge: ", i;
            dist_aux = 0;

        print "La imagen con mas similitud difieren en: ", dist, " y es la numero: ", img_fin    
        return 


@timeit
def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', default=20, type=int)
    parser.add_argument('-m', default=5, type=int)
    parser.add_argument('-img', default=1501, type=int)
    args = parser.parse_args()    

    print "Running lsh.py with parameters k =", args.k, "and m =", args.m
    print "Give we want the Nearest neighbor of image number =", args.img

    me = lsh(args.k, args.m)

    im = me.data[args.img]
    cands = me.candidates(im)
    #print cands
    print "there are ",len(cands), " candidates for image " ,args.img
    me.distance(im, cands)


    return

if __name__ == "__main__":
  sys.exit(main())
