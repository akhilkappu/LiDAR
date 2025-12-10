What is available
 
Data Type		Description		                                      Notes
.bin	      Raw point cloud (XYZ + intensity)	                 Each sensor has its own .bin files
.txt 	     Object detection / bounding boxes	                 Includes trucks, pedestrians, dust; NOT calibration
.label 	   Semantic segmentation labels 	                     Per-sensor labels for each point cloud
Folders		  ls64, ls128, ly50, ly300, m1, ouster, etc. 	       Each folder represents a different sensor mounted at a different truck position
 
What is Possible
Processing each sensor individually:
Convert .bin → .pcd
Merge .pcd files within the same sensor folder
Downsample the merged point cloud
Estimate normals
Create mesh for that single sensor
Visualizing individual sensor point clouds in 3D:
Tools: CloudCompare, Open3D, PCL, Meshlab

What is Not Possible
Merging multiple sensors (ls64, ls128, ly50, ly300, m1, ouster) into a single 3D scene because:
No extrinsic calibration provided
No sensor position, rotation, or orientation data
Cannot compute transformation matrices
Creating a truck-wide merged mesh that aligns all sensors
Using .txt annotations for geometric alignment:
Only contain bounding boxes, not transformations
Restrictions
Dataset limitation: Each sensor is treated independently
No extrinsics: Cannot combine sensors mathematically
Annotation limitation: Bounding boxes are sensor-specific, not global
Recommended Workflow (per sensor)

1. Convert .bin → .pcd
2. Merge .pcd files in the same sensor folder
3. Downsample merged point cloud (e.g., voxel grid)
4. Estimate normals for mesh reconstruction
5. Create mesh from the processed point cloud
 
Prerequisites
Before you begin, ensure your system is up to date and has the necessary packages installed. Run the following commands:
 
 
Plain Text
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-dev python3-venv build-essential -y
pip install open3d opencv-python
sudo snap install cloudcompare
sudo apt install meshlab -y
 
Folder Structure
 
Create the following folder structure for your LiDAR data processing:

LidarDustX/
│
├── ls64/
│     ├── *.bin
│     ├── *.txt
│     └── *.label
│
├── ls128/
│     ├── *.bin
│     ├── *.txt
│     └── *.label
│
├── ly50/
│
├── ly300/
│
├── m1/
│
├── ouster/
│
└── 
        ├── 1_bin_to_pcd.py
        ├── 2_merge_pcd.py
        ├── 3_downsample_normals.py
        └── 4_mesh.py
 
Script Execution Step
 
To process the LiDAR data, navigate to the LidarDustX directory and run the following commands for one of the folders (for example, ls128):
 
python3 1_bin_to_pcd.py ls128
python3 2_merge_pcd.py ls128
python3 3_downsample_normals.py ls128
python3 4_mesh.py ls128
meshlab ls128_mesh_poisson.ply

Output
The output will generate a mesh view from the processed data in the specified folder. You should see the results visualized in MeshLab.
