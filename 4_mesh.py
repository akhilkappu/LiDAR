import open3d as o3d
import sys
import time
import numpy as np  # <--- Add this line
 
folder = sys.argv[1]
pcd_path = f"{folder}_down.pcd"
 
# Read point cloud
pcd = o3d.io.read_point_cloud(pcd_path)
print("Point cloud loaded:", pcd_path)
print("Number of points:", len(pcd.points))
 
# Estimate normals if not already present
if not pcd.has_normals():
    print("Estimating normals...")
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=1.0, max_nn=30))
    pcd.orient_normals_consistent_tangent_plane(100)
 
# Poisson reconstruction
print("Creating mesh using Poisson reconstruction...")
start = time.time()
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
end = time.time()
print("Mesh creation time:", end - start, "seconds")
 
# Remove low-density vertices (to clean up mesh)
vertices_to_remove = densities < np.quantile(densities, 0.01)
mesh.remove_vertices_by_mask(vertices_to_remove)
 
# Save mesh
mesh_path = f"{folder}_mesh_poisson.ply"
o3d.io.write_triangle_mesh(mesh_path, mesh, write_ascii=True)
print("Mesh saved:", mesh_path)
