What is available

| Data Type  | Description  | Notes |
| .bin |Raw point cloud (XYZ + intensity)|Each sensor has its own .bin files|
| .txt |Object detection / bounding boxes|Includes trucks, pedestrians, dust; NOT calibration|
| .label |Semantic segmentation labels|Per-sensor labels for each point cloud|
| Folders |ls64, ls128, ly50, ly300, m1, ouster, etc.|Each folder represents a different sensor mounted at a different truck position|
