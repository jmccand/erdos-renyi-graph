from graph import Graph
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 300
    c_values = [x / 10 for x in range(2, 32, 1)]
    t = 3/4*n
    repeat_count = 500
    '''
    n = 4
    c_values = range(0, 2)
    t = 2
    repeat_count = 3
    '''
    data = []
    for c in c_values:
        t_component_count = 0
        for repeat in range(repeat_count):
            g = Graph(n, c/n)
            if g.t_component(t):
                t_component_count += 1
        data.append([c, t_component_count/repeat_count])
    
    df = pd.DataFrame(data, columns=['c', 'percentage'])
    plt.plot(df['c'], df['percentage'])
    plt.xlabel('c')
    plt.ylabel(f'Percentage of graphs (%)')
    plt.title(f'Percentage of graphs with {n} nodes that have\nconnected groups of at least size {t} for different\naverage numbers of edges per node*')
    plt.figtext(0.5, 0.01, '* p=c/n so the average number of edges per node is c(n-1)/n=c-1/n', ha="center", fontsize=10)
    plt.subplots_adjust(top=0.85, bottom=0.15)
    plt.show()