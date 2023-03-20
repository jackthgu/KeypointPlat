from mpl_toolkits import mplot3d
import typing as tp
import numpy as np
import matplotlib.pyplot as plt
import pdb


def get_chain_dots(
        dots: np.ndarray,   
        chain_dots_indexes: tp.List[int], 
                                          
                                          
        ) -> np.ndarray:    
    return dots[chain_dots_indexes]


def get_chains(
        dots: np.ndarray,   
        spine_chain_ixs: tp.List[int], 
        hands_chain_ixs: tp.List[int], 
        legs_chain_ixs: tp.List[int]   
        ):
    return (get_chain_dots(dots, spine_chain_ixs),
            get_chain_dots(dots, hands_chain_ixs),
            get_chain_dots(dots, legs_chain_ixs))


def subplot_nodes(dots: np.ndarray, 
                  ax):
    return ax.scatter3D(*dots.T, c=dots[:, -1])


def subplot_bones(chains: tp.Tuple[np.ndarray, ...], ax):
    return [ax.plot(*chain.T) for chain in chains]


def plot_skeletons(
        skeletons: tp.Sequence[np.ndarray], 
        chains_ixs: tp.Tuple[tp.List[int], tp.List[int], tp.List[int]]):
    fig = plt.figure()
    for i, dots in enumerate(skeletons, start=1):
        chains = get_chains(dots, *chains_ixs)
        pdb.set_trace()
        ax = fig.add_subplot(2, 5, i, projection='3d')
        subplot_nodes(dots, ax)
        subplot_bones(chains, ax)
        path = "D:\mp\est" + str(i) + ".jpg"
        #plt.savefig(path,dpi=300)
    plt.show()


def plot_skeletons2(
        dots: tp.Sequence[np.ndarray], 
        chains_ixs: tp.Tuple[tp.List[int], tp.List[int], tp.List[int]],
        idx, radius):
    fig = plt.figure()
    chains = get_chains(dots, *chains_ixs)
    #ax = fig.add_subplot(2, 5, i, projection='3d')
    ax = plt.axes(projection='3d')
    ax.set_xlim3d([8 , 9.5])
    ax.set_zlim3d([0, 1.5])
    ax.set_ylim3d([28, 29.5 ])
    subplot_nodes(dots, ax)
    subplot_bones(chains, ax)
    path = "D:\mp\est" + str(idx) + ".jpg"
    plt.savefig(path,dpi=300)
    plt.close()
    #plt.show()


def draw3dtest(poss, frame):
    fig = plt.figure()
    #ax = plt.axes(projection='3d')
    ax = fig.add_subplot(projection='3d')
    # Data for a three-dimensional line
    # zline = np.linspace(0, 15, 1000)
    # xline = np.sin(zline)
    # yline = np.cos(zline)
    # ax.plot3D(xline, yline, zline, 'gray')

    # Data for three-dimensional scattered points
    
    xpos=[]
    ypos=[]
    zpos=[]

    for pos in poss:
        xpos.append(pos['x'])
        ypos.append(pos['y'])
        zpos.append(pos['z'])
        

    zdata = np.array(zpos)
    xdata = np.array(xpos)
    ydata = np.array(ypos)
    

    pdb.set_trace()

    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    path = "D:\mp\est" + str(frame) + ".jpg"
    #plt.show()
    plt.savefig(path,dpi=40)
    plt.close()
    print("z")
    print(zdata)
    print("x")
    print(xdata)
    print("y")
    print(ydata)
    return


import json

f = open('D:\path2.json')
data = json.load(f)

# for i, x in enumerate(data['joints']):
#     for j, y in enumerate(x['jointPosition']):
#         y = list(y.values())
#         y = np.array_split(y, 1)
#         data['joints'][i]['jointPosition'][j] = y
        
# ret = np.array([data['joints'][0]['jointPosition']
#                 , 
#                 data['joints'][1]['jointPosition'], data['joints'][2]['jointPosition'], data['joints'][3]['jointPosition'], 
#                 data['joints'][4]['jointPosition'], data['joints'][5]['jointPosition']
#                 , data['joints'][6]['jointPosition'], data['joints'][7]['jointPosition']
#                 , data['joints'][8]['jointPosition'], data['joints'][9]['jointPosition']
#                 , data['joints'][10]['jointPosition']
#                 ])

        
# ret = np.array([data['frames'][0]
#                 , 
#                 data['frames'][1], data['frames'][2], data['frames'][3], 
#                 data['frames'][4], data['frames'][5]
#                 , data['frames'][6], data['frames'][7]
#                 , data['frames'][8], data['frames'][9]
#                 , data['frames'][10]
#                 ])

aa = [x for x in data['frames'][0]['joints']]

bb = np.zeros((len(data['frames']),11,3))

for idx, x in enumerate(data['frames']):
    for idx2, y in enumerate(x['joints']):
        for idx3,z in enumerate(y['jointPosition']):
            bb[idx][idx2][idx3] = z


#aa = [[0 for x in data['joints'][0]['jointPosition']] for x in range(len(data['joints']))]

#length = len(data['joints'][0]['jointPosition'])
#skeletons = ret.reshape(length, 11, 3)
#pdb.set_trace()

chains_ixs = ([0, 1, 2, 3, 4],  # hand_l, elbow_l, chest, elbow_r, hand_r
                  [5, 2, 6],        # pelvis, chest, head
                  [7, 8, 5, 9, 10]) # foot_l, knee_l, pelvis, knee_r, foot_r

radius =  np.abs(bb).max()

for idx, dots in enumerate(bb):
    plot_skeletons2(dots, chains_ixs,idx, radius)


#print(data['joints'][0]['jointPosition'][0])

# for i in data['joints']:
#     #print(i['jointPosition'][0])
#     for j in i['jointPosition']:
#         print(j)

# idx = 0

# for tran in ret.T:
#     draw3dtest(tran, idx)
#     idx = idx+1
#     if idx >3 : break;


f.close