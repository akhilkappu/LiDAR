import open3d as o3d
import sys
 
folder = sys.argv[1]
pcd_path = f"{folder}_merged.pcd"
 
pcd = o3d.io.read_point_cloud(pcd_path)
print("Before:", len(pcd.points))
 
pcd = pcd.voxel_down_sample(voxel_size=0.1)
print("After:", len(pcd.points))
 
pcd.estimate_normals()
o3d.io.write_point_cloud(f"{folder}_down.pcd", pcd)
 
print("Saved:", f"{folder}_down.pcd")
