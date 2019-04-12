# -*- coding: utf-8 -*-
import numpy as np
import linecache
import argparse
import time

class Converts:
	def __init__(self):
		print("Parentコンストラクタ")
		self.arr_train=[]
		self.arr_test=[]
		self.arr_valid=[]
		# self.arr_train_np = np.array([],dtype=object)
		# self.arr_test_np = np.array([],dtype=object)
		# self.arr_valid_np = np.array([],dtype=object)


	# Convert MATLAB file to list[ndarray([[x1,y1,z1],,,[x25,y25,z25]],[[x1,y1,z1],,,[x25,y25,z25]])]
	def convert(self,filename,joint):
		# arr = np.load('aaron_sheep.npz')
		# print('\n'.join(arr))
		# train:7400, valid:300, test:300, # dtype:int16
		f = open(filename)
		line = f.readlines()
		temp_posi = []

		# 人数確認
		ppl_count=int(line[1])
		# print("ppl_count:",ppl_count)

		# make python list of positions from MATLAB data format
		for l in line:
			if len(l) > 60:
				#print("(big)l:",l)
				line_arr = l.split(" ")
				# print("line_arr:",line_arr)
				if len(line_arr) == 12:
					temp_posi.append([float(line_arr[0]),float(line_arr[1]),float(line_arr[2])])
						# float(line_arr[7]),float(line_arr[8]),float(line_arr[9]),float(line_arr[10]),float(line_arr[11])])

		# print("temp_posi",temp_posi)
		
		# make frame np.ndarray (3 * 25) from list of positions, and give it to frame list
		k = 0 # line count within datum
		n = 0 # saved data count
		temp_np_array = np.array([])
		temp_frame = np.empty((0,3), dtype=np.float16)

		for t in temp_posi:
			k = k + 1
			# print("k:,t:",t,k)
			if k % 25 == joint:
				n = n + 1
				if n % ppl_count == 0:
					temp_frame = np.vstack((temp_frame,t))
					# print("temp_frame:",temp_frame)
				
		
		return temp_frame

	# randomly allocate data into train, valid and test by file
	def randomize(self,data,train=0.8,valid=0.1,test=0.1):
		r = np.random.rand()
		# print("data.shape[0]:",data.shape[0])

		if data.shape[0] < 1:
			return self.arr_train,self.arr_valid,self.arr_test
		if r < train:
			# self.arr_train=[self.arr_train,data]

			self.arr_train.append(data)

		elif r < train + valid:
			self.arr_valid.append(data)
			# self.arr_valid=[self.arr_valid,data]

		else:
			self.arr_test.append(data)
			# self.arr_test=[self.arr_test,data]

		return self.arr_train,self.arr_valid,self.arr_test

	# randomly allocate data into train, valid and test by file
	def padding(self,train=200,valid=100,test=100):
		
		while len(self.arr_train) < train:
			d = int(np.random.rand() * len(self.arr_train))
			# print("train d:",d)
			self.arr_train.append(self.arr_train[d])

		while len(self.arr_valid) < valid:
			d = int(np.random.rand() * len(self.arr_valid))
			# print("valide d:",d)
			self.arr_valid.append(self.arr_valid[d])

		while len(self.arr_test) < test:
			d = int(np.random.rand() * len(self.arr_test))
			# print("test d:",d)
			self.arr_test.append(self.arr_test[d])

		return self.arr_train,self.arr_valid,self.arr_test


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='parser from Matlab Skelton to Numpy')
	parser.add_argument('-l', '--list', help='delimited list input',  nargs='+')
	parser.add_argument('-j', '--joint', help='delimited list input')
	parser.add_argument('-p', '--padding', dest='padding', action='store_true')
	args = parser.parse_args()
	print args.list
	print args.joint
	print args.padding

	filenames = [item for item in args.list[0].split(',')]
	joint = int(args.joint)
	# print("filenames",filenames)

	arr_train_r=np.empty([],dtype=object)
	arr_valid_r=np.empty([],dtype=object)
	arr_test_r=np.empty([],dtype=object)

	converts = Converts()
	
	# arr_valid,arr_test,arr_train=initialize()

	for filename in filenames:
		# print("filename:",filename)
		d = converts.convert(filename,joint)
		arr_train_r,arr_valid_r,arr_test_r = converts.randomize(d)
	if args.padding == True:
		print("padding")
		arr_train_r,arr_valid_r,arr_test_r = converts.padding()
	# print("arr_train_np,arr_valid_np,arr_test_np in __main__:", arr_train_r,arr_valid_r,arr_test_r)

	savename = 'test' + str(int(time.time())) + '.npz'
	np.savez(savename, valid=arr_valid_r, test=arr_test_r, train=arr_train_r)
