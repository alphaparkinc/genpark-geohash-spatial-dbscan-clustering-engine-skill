from client import GeohashSpatialDbscanClusteringEngineClient

def main():
    client = GeohashSpatialDbscanClusteringEngineClient()
    res = client.cluster_coordinates()
    print('Spatial DBSCAN Engine: ' + res['clustering_run_id'] + ' (Clusters: ' + str(res['clusters_formed']) + ')')
    print('Points: ' + str(res['total_points_analyzed']) + ' | Centroid: ' + str(res['highest_density_centroid']))
    print('Vis URL: ' + res['cluster_vis_url'])

if __name__ == '__main__':
    main()
