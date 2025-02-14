from random import randint
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from k_means_constrained import KMeansConstrained

delevary_loc = []
n = 15

def find_dp(centroids):
    print(centroids)
    x = [loc_x for loc_x, loc_y in centroids]
    y = [loc_y for loc_x, loc_y in centroids]
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    return (mean_x, mean_y)

def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# incomplete
def tsp(cluster, opt_dp):
    cluster.insert(0, opt_dp)
    unvisited = cluster.copy()
    tour = [opt_dp]
    unvisited.remove(opt_dp)

    while unvisited:
        nearest_point = min(unvisited, key=lambda x: calculate_distance(tour[-1], x))
        tour.append(nearest_point)
        unvisited.remove(nearest_point)

    # Return to the starting point to complete the cycle
    tour.append(opt_dp)

    print(tour)
    return tour

def build_cluster(no_of_clusters):

    # KMeans implementation
    clf = KMeansConstrained(n_clusters=no_of_clusters, size_min=1, size_max=5)
    x = np.array(delevary_loc)
    labels = clf.fit_predict(x)
    centroids = clf.cluster_centers_

    #creating a mapping
    mapping = {label: [] for label in range(no_of_clusters)}
    for i in range(len(delevary_loc)):
        mapping[labels[i]].append(delevary_loc[i])

    return mapping, labels, centroids, x

def plot_data(labels, centroids, x):
    plt.scatter(x[:, 0], x[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red')

# Add dotted lines for coordinates
    for centroid in centroids:
        plt.axhline(y=centroid[1], linestyle='--', color='gray', alpha=0.7)
        plt.axvline(x=centroid[0], linestyle='--', color='gray', alpha=0.7)


def find_del_loc():
    for _ in range(n):
        lat = -2 + randint(1, 7) 
        lon = 3 + randint(1,7)
        loc = (lat, lon)
        delevary_loc.append(loc)
    return delevary_loc

if __name__ == "__main__":

    # creating the boundary
    x1 = -2
    y1 = 3
    x2 = 4
    y2 = 7
    print(find_del_loc())

    # calculating no of clusters
    no_of_clusters = n//5
    if(no_of_clusters*5 < n):
        no_of_clusters += 1

    # getting output from k means in the from of a mapping
    cluster_ponts, labels, centroids, x = build_cluster(no_of_clusters)
    
    #finding dp from centroids
    opt_dp = find_dp(centroids)
    print("Dp ",opt_dp)

    # applying tsp algorithm on each cluster
    optimal_path = []
    for i in range(len(cluster_ponts)):
        path = tsp(cluster_ponts[i], opt_dp)
        optimal_path.append(path)

    #plotting the data
    plot_data(labels, centroids, x)