net_struct = {'Conv-TasNet': {'net': [],
                              'name': []}}

imsize = 32000


def outFromIn(isz, net, layernum):
    totstride = 1
    insize = isz
    for layer in range(layernum):
        fsize, stride, pad, dilation = net[layer]
        outsize = (insize - dilation*(fsize-1) + 2*pad - 1) / stride + 1
        insize = outsize
        totstride = stride
    return outsize, totstride


def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad, dilation = net[layer]
        RF = ((RF - 1) * stride) + dilation*(fsize - 1) + 1
    return RF


if __name__ == '__main__':
    print("layer output sizes given image = %dx%d" % (imsize, imsize))

    for net in net_struct.keys():
        print('************net structrue name is %s**************' % net)
        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize, net_struct[net]['net'], i+1)
            rf = inFromOut(net_struct[net]['net'], i+1)
            print("Layer Name = %s, Output size = %3d, Stride = % 3d, RF size = %3d" % (net_struct[net]['name'][i], p[0], p[1], rf))
