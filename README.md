# 4D_Gesture_Generative
4D_Gesture_Generative

# Team
Misha, Prashanth, Hajime

# Data
## Download from NTU
1. Sign up you account to download
http://rose1.ntu.edu.sg/Datasets/download3.asp
2. It's heavy and slow, so I can send it to you what I already downloaded

## Camera
Kinect v2

## Data format (file name)
Each file/folder name in the dataset is in the format of SsssCcccPpppRrrrAaaa (e.g. S001C002P003R002A013), for which 
_ sss: the setup number _
- 1-17 (combination patterns of camera’s height and distance)
_ ccc: the camera ID _
- -45degree, 0degree, 45degrees
Each motion is taken twice, first one towards to left camera, second one towards right
_ ppp: the performer ID _
- 001-040
_ rrr: the replication number (1 or 2) _
- ???
_ aaa: the action class label _ 
- 60 action classes in total,
	- 40 daily actions (drinking, eating, reading, etc.)
	- 9 health-related actions (sneezing, staggering, falling down, etc.)
	- 11 mutual actions (punching, kicking, hugging, etc.)
	reference: https://github.com/shahroudy/NTURGB-D#action-classes

## Data format (in file)
(example)

1 <- number of people in the frame

72057594037931101 0 1 1 1 1 0 0.02764709 0.05745083 2 

bodyID clipedEdges handLeftConfidence handLeftState handRightConfidence handRightState isResticted leanX leanY trackingState

25 <- number of joints (always25)

0.2181153 0.1725972 3.785547 277.419 191.8218 1036.233 519.1677 -0.2059419 0.05349901 0.9692109 -0.1239193 2

0.2323292 0.4326636 3.714767 279.2439 165.8569 1041.918 444.3235 -0.2272637 0.05621852 0.964434 -0.1227094 2

.
.
.

x, y, z(3D location of the joint), X, Y(2D location of the joint j in corresponding depth/IR frame), X, Y(2D location of the joint j in corresponding RGB frame), w, x, y, z(The orientation of the joint j), trackingState

Units are described here: https://msdn.microsoft.com/en-us/library/dn785530.aspx

### About orientation 
Kinect uses "quaternion". Also, refer this image for direction.
![kinect_joint_orientation](https://github.mit.edu/kuwayama/4D_Gesture_Generative/blob/master/kinect_joint_orientation.gif "kinect_joint_orientation")

## For more details
about setups, camera IDs, ... please refer to the paper https://github.com/shahroudy/NTURGB-D or ask Hajime directly

# Data Formatter
## kinect file location (in Google Drive)
https://drive.google.com/open?id=1_lsUreZGJ4b3G96URs3Npxb1QwFLbuW1

## Data format:
- Numpyz
- 3 numpy array dataset: Train(80%), Valid(10%), Test(10%)

## Command to format all the joints (now refactoring...)
```
python npzsave.py --list filepaths
```

(Example) 
```
python npzsave.py --list “folder/aaaa.skelton”,”folder/bbbb.skelton”
```

### Output file name and locationt
test.npz in the same folder

## Command to format one joint
```
python npzsave.py --list filepaths --joint 1-25
```

(Example)
```
python npzsave.py --list “folder/aaaa.skelton”,”folder/bbbb.skelton” --joint 1
```

- The below is the data
```
>>> arr = np.load('test.npz')
>>> arr["train"]
array([array([

  [x1,y1,z1],
  [x2,y2,z2],
  [x3,y3,z3],
  [x4,y4,z4],
  [x5,y5,z5],
  ...
  ...
]
),array([

  [x1,y1,z1],
  [x2,y2,z2],
  [x3,y3,z3],
  [x4,y4,z4],
  [x5,y5,z5],
  ...
  ...
]
)], dtype=object)
```

### Output file name and locationt
test.npz in the same folder



