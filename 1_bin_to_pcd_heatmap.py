import numpy as np
import open3d as o3d
import glob
import os
import sys
import matplotlib.pyplot as plt
 
# Pass folder name as argument
folder = sys.argv[1]
 
os.makedirs(f"{folder}/pcd", exist_ok=True)
 
bin_files = sorted(glob.glob(f"{folder}/*.bin"))
print("Total .bin files:", len(bin_files))
 
for f in bin_files:
    data = np.fromfile(f, dtype=np.float32).reshape(-1, 4)
 
    xyz = data[:, :3]
    intensity = data[:, 3]
 
    # Normalize intensity (0–1)
    i_norm = (intensity - intensity.min()) / (intensity.max() - intensity.min() + 1e-6)
 
    # Apply heatmap color (JET colormap)
    colors = plt.get_cmap("jet")(i_norm)[:, :3]  # ignore alpha channel
 
    # Create point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(colors)
 
    out = f"{folder}/pcd/{os.path.basename(f).replace('.bin', '.pcd')}"
    o3d.io.write_point_cloud(out, pcd)
    print("Saved:", out)
