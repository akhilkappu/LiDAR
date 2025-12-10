import open3d as o3d
import glob
import sys
 
folder = sys.argv[1]
 
pcd_files = sorted(glob.glob(f"{folder}/pcd/*.pcd"))
merged = o3d.geometry.PointCloud()
 
for f in pcd_files:
    print("Merging:", f)
    p = o3d.io.read_point_cloud(f)
    merged += p
 
o3d.io.write_point_cloud(f"{folder}_merged.pcd", merged)
print("Saved:", f"{folder}_merged.pcd")
