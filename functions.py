import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def read_textfile(filename, skiprows):
    #filename is a string
    dataset = np.loadtxt(filename, dtype=str, skiprows = skiprows)
    dataset = np.char.replace(dataset, 'i', 'j')
    dataset = dataset.astype(complex)

    return dataset

def plots_epsilon(dataset, realpart = True):
    conductivity = np.real(dataset[:,0])

    if realpart == True:
        dataset = np.real(dataset)
        ylabel = 'Re(signal strenght) [nS]'
        xlabel = 'conductivity [S/m]'
        tickinterval = 20

    else:
        dataset = np.imag(dataset)
        ylabel = 'Im(signal strenght) [nS]'
        xlabel = 'conductivity [S/m]'
        tickinterval = 40
    #np.linspace(0.3, 1, num=len(dataset[0,:]))
    colormapping = np.array([[0,118/255,155/255,195/255,236/255], np.full(len(dataset[0,:])-1, 0), np.full(len(dataset[0,:])-1, 0)])    # this code is getting less and less functional every day
    #colormapping = np.flip(colormapping, axis=1)
    dataset = 10**9*dataset
    #print(colormapping.shape)
    fig, ax = plt.subplots()
    lazylabelling = np.array(['\u03B5' + r'$_{r}$' + '=1', '\u03B5' + r'$_{r}$' + '=5', '\u03B5' + r'$_{r}$' + '=10', '\u03B5' + r'$_{r}$' + '=15', '\u03B5' + r'$_{r}$' + '=20'])
    for i in range(1, dataset[0,:].shape[0]):                           #lazy quick coding 2 is due to data collection.
        ax.semilogx(conductivity, dataset[:, i], label=lazylabelling[i-1], color=colormapping[:,i-1])
    ax.grid(True)
    #ax.grid(which='minor')

    # here ticks start
    plt.xticks(ticks=[1E-3, 1E-2, 1E-1, 1E-0, 1E1, 1E2, 1E3])  # - deze veranderd 0501
    xticksminor = np.empty(0)
    for ii in range(-3, 3):
        xticksminor = np.append(xticksminor, np.linspace(1*10**(ii), 1*10**(ii+1), 10))
    plt.xticks(ticks=xticksminor,labels=[], minor=True)
    yticksdiff = np.min(dataset[:,1:])//10 * 10+ (np.max(dataset[:,1:])//10 * 10)+10
    #print(int(abs(yticksdiff)//10))
    yticks = np.arange(np.min(dataset[:,1:])//10 * 10, (np.max(dataset[:,1:])//10 * 10)+tickinterval, tickinterval)
    plt.yticks(ticks=yticks)

    #plt.tick_params(axis='x', which='both')
    #plt.axis('log', base=10, subs=[2, 3, 4, 5, 6, 7, 8, 9])
    #ax.minorticks_on()
    #plt.grid(True, which='both', ls='-.')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.grid(visible=True, which='minor', lw=0.2)
    plt.xlim([1E-3, 1E3])

    #legend
    plt.legend(loc='upper right', fontsize='large')
    plt.savefig('figure_'+str(realpart)+'new.png', bbox_inches='tight')
    plt.show()
    return dataset


def plots_epsilon_cover(dataset, realpart = True):
    conductivity = np.real(dataset[:,0])

    if realpart == True:
        dataset = np.real(dataset)
        ylabel = 'Re(signal strenght) [nS]'
        xlabel = 'conductivity [S/m]'
        tickinterval = 20

    else:
        dataset = np.imag(dataset)
        ylabel = 'Im(signal strenght) [nS]'
        xlabel = 'conductivity [S/m]'
        tickinterval = 40
    #np.linspace(0.3, 1, num=len(dataset[0,:]))
    colormapping = np.array([[0,0,0,1,0], np.full(len(dataset[0,:])-1, 0), np.full(len(dataset[0,:])-1, 0)])    # this code is getting less and less functional every day
    #colormapping = np.flip(colormapping, axis=1)
    dataset = 10**9*dataset
    #print(colormapping.shape)
    fig, ax = plt.subplots()
    lazylabelling = np.array(['\u03B5' + r'$_{r}$' + '=1', '\u03B5' + r'$_{r}$' + '=5', '\u03B5' + r'$_{r}$' + '=10', '\u03B5' + r'$_{r}$' + '=15', '\u03B5' + r'$_{r}$' + '=20'])
    alphas = [0., 0., 0., 1, 0.]
    for i in range(1, dataset[0,:].shape[0]):                           #lazy quick coding 2 is due to data collection.
        ax.semilogx(conductivity, dataset[:, i], label=lazylabelling[i-1], color=colormapping[:,i-1], alpha=alphas[i-1])
    ax.grid(True)
    #ax.grid(which='minor')

    # here ticks start
    plt.xticks(ticks=[1E-3, 1E-2, 1E-1, 1E-0, 1E1, 1E2, 1E3], fontsize=12)  # - deze veranderd 0501
    xticksminor = np.empty(0)
    for ii in range(-3, 3):
        xticksminor = np.append(xticksminor, np.linspace(1*10**(ii), 1*10**(ii+1), 10))
    plt.xticks(ticks=xticksminor,labels=[], minor=True, fontsize=12)
    yticksdiff = np.min(dataset[:,1:])//10 * 10+ (np.max(dataset[:,1:])//10 * 10)+10
    #print(int(abs(yticksdiff)//10))
    #yticks = np.arange(np.min(dataset[:,1:])//10 * 10, (np.max(dataset[:,1:])//10 * 10)+tickinterval, tickinterval)
    yticks = np.arange(-40,5,5)
    plt.yticks(fontsize=12)

    #plt.tick_params(axis='x', which='both')
    #plt.axis('log', base=10, subs=[2, 3, 4, 5, 6, 7, 8, 9])
    #ax.minorticks_on()
    #plt.grid(True, which='both', ls='-.')
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.grid(visible=True, which='minor', lw=0.2)
    plt.xlim([1E-3, 1E3])
    plt.ylim([-40, 0])
    #legend
    plt.savefig('figure_'+str(realpart)+'cover_zoom_2.png', bbox_inches='tight')
    plt.show()
    return dataset
