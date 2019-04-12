# -*- coding: utf-8 -*-
import numpy as np
import linecache
import argparse

def initialize():
	# ここから書くか

	# arr_all = np.empty((0,3), dtype=float)
	# arr_valid = np.empty((0,3), dtype=float)
	# arr_test = np.empty((0,3), dtype=float)
	# arr_train = np.empty((0,3), dtype=float)
	# arr_all=np.empty((0,3), dtype=float)

	arr_valid=[]
	arr_test=[]
	arr_train=[]

	return arr_valid,arr_test,arr_train

# Convert MATLAB file to list[ndarray([[x1,y1,z1],,,[x25,y25,z25]],[[x1,y1,z1],,,[x25,y25,z25]])]
def convert(filename):
	# arr = np.load('aaron_sheep.npz')
	# print('\n'.join(arr))
	# train:7400, valid:300, test:300, # dtype:int16
	f = open(filename)
	line = f.readlines()
	temp_posi = []

	# 人数確認
	ppl_count=int(line[1])
	print("ppl_count:",ppl_count)

	# make python list of positions from MATLAB data format
	for l in line:
		if len(l) > 60:
			#print("(big)l:",l)
			line_arr = l.split(" ")
			#print("line_arr:",line_arr)
			temp_posi.append([float(line_arr[0]),float(line_arr[1]),float(line_arr[2])])
			# body_arr = np.array([float(line_arr[0]),float(line_arr[1]),float(line_arr[2])])
			# print("body_arr:",body_arr)
			# arr_all = np.vstack((arr_all,body_arr))
	print("temp_posi",temp_posi)
	
	# make frame np.ndarray (3 * 25) from list of positions, and give it to frame list
	k = 0 # line count within datum
	n = 0 # saved data count

	temp_movie = []
	temp_frame = np.empty((0,3), dtype=float)

	for t in temp_posi:
		k = k + 1
		print("k:",k)
		print("t:",t)
		temp_frame = np.vstack((temp_frame,t))
		print("temp_frame:",temp_frame)
		if k % 25 == 0:
			n = n + 1
			if n % ppl_count == 0:
				temp_movie.append(temp_frame)
				temp_frame = np.empty((0,3), dtype=float)

	temp_movie_np = np.array(temp_movie)
	print("temp_movie_np:",temp_movie_np)
	
	return temp_movie_np

def randomize(data,arr_train,arr_valid,arr_test,train=0.8,valid=0.1,test=0.1):
	r = np.random.rand()

	if r < train:
		arr_train.append(data)
		# arr_train_np = np.array(arr_train,dtype=object)
	elif r < train + valid:
		arr_valid.append(data)
		# arr_valid_np = np.array(arr_valid,dtype=object)
	else:
		arr_test.append(data)
		# arr_test_np = np.array(arr_test,dtype=object)
	return arr_train,arr_valid,arr_test

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='parser from Matlab Skelton to Numpy')
	parser.add_argument('-l', '--list', help='delimited list input',  nargs='+')
	args = parser.parse_args()
	print args.list
	filenames = [item for item in args.list[0].split(',')]
	print("filenames",filenames)
	
	# filenames = ["nturgb+d_skeletons/S006C001P023R001A001.skeleton","nturgb+d_skeletons/S006C001P023R001A002.skeleton","nturgb+d_skeletons/S006C001P023R001A003.skeleton","nturgb+d_skeletons/S006C001P023R001A004.skeleton","nturgb+d_skeletons/S006C001P023R001A005.skeleton","nturgb+d_skeletons/S006C001P023R001A006.skeleton","nturgb+d_skeletons/S006C001P023R001A007.skeleton","nturgb+d_skeletons/S006C001P023R001A008.skeleton","nturgb+d_skeletons/S006C001P023R001A009.skeleton","nturgb+d_skeletons/S006C001P023R001A010.skeleton","nturgb+d_skeletons/S006C001P023R001A011.skeleton","nturgb+d_skeletons/S006C001P023R001A012.skeleton","nturgb+d_skeletons/S006C001P023R001A013.skeleton","nturgb+d_skeletons/S006C001P023R001A014.skeleton","nturgb+d_skeletons/S006C001P023R001A015.skeleton","nturgb+d_skeletons/S006C001P023R001A016.skeleton","nturgb+d_skeletons/S006C001P023R001A017.skeleton","nturgb+d_skeletons/S006C001P023R001A018.skeleton","nturgb+d_skeletons/S006C001P023R001A019.skeleton","nturgb+d_skeletons/S006C001P023R001A020.skeleton","nturgb+d_skeletons/S006C001P023R001A021.skeleton","nturgb+d_skeletons/S006C001P023R001A022.skeleton","nturgb+d_skeletons/S006C001P023R001A023.skeleton","nturgb+d_skeletons/S006C001P023R001A024.skeleton","nturgb+d_skeletons/S006C001P023R001A025.skeleton","nturgb+d_skeletons/S006C001P023R001A026.skeleton","nturgb+d_skeletons/S006C001P023R001A027.skeleton","nturgb+d_skeletons/S006C001P023R001A028.skeleton","nturgb+d_skeletons/S006C001P023R001A029.skeleton","nturgb+d_skeletons/S006C001P023R001A030.skeleton","nturgb+d_skeletons/S006C001P023R001A031.skeleton","nturgb+d_skeletons/S006C001P023R001A032.skeleton","nturgb+d_skeletons/S006C001P023R001A033.skeleton","nturgb+d_skeletons/S006C001P023R001A034.skeleton","nturgb+d_skeletons/S006C001P023R001A035.skeleton","nturgb+d_skeletons/S006C001P023R001A036.skeleton","nturgb+d_skeletons/S006C001P023R001A037.skeleton","nturgb+d_skeletons/S006C001P023R001A038.skeleton","nturgb+d_skeletons/S006C001P023R001A039.skeleton","nturgb+d_skeletons/S006C001P023R001A040.skeleton","nturgb+d_skeletons/S006C001P023R001A041.skeleton","nturgb+d_skeletons/S006C001P023R001A042.skeleton","nturgb+d_skeletons/S006C001P023R001A043.skeleton","nturgb+d_skeletons/S006C001P023R001A044.skeleton","nturgb+d_skeletons/S006C001P023R001A045.skeleton","nturgb+d_skeletons/S006C001P023R001A046.skeleton","nturgb+d_skeletons/S006C001P023R001A047.skeleton","nturgb+d_skeletons/S006C001P023R001A048.skeleton","nturgb+d_skeletons/S006C001P023R001A049.skeleton","nturgb+d_skeletons/S006C001P023R001A050.skeleton","nturgb+d_skeletons/S006C001P023R001A051.skeleton","nturgb+d_skeletons/S006C001P023R001A052.skeleton","nturgb+d_skeletons/S006C001P023R001A053.skeleton","nturgb+d_skeletons/S006C001P023R001A054.skeleton","nturgb+d_skeletons/S006C001P023R001A055.skeleton","nturgb+d_skeletons/S006C001P023R001A056.skeleton","nturgb+d_skeletons/S006C001P023R001A057.skeleton","nturgb+d_skeletons/S006C001P023R001A058.skeleton","nturgb+d_skeletons/S006C001P023R001A059.skeleton","nturgb+d_skeletons/S006C001P023R001A060.skeleton","nturgb+d_skeletons/S006C001P023R002A001.skeleton","nturgb+d_skeletons/S006C001P023R002A002.skeleton","nturgb+d_skeletons/S006C001P023R002A003.skeleton","nturgb+d_skeletons/S006C001P023R002A004.skeleton","nturgb+d_skeletons/S006C001P023R002A005.skeleton","nturgb+d_skeletons/S006C001P023R002A006.skeleton","nturgb+d_skeletons/S006C001P023R002A007.skeleton","nturgb+d_skeletons/S006C001P023R002A008.skeleton","nturgb+d_skeletons/S006C001P023R002A009.skeleton","nturgb+d_skeletons/S006C001P023R002A010.skeleton","nturgb+d_skeletons/S006C001P023R002A011.skeleton","nturgb+d_skeletons/S006C001P023R002A012.skeleton","nturgb+d_skeletons/S006C001P023R002A013.skeleton","nturgb+d_skeletons/S006C001P023R002A014.skeleton","nturgb+d_skeletons/S006C001P023R002A015.skeleton","nturgb+d_skeletons/S006C001P023R002A016.skeleton","nturgb+d_skeletons/S006C001P023R002A017.skeleton","nturgb+d_skeletons/S006C001P023R002A018.skeleton","nturgb+d_skeletons/S006C001P023R002A019.skeleton","nturgb+d_skeletons/S006C001P023R002A020.skeleton","nturgb+d_skeletons/S006C001P023R002A021.skeleton","nturgb+d_skeletons/S006C001P023R002A022.skeleton","nturgb+d_skeletons/S006C001P023R002A023.skeleton","nturgb+d_skeletons/S006C001P023R002A024.skeleton","nturgb+d_skeletons/S006C001P023R002A025.skeleton","nturgb+d_skeletons/S006C001P023R002A026.skeleton","nturgb+d_skeletons/S006C001P023R002A027.skeleton","nturgb+d_skeletons/S006C001P023R002A028.skeleton","nturgb+d_skeletons/S006C001P023R002A029.skeleton","nturgb+d_skeletons/S006C001P023R002A030.skeleton","nturgb+d_skeletons/S006C001P023R002A031.skeleton","nturgb+d_skeletons/S006C001P023R002A032.skeleton","nturgb+d_skeletons/S006C001P023R002A033.skeleton","nturgb+d_skeletons/S006C001P023R002A034.skeleton","nturgb+d_skeletons/S006C001P023R002A035.skeleton","nturgb+d_skeletons/S006C001P023R002A036.skeleton","nturgb+d_skeletons/S006C001P023R002A037.skeleton","nturgb+d_skeletons/S006C001P023R002A038.skeleton","nturgb+d_skeletons/S006C001P023R002A039.skeleton","nturgb+d_skeletons/S006C001P023R002A040.skeleton","nturgb+d_skeletons/S006C001P023R002A041.skeleton","nturgb+d_skeletons/S006C001P023R002A042.skeleton","nturgb+d_skeletons/S006C001P023R002A043.skeleton","nturgb+d_skeletons/S006C001P023R002A044.skeleton","nturgb+d_skeletons/S006C001P023R002A045.skeleton","nturgb+d_skeletons/S006C001P023R002A046.skeleton","nturgb+d_skeletons/S006C001P023R002A047.skeleton","nturgb+d_skeletons/S006C001P023R002A048.skeleton","nturgb+d_skeletons/S006C001P023R002A049.skeleton","nturgb+d_skeletons/S006C001P023R002A050.skeleton","nturgb+d_skeletons/S006C001P023R002A051.skeleton","nturgb+d_skeletons/S006C001P023R002A052.skeleton","nturgb+d_skeletons/S006C001P023R002A053.skeleton","nturgb+d_skeletons/S006C001P023R002A054.skeleton","nturgb+d_skeletons/S006C001P023R002A055.skeleton","nturgb+d_skeletons/S006C001P023R002A056.skeleton","nturgb+d_skeletons/S006C001P023R002A057.skeleton","nturgb+d_skeletons/S006C001P023R002A058.skeleton","nturgb+d_skeletons/S006C001P023R002A059.skeleton","nturgb+d_skeletons/S006C001P023R002A060.skeleton","nturgb+d_skeletons/S006C002P023R001A001.skeleton","nturgb+d_skeletons/S006C002P023R001A002.skeleton","nturgb+d_skeletons/S006C002P023R001A003.skeleton","nturgb+d_skeletons/S006C002P023R001A004.skeleton","nturgb+d_skeletons/S006C002P023R001A005.skeleton","nturgb+d_skeletons/S006C002P023R001A006.skeleton","nturgb+d_skeletons/S006C002P023R001A007.skeleton","nturgb+d_skeletons/S006C002P023R001A008.skeleton","nturgb+d_skeletons/S006C002P023R001A009.skeleton","nturgb+d_skeletons/S006C002P023R001A010.skeleton","nturgb+d_skeletons/S006C002P023R001A011.skeleton","nturgb+d_skeletons/S006C002P023R001A012.skeleton","nturgb+d_skeletons/S006C002P023R001A013.skeleton","nturgb+d_skeletons/S006C002P023R001A014.skeleton","nturgb+d_skeletons/S006C002P023R001A015.skeleton","nturgb+d_skeletons/S006C002P023R001A016.skeleton","nturgb+d_skeletons/S006C002P023R001A017.skeleton","nturgb+d_skeletons/S006C002P023R001A018.skeleton","nturgb+d_skeletons/S006C002P023R001A019.skeleton","nturgb+d_skeletons/S006C002P023R001A020.skeleton","nturgb+d_skeletons/S006C002P023R001A021.skeleton","nturgb+d_skeletons/S006C002P023R001A022.skeleton","nturgb+d_skeletons/S006C002P023R001A023.skeleton","nturgb+d_skeletons/S006C002P023R001A024.skeleton","nturgb+d_skeletons/S006C002P023R001A025.skeleton","nturgb+d_skeletons/S006C002P023R001A026.skeleton","nturgb+d_skeletons/S006C002P023R001A027.skeleton","nturgb+d_skeletons/S006C002P023R001A028.skeleton","nturgb+d_skeletons/S006C002P023R001A029.skeleton","nturgb+d_skeletons/S006C002P023R001A030.skeleton","nturgb+d_skeletons/S006C002P023R001A031.skeleton","nturgb+d_skeletons/S006C002P023R001A032.skeleton","nturgb+d_skeletons/S006C002P023R001A033.skeleton","nturgb+d_skeletons/S006C002P023R001A034.skeleton","nturgb+d_skeletons/S006C002P023R001A035.skeleton","nturgb+d_skeletons/S006C002P023R001A036.skeleton","nturgb+d_skeletons/S006C002P023R001A037.skeleton","nturgb+d_skeletons/S006C002P023R001A038.skeleton","nturgb+d_skeletons/S006C002P023R001A039.skeleton","nturgb+d_skeletons/S006C002P023R001A040.skeleton","nturgb+d_skeletons/S006C002P023R001A041.skeleton","nturgb+d_skeletons/S006C002P023R001A042.skeleton","nturgb+d_skeletons/S006C002P023R001A043.skeleton","nturgb+d_skeletons/S006C002P023R001A044.skeleton","nturgb+d_skeletons/S006C002P023R001A045.skeleton","nturgb+d_skeletons/S006C002P023R001A046.skeleton","nturgb+d_skeletons/S006C002P023R001A047.skeleton","nturgb+d_skeletons/S006C002P023R001A048.skeleton","nturgb+d_skeletons/S006C002P023R001A049.skeleton","nturgb+d_skeletons/S006C002P023R001A050.skeleton","nturgb+d_skeletons/S006C002P023R001A051.skeleton","nturgb+d_skeletons/S006C002P023R001A052.skeleton","nturgb+d_skeletons/S006C002P023R001A053.skeleton","nturgb+d_skeletons/S006C002P023R001A054.skeleton","nturgb+d_skeletons/S006C002P023R001A055.skeleton","nturgb+d_skeletons/S006C002P023R001A056.skeleton","nturgb+d_skeletons/S006C002P023R001A057.skeleton","nturgb+d_skeletons/S006C002P023R001A058.skeleton","nturgb+d_skeletons/S006C002P023R001A059.skeleton","nturgb+d_skeletons/S006C002P023R001A060.skeleton","nturgb+d_skeletons/S006C002P023R002A001.skeleton","nturgb+d_skeletons/S006C002P023R002A002.skeleton","nturgb+d_skeletons/S006C002P023R002A003.skeleton","nturgb+d_skeletons/S006C002P023R002A004.skeleton","nturgb+d_skeletons/S006C002P023R002A005.skeleton","nturgb+d_skeletons/S006C002P023R002A006.skeleton","nturgb+d_skeletons/S006C002P023R002A007.skeleton","nturgb+d_skeletons/S006C002P023R002A008.skeleton","nturgb+d_skeletons/S006C002P023R002A009.skeleton","nturgb+d_skeletons/S006C002P023R002A010.skeleton","nturgb+d_skeletons/S006C002P023R002A011.skeleton","nturgb+d_skeletons/S006C002P023R002A012.skeleton","nturgb+d_skeletons/S006C002P023R002A013.skeleton","nturgb+d_skeletons/S006C002P023R002A014.skeleton","nturgb+d_skeletons/S006C002P023R002A015.skeleton","nturgb+d_skeletons/S006C002P023R002A016.skeleton","nturgb+d_skeletons/S006C002P023R002A017.skeleton","nturgb+d_skeletons/S006C002P023R002A018.skeleton","nturgb+d_skeletons/S006C002P023R002A019.skeleton","nturgb+d_skeletons/S006C002P023R002A020.skeleton","nturgb+d_skeletons/S006C002P023R002A021.skeleton","nturgb+d_skeletons/S006C002P023R002A022.skeleton","nturgb+d_skeletons/S006C002P023R002A023.skeleton","nturgb+d_skeletons/S006C002P023R002A024.skeleton","nturgb+d_skeletons/S006C002P023R002A025.skeleton","nturgb+d_skeletons/S006C002P023R002A026.skeleton","nturgb+d_skeletons/S006C002P023R002A027.skeleton","nturgb+d_skeletons/S006C002P023R002A028.skeleton","nturgb+d_skeletons/S006C002P023R002A029.skeleton","nturgb+d_skeletons/S006C002P023R002A030.skeleton","nturgb+d_skeletons/S006C002P023R002A031.skeleton","nturgb+d_skeletons/S006C002P023R002A032.skeleton","nturgb+d_skeletons/S006C002P023R002A033.skeleton","nturgb+d_skeletons/S006C002P023R002A034.skeleton","nturgb+d_skeletons/S006C002P023R002A035.skeleton","nturgb+d_skeletons/S006C002P023R002A036.skeleton","nturgb+d_skeletons/S006C002P023R002A037.skeleton","nturgb+d_skeletons/S006C002P023R002A038.skeleton","nturgb+d_skeletons/S006C002P023R002A039.skeleton","nturgb+d_skeletons/S006C002P023R002A040.skeleton","nturgb+d_skeletons/S006C002P023R002A041.skeleton","nturgb+d_skeletons/S006C002P023R002A042.skeleton","nturgb+d_skeletons/S006C002P023R002A043.skeleton","nturgb+d_skeletons/S006C002P023R002A044.skeleton","nturgb+d_skeletons/S006C002P023R002A045.skeleton","nturgb+d_skeletons/S006C002P023R002A046.skeleton","nturgb+d_skeletons/S006C002P023R002A047.skeleton","nturgb+d_skeletons/S006C002P023R002A048.skeleton","nturgb+d_skeletons/S006C002P023R002A049.skeleton","nturgb+d_skeletons/S006C002P023R002A050.skeleton","nturgb+d_skeletons/S006C002P023R002A051.skeleton","nturgb+d_skeletons/S006C002P023R002A052.skeleton","nturgb+d_skeletons/S006C002P023R002A053.skeleton","nturgb+d_skeletons/S006C002P023R002A054.skeleton","nturgb+d_skeletons/S006C002P023R002A055.skeleton","nturgb+d_skeletons/S006C002P023R002A056.skeleton","nturgb+d_skeletons/S006C002P023R002A057.skeleton","nturgb+d_skeletons/S006C002P023R002A058.skeleton","nturgb+d_skeletons/S006C002P023R002A059.skeleton","nturgb+d_skeletons/S006C002P023R002A060.skeleton","nturgb+d_skeletons/S006C003P023R001A001.skeleton","nturgb+d_skeletons/S006C003P023R001A002.skeleton","nturgb+d_skeletons/S006C003P023R001A003.skeleton","nturgb+d_skeletons/S006C003P023R001A004.skeleton","nturgb+d_skeletons/S006C003P023R001A005.skeleton","nturgb+d_skeletons/S006C003P023R001A006.skeleton","nturgb+d_skeletons/S006C003P023R001A007.skeleton","nturgb+d_skeletons/S006C003P023R001A008.skeleton","nturgb+d_skeletons/S006C003P023R001A009.skeleton","nturgb+d_skeletons/S006C003P023R001A010.skeleton","nturgb+d_skeletons/S006C003P023R001A011.skeleton","nturgb+d_skeletons/S006C003P023R001A012.skeleton","nturgb+d_skeletons/S006C003P023R001A013.skeleton","nturgb+d_skeletons/S006C003P023R001A014.skeleton","nturgb+d_skeletons/S006C003P023R001A015.skeleton","nturgb+d_skeletons/S006C003P023R001A016.skeleton","nturgb+d_skeletons/S006C003P023R001A017.skeleton","nturgb+d_skeletons/S006C003P023R001A018.skeleton","nturgb+d_skeletons/S006C003P023R001A019.skeleton","nturgb+d_skeletons/S006C003P023R001A020.skeleton","nturgb+d_skeletons/S006C003P023R001A021.skeleton","nturgb+d_skeletons/S006C003P023R001A022.skeleton","nturgb+d_skeletons/S006C003P023R001A023.skeleton","nturgb+d_skeletons/S006C003P023R001A024.skeleton","nturgb+d_skeletons/S006C003P023R001A025.skeleton","nturgb+d_skeletons/S006C003P023R001A026.skeleton","nturgb+d_skeletons/S006C003P023R001A027.skeleton","nturgb+d_skeletons/S006C003P023R001A028.skeleton","nturgb+d_skeletons/S006C003P023R001A029.skeleton","nturgb+d_skeletons/S006C003P023R001A030.skeleton","nturgb+d_skeletons/S006C003P023R001A031.skeleton","nturgb+d_skeletons/S006C003P023R001A032.skeleton","nturgb+d_skeletons/S006C003P023R001A033.skeleton","nturgb+d_skeletons/S006C003P023R001A034.skeleton","nturgb+d_skeletons/S006C003P023R001A035.skeleton","nturgb+d_skeletons/S006C003P023R001A036.skeleton","nturgb+d_skeletons/S006C003P023R001A037.skeleton","nturgb+d_skeletons/S006C003P023R001A038.skeleton","nturgb+d_skeletons/S006C003P023R001A039.skeleton","nturgb+d_skeletons/S006C003P023R001A040.skeleton","nturgb+d_skeletons/S006C003P023R001A041.skeleton","nturgb+d_skeletons/S006C003P023R001A042.skeleton","nturgb+d_skeletons/S006C003P023R001A043.skeleton","nturgb+d_skeletons/S006C003P023R001A044.skeleton","nturgb+d_skeletons/S006C003P023R001A045.skeleton","nturgb+d_skeletons/S006C003P023R001A046.skeleton","nturgb+d_skeletons/S006C003P023R001A047.skeleton","nturgb+d_skeletons/S006C003P023R001A048.skeleton","nturgb+d_skeletons/S006C003P023R001A049.skeleton","nturgb+d_skeletons/S006C003P023R001A050.skeleton","nturgb+d_skeletons/S006C003P023R001A051.skeleton","nturgb+d_skeletons/S006C003P023R001A052.skeleton","nturgb+d_skeletons/S006C003P023R001A053.skeleton","nturgb+d_skeletons/S006C003P023R001A054.skeleton","nturgb+d_skeletons/S006C003P023R001A055.skeleton","nturgb+d_skeletons/S006C003P023R001A056.skeleton","nturgb+d_skeletons/S006C003P023R001A057.skeleton","nturgb+d_skeletons/S006C003P023R001A058.skeleton","nturgb+d_skeletons/S006C003P023R001A059.skeleton","nturgb+d_skeletons/S006C003P023R001A060.skeleton","nturgb+d_skeletons/S006C003P023R002A001.skeleton","nturgb+d_skeletons/S006C003P023R002A002.skeleton","nturgb+d_skeletons/S006C003P023R002A003.skeleton","nturgb+d_skeletons/S006C003P023R002A004.skeleton","nturgb+d_skeletons/S006C003P023R002A005.skeleton","nturgb+d_skeletons/S006C003P023R002A006.skeleton","nturgb+d_skeletons/S006C003P023R002A007.skeleton","nturgb+d_skeletons/S006C003P023R002A008.skeleton","nturgb+d_skeletons/S006C003P023R002A009.skeleton","nturgb+d_skeletons/S006C003P023R002A010.skeleton","nturgb+d_skeletons/S006C003P023R002A011.skeleton","nturgb+d_skeletons/S006C003P023R002A012.skeleton","nturgb+d_skeletons/S006C003P023R002A013.skeleton","nturgb+d_skeletons/S006C003P023R002A014.skeleton","nturgb+d_skeletons/S006C003P023R002A015.skeleton","nturgb+d_skeletons/S006C003P023R002A016.skeleton","nturgb+d_skeletons/S006C003P023R002A017.skeleton","nturgb+d_skeletons/S006C003P023R002A018.skeleton","nturgb+d_skeletons/S006C003P023R002A019.skeleton","nturgb+d_skeletons/S006C003P023R002A020.skeleton","nturgb+d_skeletons/S006C003P023R002A021.skeleton","nturgb+d_skeletons/S006C003P023R002A022.skeleton","nturgb+d_skeletons/S006C003P023R002A023.skeleton","nturgb+d_skeletons/S006C003P023R002A024.skeleton","nturgb+d_skeletons/S006C003P023R002A025.skeleton","nturgb+d_skeletons/S006C003P023R002A026.skeleton","nturgb+d_skeletons/S006C003P023R002A027.skeleton","nturgb+d_skeletons/S006C003P023R002A028.skeleton","nturgb+d_skeletons/S006C003P023R002A029.skeleton","nturgb+d_skeletons/S006C003P023R002A030.skeleton","nturgb+d_skeletons/S006C003P023R002A031.skeleton","nturgb+d_skeletons/S006C003P023R002A032.skeleton","nturgb+d_skeletons/S006C003P023R002A033.skeleton","nturgb+d_skeletons/S006C003P023R002A034.skeleton","nturgb+d_skeletons/S006C003P023R002A035.skeleton","nturgb+d_skeletons/S006C003P023R002A036.skeleton","nturgb+d_skeletons/S006C003P023R002A037.skeleton","nturgb+d_skeletons/S006C003P023R002A038.skeleton","nturgb+d_skeletons/S006C003P023R002A039.skeleton","nturgb+d_skeletons/S006C003P023R002A040.skeleton","nturgb+d_skeletons/S006C003P023R002A041.skeleton","nturgb+d_skeletons/S006C003P023R002A042.skeleton","nturgb+d_skeletons/S006C003P023R002A043.skeleton","nturgb+d_skeletons/S006C003P023R002A044.skeleton","nturgb+d_skeletons/S006C003P023R002A045.skeleton","nturgb+d_skeletons/S006C003P023R002A046.skeleton","nturgb+d_skeletons/S006C003P023R002A047.skeleton","nturgb+d_skeletons/S006C003P023R002A048.skeleton","nturgb+d_skeletons/S006C003P023R002A049.skeleton","nturgb+d_skeletons/S006C003P023R002A050.skeleton","nturgb+d_skeletons/S006C003P023R002A051.skeleton","nturgb+d_skeletons/S006C003P023R002A052.skeleton","nturgb+d_skeletons/S006C003P023R002A053.skeleton","nturgb+d_skeletons/S006C003P023R002A054.skeleton","nturgb+d_skeletons/S006C003P023R002A055.skeleton","nturgb+d_skeletons/S006C003P023R002A056.skeleton","nturgb+d_skeletons/S006C003P023R002A057.skeleton","nturgb+d_skeletons/S006C003P023R002A058.skeleton","nturgb+d_skeletons/S006C003P023R002A059.skeleton","nturgb+d_skeletons/S006C003P023R002A060.skeleton"]

	arr_valid,arr_test,arr_train=initialize()

	for filename in filenames:
		print("filename:",filename)
		d = convert(filename)

	arr_train,arr_valid,arr_test = randomize(d,arr_train,arr_valid,arr_test)

	np.savez('test.npz', valid=arr_valid, test=arr_test, train=arr_train)

# ------------------------------------------
	# 	if r < 0.1:
	# 		print("valid")
	# 		# arr_valid = np.vstack((arr_test,temp_arr))
	# 		arr_valid.append(temp_arr)
	# 	elif r < 0.2:
	# 		print("test")
	# 		# arr_test = np.vstack((arr_test,temp_arr))
	# 		arr_test.append(temp_arr)
	# 	else:
	# 		print("train")
	# 		# arr_train = np.vstack((arr_train,temp_arr))
	# 		arr_train.append(temp_arr)
	# 	print("filename:",filename)
	# 	print("arr_valid.shape:",arr_valid.shape)
	# return arr_valid,arr_test,arr_train


	# print("arr_all",arr_all)

	# for n in range(0,arr_all.length(),25):
	# 	#25個ごとにランダムに分ける
	# 	print("n:",n)
	# 	print("np.random.rand():",np.random.rand())
	# 	r = np.random.rand()
	# 	temp_arr = np.empty((0,3), dtype=float)
	# 	temp_arr = arr_all[n:n+25,0:3]
	# 	# print("temp_arr:",temp_arr)
